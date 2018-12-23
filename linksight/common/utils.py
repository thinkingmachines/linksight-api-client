# -*- coding: utf-8 -*-


def urljoin(*args):
    return '/'.join(map(lambda a: a.strip('/'), args))
