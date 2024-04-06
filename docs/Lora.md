# Lora


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_name** | **str** |  | 
**weight** | **float** |  | [optional] [default to 0.5]

## Example

```python
from fooocusapi_client.models.lora import Lora

# TODO update the JSON string below
json = "{}"
# create an instance of Lora from a JSON string
lora_instance = Lora.from_json(json)
# print the JSON string representation of the object
print(Lora.to_json())

# convert the object into a dict
lora_dict = lora_instance.to_dict()
# create an instance of Lora from a dict
lora_form_dict = lora.from_dict(lora_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


