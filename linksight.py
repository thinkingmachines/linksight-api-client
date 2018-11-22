import requests

version = '0.1'
user_agent = 'linksight-api-client/{}'.format(version)
endpoint = 'https://linksight-stg.thinkingmachin.es/api'


def urljoin(*args):
    return '/'.join(map(lambda a: a.strip('/'), args))


class Resource(dict):

    @classmethod
    def create(cls, client, **kwargs):
        url = urljoin(endpoint, cls.url)
        resp = client.request('post', url, **kwargs)
        resp.raise_for_status()
        return cls(client, resp)

    @classmethod
    def retrieve(cls, client, id):
        url = urljoin(endpoint, cls.url, id)
        resp = client.request('get', url)
        resp.raise_for_status()
        return cls(client, resp)

    def __init__(self, client, resp):
        super().__init__(resp.json())
        self.client = client
        self.response = resp

    def instance_url(self, *args):
        return urljoin(endpoint, self.url, self['id'], *args)


class User(Resource):
    url = 'users'


class Dataset(Resource):
    url = 'datasets'

    def match(
        self,
        source_bgy_col=None,
        source_municity_col=None,
        source_prov_col=None,
        export=True,
    ):
        if not any([source_bgy_col, source_municity_col, source_prov_col]):
            raise ValueError('At least one column must be defined')
        url = self.instance_url('match')
        resp = self.client.request('post', url, json={
            'source_bgy_col': source_bgy_col,
            'source_municity_col': source_municity_col,
            'source_prov_col': source_prov_col,
            'export': export,
        })
        return Match(self.client, resp)


class Match(Resource):
    url = 'matches'


class Client(requests.Session):

    def __init__(self, token):
        super().__init__()
        self.headers.update({
            'User-Agent': user_agent,
            'Authorization': 'Token {}'.format(token),
        })

    def get_user(self, id='me'):
        return User.retrieve(self, id)

    def create_dataset(self, file):
        return Dataset.create(self, files={'file': file})

