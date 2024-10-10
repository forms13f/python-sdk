# ApiV1Fund


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the company. | [optional] 
**cik** | **str** | The CIK of the company. | [optional] 

## Example

```python
from forms13f.models.api_v1_fund import ApiV1Fund

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1Fund from a JSON string
api_v1_fund_instance = ApiV1Fund.from_json(json)
# print the JSON string representation of the object
print(ApiV1Fund.to_json())

# convert the object into a dict
api_v1_fund_dict = api_v1_fund_instance.to_dict()
# create an instance of ApiV1Fund from a dict
api_v1_fund_from_dict = ApiV1Fund.from_dict(api_v1_fund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


