# ImgPromptRequestJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** |  | [optional] [default to '']
**negative_prompt** | **str** |  | [optional] [default to '']
**style_selections** | **List[str]** |  | [optional] [default to [Fooocus V2, Fooocus Enhance, Fooocus Sharp]]
**performance_selection** | [**PerfomanceSelection**](PerfomanceSelection.md) |  | [optional] 
**aspect_ratios_selection** | **str** |  | [optional] [default to '1152*896']
**image_number** | **int** | Image number | [optional] [default to 1]
**image_seed** | **int** | Seed to generate image, -1 for random | [optional] [default to -1]
**sharpness** | **float** |  | [optional] [default to 2.0]
**guidance_scale** | **float** |  | [optional] [default to 4.0]
**base_model_name** | **str** |  | [optional] [default to 'juggernautXL_version6Rundiffusion.safetensors']
**refiner_model_name** | **str** |  | [optional] [default to 'None']
**refiner_switch** | **float** | Refiner Switch At | [optional] [default to 0.5]
**loras** | [**List[Lora]**](Lora.md) |  | [optional] [default to [{model_name=sd_xl_offset_example-lora_1.0.safetensors, weight=0.1}]]
**advanced_params** | [**ImgInpaintOrOutpaintRequestJsonAdvancedParams**](ImgInpaintOrOutpaintRequestJsonAdvancedParams.md) |  | [optional] 
**require_base64** | **bool** | Return base64 data of generated image | [optional] [default to False]
**async_process** | **bool** | Set to true will run async and return job info for retrieve generataion result later | [optional] [default to False]
**webhook_url** | [**WebhookUrl**](WebhookUrl.md) |  | [optional] 
**input_image** | [**InputImage**](InputImage.md) |  | [optional] 
**input_mask** | [**InputMask**](InputMask.md) |  | [optional] 
**inpaint_additional_prompt** | [**InpaintAdditionalPrompt1**](InpaintAdditionalPrompt1.md) |  | [optional] 
**outpaint_selections** | [**List[OutpaintExpansion]**](OutpaintExpansion.md) |  | [optional] [default to []]
**outpaint_distance_left** | [**OutpaintDistanceLeft**](OutpaintDistanceLeft.md) |  | [optional] 
**outpaint_distance_right** | [**OutpaintDistanceRight**](OutpaintDistanceRight.md) |  | [optional] 
**outpaint_distance_top** | [**OutpaintDistanceTop**](OutpaintDistanceTop.md) |  | [optional] 
**outpaint_distance_bottom** | [**OutpaintDistanceBottom**](OutpaintDistanceBottom.md) |  | [optional] 
**image_prompts** | [**List[ImgInpaintOrOutpaintRequestJsonImagePromptsInner]**](ImgInpaintOrOutpaintRequestJsonImagePromptsInner.md) |  | 

## Example

```python
from fooocusapi_client.models.img_prompt_request_json import ImgPromptRequestJson

# TODO update the JSON string below
json = "{}"
# create an instance of ImgPromptRequestJson from a JSON string
img_prompt_request_json_instance = ImgPromptRequestJson.from_json(json)
# print the JSON string representation of the object
print(ImgPromptRequestJson.to_json())

# convert the object into a dict
img_prompt_request_json_dict = img_prompt_request_json_instance.to_dict()
# create an instance of ImgPromptRequestJson from a dict
img_prompt_request_json_form_dict = img_prompt_request_json.from_dict(img_prompt_request_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


