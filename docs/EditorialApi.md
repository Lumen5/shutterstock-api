# shutterstock_api.EditorialApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_editorial_image**](EditorialApi.md#get_editorial_image) | **GET** /v2/editorial/{id} | Get editorial content details
[**get_editorial_livefeed**](EditorialApi.md#get_editorial_livefeed) | **GET** /v2/editorial/livefeeds/{id} | Get editorial livefeed
[**get_editorial_livefeed_items**](EditorialApi.md#get_editorial_livefeed_items) | **GET** /v2/editorial/livefeeds/{id}/items | Get editorial livefeed items
[**get_editorial_livefeed_list**](EditorialApi.md#get_editorial_livefeed_list) | **GET** /v2/editorial/livefeeds | Get editorial livefeed list
[**license_editorial_image**](EditorialApi.md#license_editorial_image) | **POST** /v2/editorial/licenses | License editorial content
[**search_editorial**](EditorialApi.md#search_editorial) | **GET** /v2/editorial/search | Search editorial content


# **get_editorial_image**
> EditorialContent get_editorial_image(id, country)

Get editorial content details

This endpoint shows information about an editorial image, including a URL to a preview image and the sizes that it is available in.

### Example
```python
from __future__ import print_function
import time
import shutterstock_api
from shutterstock_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = shutterstock_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_api.EditorialApi(shutterstock_api.ApiClient(configuration))
id = '\"9926131a\"' # str | Editorial ID
country = '\"USA\"' # str | Returns only if the content is available for distribution in a certain country; specify with 3-letter country code

try:
    # Get editorial content details
    api_response = api_instance.get_editorial_image(id, country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialApi->get_editorial_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Editorial ID | 
 **country** | **str**| Returns only if the content is available for distribution in a certain country; specify with 3-letter country code | 

### Return type

[**EditorialContent**](EditorialContent.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editorial_livefeed**
> EditorialLivefeed get_editorial_livefeed(id, country)

Get editorial livefeed

### Example
```python
from __future__ import print_function
import time
import shutterstock_api
from shutterstock_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = shutterstock_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_api.EditorialApi(shutterstock_api.ApiClient(configuration))
id = '\"2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London\"' # str | Editorial livefeed ID; must be an URI encoded string
country = '\"USA\"' # str | Returns only if the livefeed is available for distribution in a certain country; specify with 3-letter country code

try:
    # Get editorial livefeed
    api_response = api_instance.get_editorial_livefeed(id, country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialApi->get_editorial_livefeed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Editorial livefeed ID; must be an URI encoded string | 
 **country** | **str**| Returns only if the livefeed is available for distribution in a certain country; specify with 3-letter country code | 

### Return type

[**EditorialLivefeed**](EditorialLivefeed.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editorial_livefeed_items**
> EditorialContentDataList get_editorial_livefeed_items(id, country)

Get editorial livefeed items

### Example
```python
from __future__ import print_function
import time
import shutterstock_api
from shutterstock_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = shutterstock_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_api.EditorialApi(shutterstock_api.ApiClient(configuration))
id = '\"2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London\"' # str | Editorial livefeed ID; must be an URI encoded string
country = '\"USA\"' # str | Returns only if the livefeed items are available for distribution in a certain country; specify with 3-letter country code

try:
    # Get editorial livefeed items
    api_response = api_instance.get_editorial_livefeed_items(id, country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialApi->get_editorial_livefeed_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Editorial livefeed ID; must be an URI encoded string | 
 **country** | **str**| Returns only if the livefeed items are available for distribution in a certain country; specify with 3-letter country code | 

### Return type

[**EditorialContentDataList**](EditorialContentDataList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editorial_livefeed_list**
> EditorialLivefeedList get_editorial_livefeed_list(country, page=page, per_page=per_page)

Get editorial livefeed list

### Example
```python
from __future__ import print_function
import time
import shutterstock_api
from shutterstock_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = shutterstock_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_api.EditorialApi(shutterstock_api.ApiClient(configuration))
country = '\"USA\"' # str | Returns only livefeeds that are available for distribution in a certain country; specify with 3-letter country code
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page, defaults to 20 (optional) (default to 20)

try:
    # Get editorial livefeed list
    api_response = api_instance.get_editorial_livefeed_list(country, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialApi->get_editorial_livefeed_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Returns only livefeeds that are available for distribution in a certain country; specify with 3-letter country code | 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page, defaults to 20 | [optional] [default to 20]

### Return type

[**EditorialLivefeedList**](EditorialLivefeedList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_editorial_image**
> LicenseEditorialContentResultDataList license_editorial_image(body)

License editorial content

This endpoint gets licenses for one or more editorial images. You must specify the country and one or more editorial images to license.

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
api_instance = shutterstock_api.EditorialApi(shutterstock_api.ApiClient(configuration))
body = shutterstock_api.LicenseEditorialContentRequest() # LicenseEditorialContentRequest | License editorial content

try:
    # License editorial content
    api_response = api_instance.license_editorial_image(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialApi->license_editorial_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LicenseEditorialContentRequest**](LicenseEditorialContentRequest.md)| License editorial content | 

### Return type

[**LicenseEditorialContentResultDataList**](LicenseEditorialContentResultDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_editorial**
> EditorialSearchResults search_editorial(country, query=query, sort=sort, category=category, supplier_code=supplier_code, date_start=date_start, date_end=date_end, per_page=per_page, cursor=cursor)

Search editorial content

This endpoint searches for editorial images. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the `query` parameter by prefixing the term with NOT.

### Example
```python
from __future__ import print_function
import time
import shutterstock_api
from shutterstock_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = shutterstock_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: customer_accessCode
configuration = shutterstock_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = shutterstock_api.EditorialApi(shutterstock_api.ApiClient(configuration))
country = '\"USA\"' # str | Show only editorial content that is available for distribution in a certain country; specify with 3-letter country code
query = 'query_example' # str | One or more search terms separated by spaces (optional)
sort = 'relevant' # str | Sort by (optional) (default to relevant)
category = 'category_example' # str | Show editorial content within a certain editorial category; specify by category name (optional)
supplier_code = ['supplier_code_example'] # list[str] | Show only editorial content from certain suppliers (optional)
date_start = '2013-10-20' # date | Show only editorial content generated on or after a specific date, in the format of YYYY-MM-DD (optional)
date_end = '2013-10-20' # date | Show only editorial content generated on or before a specific date, in the format of YYYY-MM-DD (optional)
per_page = 20 # int | Number of results per page, defaults to 20 (optional) (default to 20)
cursor = 'cursor_example' # str | The cursor of the page with which to start fetching results; this cursor is returned from previous requests (optional)

try:
    # Search editorial content
    api_response = api_instance.search_editorial(country, query=query, sort=sort, category=category, supplier_code=supplier_code, date_start=date_start, date_end=date_end, per_page=per_page, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorialApi->search_editorial: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Show only editorial content that is available for distribution in a certain country; specify with 3-letter country code | 
 **query** | **str**| One or more search terms separated by spaces | [optional] 
 **sort** | **str**| Sort by | [optional] [default to relevant]
 **category** | **str**| Show editorial content within a certain editorial category; specify by category name | [optional] 
 **supplier_code** | [**list[str]**](str.md)| Show only editorial content from certain suppliers | [optional] 
 **date_start** | **date**| Show only editorial content generated on or after a specific date, in the format of YYYY-MM-DD | [optional] 
 **date_end** | **date**| Show only editorial content generated on or before a specific date, in the format of YYYY-MM-DD | [optional] 
 **per_page** | **int**| Number of results per page, defaults to 20 | [optional] [default to 20]
 **cursor** | **str**| The cursor of the page with which to start fetching results; this cursor is returned from previous requests | [optional] 

### Return type

[**EditorialSearchResults**](EditorialSearchResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

