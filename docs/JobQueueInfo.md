# JobQueueInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**running_size** | **int** | The current running and waiting job count | 
**finished_size** | **int** | Finished job cound (after auto clean) | 
**last_job_id** | [**LastJobId**](LastJobId.md) |  | 

## Example

```python
from fooocusapi_client.models.job_queue_info import JobQueueInfo

# TODO update the JSON string below
json = "{}"
# create an instance of JobQueueInfo from a JSON string
job_queue_info_instance = JobQueueInfo.from_json(json)
# print the JSON string representation of the object
print(JobQueueInfo.to_json())

# convert the object into a dict
job_queue_info_dict = job_queue_info_instance.to_dict()
# create an instance of JobQueueInfo from a dict
job_queue_info_form_dict = job_queue_info.from_dict(job_queue_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


