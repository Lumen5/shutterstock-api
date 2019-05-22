# shutterstock_api.UsersApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /v2/user | Register user
[**get_access_token**](UsersApi.md#get_access_token) | **GET** /v2/user/access_token | Get access token details
[**get_user**](UsersApi.md#get_user) | **GET** /v2/user | Get user details
[**get_user_subsciption_list**](UsersApi.md#get_user_subsciption_list) | **GET** /v2/user/subscriptions | List user subscriptions


# **create_user**
> UserPostResponse create_user(body)

Register user

### Example
```python
from __future__ import print_function
import time
import shutterstock_api
from shutterstock_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_api.UsersApi(shutterstock_api.ApiClient(configuration))
body = shutterstock_api.UserPostRequest() # UserPostRequest | User details

try:
    # Register user
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserPostRequest**](UserPostRequest.md)| User details | 

### Return type

[**UserPostResponse**](UserPostResponse.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_token**
> AccessTokenDetails get_access_token()

Get access token details

### Example
```python
from __future__ import print_function
import time
import shutterstock_api
from shutterstock_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_api.UsersApi(shutterstock_api.ApiClient(configuration))

try:
    # Get access token details
    api_response = api_instance.get_access_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_access_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessTokenDetails**](AccessTokenDetails.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserDetails get_user()

Get user details

### Example
```python
from __future__ import print_function
import time
import shutterstock_api
from shutterstock_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_api.UsersApi(shutterstock_api.ApiClient(configuration))

try:
    # Get user details
    api_response = api_instance.get_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserDetails**](UserDetails.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_subsciption_list**
> SubscriptionDataList get_user_subsciption_list()

List user subscriptions

### Example
```python
from __future__ import print_function
import time
import shutterstock_api
from shutterstock_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_api.UsersApi(shutterstock_api.ApiClient(configuration))

try:
    # List user subscriptions
    api_response = api_instance.get_user_subsciption_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_subsciption_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SubscriptionDataList**](SubscriptionDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

