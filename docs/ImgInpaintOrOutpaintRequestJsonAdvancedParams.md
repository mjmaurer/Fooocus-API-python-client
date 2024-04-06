# ImgInpaintOrOutpaintRequestJsonAdvancedParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_preview** | **object** | Disable preview during generation | [optional] 
**adm_scaler_positive** | **object** | Positive ADM Guidance Scaler | [optional] 
**adm_scaler_negative** | **object** | Negative ADM Guidance Scaler | [optional] 
**adm_scaler_end** | **object** | ADM Guidance End At Step | [optional] 
**refiner_swap_method** | **object** | Refiner swap method | [optional] 
**adaptive_cfg** | **object** | CFG Mimicking from TSNR | [optional] 
**sampler_name** | **object** | Sampler | [optional] 
**scheduler_name** | **object** | Scheduler | [optional] 
**overwrite_step** | **object** | Forced Overwrite of Sampling Step | [optional] 
**overwrite_switch** | **object** | Forced Overwrite of Refiner Switch Step | [optional] 
**overwrite_width** | **object** | Forced Overwrite of Generating Width | [optional] 
**overwrite_height** | **object** | Forced Overwrite of Generating Height | [optional] 
**overwrite_vary_strength** | **object** | Forced Overwrite of Denoising Strength of \&quot;Vary\&quot; | [optional] 
**overwrite_upscale_strength** | **object** | Forced Overwrite of Denoising Strength of \&quot;Upscale\&quot; | [optional] 
**mixing_image_prompt_and_vary_upscale** | **object** | Mixing Image Prompt and Vary/Upscale | [optional] 
**mixing_image_prompt_and_inpaint** | **object** | Mixing Image Prompt and Inpaint | [optional] 
**debugging_cn_preprocessor** | **object** | Debug Preprocessors | [optional] 
**skipping_cn_preprocessor** | **object** | Skip Preprocessors | [optional] 
**controlnet_softness** | **object** | Softness of ControlNet | [optional] 
**canny_low_threshold** | **object** | Canny Low Threshold | [optional] 
**canny_high_threshold** | **object** | Canny High Threshold | [optional] 
**freeu_enabled** | **object** | FreeU enabled | [optional] 
**freeu_b1** | **object** | FreeU B1 | [optional] 
**freeu_b2** | **object** | FreeU B2 | [optional] 
**freeu_s1** | **object** | FreeU B3 | [optional] 
**freeu_s2** | **object** | FreeU B4 | [optional] 
**debugging_inpaint_preprocessor** | **object** | Debug Inpaint Preprocessing | [optional] 
**inpaint_disable_initial_latent** | **object** | Disable initial latent in inpaint | [optional] 
**inpaint_engine** | **object** | Inpaint Engine | [optional] 
**inpaint_strength** | **object** | Inpaint Denoising Strength | [optional] 
**inpaint_respective_field** | **object** | Inpaint Respective Field | [optional] 
**invert_mask_checkbox** | **object** | Invert Mask | [optional] 
**inpaint_erode_or_dilate** | **object** | Mask Erode or Dilate | [optional] 

## Example

```python
from fooocusapi_client.models.img_inpaint_or_outpaint_request_json_advanced_params import ImgInpaintOrOutpaintRequestJsonAdvancedParams

# TODO update the JSON string below
json = "{}"
# create an instance of ImgInpaintOrOutpaintRequestJsonAdvancedParams from a JSON string
img_inpaint_or_outpaint_request_json_advanced_params_instance = ImgInpaintOrOutpaintRequestJsonAdvancedParams.from_json(json)
# print the JSON string representation of the object
print(ImgInpaintOrOutpaintRequestJsonAdvancedParams.to_json())

# convert the object into a dict
img_inpaint_or_outpaint_request_json_advanced_params_dict = img_inpaint_or_outpaint_request_json_advanced_params_instance.to_dict()
# create an instance of ImgInpaintOrOutpaintRequestJsonAdvancedParams from a dict
img_inpaint_or_outpaint_request_json_advanced_params_form_dict = img_inpaint_or_outpaint_request_json_advanced_params.from_dict(img_inpaint_or_outpaint_request_json_advanced_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


