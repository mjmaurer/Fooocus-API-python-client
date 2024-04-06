# JobHistoryInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**is_finished** | **bool** |  | [optional] [default to False]

## Example

```python
from fooocusapi_client.models.job_history_info import JobHistoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of JobHistoryInfo from a JSON string
job_history_info_instance = JobHistoryInfo.from_json(json)
# print the JSON string representation of the object
print(JobHistoryInfo.to_json())

# convert the object into a dict
job_history_info_dict = job_history_info_instance.to_dict()
# create an instance of JobHistoryInfo from a dict
job_history_info_form_dict = job_history_info.from_dict(job_history_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


