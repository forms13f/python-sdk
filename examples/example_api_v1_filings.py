from __future__ import print_function
from forms13f.api.default_api import DefaultApi
import time
from pprint import pprint
from forms13f.rest import ApiException



# Create an instance of the API class
api_instance = DefaultApi()
from_date = "2023-01-01"  # date | All filings returned will be on or after this filing date. (default to null)
to_date = "2023-12-31"  # date | All filings returned will be on or before this filing date. (default to null)
offset = 0  # Integer | Skip the first offset filings. (optional) (default to 0)
limit = 100  # Integer | Return at most limit filings. (optional) (default to 100)

try:
    # Retrieve 13F filings for all filers in the time range
    api_response = api_instance.api_v1_filings_get(from_date, to_date, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v1_filings_get: %s\n" % e)
