from __future__ import print_function
from forms13f.api.default_api import DefaultApi
import time
from pprint import pprint
from forms13f.rest import ApiException

# Create an instance of the API class
api_instance = DefaultApi()
accession_number = "0000950123-24-008740"  # String | The accession number of the form entry. (default to null)
cik = "0001067983"  # String | The Central Index Key (CIK) of the form entry. (default to null)
offset = 0  # Integer | The offset for pagination. (optional) (default to 0)
limit = 100  # Integer | The limit for pagination. (optional) (default to 100)

try:
    # Get SEC Form 13F
    api_response = api_instance.api_v1_form_get(accession_number, cik, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v1_form_get: %s\n" % e)
