![linksight banner](/assets/linksight_api_client_banner.png)

[![Build Status](https://travis-ci.org/thinkingmachines/linksight-api-client.svg?branch=master)](https://travis-ci.org/thinkingmachines/linksight-api-client)
[![Documentation Status](https://readthedocs.org/projects/linksight-api-client/badge/?version=latest)](https://linksight-api-client.readthedocs.io/en/latest/?badge=latest)
![Python Version](https://img.shields.io/badge/python-3.5%2C%203.6-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This is the Python API Client for
[LinkSight](https://linksight.thinkingmachin.es/). You can use this to
programmatically standardize your messy and misspelled barangay, municipality,
city, and province names. It works on Python 3.5.X. and 3.6.X.

## Installation 

You can see the requirements in the `requirements.txt` file. Some notable
dependencies include:

- requests==2.21.0
- numpy==1.15.4
- pandas==0.23.4

You can install the API client either via `pip` or manually through the
`setup.py` file. Using `pip`, simply run the following command:

```sh
pip install git+https://github.com/thinkingmachines/linksight-api-client.git
```

On the other hand, you can also clone this repository then run `install`:

```sh
git clone git@github.com:thinkingmachines/linksight-api-client.git 
cd linksight-api-client
python setup.py install
```

## Usage

### Generating your access token

Using the Python API requires an API token, which you can obtain from this
[link](https://linksight-stg.thinkingmachin.es/). Simply log-in, go to the
*upper-rightmost* corner, click the "Need API Access?" button, then "Generate
token":

![linksight api token](/assets/linksight_api_token_instructions.png)


### Basic usage

The LinkSight API client can be used like any other Python packages. To perform
matching, simply follow these steps:
- Create an instance of `linksight.Client` by supplying your API token
- Call `create_dataset` while providing the path to your dataset as a CSV file.
- Perform matching on the resulting dataset by providing the columns
    corresponding to the "Barangay", "Municipality", and "Province"

```python
import linksight
import pandas

# Insert your API token here
# In practice, you should not expose nor share your 
# personal token to others
API_TOKEN = <API_TOKEN> 

# Create an instance of the Client
ls = linksight.Client(<API_TOKEN>)

# Provide your dataset to the API
# You can also pass a DataFrame, i.e. ls.create_dataset(df)
with open('path/to/my/dataset.csv') as fp:
    ds = ls.create_dataset(fp)

# Perform matching by specifying the column names
# for the respective admin level
match = ds.match(
    source_bgy_col='Barangay',
    source_municity_col='City',
    source_prov_col='Province',
)

# Get the matched dataset as a DataFrame
match.df
```

## Contributing

This project is open for contributors! Contibutions can come in the form of
feature requests, bug fixes, documentation, tutorials and the like! We highly
recommend to file an Issue first before [submitting a Pull
Request](https://help.github.com/articles/creating-a-pull-request/).

### Setting up your dev environment

To set-up your development environment, simply clone this repository and
install the dev dependencies in `requirements-dev.txt`. We recommend that all
these steps are done inside a virtual environment

```sh
git clone git@github.com:thinkingmachines/linksight-api-client.git 
cd linksight-api-client
virtualenv venv # Create a virtualenv
source venv/bin/activate
pip install -r requirements-dev.txt
```

We also provided a `Makefile` to make everything much easier:

```sh
git clone git@github.com:thinkingmachines/linksight-api-client.git 
cd linksight-api-client
make venv # Create a virtualenv and install pip-tools
make dev # Set-up dev environment
```

### Running the tests

We use [pytest](https://docs.pytest.org/en/latest/) for testing. There are
three sets of tests in the API Client:

- **Regular Tests**: invokes a mocked API and can be run offline
- **Web Tests** (`web`): hits the external server and requires an API token.
- **Contract Tests** (`contract`): checks for consistency of mocked data to live data. 

All contract tests are web tests. It is recommended that external developers
write both regular and web tests, but locally do their checks on regular tests.
Web tests should only be handled by a continuous integration service (via a
testing account), unless you want to use your own API token.

To run regular tests:

```shell
# In project root
pytest -m "not webtest" -v
```

Lastly, to run all tests:

```shell
# In project root
pytest -v
```

## License

MIT License (c) 2018, Thinking Machines Data Science
