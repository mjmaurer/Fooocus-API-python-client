# ImgInpaintOrOutpaintRequestJsonImagePromptsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cn_img** | [**CnImg**](CnImg.md) |  | [optional] 
**cn_stop** | [**CnStop**](CnStop.md) |  | [optional] 
**cn_weight** | [**CnWeight**](CnWeight.md) |  | [optional] 
**cn_type** | [**ControlNetType**](ControlNetType.md) |  | [optional] 

## Example

```python
from fooocusapi_client.models.img_inpaint_or_outpaint_request_json_image_prompts_inner import ImgInpaintOrOutpaintRequestJsonImagePromptsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImgInpaintOrOutpaintRequestJsonImagePromptsInner from a JSON string
img_inpaint_or_outpaint_request_json_image_prompts_inner_instance = ImgInpaintOrOutpaintRequestJsonImagePromptsInner.from_json(json)
# print the JSON string representation of the object
print(ImgInpaintOrOutpaintRequestJsonImagePromptsInner.to_json())

# convert the object into a dict
img_inpaint_or_outpaint_request_json_image_prompts_inner_dict = img_inpaint_or_outpaint_request_json_image_prompts_inner_instance.to_dict()
# create an instance of ImgInpaintOrOutpaintRequestJsonImagePromptsInner from a dict
img_inpaint_or_outpaint_request_json_image_prompts_inner_form_dict = img_inpaint_or_outpaint_request_json_image_prompts_inner.from_dict(img_inpaint_or_outpaint_request_json_image_prompts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


