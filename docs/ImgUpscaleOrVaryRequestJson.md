# ImgUpscaleOrVaryRequestJson


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
**uov_method** | [**UpscaleOrVaryMethod**](UpscaleOrVaryMethod.md) |  | [optional] 
**upscale_value** | [**UpscaleValue1**](UpscaleValue1.md) |  | [optional] 
**input_image** | **str** | Init image for upsacale or outpaint as base64 | 
**image_prompts** | [**List[ImgInpaintOrOutpaintRequestJsonImagePromptsInner]**](ImgInpaintOrOutpaintRequestJsonImagePromptsInner.md) |  | [optional] [default to []]

## Example

```python
from fooocusapi_client.models.img_upscale_or_vary_request_json import ImgUpscaleOrVaryRequestJson

# TODO update the JSON string below
json = "{}"
# create an instance of ImgUpscaleOrVaryRequestJson from a JSON string
img_upscale_or_vary_request_json_instance = ImgUpscaleOrVaryRequestJson.from_json(json)
# print the JSON string representation of the object
print(ImgUpscaleOrVaryRequestJson.to_json())

# convert the object into a dict
img_upscale_or_vary_request_json_dict = img_upscale_or_vary_request_json_instance.to_dict()
# create an instance of ImgUpscaleOrVaryRequestJson from a dict
img_upscale_or_vary_request_json_form_dict = img_upscale_or_vary_request_json.from_dict(img_upscale_or_vary_request_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


