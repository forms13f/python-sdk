from forms13f.rest import ApiException
from forms13f.api.default_api import DefaultApi
from pprint import pprint
from forms13f.api_client import ApiClient

# Create an instance of the API class
# use ApiClient with exponential backoffs
api_client = ApiClient(n_retries=5)
api_instance = DefaultApi(api_client)
cik = "1012622"  # String | The Central Index Key (CIK) of the filer.
try:
    # Retrieve a filer by CIK
    api_response = api_instance.api_v1_filer_get(cik)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v1_filer_get: %s\n" % e)
