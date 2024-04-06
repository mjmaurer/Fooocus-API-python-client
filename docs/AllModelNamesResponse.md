# AllModelNamesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_filenames** | **List[str]** | All available model filenames | 
**lora_filenames** | **List[str]** | All available lora filenames | 

## Example

```python
from fooocusapi_client.models.all_model_names_response import AllModelNamesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllModelNamesResponse from a JSON string
all_model_names_response_instance = AllModelNamesResponse.from_json(json)
# print the JSON string representation of the object
print(AllModelNamesResponse.to_json())

# convert the object into a dict
all_model_names_response_dict = all_model_names_response_instance.to_dict()
# create an instance of AllModelNamesResponse from a dict
all_model_names_response_form_dict = all_model_names_response.from_dict(all_model_names_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


