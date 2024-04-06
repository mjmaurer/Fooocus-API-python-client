# Loras

Lora config in JSON. Format as [{\"model_name\": \"sd_xl_offset_example-lora_1.0.safetensors\", \"weight\": 0.5}]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from fooocusapi_client.models.loras import Loras

# TODO update the JSON string below
json = "{}"
# create an instance of Loras from a JSON string
loras_instance = Loras.from_json(json)
# print the JSON string representation of the object
print(Loras.to_json())

# convert the object into a dict
loras_dict = loras_instance.to_dict()
# create an instance of Loras from a dict
loras_form_dict = loras.from_dict(loras_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


