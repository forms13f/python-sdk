# ApiV1Form


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the form. | [optional] 
**accession_number** | **str** | The accession number of the form. | [optional] 
**submission_type** | **str** | The submission type of the form. | [optional] 
**public_document_count** | **int** | The public document count. | [optional] 
**period_of_report** | **date** | The period of the report. | [optional] 
**filed_as_of_date** | **date** | The filed as of date. | [optional] 
**date_as_of_change** | **date** | The date as of change. | [optional] 
**effectiveness_date** | **date** | The effectiveness date. | [optional] 
**cik** | **str** | The Central Index Key (CIK). | [optional] 
**company_name** | **str** | The company name. | [optional] 
**irs_number** | **str** | The IRS number. | [optional] 
**state_of_incorporation** | **str** | The state of incorporation. | [optional] 
**fiscal_year_end** | **str** | The fiscal year end. | [optional] 
**form_type** | **str** | The form type. | [optional] 
**sec_act** | **str** | The SEC act. | [optional] 
**sec_file_number** | **str** | The SEC file number. | [optional] 
**film_number** | **str** | The film number. | [optional] 
**business_address** | **str** | The business address. | [optional] 
**business_phone** | **str** | The business phone. | [optional] 
**table_value_total** | **int** | The total value of the table. | [optional] 
**table_entry_total** | **int** | The total entry count of the table. | [optional] 
**is_amendment** | **bool** | Indicates if the form is an amendment. | [optional] 
**amendment_type** | **str** | The type of amendment. | [optional] 
**conf_denied_expired** | **bool** | Indicates if the confidentiality request was denied or expired. | [optional] 
**conf_date_denied_expired** | **date** | The date when the confidentiality request was denied or expired. | [optional] 
**amendment_date_reported** | **date** | The date when the amendment was reported. | [optional] 

## Example

```python
from forms13f.models.api_v1_form import ApiV1Form

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1Form from a JSON string
api_v1_form_instance = ApiV1Form.from_json(json)
# print the JSON string representation of the object
print(ApiV1Form.to_json())

# convert the object into a dict
api_v1_form_dict = api_v1_form_instance.to_dict()
# create an instance of ApiV1Form from a dict
api_v1_form_from_dict = ApiV1Form.from_dict(api_v1_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


