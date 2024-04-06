# ResponseTextToImgWithIpV2GenerationTextToImageWithIpPost


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
from fooocusapi_client.models.response_text_to_img_with_ip_v2_generation_text_to_image_with_ip_post import ResponseTextToImgWithIpV2GenerationTextToImageWithIpPost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseTextToImgWithIpV2GenerationTextToImageWithIpPost from a JSON string
response_text_to_img_with_ip_v2_generation_text_to_image_with_ip_post_instance = ResponseTextToImgWithIpV2GenerationTextToImageWithIpPost.from_json(json)
# print the JSON string representation of the object
print(ResponseTextToImgWithIpV2GenerationTextToImageWithIpPost.to_json())

# convert the object into a dict
response_text_to_img_with_ip_v2_generation_text_to_image_with_ip_post_dict = response_text_to_img_with_ip_v2_generation_text_to_image_with_ip_post_instance.to_dict()
# create an instance of ResponseTextToImgWithIpV2GenerationTextToImageWithIpPost from a dict
response_text_to_img_with_ip_v2_generation_text_to_image_with_ip_post_form_dict = response_text_to_img_with_ip_v2_generation_text_to_image_with_ip_post.from_dict(response_text_to_img_with_ip_v2_generation_text_to_image_with_ip_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


