# ImagePromptJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cn_img** | [**CnImg1**](CnImg1.md) |  | [optional] 
**cn_stop** | [**CnStop1**](CnStop1.md) |  | [optional] 
**cn_weight** | [**CnWeight1**](CnWeight1.md) |  | [optional] 
**cn_type** | [**ControlNetType**](ControlNetType.md) | ControlNet type for image prompt | [optional] 

## Example

```python
from fooocusapi_client.models.image_prompt_json import ImagePromptJson

# TODO update the JSON string below
json = "{}"
# create an instance of ImagePromptJson from a JSON string
image_prompt_json_instance = ImagePromptJson.from_json(json)
# print the JSON string representation of the object
print(ImagePromptJson.to_json())

# convert the object into a dict
image_prompt_json_dict = image_prompt_json_instance.to_dict()
# create an instance of ImagePromptJson from a dict
image_prompt_json_form_dict = image_prompt_json.from_dict(image_prompt_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


