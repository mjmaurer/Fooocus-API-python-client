# ResponseImgUpscaleOrVaryV2V2GenerationImageUpscaleVaryPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **object** | Job ID | 
**job_type** | [**TaskType**](TaskType.md) | Job type | 
**job_stage** | [**AsyncJobStage**](AsyncJobStage.md) | Job running stage | 
**job_progress** | **object** | Job running progress, 100 is for finished. | 
**job_status** | [**JobStatus**](JobStatus.md) |  | [optional] 
**job_step_preview** | [**JobStepPreview**](JobStepPreview.md) |  | [optional] 
**job_result** | [**JobResult**](JobResult.md) |  | [optional] 

## Example

```python
from fooocusapi_client.models.response_img_upscale_or_vary_v2_v2_generation_image_upscale_vary_post import ResponseImgUpscaleOrVaryV2V2GenerationImageUpscaleVaryPost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseImgUpscaleOrVaryV2V2GenerationImageUpscaleVaryPost from a JSON string
response_img_upscale_or_vary_v2_v2_generation_image_upscale_vary_post_instance = ResponseImgUpscaleOrVaryV2V2GenerationImageUpscaleVaryPost.from_json(json)
# print the JSON string representation of the object
print(ResponseImgUpscaleOrVaryV2V2GenerationImageUpscaleVaryPost.to_json())

# convert the object into a dict
response_img_upscale_or_vary_v2_v2_generation_image_upscale_vary_post_dict = response_img_upscale_or_vary_v2_v2_generation_image_upscale_vary_post_instance.to_dict()
# create an instance of ResponseImgUpscaleOrVaryV2V2GenerationImageUpscaleVaryPost from a dict
response_img_upscale_or_vary_v2_v2_generation_image_upscale_vary_post_form_dict = response_img_upscale_or_vary_v2_v2_generation_image_upscale_vary_post.from_dict(response_img_upscale_or_vary_v2_v2_generation_image_upscale_vary_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


