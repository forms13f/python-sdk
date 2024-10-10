from __future__ import print_function
from forms13f.api.default_api import DefaultApi
import time
from pprint import pprint
from forms13f.rest import ApiException

# Create an instance of the API class
api_instance = DefaultApi()
name = "berkshire"  # String | Filter companies by name (optional) (default to null)
offset = 0  # Integer | Skip previous offset companies (optional) (default to 0)
limit = 100  # Integer | Return max limit companies (optional) (default to 100)

try:
    # Retrieve unique companies
    api_response = api_instance.api_v1_funds_get(name=name, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v1_funds_get: %s\n" % e)
