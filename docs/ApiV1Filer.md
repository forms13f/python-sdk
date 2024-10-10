# ApiV1Filer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cik** | **str** | The Central Index Key (CIK) of the filer. | [optional] 
**company_names** | **List[str]** | An array of company names associated with the CIK. | [optional] 

## Example

```python
from forms13f.models.api_v1_filer import ApiV1Filer

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1Filer from a JSON string
api_v1_filer_instance = ApiV1Filer.from_json(json)
# print the JSON string representation of the object
print(ApiV1Filer.to_json())

# convert the object into a dict
api_v1_filer_dict = api_v1_filer_instance.to_dict()
# create an instance of ApiV1Filer from a dict
api_v1_filer_from_dict = ApiV1Filer.from_dict(api_v1_filer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


