# forms13f.DefaultApi

All URIs are relative to *https://forms13f.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_filer_get**](DefaultApi.md#api_v1_filer_get) | **GET** /api/v1/filer | Retrieve a filer by CIK.
[**api_v1_filers_get**](DefaultApi.md#api_v1_filers_get) | **GET** /api/v1/filers | Retrieve unique filers.
[**api_v1_filings_get**](DefaultApi.md#api_v1_filings_get) | **GET** /api/v1/filings | Retrieve 13F filings for all filers in the time range.
[**api_v1_form_get**](DefaultApi.md#api_v1_form_get) | **GET** /api/v1/form | Get SEC Form 13F.
[**api_v1_forms_get**](DefaultApi.md#api_v1_forms_get) | **GET** /api/v1/forms | Retrieve SEC forms 13F for a filer.
[**api_v1_funds_get**](DefaultApi.md#api_v1_funds_get) | **GET** /api/v1/funds | Retrieve unique companies.
[**api_v1_tickers_get**](DefaultApi.md#api_v1_tickers_get) | **GET** /api/v1/tickers | Returns cusip, ticker, and company name for provided matching cusips or tickers parameters


# **api_v1_filer_get**
> ApiV1Filer api_v1_filer_get(cik)

Retrieve a filer by CIK.

Returns a filer with the specified CIK (Central Index Key) and associated company names.

### Example


```python
import forms13f
from forms13f.models.api_v1_filer import ApiV1Filer
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
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_filer_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cik** | **str**| The Central Index Key (CIK) of the filer. | 

### Return type

[**ApiV1Filer**](ApiV1Filer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object representing the filer |  -  |
**400** | Invalid request parameters |  -  |
**404** | Filer not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filers_get**
> List[ApiV1Filer] api_v1_filers_get(offset=offset, limit=limit)

Retrieve unique filers.

Returns a list of unique filers with their CIK and associated company names.

### Example


```python
import forms13f
from forms13f.models.api_v1_filer import ApiV1Filer
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
    offset = 0 # int | Skip previous offset CIKs (optional) (default to 0)
    limit = 100 # int | Return max limit CIKs (optional) (default to 100)

    try:
        # Retrieve unique filers.
        api_response = api_instance.api_v1_filers_get(offset=offset, limit=limit)
        print("The response of DefaultApi->api_v1_filers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_filers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Skip previous offset CIKs | [optional] [default to 0]
 **limit** | **int**| Return max limit CIKs | [optional] [default to 100]

### Return type

[**List[ApiV1Filer]**](ApiV1Filer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of filers |  -  |
**400** | Invalid request parameters |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_filings_get**
> List[ApiV1Form] api_v1_filings_get(var_from, to, offset=offset, limit=limit)

Retrieve 13F filings for all filers in the time range.

Get the 13F filings for all filers in the specified time range. Uses a form filing date as timestamp.

### Example


```python
import forms13f
from forms13f.models.api_v1_form import ApiV1Form
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
    var_from = '2023-01-01' # date | All filings returned will be on or after this filing date.
    to = '2023-12-31' # date | All filings returned will be on or before this filing date.
    offset = 0 # int | Skip the first offset filings. (optional) (default to 0)
    limit = 100 # int | Return at most limit filings. (optional) (default to 100)

    try:
        # Retrieve 13F filings for all filers in the time range.
        api_response = api_instance.api_v1_filings_get(var_from, to, offset=offset, limit=limit)
        print("The response of DefaultApi->api_v1_filings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_filings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **date**| All filings returned will be on or after this filing date. | 
 **to** | **date**| All filings returned will be on or before this filing date. | 
 **offset** | **int**| Skip the first offset filings. | [optional] [default to 0]
 **limit** | **int**| Return at most limit filings. | [optional] [default to 100]

### Return type

[**List[ApiV1Form]**](ApiV1Form.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of FormHeader |  -  |
**400** | Invalid request parameters |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_form_get**
> List[ApiV1FormEntry] api_v1_form_get(accession_number, cik, offset=offset, limit=limit)

Get SEC Form 13F.

Retrieve a content of form 13F by accession number and CIK.

### Example


```python
import forms13f
from forms13f.models.api_v1_form_entry import ApiV1FormEntry
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
    accession_number = '0000950123-24-008740' # str | The accession number of the form entry.
    cik = '0001067983' # str | The Central Index Key (CIK) of the form entry.
    offset = 0 # int | The offset for pagination. (optional) (default to 0)
    limit = 100 # int | The limit for pagination. (optional) (default to 100)

    try:
        # Get SEC Form 13F.
        api_response = api_instance.api_v1_form_get(accession_number, cik, offset=offset, limit=limit)
        print("The response of DefaultApi->api_v1_form_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_form_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accession_number** | **str**| The accession number of the form entry. | 
 **cik** | **str**| The Central Index Key (CIK) of the form entry. | 
 **offset** | **int**| The offset for pagination. | [optional] [default to 0]
 **limit** | **int**| The limit for pagination. | [optional] [default to 100]

### Return type

[**List[ApiV1FormEntry]**](ApiV1FormEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array containing form entries. |  -  |
**400** | Invalid input, object invalid. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_forms_get**
> List[ApiV1Form] api_v1_forms_get(cik, var_from=var_from, to=to, offset=offset, limit=limit)

Retrieve SEC forms 13F for a filer.

This API returns SEC 13F forms between dates for a filer with CIK. Uses a period of report as timestamp.

### Example


```python
import forms13f
from forms13f.models.api_v1_form import ApiV1Form
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
    cik = '0001067983' # str | The Central Index Key (CIK) of the filer.
    var_from = '2010-01-01' # str | All forms returned will be on or after this period of report date. (optional) (default to '2010-01-01')
    to = '2030-01-01' # str | All forms returned will be on or before this period of report date. (optional) (default to '2030-01-01')
    offset = 0 # int | Skip the first offset forms. (optional) (default to 0)
    limit = 100 # int | Return at most limit forms. (optional) (default to 100)

    try:
        # Retrieve SEC forms 13F for a filer.
        api_response = api_instance.api_v1_forms_get(cik, var_from=var_from, to=to, offset=offset, limit=limit)
        print("The response of DefaultApi->api_v1_forms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_forms_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cik** | **str**| The Central Index Key (CIK) of the filer. | 
 **var_from** | **str**| All forms returned will be on or after this period of report date. | [optional] [default to &#39;2010-01-01&#39;]
 **to** | **str**| All forms returned will be on or before this period of report date. | [optional] [default to &#39;2030-01-01&#39;]
 **offset** | **int**| Skip the first offset forms. | [optional] [default to 0]
 **limit** | **int**| Return at most limit forms. | [optional] [default to 100]

### Return type

[**List[ApiV1Form]**](ApiV1Form.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of FormHeader |  -  |
**400** | Invalid request parameters |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_funds_get**
> List[ApiV1Fund] api_v1_funds_get(name=name, offset=offset, limit=limit)

Retrieve unique companies.

Returns a list of unique companies with their names and associated CIKs.

### Example


```python
import forms13f
from forms13f.models.api_v1_fund import ApiV1Fund
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
    name = 'berkshire' # str | Filter companies by by a substring of their name (optional)
    offset = 0 # int | Skip previous offset companies (optional) (default to 0)
    limit = 100 # int | Return max limit companies (optional) (default to 100)

    try:
        # Retrieve unique companies.
        api_response = api_instance.api_v1_funds_get(name=name, offset=offset, limit=limit)
        print("The response of DefaultApi->api_v1_funds_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_funds_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter companies by by a substring of their name | [optional] 
 **offset** | **int**| Skip previous offset companies | [optional] [default to 0]
 **limit** | **int**| Return max limit companies | [optional] [default to 100]

### Return type

[**List[ApiV1Fund]**](ApiV1Fund.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of companies |  -  |
**400** | Invalid request parameters |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_tickers_get**
> List[TickerInfo] api_v1_tickers_get(cusips=cusips, tickers=tickers)

Returns cusip, ticker, and company name for provided matching cusips or tickers parameters

Either `cusips` or `tickers` parameter must be provided. 

### Example


```python
import forms13f
from forms13f.models.ticker_info import TickerInfo
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
    cusips = ['037833100,594918104'] # List[str] | Array of CUSIPs to match (optional)
    tickers = ['tickers_example'] # List[str] | Array of tickers to match (optional)

    try:
        # Returns cusip, ticker, and company name for provided matching cusips or tickers parameters
        api_response = api_instance.api_v1_tickers_get(cusips=cusips, tickers=tickers)
        print("The response of DefaultApi->api_v1_tickers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_v1_tickers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cusips** | [**List[str]**](str.md)| Array of CUSIPs to match | [optional] 
 **tickers** | [**List[str]**](str.md)| Array of tickers to match | [optional] 

### Return type

[**List[TickerInfo]**](TickerInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of matching tickers |  -  |
**400** | Invalid request parameters |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

