# ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost


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
from fooocusapi_client.models.response_img_inpaint_or_outpaint_v2_v2_generation_image_inpaint_outpaint_post import ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost from a JSON string
response_img_inpaint_or_outpaint_v2_v2_generation_image_inpaint_outpaint_post_instance = ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost.from_json(json)
# print the JSON string representation of the object
print(ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost.to_json())

# convert the object into a dict
response_img_inpaint_or_outpaint_v2_v2_generation_image_inpaint_outpaint_post_dict = response_img_inpaint_or_outpaint_v2_v2_generation_image_inpaint_outpaint_post_instance.to_dict()
# create an instance of ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost from a dict
response_img_inpaint_or_outpaint_v2_v2_generation_image_inpaint_outpaint_post_form_dict = response_img_inpaint_or_outpaint_v2_v2_generation_image_inpaint_outpaint_post.from_dict(response_img_inpaint_or_outpaint_v2_v2_generation_image_inpaint_outpaint_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


