# AsyncJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Job ID | 
**job_type** | [**TaskType**](TaskType.md) | Job type | 
**job_stage** | [**AsyncJobStage**](AsyncJobStage.md) | Job running stage | 
**job_progress** | **int** | Job running progress, 100 is for finished. | 
**job_status** | [**JobStatus**](JobStatus.md) |  | [optional] 
**job_step_preview** | [**JobStepPreview**](JobStepPreview.md) |  | [optional] 
**job_result** | [**JobResult**](JobResult.md) |  | [optional] 

## Example

```python
from fooocusapi_client.models.async_job_response import AsyncJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncJobResponse from a JSON string
async_job_response_instance = AsyncJobResponse.from_json(json)
# print the JSON string representation of the object
print(AsyncJobResponse.to_json())

# convert the object into a dict
async_job_response_dict = async_job_response_instance.to_dict()
# create an instance of AsyncJobResponse from a dict
async_job_response_form_dict = async_job_response.from_dict(async_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


