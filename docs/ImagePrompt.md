# ImagePrompt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cn_img** | [**CnImg**](CnImg.md) |  | [optional] 
**cn_stop** | [**CnStop**](CnStop.md) |  | [optional] 
**cn_weight** | [**CnWeight**](CnWeight.md) |  | [optional] 
**cn_type** | [**ControlNetType**](ControlNetType.md) |  | [optional] 

## Example

```python
from fooocusapi_client.models.image_prompt import ImagePrompt

# TODO update the JSON string below
json = "{}"
# create an instance of ImagePrompt from a JSON string
image_prompt_instance = ImagePrompt.from_json(json)
# print the JSON string representation of the object
print(ImagePrompt.to_json())

# convert the object into a dict
image_prompt_dict = image_prompt_instance.to_dict()
# create an instance of ImagePrompt from a dict
image_prompt_form_dict = image_prompt.from_dict(image_prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


