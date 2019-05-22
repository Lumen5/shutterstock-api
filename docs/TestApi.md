# shutterstock_api.TestApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**echo**](TestApi.md#echo) | **GET** /v2/test | Echo text
[**validate**](TestApi.md#validate) | **GET** /v2/test/validate | Validate input


# **echo**
> TestEcho echo(text=text)

Echo text

### Example
```python
from __future__ import print_function
import time
import shutterstock_api
from shutterstock_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = shutterstock_api.TestApi()
text = 'ok' # str | Text to echo (optional) (default to ok)

try:
    # Echo text
    api_response = api_instance.echo(text=text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestApi->echo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Text to echo | [optional] [default to ok]

### Return type

[**TestEcho**](TestEcho.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate**
> TestValidate validate(id, tag=tag, user_agent=user_agent)

Validate input

### Example
```python
from __future__ import print_function
import time
import shutterstock_api
from shutterstock_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = shutterstock_api.TestApi()
id = 123 # int | Integer ID
tag = ['tag_example'] # list[str] | List of tags (optional)
user_agent = 'user_agent_example' # str | User agent (optional)

try:
    # Validate input
    api_response = api_instance.validate(id, tag=tag, user_agent=user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestApi->validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Integer ID | 
 **tag** | [**list[str]**](str.md)| List of tags | [optional] 
 **user_agent** | **str**| User agent | [optional] 

### Return type

[**TestValidate**](TestValidate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

