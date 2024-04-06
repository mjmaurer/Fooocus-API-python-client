# JobHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queue** | [**List[JobHistoryInfo]**](JobHistoryInfo.md) |  | [optional] [default to []]
**history** | [**List[JobHistoryInfo]**](JobHistoryInfo.md) |  | [optional] [default to []]

## Example

```python
from fooocusapi_client.models.job_history_response import JobHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobHistoryResponse from a JSON string
job_history_response_instance = JobHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(JobHistoryResponse.to_json())

# convert the object into a dict
job_history_response_dict = job_history_response_instance.to_dict()
# create an instance of JobHistoryResponse from a dict
job_history_response_form_dict = job_history_response.from_dict(job_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


