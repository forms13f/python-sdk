# TickerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cusip** | **str** |  | [optional] 
**ticker** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 

## Example

```python
from forms13f.models.ticker_info import TickerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TickerInfo from a JSON string
ticker_info_instance = TickerInfo.from_json(json)
# print the JSON string representation of the object
print(TickerInfo.to_json())

# convert the object into a dict
ticker_info_dict = ticker_info_instance.to_dict()
# create an instance of TickerInfo from a dict
ticker_info_from_dict = TickerInfo.from_dict(ticker_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


