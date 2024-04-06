# fooocusapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_models_v1_engines_all_models_get**](DefaultApi.md#all_models_v1_engines_all_models_get) | **GET** /v1/engines/all-models | All Models
[**all_styles_v1_engines_styles_get**](DefaultApi.md#all_styles_v1_engines_styles_get) | **GET** /v1/engines/styles | All Styles
[**describe_image_v1_tools_describe_image_post**](DefaultApi.md#describe_image_v1_tools_describe_image_post) | **POST** /v1/tools/describe-image | Describe Image
[**get_history_v1_generation_job_history_get**](DefaultApi.md#get_history_v1_generation_job_history_get) | **GET** /v1/generation/job-history | Get History
[**home_get**](DefaultApi.md#home_get) | **GET** / | Home
[**img_inpaint_or_outpaint_v1_generation_image_inpaint_outpaint_post**](DefaultApi.md#img_inpaint_or_outpaint_v1_generation_image_inpaint_outpaint_post) | **POST** /v1/generation/image-inpaint-outpaint | Img Inpaint Or Outpaint
[**img_inpaint_or_outpaint_v2_v2_generation_image_inpaint_outpaint_post**](DefaultApi.md#img_inpaint_or_outpaint_v2_v2_generation_image_inpaint_outpaint_post) | **POST** /v2/generation/image-inpaint-outpaint | Img Inpaint Or Outpaint V2
[**img_prompt_v1_generation_image_prompt_post**](DefaultApi.md#img_prompt_v1_generation_image_prompt_post) | **POST** /v1/generation/image-prompt | Img Prompt
[**img_prompt_v2_generation_image_prompt_post**](DefaultApi.md#img_prompt_v2_generation_image_prompt_post) | **POST** /v2/generation/image-prompt | Img Prompt
[**img_upscale_or_vary_v1_generation_image_upscale_vary_post**](DefaultApi.md#img_upscale_or_vary_v1_generation_image_upscale_vary_post) | **POST** /v1/generation/image-upscale-vary | Img Upscale Or Vary
[**img_upscale_or_vary_v2_v2_generation_image_upscale_vary_post**](DefaultApi.md#img_upscale_or_vary_v2_v2_generation_image_upscale_vary_post) | **POST** /v2/generation/image-upscale-vary | Img Upscale Or Vary V2
[**job_queue_v1_generation_job_queue_get**](DefaultApi.md#job_queue_v1_generation_job_queue_get) | **GET** /v1/generation/job-queue | Job Queue
[**ping_ping_get**](DefaultApi.md#ping_ping_get) | **GET** /ping | Ping
[**query_job_v1_generation_query_job_get**](DefaultApi.md#query_job_v1_generation_query_job_get) | **GET** /v1/generation/query-job | Query Job
[**refresh_models_v1_engines_refresh_models_post**](DefaultApi.md#refresh_models_v1_engines_refresh_models_post) | **POST** /v1/engines/refresh-models | Refresh Models
[**stop_v1_generation_stop_post**](DefaultApi.md#stop_v1_generation_stop_post) | **POST** /v1/generation/stop | Stop
[**text2img_generation_v1_generation_text_to_image_post**](DefaultApi.md#text2img_generation_v1_generation_text_to_image_post) | **POST** /v1/generation/text-to-image | Text2Img Generation
[**text_to_img_with_ip_v2_generation_text_to_image_with_ip_post**](DefaultApi.md#text_to_img_with_ip_v2_generation_text_to_image_with_ip_post) | **POST** /v2/generation/text-to-image-with-ip | Text To Img With Ip


# **all_models_v1_engines_all_models_get**
> AllModelNamesResponse all_models_v1_engines_all_models_get()

All Models

Get all filenames of base model and lora

### Example


```python
import fooocusapi_client
from fooocusapi_client.models.all_model_names_response import AllModelNamesResponse
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)

    try:
        # All Models
        api_response = api_instance.all_models_v1_engines_all_models_get()
        print("The response of DefaultApi->all_models_v1_engines_all_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->all_models_v1_engines_all_models_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AllModelNamesResponse**](AllModelNamesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_styles_v1_engines_styles_get**
> List[str] all_styles_v1_engines_styles_get()

All Styles

Get all legal Fooocus styles

### Example


```python
import fooocusapi_client
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)

    try:
        # All Styles
        api_response = api_instance.all_styles_v1_engines_styles_get()
        print("The response of DefaultApi->all_styles_v1_engines_styles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->all_styles_v1_engines_styles_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_image_v1_tools_describe_image_post**
> DescribeImageResponse describe_image_v1_tools_describe_image_post(image, type=type)

Describe Image

### Example


```python
import fooocusapi_client
from fooocusapi_client.models.describe_image_response import DescribeImageResponse
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)
    image = None # bytearray | 
    type = fooocusapi_client.DescribeImageType() # DescribeImageType | Image type, 'Photo' or 'Anime' (optional)

    try:
        # Describe Image
        api_response = api_instance.describe_image_v1_tools_describe_image_post(image, type=type)
        print("The response of DefaultApi->describe_image_v1_tools_describe_image_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->describe_image_v1_tools_describe_image_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **bytearray**|  | 
 **type** | [**DescribeImageType**](.md)| Image type, &#39;Photo&#39; or &#39;Anime&#39; | [optional] 

### Return type

[**DescribeImageResponse**](DescribeImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history_v1_generation_job_history_get**
> ResponseGetHistoryV1GenerationJobHistoryGet get_history_v1_generation_job_history_get(job_id=job_id, page=page, page_size=page_size)

Get History

Query historical job data

### Example


```python
import fooocusapi_client
from fooocusapi_client.models.response_get_history_v1_generation_job_history_get import ResponseGetHistoryV1GenerationJobHistoryGet
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)
    job_id = 'job_id_example' # str |  (optional)
    page = 0 # int |  (optional) (default to 0)
    page_size = 20 # int |  (optional) (default to 20)

    try:
        # Get History
        api_response = api_instance.get_history_v1_generation_job_history_get(job_id=job_id, page=page, page_size=page_size)
        print("The response of DefaultApi->get_history_v1_generation_job_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_history_v1_generation_job_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 20]

### Return type

[**ResponseGetHistoryV1GenerationJobHistoryGet**](ResponseGetHistoryV1GenerationJobHistoryGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **home_get**
> object home_get()

Home

### Example


```python
import fooocusapi_client
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)

    try:
        # Home
        api_response = api_instance.home_get()
        print("The response of DefaultApi->home_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->home_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **img_inpaint_or_outpaint_v1_generation_image_inpaint_outpaint_post**
> ResponseImgInpaintOrOutpaintV1GenerationImageInpaintOutpaintPost img_inpaint_or_outpaint_v1_generation_image_inpaint_outpaint_post(input_image, accept=accept, accept2=accept2, input_mask=input_mask, inpaint_additional_prompt=inpaint_additional_prompt, outpaint_selections=outpaint_selections, outpaint_distance_left=outpaint_distance_left, outpaint_distance_right=outpaint_distance_right, outpaint_distance_top=outpaint_distance_top, outpaint_distance_bottom=outpaint_distance_bottom, prompt=prompt, negative_prompt=negative_prompt, style_selections=style_selections, performance_selection=performance_selection, aspect_ratios_selection=aspect_ratios_selection, image_number=image_number, image_seed=image_seed, sharpness=sharpness, guidance_scale=guidance_scale, base_model_name=base_model_name, refiner_model_name=refiner_model_name, refiner_switch=refiner_switch, loras=loras, advanced_params=advanced_params, require_base64=require_base64, async_process=async_process)

Img Inpaint Or Outpaint

### Example


```python
import fooocusapi_client
from fooocusapi_client.models.advanced_params import AdvancedParams
from fooocusapi_client.models.inpaint_additional_prompt import InpaintAdditionalPrompt
from fooocusapi_client.models.loras import Loras
from fooocusapi_client.models.response_img_inpaint_or_outpaint_v1_generation_image_inpaint_outpaint_post import ResponseImgInpaintOrOutpaintV1GenerationImageInpaintOutpaintPost
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)
    input_image = None # bytearray | Init image for inpaint or outpaint
    accept = fooocusapi_client.Accept() # Accept | Parameter to overvide 'Accept' header, 'image/png' for output bytes (optional)
    accept2 = 'accept_example' # str |  (optional)
    input_mask = None # bytearray | Inpaint or outpaint mask (optional)
    inpaint_additional_prompt = fooocusapi_client.InpaintAdditionalPrompt() # InpaintAdditionalPrompt |  (optional)
    outpaint_selections = ['outpaint_selections_example'] # List[str] | Outpaint expansion selections, literal 'Left', 'Right', 'Top', 'Bottom' seperated by comma (optional)
    outpaint_distance_left = 0 # int | Set outpaint left distance, -1 for default (optional) (default to 0)
    outpaint_distance_right = 0 # int | Set outpaint right distance, -1 for default (optional) (default to 0)
    outpaint_distance_top = 0 # int | Set outpaint top distance, -1 for default (optional) (default to 0)
    outpaint_distance_bottom = 0 # int | Set outpaint bottom distance, -1 for default (optional) (default to 0)
    prompt = '' # str |  (optional) (default to '')
    negative_prompt = '' # str |  (optional) (default to '')
    style_selections = ['style_selections_example'] # List[str] | Fooocus style selections, seperated by comma (optional)
    performance_selection = fooocusapi_client.PerfomanceSelection() # PerfomanceSelection | Performance Selection, one of 'Speed','Quality','Extreme Speed' (optional)
    aspect_ratios_selection = '1152*896' # str | Aspect Ratios Selection, default 1152*896 (optional) (default to '1152*896')
    image_number = 1 # int | Image number (optional) (default to 1)
    image_seed = -1 # int | Seed to generate image, -1 for random (optional) (default to -1)
    sharpness = 2.0 # float |  (optional) (default to 2.0)
    guidance_scale = 4.0 # float |  (optional) (default to 4.0)
    base_model_name = 'juggernautXL_version6Rundiffusion.safetensors' # str |  (optional) (default to 'juggernautXL_version6Rundiffusion.safetensors')
    refiner_model_name = 'None' # str |  (optional) (default to 'None')
    refiner_switch = 0.5 # float | Refiner Switch At (optional) (default to 0.5)
    loras = fooocusapi_client.Loras() # Loras |  (optional)
    advanced_params = fooocusapi_client.AdvancedParams() # AdvancedParams |  (optional)
    require_base64 = False # bool | Return base64 data of generated image (optional) (default to False)
    async_process = False # bool | Set to true will run async and return job info for retrieve generataion result later (optional) (default to False)

    try:
        # Img Inpaint Or Outpaint
        api_response = api_instance.img_inpaint_or_outpaint_v1_generation_image_inpaint_outpaint_post(input_image, accept=accept, accept2=accept2, input_mask=input_mask, inpaint_additional_prompt=inpaint_additional_prompt, outpaint_selections=outpaint_selections, outpaint_distance_left=outpaint_distance_left, outpaint_distance_right=outpaint_distance_right, outpaint_distance_top=outpaint_distance_top, outpaint_distance_bottom=outpaint_distance_bottom, prompt=prompt, negative_prompt=negative_prompt, style_selections=style_selections, performance_selection=performance_selection, aspect_ratios_selection=aspect_ratios_selection, image_number=image_number, image_seed=image_seed, sharpness=sharpness, guidance_scale=guidance_scale, base_model_name=base_model_name, refiner_model_name=refiner_model_name, refiner_switch=refiner_switch, loras=loras, advanced_params=advanced_params, require_base64=require_base64, async_process=async_process)
        print("The response of DefaultApi->img_inpaint_or_outpaint_v1_generation_image_inpaint_outpaint_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->img_inpaint_or_outpaint_v1_generation_image_inpaint_outpaint_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_image** | **bytearray**| Init image for inpaint or outpaint | 
 **accept** | [**Accept**](.md)| Parameter to overvide &#39;Accept&#39; header, &#39;image/png&#39; for output bytes | [optional] 
 **accept2** | **str**|  | [optional] 
 **input_mask** | **bytearray**| Inpaint or outpaint mask | [optional] 
 **inpaint_additional_prompt** | [**InpaintAdditionalPrompt**](InpaintAdditionalPrompt.md)|  | [optional] 
 **outpaint_selections** | [**List[str]**](str.md)| Outpaint expansion selections, literal &#39;Left&#39;, &#39;Right&#39;, &#39;Top&#39;, &#39;Bottom&#39; seperated by comma | [optional] 
 **outpaint_distance_left** | **int**| Set outpaint left distance, -1 for default | [optional] [default to 0]
 **outpaint_distance_right** | **int**| Set outpaint right distance, -1 for default | [optional] [default to 0]
 **outpaint_distance_top** | **int**| Set outpaint top distance, -1 for default | [optional] [default to 0]
 **outpaint_distance_bottom** | **int**| Set outpaint bottom distance, -1 for default | [optional] [default to 0]
 **prompt** | **str**|  | [optional] [default to &#39;&#39;]
 **negative_prompt** | **str**|  | [optional] [default to &#39;&#39;]
 **style_selections** | [**List[str]**](str.md)| Fooocus style selections, seperated by comma | [optional] 
 **performance_selection** | [**PerfomanceSelection**](PerfomanceSelection.md)| Performance Selection, one of &#39;Speed&#39;,&#39;Quality&#39;,&#39;Extreme Speed&#39; | [optional] 
 **aspect_ratios_selection** | **str**| Aspect Ratios Selection, default 1152*896 | [optional] [default to &#39;1152*896&#39;]
 **image_number** | **int**| Image number | [optional] [default to 1]
 **image_seed** | **int**| Seed to generate image, -1 for random | [optional] [default to -1]
 **sharpness** | **float**|  | [optional] [default to 2.0]
 **guidance_scale** | **float**|  | [optional] [default to 4.0]
 **base_model_name** | **str**|  | [optional] [default to &#39;juggernautXL_version6Rundiffusion.safetensors&#39;]
 **refiner_model_name** | **str**|  | [optional] [default to &#39;None&#39;]
 **refiner_switch** | **float**| Refiner Switch At | [optional] [default to 0.5]
 **loras** | [**Loras**](Loras.md)|  | [optional] 
 **advanced_params** | [**AdvancedParams**](AdvancedParams.md)|  | [optional] 
 **require_base64** | **bool**| Return base64 data of generated image | [optional] [default to False]
 **async_process** | **bool**| Set to true will run async and return job info for retrieve generataion result later | [optional] [default to False]

### Return type

[**ResponseImgInpaintOrOutpaintV1GenerationImageInpaintOutpaintPost**](ResponseImgInpaintOrOutpaintV1GenerationImageInpaintOutpaintPost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/json async, image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PNG bytes if request&#39;s &#39;Accept&#39; header is &#39;image/png&#39;, otherwise JSON |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **img_inpaint_or_outpaint_v2_v2_generation_image_inpaint_outpaint_post**
> ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost img_inpaint_or_outpaint_v2_v2_generation_image_inpaint_outpaint_post(img_inpaint_or_outpaint_request_json, accept=accept, accept2=accept2)

Img Inpaint Or Outpaint V2

### Example


```python
import fooocusapi_client
from fooocusapi_client.models.img_inpaint_or_outpaint_request_json import ImgInpaintOrOutpaintRequestJson
from fooocusapi_client.models.response_img_inpaint_or_outpaint_v2_v2_generation_image_inpaint_outpaint_post import ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)
    img_inpaint_or_outpaint_request_json = fooocusapi_client.ImgInpaintOrOutpaintRequestJson() # ImgInpaintOrOutpaintRequestJson | 
    accept = fooocusapi_client.Accept() # Accept | Parameter to overvide 'Accept' header, 'image/png' for output bytes (optional)
    accept2 = 'accept_example' # str |  (optional)

    try:
        # Img Inpaint Or Outpaint V2
        api_response = api_instance.img_inpaint_or_outpaint_v2_v2_generation_image_inpaint_outpaint_post(img_inpaint_or_outpaint_request_json, accept=accept, accept2=accept2)
        print("The response of DefaultApi->img_inpaint_or_outpaint_v2_v2_generation_image_inpaint_outpaint_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->img_inpaint_or_outpaint_v2_v2_generation_image_inpaint_outpaint_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **img_inpaint_or_outpaint_request_json** | [**ImgInpaintOrOutpaintRequestJson**](ImgInpaintOrOutpaintRequestJson.md)|  | 
 **accept** | [**Accept**](.md)| Parameter to overvide &#39;Accept&#39; header, &#39;image/png&#39; for output bytes | [optional] 
 **accept2** | **str**|  | [optional] 

### Return type

[**ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost**](ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json async, image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PNG bytes if request&#39;s &#39;Accept&#39; header is &#39;image/png&#39;, otherwise JSON |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **img_prompt_v1_generation_image_prompt_post**
> ResponseImgPromptV1GenerationImagePromptPost img_prompt_v1_generation_image_prompt_post(accept=accept, accept2=accept2, cn_img1=cn_img1, input_image=input_image, input_mask=input_mask, inpaint_additional_prompt=inpaint_additional_prompt, outpaint_selections=outpaint_selections, outpaint_distance_left=outpaint_distance_left, outpaint_distance_right=outpaint_distance_right, outpaint_distance_top=outpaint_distance_top, outpaint_distance_bottom=outpaint_distance_bottom, cn_stop1=cn_stop1, cn_weight1=cn_weight1, cn_type1=cn_type1, cn_img2=cn_img2, cn_stop2=cn_stop2, cn_weight2=cn_weight2, cn_type2=cn_type2, cn_img3=cn_img3, cn_stop3=cn_stop3, cn_weight3=cn_weight3, cn_type3=cn_type3, cn_img4=cn_img4, cn_stop4=cn_stop4, cn_weight4=cn_weight4, cn_type4=cn_type4, prompt=prompt, negative_prompt=negative_prompt, style_selections=style_selections, performance_selection=performance_selection, aspect_ratios_selection=aspect_ratios_selection, image_number=image_number, image_seed=image_seed, sharpness=sharpness, guidance_scale=guidance_scale, base_model_name=base_model_name, refiner_model_name=refiner_model_name, refiner_switch=refiner_switch, loras=loras, advanced_params=advanced_params, require_base64=require_base64, async_process=async_process)

Img Prompt

### Example


```python
import fooocusapi_client
from fooocusapi_client.models.advanced_params import AdvancedParams
from fooocusapi_client.models.cn_stop1 import CnStop1
from fooocusapi_client.models.cn_stop2 import CnStop2
from fooocusapi_client.models.cn_stop3 import CnStop3
from fooocusapi_client.models.cn_stop4 import CnStop4
from fooocusapi_client.models.cn_weight1 import CnWeight1
from fooocusapi_client.models.cn_weight2 import CnWeight2
from fooocusapi_client.models.cn_weight3 import CnWeight3
from fooocusapi_client.models.cn_weight4 import CnWeight4
from fooocusapi_client.models.inpaint_additional_prompt import InpaintAdditionalPrompt
from fooocusapi_client.models.loras import Loras
from fooocusapi_client.models.response_img_prompt_v1_generation_image_prompt_post import ResponseImgPromptV1GenerationImagePromptPost
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)
    accept = fooocusapi_client.Accept() # Accept | Parameter to overvide 'Accept' header, 'image/png' for output bytes (optional)
    accept2 = 'accept_example' # str |  (optional)
    cn_img1 = None # bytearray | Input image for image prompt (optional)
    input_image = None # bytearray | Init image for inpaint or outpaint (optional)
    input_mask = None # bytearray | Inpaint or outpaint mask (optional)
    inpaint_additional_prompt = fooocusapi_client.InpaintAdditionalPrompt() # InpaintAdditionalPrompt |  (optional)
    outpaint_selections = ['outpaint_selections_example'] # List[str] | Outpaint expansion selections, literal 'Left', 'Right', 'Top', 'Bottom' seperated by comma (optional)
    outpaint_distance_left = 0 # int | Set outpaint left distance, 0 for default (optional) (default to 0)
    outpaint_distance_right = 0 # int | Set outpaint right distance, 0 for default (optional) (default to 0)
    outpaint_distance_top = 0 # int | Set outpaint top distance, 0 for default (optional) (default to 0)
    outpaint_distance_bottom = 0 # int | Set outpaint bottom distance, 0 for default (optional) (default to 0)
    cn_stop1 = fooocusapi_client.CnStop1() # CnStop1 |  (optional)
    cn_weight1 = fooocusapi_client.CnWeight1() # CnWeight1 |  (optional)
    cn_type1 = fooocusapi_client.ControlNetType() # ControlNetType | ControlNet type for image prompt (optional)
    cn_img2 = None # bytearray | Input image for image prompt (optional)
    cn_stop2 = fooocusapi_client.CnStop2() # CnStop2 |  (optional)
    cn_weight2 = fooocusapi_client.CnWeight2() # CnWeight2 |  (optional)
    cn_type2 = fooocusapi_client.ControlNetType() # ControlNetType | ControlNet type for image prompt (optional)
    cn_img3 = None # bytearray | Input image for image prompt (optional)
    cn_stop3 = fooocusapi_client.CnStop3() # CnStop3 |  (optional)
    cn_weight3 = fooocusapi_client.CnWeight3() # CnWeight3 |  (optional)
    cn_type3 = fooocusapi_client.ControlNetType() # ControlNetType | ControlNet type for image prompt (optional)
    cn_img4 = None # bytearray | Input image for image prompt (optional)
    cn_stop4 = fooocusapi_client.CnStop4() # CnStop4 |  (optional)
    cn_weight4 = fooocusapi_client.CnWeight4() # CnWeight4 |  (optional)
    cn_type4 = fooocusapi_client.ControlNetType() # ControlNetType | ControlNet type for image prompt (optional)
    prompt = '' # str |  (optional) (default to '')
    negative_prompt = '' # str |  (optional) (default to '')
    style_selections = ['style_selections_example'] # List[str] | Fooocus style selections, seperated by comma (optional)
    performance_selection = fooocusapi_client.PerfomanceSelection() # PerfomanceSelection |  (optional)
    aspect_ratios_selection = '1152*896' # str |  (optional) (default to '1152*896')
    image_number = 1 # int | Image number (optional) (default to 1)
    image_seed = -1 # int | Seed to generate image, -1 for random (optional) (default to -1)
    sharpness = 2.0 # float |  (optional) (default to 2.0)
    guidance_scale = 4.0 # float |  (optional) (default to 4.0)
    base_model_name = 'juggernautXL_version6Rundiffusion.safetensors' # str |  (optional) (default to 'juggernautXL_version6Rundiffusion.safetensors')
    refiner_model_name = 'None' # str |  (optional) (default to 'None')
    refiner_switch = 0.5 # float | Refiner Switch At (optional) (default to 0.5)
    loras = fooocusapi_client.Loras() # Loras |  (optional)
    advanced_params = fooocusapi_client.AdvancedParams() # AdvancedParams |  (optional)
    require_base64 = False # bool | Return base64 data of generated image (optional) (default to False)
    async_process = False # bool | Set to true will run async and return job info for retrieve generataion result later (optional) (default to False)

    try:
        # Img Prompt
        api_response = api_instance.img_prompt_v1_generation_image_prompt_post(accept=accept, accept2=accept2, cn_img1=cn_img1, input_image=input_image, input_mask=input_mask, inpaint_additional_prompt=inpaint_additional_prompt, outpaint_selections=outpaint_selections, outpaint_distance_left=outpaint_distance_left, outpaint_distance_right=outpaint_distance_right, outpaint_distance_top=outpaint_distance_top, outpaint_distance_bottom=outpaint_distance_bottom, cn_stop1=cn_stop1, cn_weight1=cn_weight1, cn_type1=cn_type1, cn_img2=cn_img2, cn_stop2=cn_stop2, cn_weight2=cn_weight2, cn_type2=cn_type2, cn_img3=cn_img3, cn_stop3=cn_stop3, cn_weight3=cn_weight3, cn_type3=cn_type3, cn_img4=cn_img4, cn_stop4=cn_stop4, cn_weight4=cn_weight4, cn_type4=cn_type4, prompt=prompt, negative_prompt=negative_prompt, style_selections=style_selections, performance_selection=performance_selection, aspect_ratios_selection=aspect_ratios_selection, image_number=image_number, image_seed=image_seed, sharpness=sharpness, guidance_scale=guidance_scale, base_model_name=base_model_name, refiner_model_name=refiner_model_name, refiner_switch=refiner_switch, loras=loras, advanced_params=advanced_params, require_base64=require_base64, async_process=async_process)
        print("The response of DefaultApi->img_prompt_v1_generation_image_prompt_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->img_prompt_v1_generation_image_prompt_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | [**Accept**](.md)| Parameter to overvide &#39;Accept&#39; header, &#39;image/png&#39; for output bytes | [optional] 
 **accept2** | **str**|  | [optional] 
 **cn_img1** | **bytearray**| Input image for image prompt | [optional] 
 **input_image** | **bytearray**| Init image for inpaint or outpaint | [optional] 
 **input_mask** | **bytearray**| Inpaint or outpaint mask | [optional] 
 **inpaint_additional_prompt** | [**InpaintAdditionalPrompt**](InpaintAdditionalPrompt.md)|  | [optional] 
 **outpaint_selections** | [**List[str]**](str.md)| Outpaint expansion selections, literal &#39;Left&#39;, &#39;Right&#39;, &#39;Top&#39;, &#39;Bottom&#39; seperated by comma | [optional] 
 **outpaint_distance_left** | **int**| Set outpaint left distance, 0 for default | [optional] [default to 0]
 **outpaint_distance_right** | **int**| Set outpaint right distance, 0 for default | [optional] [default to 0]
 **outpaint_distance_top** | **int**| Set outpaint top distance, 0 for default | [optional] [default to 0]
 **outpaint_distance_bottom** | **int**| Set outpaint bottom distance, 0 for default | [optional] [default to 0]
 **cn_stop1** | [**CnStop1**](CnStop1.md)|  | [optional] 
 **cn_weight1** | [**CnWeight1**](CnWeight1.md)|  | [optional] 
 **cn_type1** | [**ControlNetType**](ControlNetType.md)| ControlNet type for image prompt | [optional] 
 **cn_img2** | **bytearray**| Input image for image prompt | [optional] 
 **cn_stop2** | [**CnStop2**](CnStop2.md)|  | [optional] 
 **cn_weight2** | [**CnWeight2**](CnWeight2.md)|  | [optional] 
 **cn_type2** | [**ControlNetType**](ControlNetType.md)| ControlNet type for image prompt | [optional] 
 **cn_img3** | **bytearray**| Input image for image prompt | [optional] 
 **cn_stop3** | [**CnStop3**](CnStop3.md)|  | [optional] 
 **cn_weight3** | [**CnWeight3**](CnWeight3.md)|  | [optional] 
 **cn_type3** | [**ControlNetType**](ControlNetType.md)| ControlNet type for image prompt | [optional] 
 **cn_img4** | **bytearray**| Input image for image prompt | [optional] 
 **cn_stop4** | [**CnStop4**](CnStop4.md)|  | [optional] 
 **cn_weight4** | [**CnWeight4**](CnWeight4.md)|  | [optional] 
 **cn_type4** | [**ControlNetType**](ControlNetType.md)| ControlNet type for image prompt | [optional] 
 **prompt** | **str**|  | [optional] [default to &#39;&#39;]
 **negative_prompt** | **str**|  | [optional] [default to &#39;&#39;]
 **style_selections** | [**List[str]**](str.md)| Fooocus style selections, seperated by comma | [optional] 
 **performance_selection** | [**PerfomanceSelection**](PerfomanceSelection.md)|  | [optional] 
 **aspect_ratios_selection** | **str**|  | [optional] [default to &#39;1152*896&#39;]
 **image_number** | **int**| Image number | [optional] [default to 1]
 **image_seed** | **int**| Seed to generate image, -1 for random | [optional] [default to -1]
 **sharpness** | **float**|  | [optional] [default to 2.0]
 **guidance_scale** | **float**|  | [optional] [default to 4.0]
 **base_model_name** | **str**|  | [optional] [default to &#39;juggernautXL_version6Rundiffusion.safetensors&#39;]
 **refiner_model_name** | **str**|  | [optional] [default to &#39;None&#39;]
 **refiner_switch** | **float**| Refiner Switch At | [optional] [default to 0.5]
 **loras** | [**Loras**](Loras.md)|  | [optional] 
 **advanced_params** | [**AdvancedParams**](AdvancedParams.md)|  | [optional] 
 **require_base64** | **bool**| Return base64 data of generated image | [optional] [default to False]
 **async_process** | **bool**| Set to true will run async and return job info for retrieve generataion result later | [optional] [default to False]

### Return type

[**ResponseImgPromptV1GenerationImagePromptPost**](ResponseImgPromptV1GenerationImagePromptPost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/json async, image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PNG bytes if request&#39;s &#39;Accept&#39; header is &#39;image/png&#39;, otherwise JSON |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **img_prompt_v2_generation_image_prompt_post**
> ResponseImgPromptV2GenerationImagePromptPost img_prompt_v2_generation_image_prompt_post(img_prompt_request_json, accept=accept, accept2=accept2)

Img Prompt

### Example


```python
import fooocusapi_client
from fooocusapi_client.models.img_prompt_request_json import ImgPromptRequestJson
from fooocusapi_client.models.response_img_prompt_v2_generation_image_prompt_post import ResponseImgPromptV2GenerationImagePromptPost
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)
    img_prompt_request_json = fooocusapi_client.ImgPromptRequestJson() # ImgPromptRequestJson | 
    accept = fooocusapi_client.Accept() # Accept | Parameter to overvide 'Accept' header, 'image/png' for output bytes (optional)
    accept2 = 'accept_example' # str |  (optional)

    try:
        # Img Prompt
        api_response = api_instance.img_prompt_v2_generation_image_prompt_post(img_prompt_request_json, accept=accept, accept2=accept2)
        print("The response of DefaultApi->img_prompt_v2_generation_image_prompt_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->img_prompt_v2_generation_image_prompt_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **img_prompt_request_json** | [**ImgPromptRequestJson**](ImgPromptRequestJson.md)|  | 
 **accept** | [**Accept**](.md)| Parameter to overvide &#39;Accept&#39; header, &#39;image/png&#39; for output bytes | [optional] 
 **accept2** | **str**|  | [optional] 

### Return type

[**ResponseImgPromptV2GenerationImagePromptPost**](ResponseImgPromptV2GenerationImagePromptPost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json async, image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PNG bytes if request&#39;s &#39;Accept&#39; header is &#39;image/png&#39;, otherwise JSON |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **img_upscale_or_vary_v1_generation_image_upscale_vary_post**
> ResponseImgUpscaleOrVaryV1GenerationImageUpscaleVaryPost img_upscale_or_vary_v1_generation_image_upscale_vary_post(input_image, uov_method, accept=accept, accept2=accept2, upscale_value=upscale_value, prompt=prompt, negative_prompt=negative_prompt, style_selections=style_selections, performance_selection=performance_selection, aspect_ratios_selection=aspect_ratios_selection, image_number=image_number, image_seed=image_seed, sharpness=sharpness, guidance_scale=guidance_scale, base_model_name=base_model_name, refiner_model_name=refiner_model_name, refiner_switch=refiner_switch, loras=loras, advanced_params=advanced_params, require_base64=require_base64, async_process=async_process)

Img Upscale Or Vary

### Example


```python
import fooocusapi_client
from fooocusapi_client.models.advanced_params import AdvancedParams
from fooocusapi_client.models.loras import Loras
from fooocusapi_client.models.response_img_upscale_or_vary_v1_generation_image_upscale_vary_post import ResponseImgUpscaleOrVaryV1GenerationImageUpscaleVaryPost
from fooocusapi_client.models.upscale_or_vary_method import UpscaleOrVaryMethod
from fooocusapi_client.models.upscale_value import UpscaleValue
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)
    input_image = None # bytearray | Init image for upsacale or outpaint
    uov_method = fooocusapi_client.UpscaleOrVaryMethod() # UpscaleOrVaryMethod | 
    accept = fooocusapi_client.Accept() # Accept | Parameter to overvide 'Accept' header, 'image/png' for output bytes (optional)
    accept2 = 'accept_example' # str |  (optional)
    upscale_value = fooocusapi_client.UpscaleValue() # UpscaleValue |  (optional)
    prompt = '' # str |  (optional) (default to '')
    negative_prompt = '' # str |  (optional) (default to '')
    style_selections = ['style_selections_example'] # List[str] | Fooocus style selections, seperated by comma (optional)
    performance_selection = fooocusapi_client.PerfomanceSelection() # PerfomanceSelection | Performance Selection, one of 'Speed','Quality','Extreme Speed' (optional)
    aspect_ratios_selection = '1152*896' # str | Aspect Ratios Selection, default 1152*896 (optional) (default to '1152*896')
    image_number = 1 # int | Image number (optional) (default to 1)
    image_seed = -1 # int | Seed to generate image, -1 for random (optional) (default to -1)
    sharpness = 2.0 # float |  (optional) (default to 2.0)
    guidance_scale = 4.0 # float |  (optional) (default to 4.0)
    base_model_name = 'juggernautXL_version6Rundiffusion.safetensors' # str | checkpoint file name (optional) (default to 'juggernautXL_version6Rundiffusion.safetensors')
    refiner_model_name = 'None' # str | refiner file name (optional) (default to 'None')
    refiner_switch = 0.5 # float | Refiner Switch At (optional) (default to 0.5)
    loras = fooocusapi_client.Loras() # Loras |  (optional)
    advanced_params = fooocusapi_client.AdvancedParams() # AdvancedParams |  (optional)
    require_base64 = False # bool | Return base64 data of generated image (optional) (default to False)
    async_process = False # bool | Set to true will run async and return job info for retrieve generataion result later (optional) (default to False)

    try:
        # Img Upscale Or Vary
        api_response = api_instance.img_upscale_or_vary_v1_generation_image_upscale_vary_post(input_image, uov_method, accept=accept, accept2=accept2, upscale_value=upscale_value, prompt=prompt, negative_prompt=negative_prompt, style_selections=style_selections, performance_selection=performance_selection, aspect_ratios_selection=aspect_ratios_selection, image_number=image_number, image_seed=image_seed, sharpness=sharpness, guidance_scale=guidance_scale, base_model_name=base_model_name, refiner_model_name=refiner_model_name, refiner_switch=refiner_switch, loras=loras, advanced_params=advanced_params, require_base64=require_base64, async_process=async_process)
        print("The response of DefaultApi->img_upscale_or_vary_v1_generation_image_upscale_vary_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->img_upscale_or_vary_v1_generation_image_upscale_vary_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_image** | **bytearray**| Init image for upsacale or outpaint | 
 **uov_method** | [**UpscaleOrVaryMethod**](UpscaleOrVaryMethod.md)|  | 
 **accept** | [**Accept**](.md)| Parameter to overvide &#39;Accept&#39; header, &#39;image/png&#39; for output bytes | [optional] 
 **accept2** | **str**|  | [optional] 
 **upscale_value** | [**UpscaleValue**](UpscaleValue.md)|  | [optional] 
 **prompt** | **str**|  | [optional] [default to &#39;&#39;]
 **negative_prompt** | **str**|  | [optional] [default to &#39;&#39;]
 **style_selections** | [**List[str]**](str.md)| Fooocus style selections, seperated by comma | [optional] 
 **performance_selection** | [**PerfomanceSelection**](PerfomanceSelection.md)| Performance Selection, one of &#39;Speed&#39;,&#39;Quality&#39;,&#39;Extreme Speed&#39; | [optional] 
 **aspect_ratios_selection** | **str**| Aspect Ratios Selection, default 1152*896 | [optional] [default to &#39;1152*896&#39;]
 **image_number** | **int**| Image number | [optional] [default to 1]
 **image_seed** | **int**| Seed to generate image, -1 for random | [optional] [default to -1]
 **sharpness** | **float**|  | [optional] [default to 2.0]
 **guidance_scale** | **float**|  | [optional] [default to 4.0]
 **base_model_name** | **str**| checkpoint file name | [optional] [default to &#39;juggernautXL_version6Rundiffusion.safetensors&#39;]
 **refiner_model_name** | **str**| refiner file name | [optional] [default to &#39;None&#39;]
 **refiner_switch** | **float**| Refiner Switch At | [optional] [default to 0.5]
 **loras** | [**Loras**](Loras.md)|  | [optional] 
 **advanced_params** | [**AdvancedParams**](AdvancedParams.md)|  | [optional] 
 **require_base64** | **bool**| Return base64 data of generated image | [optional] [default to False]
 **async_process** | **bool**| Set to true will run async and return job info for retrieve generataion result later | [optional] [default to False]

### Return type

[**ResponseImgUpscaleOrVaryV1GenerationImageUpscaleVaryPost**](ResponseImgUpscaleOrVaryV1GenerationImageUpscaleVaryPost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/json async, image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PNG bytes if request&#39;s &#39;Accept&#39; header is &#39;image/png&#39;, otherwise JSON |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **img_upscale_or_vary_v2_v2_generation_image_upscale_vary_post**
> ResponseImgUpscaleOrVaryV2V2GenerationImageUpscaleVaryPost img_upscale_or_vary_v2_v2_generation_image_upscale_vary_post(img_upscale_or_vary_request_json, accept=accept, accept2=accept2)

Img Upscale Or Vary V2

### Example


```python
import fooocusapi_client
from fooocusapi_client.models.img_upscale_or_vary_request_json import ImgUpscaleOrVaryRequestJson
from fooocusapi_client.models.response_img_upscale_or_vary_v2_v2_generation_image_upscale_vary_post import ResponseImgUpscaleOrVaryV2V2GenerationImageUpscaleVaryPost
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)
    img_upscale_or_vary_request_json = fooocusapi_client.ImgUpscaleOrVaryRequestJson() # ImgUpscaleOrVaryRequestJson | 
    accept = fooocusapi_client.Accept() # Accept | Parameter to overvide 'Accept' header, 'image/png' for output bytes (optional)
    accept2 = 'accept_example' # str |  (optional)

    try:
        # Img Upscale Or Vary V2
        api_response = api_instance.img_upscale_or_vary_v2_v2_generation_image_upscale_vary_post(img_upscale_or_vary_request_json, accept=accept, accept2=accept2)
        print("The response of DefaultApi->img_upscale_or_vary_v2_v2_generation_image_upscale_vary_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->img_upscale_or_vary_v2_v2_generation_image_upscale_vary_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **img_upscale_or_vary_request_json** | [**ImgUpscaleOrVaryRequestJson**](ImgUpscaleOrVaryRequestJson.md)|  | 
 **accept** | [**Accept**](.md)| Parameter to overvide &#39;Accept&#39; header, &#39;image/png&#39; for output bytes | [optional] 
 **accept2** | **str**|  | [optional] 

### Return type

[**ResponseImgUpscaleOrVaryV2V2GenerationImageUpscaleVaryPost**](ResponseImgUpscaleOrVaryV2V2GenerationImageUpscaleVaryPost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json async, image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PNG bytes if request&#39;s &#39;Accept&#39; header is &#39;image/png&#39;, otherwise JSON |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_queue_v1_generation_job_queue_get**
> JobQueueInfo job_queue_v1_generation_job_queue_get()

Job Queue

Query job queue info

### Example


```python
import fooocusapi_client
from fooocusapi_client.models.job_queue_info import JobQueueInfo
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)

    try:
        # Job Queue
        api_response = api_instance.job_queue_v1_generation_job_queue_get()
        print("The response of DefaultApi->job_queue_v1_generation_job_queue_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->job_queue_v1_generation_job_queue_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JobQueueInfo**](JobQueueInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_ping_get**
> object ping_ping_get()

Ping

Returns a simple 'pong' response

### Example


```python
import fooocusapi_client
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)

    try:
        # Ping
        api_response = api_instance.ping_ping_get()
        print("The response of DefaultApi->ping_ping_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->ping_ping_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_job_v1_generation_query_job_get**
> AsyncJobResponse query_job_v1_generation_query_job_get(job_id, require_step_preview=require_step_preview)

Query Job

Query async generation job

### Example


```python
import fooocusapi_client
from fooocusapi_client.models.async_job_response import AsyncJobResponse
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)
    job_id = 'job_id_example' # str | 
    require_step_preview = False # bool |  (optional) (default to False)

    try:
        # Query Job
        api_response = api_instance.query_job_v1_generation_query_job_get(job_id, require_step_preview=require_step_preview)
        print("The response of DefaultApi->query_job_v1_generation_query_job_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->query_job_v1_generation_query_job_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **require_step_preview** | **bool**|  | [optional] [default to False]

### Return type

[**AsyncJobResponse**](AsyncJobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_models_v1_engines_refresh_models_post**
> AllModelNamesResponse refresh_models_v1_engines_refresh_models_post()

Refresh Models

Refresh local files and get all filenames of base model and lora

### Example


```python
import fooocusapi_client
from fooocusapi_client.models.all_model_names_response import AllModelNamesResponse
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)

    try:
        # Refresh Models
        api_response = api_instance.refresh_models_v1_engines_refresh_models_post()
        print("The response of DefaultApi->refresh_models_v1_engines_refresh_models_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->refresh_models_v1_engines_refresh_models_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AllModelNamesResponse**](AllModelNamesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_v1_generation_stop_post**
> StopResponse stop_v1_generation_stop_post()

Stop

Job stoping

### Example


```python
import fooocusapi_client
from fooocusapi_client.models.stop_response import StopResponse
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)

    try:
        # Stop
        api_response = api_instance.stop_v1_generation_stop_post()
        print("The response of DefaultApi->stop_v1_generation_stop_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->stop_v1_generation_stop_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StopResponse**](StopResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text2img_generation_v1_generation_text_to_image_post**
> ResponseText2ImgGenerationV1GenerationTextToImagePost text2img_generation_v1_generation_text_to_image_post(text2_img_request, accept=accept, accept2=accept2)

Text2Img Generation

### Example


```python
import fooocusapi_client
from fooocusapi_client.models.response_text2_img_generation_v1_generation_text_to_image_post import ResponseText2ImgGenerationV1GenerationTextToImagePost
from fooocusapi_client.models.text2_img_request import Text2ImgRequest
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)
    text2_img_request = fooocusapi_client.Text2ImgRequest() # Text2ImgRequest | 
    accept = fooocusapi_client.Accept() # Accept | Parameter to overvide 'Accept' header, 'image/png' for output bytes (optional)
    accept2 = 'accept_example' # str |  (optional)

    try:
        # Text2Img Generation
        api_response = api_instance.text2img_generation_v1_generation_text_to_image_post(text2_img_request, accept=accept, accept2=accept2)
        print("The response of DefaultApi->text2img_generation_v1_generation_text_to_image_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->text2img_generation_v1_generation_text_to_image_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text2_img_request** | [**Text2ImgRequest**](Text2ImgRequest.md)|  | 
 **accept** | [**Accept**](.md)| Parameter to overvide &#39;Accept&#39; header, &#39;image/png&#39; for output bytes | [optional] 
 **accept2** | **str**|  | [optional] 

### Return type

[**ResponseText2ImgGenerationV1GenerationTextToImagePost**](ResponseText2ImgGenerationV1GenerationTextToImagePost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json async, image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PNG bytes if request&#39;s &#39;Accept&#39; header is &#39;image/png&#39;, otherwise JSON |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_to_img_with_ip_v2_generation_text_to_image_with_ip_post**
> ResponseTextToImgWithIpV2GenerationTextToImageWithIpPost text_to_img_with_ip_v2_generation_text_to_image_with_ip_post(text2_img_request_with_prompt, accept=accept, accept2=accept2)

Text To Img With Ip

### Example


```python
import fooocusapi_client
from fooocusapi_client.models.response_text_to_img_with_ip_v2_generation_text_to_image_with_ip_post import ResponseTextToImgWithIpV2GenerationTextToImageWithIpPost
from fooocusapi_client.models.text2_img_request_with_prompt import Text2ImgRequestWithPrompt
from fooocusapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fooocusapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fooocusapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fooocusapi_client.DefaultApi(api_client)
    text2_img_request_with_prompt = fooocusapi_client.Text2ImgRequestWithPrompt() # Text2ImgRequestWithPrompt | 
    accept = fooocusapi_client.Accept() # Accept | Parameter to overvide 'Accept' header, 'image/png' for output bytes (optional)
    accept2 = 'accept_example' # str |  (optional)

    try:
        # Text To Img With Ip
        api_response = api_instance.text_to_img_with_ip_v2_generation_text_to_image_with_ip_post(text2_img_request_with_prompt, accept=accept, accept2=accept2)
        print("The response of DefaultApi->text_to_img_with_ip_v2_generation_text_to_image_with_ip_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->text_to_img_with_ip_v2_generation_text_to_image_with_ip_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text2_img_request_with_prompt** | [**Text2ImgRequestWithPrompt**](Text2ImgRequestWithPrompt.md)|  | 
 **accept** | [**Accept**](.md)| Parameter to overvide &#39;Accept&#39; header, &#39;image/png&#39; for output bytes | [optional] 
 **accept2** | **str**|  | [optional] 

### Return type

[**ResponseTextToImgWithIpV2GenerationTextToImageWithIpPost**](ResponseTextToImgWithIpV2GenerationTextToImageWithIpPost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json async, image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PNG bytes if request&#39;s &#39;Accept&#39; header is &#39;image/png&#39;, otherwise JSON |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

