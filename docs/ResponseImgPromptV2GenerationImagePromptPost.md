# ResponseImgPromptV2GenerationImagePromptPost


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
from fooocusapi_client.models.response_img_prompt_v2_generation_image_prompt_post import ResponseImgPromptV2GenerationImagePromptPost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseImgPromptV2GenerationImagePromptPost from a JSON string
response_img_prompt_v2_generation_image_prompt_post_instance = ResponseImgPromptV2GenerationImagePromptPost.from_json(json)
# print the JSON string representation of the object
print(ResponseImgPromptV2GenerationImagePromptPost.to_json())

# convert the object into a dict
response_img_prompt_v2_generation_image_prompt_post_dict = response_img_prompt_v2_generation_image_prompt_post_instance.to_dict()
# create an instance of ResponseImgPromptV2GenerationImagePromptPost from a dict
response_img_prompt_v2_generation_image_prompt_post_form_dict = response_img_prompt_v2_generation_image_prompt_post.from_dict(response_img_prompt_v2_generation_image_prompt_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


