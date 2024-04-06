# ResponseText2ImgGenerationV1GenerationTextToImagePost


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
from fooocusapi_client.models.response_text2_img_generation_v1_generation_text_to_image_post import ResponseText2ImgGenerationV1GenerationTextToImagePost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseText2ImgGenerationV1GenerationTextToImagePost from a JSON string
response_text2_img_generation_v1_generation_text_to_image_post_instance = ResponseText2ImgGenerationV1GenerationTextToImagePost.from_json(json)
# print the JSON string representation of the object
print(ResponseText2ImgGenerationV1GenerationTextToImagePost.to_json())

# convert the object into a dict
response_text2_img_generation_v1_generation_text_to_image_post_dict = response_text2_img_generation_v1_generation_text_to_image_post_instance.to_dict()
# create an instance of ResponseText2ImgGenerationV1GenerationTextToImagePost from a dict
response_text2_img_generation_v1_generation_text_to_image_post_form_dict = response_text2_img_generation_v1_generation_text_to_image_post.from_dict(response_text2_img_generation_v1_generation_text_to_image_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


