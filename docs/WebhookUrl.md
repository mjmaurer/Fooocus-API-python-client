# WebhookUrl

Optional URL for a webhook callback. If provided, the system will send a POST request to this URL upon task completion or failure. This allows for asynchronous notification of task status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from fooocusapi_client.models.webhook_url import WebhookUrl

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookUrl from a JSON string
webhook_url_instance = WebhookUrl.from_json(json)
# print the JSON string representation of the object
print(WebhookUrl.to_json())

# convert the object into a dict
webhook_url_dict = webhook_url_instance.to_dict()
# create an instance of WebhookUrl from a dict
webhook_url_form_dict = webhook_url.from_dict(webhook_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


