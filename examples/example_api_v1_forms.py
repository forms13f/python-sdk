from __future__ import print_function
from forms13f.api.default_api import DefaultApi
import time
from pprint import pprint
from forms13f.rest import ApiException

# Create an instance of the API class
api_instance = DefaultApi()
cik = "0001067983"  # String | The Central Index Key (CIK) of the filer. (default to null)
from_date = "2023-12-31"  # String | All forms returned will be on or after this period of report date. (optional) (default to 2010-01-01)
to_date = "2024-12-31"  # String | All forms returned will be on or before this period of report date. (optional) (default to 2030-01-01)
offset = 0  # Integer | Skip the first offset forms. (optional) (default to 0)
limit = 100  # Integer | Return at most limit forms. (optional) (default to 100)

try:
    # Retrieve SEC forms 13F for a filer
    api_response = api_instance.api_v1_forms_get(cik, from_date, to_date, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v1_forms_get: %s\n" % e)
