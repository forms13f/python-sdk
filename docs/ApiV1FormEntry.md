# ApiV1FormEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession_number** | **str** | The accession number of the form entry. | [optional] 
**cik** | **str** | The Central Index Key (CIK) of the form entry. | [optional] 
**name_of_issuer** | **str** | The name of the issuer. | [optional] 
**title_of_class** | **str** | The title of the class of securities. | [optional] 
**cusip** | **str** | The CUSIP number of the securities. | [optional] 
**value** | **int** | The value of the securities. | [optional] 
**ssh_prnamt** | **int** | The number of shares or principal amount. | [optional] 
**ssh_prnamt_type** | **str** | The type of shares or principal amount. | [optional] 
**investment_discretion** | **str** | The investment discretion. | [optional] 
**voting_authority_sole** | **int** | The sole voting authority. | [optional] 
**voting_authority_shared** | **int** | The shared voting authority. | [optional] 
**voting_authority_none** | **int** | The no voting authority. | [optional] 

## Example

```python
from forms13f.models.api_v1_form_entry import ApiV1FormEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FormEntry from a JSON string
api_v1_form_entry_instance = ApiV1FormEntry.from_json(json)
# print the JSON string representation of the object
print(ApiV1FormEntry.to_json())

# convert the object into a dict
api_v1_form_entry_dict = api_v1_form_entry_instance.to_dict()
# create an instance of ApiV1FormEntry from a dict
api_v1_form_entry_from_dict = ApiV1FormEntry.from_dict(api_v1_form_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


