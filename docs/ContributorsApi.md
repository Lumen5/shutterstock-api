# shutterstock_api.ContributorsApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contributor**](ContributorsApi.md#get_contributor) | **GET** /v2/contributors/{contributor_id} | Get details about a single contributor
[**get_contributor_collection_items**](ContributorsApi.md#get_contributor_collection_items) | **GET** /v2/contributors/{contributor_id}/collections/{id}/items | Get the items in contributors&#39; collections
[**get_contributor_collections**](ContributorsApi.md#get_contributor_collections) | **GET** /v2/contributors/{contributor_id}/collections/{id} | Get details about contributors&#39; collections
[**get_contributor_collections_list**](ContributorsApi.md#get_contributor_collections_list) | **GET** /v2/contributors/{contributor_id}/collections | List contributors&#39; collections
[**get_contributor_list**](ContributorsApi.md#get_contributor_list) | **GET** /v2/contributors | Get details about multiple contributors


# **get_contributor**
> ContributorProfile get_contributor(contributor_id)

Get details about a single contributor

This endpoint shows information about a single contributor, including contributor type, equipment they use, and other attributes.

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
api_instance = shutterstock_api.ContributorsApi(shutterstock_api.ApiClient(configuration))
contributor_id = '1653538' # str | Contributor ID

try:
    # Get details about a single contributor
    api_response = api_instance.get_contributor(contributor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContributorsApi->get_contributor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contributor_id** | **str**| Contributor ID | 

### Return type

[**ContributorProfile**](ContributorProfile.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contributor_collection_items**
> CollectionItemDataList get_contributor_collection_items(contributor_id, id, page=page, per_page=per_page, sort=sort)

Get the items in contributors' collections

This endpoint lists the IDs of items in a contributor's collection and the date that each was added.

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
api_instance = shutterstock_api.ContributorsApi(shutterstock_api.ApiClient(configuration))
contributor_id = '800506' # str | Contributor ID
id = '1991678' # str | Collection ID that belongs to the contributor
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page (optional) (default to 20)
sort = 'sort_example' # str | Sort order (optional)

try:
    # Get the items in contributors' collections
    api_response = api_instance.get_contributor_collection_items(contributor_id, id, page=page, per_page=per_page, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContributorsApi->get_contributor_collection_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contributor_id** | **str**| Contributor ID | 
 **id** | **str**| Collection ID that belongs to the contributor | 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 20]
 **sort** | **str**| Sort order | [optional] 

### Return type

[**CollectionItemDataList**](CollectionItemDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contributor_collections**
> Collection get_contributor_collections(contributor_id, id)

Get details about contributors' collections

This endpoint gets more detailed information about a contributor's collection, including its cover image, timestamps for its creation, and most recent update. To get the items in collections, use GET /contributors/{contributor_id}/collections/{id}/items.

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
api_instance = shutterstock_api.ContributorsApi(shutterstock_api.ApiClient(configuration))
contributor_id = '800506' # str | Contributor ID
id = '1991678' # str | Collection ID that belongs to the contributor

try:
    # Get details about contributors' collections
    api_response = api_instance.get_contributor_collections(contributor_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContributorsApi->get_contributor_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contributor_id** | **str**| Contributor ID | 
 **id** | **str**| Collection ID that belongs to the contributor | 

### Return type

[**Collection**](Collection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contributor_collections_list**
> CollectionDataList get_contributor_collections_list(contributor_id, sort=sort)

List contributors' collections

This endpoint lists collections based on contributor ID.

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
api_instance = shutterstock_api.ContributorsApi(shutterstock_api.ApiClient(configuration))
contributor_id = '800506' # str | Contributor ID
sort = 'sort_example' # str | Sort order (optional)

try:
    # List contributors' collections
    api_response = api_instance.get_contributor_collections_list(contributor_id, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContributorsApi->get_contributor_collections_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contributor_id** | **str**| Contributor ID | 
 **sort** | **str**| Sort order | [optional] 

### Return type

[**CollectionDataList**](CollectionDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contributor_list**
> ContributorProfileDataList get_contributor_list(id)

Get details about multiple contributors

This endpoint lists information about one or more contributors, including contributor type, equipment they use and other attributes.

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
api_instance = shutterstock_api.ContributorsApi(shutterstock_api.ApiClient(configuration))
id = ['[ 800506, 1653538 ]'] # list[str] | One or more contributor IDs

try:
    # Get details about multiple contributors
    api_response = api_instance.get_contributor_list(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContributorsApi->get_contributor_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| One or more contributor IDs | 

### Return type

[**ContributorProfileDataList**](ContributorProfileDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

