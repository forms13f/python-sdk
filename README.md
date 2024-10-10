# forms13f
API for SEC form filings such as 13F.

The package is a wrapper around the [forms13f.com](https://forms13f.com) API.

- API version: 1.0.0
- Package version: 1.0.0

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

```sh
pip install git+https://github.com/forms13f/python-sdk.git
```

Then import the package:
```python
import forms13f
```

### Installing under virtualenv
```python
#create venv
python3 -m venv venv
source venv/bin/activate
pip install git+https://github.com/forms13f/python-sdk.git

# run the code

# deactivate venv
deactivate
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

Then import the package:
```python
import forms13f
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import forms13f
from forms13f.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forms13f.com
# See configuration.py for a list of all supported configuration parameters.
configuration = forms13f.Configuration(
    host = "https://forms13f.com"
)



# Enter a context with an instance of the API client
with forms13f.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forms13f.DefaultApi(api_client)
    cik = '1067983' # str | The Central Index Key (CIK) of the filer.

    try:
        # Retrieve a filer by CIK.
        api_response = api_instance.api_v1_filer_get(cik)
        print("The response of DefaultApi->api_v1_filer_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->api_v1_filer_get: %s\n" % e)

```

### More examples

You can find example scripts in the [examples](./examples) directory. To run examples:

```python
cd examples
python3 example_api_v1_filer.py
python3 example_api_v1_filings.py
python3 example_api_v1_forms.py
python3 example_api_v1_filers.py
python3 example_api_v1_form.py
python3 example_api_v1_funds.py
```

## Documentation for API Endpoints

All URIs are relative to *https://forms13f.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**api_v1_filer_get**](docs/DefaultApi.md#api_v1_filer_get) | **GET** /api/v1/filer | Retrieve a filer by CIK.
*DefaultApi* | [**api_v1_filers_get**](docs/DefaultApi.md#api_v1_filers_get) | **GET** /api/v1/filers | Retrieve unique filers.
*DefaultApi* | [**api_v1_filings_get**](docs/DefaultApi.md#api_v1_filings_get) | **GET** /api/v1/filings | Retrieve 13F filings for all filers in the time range.
*DefaultApi* | [**api_v1_form_get**](docs/DefaultApi.md#api_v1_form_get) | **GET** /api/v1/form | Get SEC Form 13F.
*DefaultApi* | [**api_v1_forms_get**](docs/DefaultApi.md#api_v1_forms_get) | **GET** /api/v1/forms | Retrieve SEC forms 13F for a filer.
*DefaultApi* | [**api_v1_funds_get**](docs/DefaultApi.md#api_v1_funds_get) | **GET** /api/v1/funds | Retrieve unique companies.
*DefaultApi* | [**api_v1_tickers_get**](docs/DefaultApi.md#api_v1_tickers_get) | **GET** /api/v1/tickers | Returns cusip, ticker, and company name for provided matching cusips or tickers parameters


## Documentation For Models

 - [ApiV1Filer](docs/ApiV1Filer.md)
 - [ApiV1Form](docs/ApiV1Form.md)
 - [ApiV1FormEntry](docs/ApiV1FormEntry.md)
 - [ApiV1Fund](docs/ApiV1Fund.md)
 - [TickerInfo](docs/TickerInfo.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

forms13f@gmail.com

