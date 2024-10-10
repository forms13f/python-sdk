from forms13f.rest import ApiException
from forms13f.api.default_api import DefaultApi
from pprint import pprint

# Create an instance of the API class
api_instance = DefaultApi()
offset = 0  # Integer | Skip previous offset CIKs (optional) (default to 0)
limit = 100  # Integer | Return max limit CIKs (optional) (default to 100)

try:
    # Retrieve unique filers
    api_response = api_instance.api_v1_filers_get(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v1_filers_get: %s\n" % e)
