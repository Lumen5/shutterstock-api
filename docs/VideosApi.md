# shutterstock_api.VideosApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_clipbox_items**](VideosApi.md#add_clipbox_items) | **POST** /v2/videos/collections/{id}/items | Add videos to collections
[**create_clipbox**](VideosApi.md#create_clipbox) | **POST** /v2/videos/collections | Create video collections
[**delete_clipbox**](VideosApi.md#delete_clipbox) | **DELETE** /v2/videos/collections/{id} | Delete video collections
[**delete_clipbox_items**](VideosApi.md#delete_clipbox_items) | **DELETE** /v2/videos/collections/{id}/items | Remove videos from collections
[**download_videos**](VideosApi.md#download_videos) | **POST** /v2/videos/licenses/{id}/downloads | Download videos
[**get_clipbox**](VideosApi.md#get_clipbox) | **GET** /v2/videos/collections/{id} | Get the details of video collections
[**get_clipbox_items**](VideosApi.md#get_clipbox_items) | **GET** /v2/videos/collections/{id}/items | Get the contents of video collections
[**get_clipbox_list**](VideosApi.md#get_clipbox_list) | **GET** /v2/videos/collections | List video collections
[**get_similar_videos**](VideosApi.md#get_similar_videos) | **GET** /v2/videos/{id}/similar | List similar videos
[**get_updated_videos**](VideosApi.md#get_updated_videos) | **GET** /v2/videos/updated | List updated videos
[**get_video**](VideosApi.md#get_video) | **GET** /v2/videos/{id} | Get details about videos
[**get_video_categories**](VideosApi.md#get_video_categories) | **GET** /v2/videos/categories | List video categories
[**get_video_license_list**](VideosApi.md#get_video_license_list) | **GET** /v2/videos/licenses | List video licenses
[**get_video_list**](VideosApi.md#get_video_list) | **GET** /v2/videos | List videos
[**license_videos**](VideosApi.md#license_videos) | **POST** /v2/videos/licenses | License videos
[**rename_clipbox**](VideosApi.md#rename_clipbox) | **POST** /v2/videos/collections/{id} | Rename video collections
[**search_videos**](VideosApi.md#search_videos) | **GET** /v2/videos/search | Search for videos


# **add_clipbox_items**
> add_clipbox_items(id, body)

Add videos to collections

This endpoint adds one or more videos to a collection by video IDs.

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
api_instance = shutterstock_api.VideosApi(shutterstock_api.ApiClient(configuration))
id = '\"17555176\"' # str | The ID of the collection to which items should be added
body = shutterstock_api.CollectionItemRequest() # CollectionItemRequest | Array of video IDs to add to the collection

try:
    # Add videos to collections
    api_instance.add_clipbox_items(id, body)
except ApiException as e:
    print("Exception when calling VideosApi->add_clipbox_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the collection to which items should be added | 
 **body** | [**CollectionItemRequest**](CollectionItemRequest.md)| Array of video IDs to add to the collection | 

### Return type

void (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_clipbox**
> CollectionCreateResponse create_clipbox(body)

Create video collections

This endpoint creates one or more collections (clipboxes). To add videos to collections, use `POST /videos/collections/{id}/items`.

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
api_instance = shutterstock_api.VideosApi(shutterstock_api.ApiClient(configuration))
body = shutterstock_api.CollectionCreateRequest() # CollectionCreateRequest | Collection metadata

try:
    # Create video collections
    api_response = api_instance.create_clipbox(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->create_clipbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionCreateRequest**](CollectionCreateRequest.md)| Collection metadata | 

### Return type

[**CollectionCreateResponse**](CollectionCreateResponse.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_clipbox**
> delete_clipbox(id)

Delete video collections

This endpoint deletes a collection.

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
api_instance = shutterstock_api.VideosApi(shutterstock_api.ApiClient(configuration))
id = '\"17555176\"' # str | The ID of the collection to delete

try:
    # Delete video collections
    api_instance.delete_clipbox(id)
except ApiException as e:
    print("Exception when calling VideosApi->delete_clipbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the collection to delete | 

### Return type

void (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_clipbox_items**
> delete_clipbox_items(id, item_id=item_id)

Remove videos from collections

This endpoint removes one or more videos from a collection.

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
api_instance = shutterstock_api.VideosApi(shutterstock_api.ApiClient(configuration))
id = '\"17555176\"' # str | The ID of the Collection from which items will be deleted
item_id = ['item_id_example'] # list[str] | One or more video IDs to remove from the collection (optional)

try:
    # Remove videos from collections
    api_instance.delete_clipbox_items(id, item_id=item_id)
except ApiException as e:
    print("Exception when calling VideosApi->delete_clipbox_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Collection from which items will be deleted | 
 **item_id** | [**list[str]**](str.md)| One or more video IDs to remove from the collection | [optional] 

### Return type

void (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_videos**
> Url download_videos(id, body)

Download videos

This endpoint redownloads videos that you have already received a license for.

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
api_instance = shutterstock_api.VideosApi(shutterstock_api.ApiClient(configuration))
id = '\"i1188641347\"' # str | The license ID of the item to (re)download
body = shutterstock_api.RedownloadVideo() # RedownloadVideo | Information about the videos to redownload

try:
    # Download videos
    api_response = api_instance.download_videos(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->download_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The license ID of the item to (re)download | 
 **body** | [**RedownloadVideo**](RedownloadVideo.md)| Information about the videos to redownload | 

### Return type

[**Url**](Url.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clipbox**
> Collection get_clipbox(id)

Get the details of video collections

This endpoint gets more detailed information about a collection, including the timestamp for its creation and the number of videos in it. To get the videos in collections, use GET /videos/collections/{id}/items.

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
api_instance = shutterstock_api.VideosApi(shutterstock_api.ApiClient(configuration))
id = '\"17555176\"' # str | The ID of the collection to return

try:
    # Get the details of video collections
    api_response = api_instance.get_clipbox(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_clipbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the collection to return | 

### Return type

[**Collection**](Collection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clipbox_items**
> CollectionItemDataList get_clipbox_items(id, page=page, per_page=per_page, sort=sort)

Get the contents of video collections

This endpoint lists the IDs of videos in a collection and the date that each was added.

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
api_instance = shutterstock_api.VideosApi(shutterstock_api.ApiClient(configuration))
id = '\"17555176\"' # str | The ID of the Collection whose items are to be returned
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Number of results per page (optional) (default to 100)
sort = 'oldest' # str | Sort order (optional) (default to oldest)

try:
    # Get the contents of video collections
    api_response = api_instance.get_clipbox_items(id, page=page, per_page=per_page, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_clipbox_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Collection whose items are to be returned | 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 100]
 **sort** | **str**| Sort order | [optional] [default to oldest]

### Return type

[**CollectionItemDataList**](CollectionItemDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clipbox_list**
> CollectionDataList get_clipbox_list(page=page, per_page=per_page)

List video collections

This endpoint lists your collections of videos and their basic attributes.

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
api_instance = shutterstock_api.VideosApi(shutterstock_api.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Number of results per page (optional) (default to 100)

try:
    # List video collections
    api_response = api_instance.get_clipbox_list(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_clipbox_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 100]

### Return type

[**CollectionDataList**](CollectionDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_similar_videos**
> VideoSearchResults get_similar_videos(id, page=page, per_page=per_page, view=view)

List similar videos

This endpoint searches for videos that are similar to a video that you specify.

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
api_instance = shutterstock_api.VideosApi(shutterstock_api.ApiClient(configuration))
id = '\"2140697\"' # str | The ID of a video for which similar videos should be returned
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page (optional) (default to 20)
view = 'minimal' # str | Amount of detail to render in the response (optional) (default to minimal)

try:
    # List similar videos
    api_response = api_instance.get_similar_videos(id, page=page, per_page=per_page, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_similar_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of a video for which similar videos should be returned | 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 20]
 **view** | **str**| Amount of detail to render in the response | [optional] [default to minimal]

### Return type

[**VideoSearchResults**](VideoSearchResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_updated_videos**
> UpdatedMediaDataList get_updated_videos(start_date=start_date, end_date=end_date, interval=interval, page=page, per_page=per_page, sort=sort)

List updated videos

This endpoint lists videos that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the `interval` parameter to show videos that were updated recently, but you can also use the `start_date` and `end_date` parameters to specify a range of no more than three days. Do not use the `interval` parameter with either `start_date` or `end_date`.

### Example
```python
from __future__ import print_function
import time
import shutterstock_api
from shutterstock_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = shutterstock_api.VideosApi()
start_date = '2013-10-20' # date | Show videos updated on or after the specified date, in the format YYYY-MM-DD (optional)
end_date = '2013-10-20' # date | Show videos updated before the specified date, in the format YYYY-MM-DD (optional)
interval = '1 HOUR' # str | Show videos updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows videos that were updated in the hour preceding the request (optional) (default to 1 HOUR)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Number of results per page (optional) (default to 100)
sort = 'newest' # str | Sort by oldest or newest videos first (optional) (default to newest)

try:
    # List updated videos
    api_response = api_instance.get_updated_videos(start_date=start_date, end_date=end_date, interval=interval, page=page, per_page=per_page, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_updated_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| Show videos updated on or after the specified date, in the format YYYY-MM-DD | [optional] 
 **end_date** | **date**| Show videos updated before the specified date, in the format YYYY-MM-DD | [optional] 
 **interval** | **str**| Show videos updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows videos that were updated in the hour preceding the request | [optional] [default to 1 HOUR]
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 100]
 **sort** | **str**| Sort by oldest or newest videos first | [optional] [default to newest]

### Return type

[**UpdatedMediaDataList**](UpdatedMediaDataList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video**
> Video get_video(id, view=view)

Get details about videos

This endpoint shows information about a video, including URLs to previews and the sizes that it is available in.

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
api_instance = shutterstock_api.VideosApi(shutterstock_api.ApiClient(configuration))
id = '\"30867073\"' # str | Video ID
view = 'full' # str | Amount of detail to render in the response (optional) (default to full)

try:
    # Get details about videos
    api_response = api_instance.get_video(id, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Video ID | 
 **view** | **str**| Amount of detail to render in the response | [optional] [default to full]

### Return type

[**Video**](Video.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_categories**
> CategoryDataList get_video_categories()

List video categories

This endpoint lists the categories (Shutterstock-assigned genres) that videos can belong to.

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
api_instance = shutterstock_api.VideosApi(shutterstock_api.ApiClient(configuration))

try:
    # List video categories
    api_response = api_instance.get_video_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CategoryDataList**](CategoryDataList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_license_list**
> DownloadHistoryDataList get_video_license_list(video_id=video_id, license=license, page=page, per_page=per_page, sort=sort)

List video licenses

This endpoint lists existing licenses. You can filter the results according to the type of license or the video ID.

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
api_instance = shutterstock_api.VideosApi(shutterstock_api.ApiClient(configuration))
video_id = 'video_id_example' # str | Show licenses for the specified video ID (optional)
license = 'license_example' # str | Show videos that are available with the specified license, such as `standard` or `enhanced`; prepending a `-` sign excludes results from that license (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page (optional) (default to 20)
sort = 'newest' # str | Sort by oldest or newest videos first (optional) (default to newest)

try:
    # List video licenses
    api_response = api_instance.get_video_license_list(video_id=video_id, license=license, page=page, per_page=per_page, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_license_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Show licenses for the specified video ID | [optional] 
 **license** | **str**| Show videos that are available with the specified license, such as &#x60;standard&#x60; or &#x60;enhanced&#x60;; prepending a &#x60;-&#x60; sign excludes results from that license | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 20]
 **sort** | **str**| Sort by oldest or newest videos first | [optional] [default to newest]

### Return type

[**DownloadHistoryDataList**](DownloadHistoryDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_list**
> VideoDataList get_video_list(id, view=view)

List videos

This endpoint lists information about one or more videos, including the aspect ratio and URLs to previews.

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
api_instance = shutterstock_api.VideosApi(shutterstock_api.ApiClient(configuration))
id = ['[ \"639703\", \"993721\" ]'] # list[str] | One or more video IDs
view = 'minimal' # str | Amount of detail to render in the response (optional) (default to minimal)

try:
    # List videos
    api_response = api_instance.get_video_list(id, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| One or more video IDs | 
 **view** | **str**| Amount of detail to render in the response | [optional] [default to minimal]

### Return type

[**VideoDataList**](VideoDataList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_videos**
> LicenseVideoResultDataList license_videos(body, subscription_id=subscription_id, size=size, search_id=search_id)

License videos

This endpoint gets licenses for one or more videos. You must specify the video IDs in the body parameter and the size and subscription ID either in the query parameter or with each video ID in the body parameter. Values in the body parameter override values in the query parameters.

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
api_instance = shutterstock_api.VideosApi(shutterstock_api.ApiClient(configuration))
body = shutterstock_api.LicenseVideoRequest() # LicenseVideoRequest | List of videos to request licenses for and information about each license transaction; these values override the defaults in the query parameters
subscription_id = 'subscription_id_example' # str | The subscription ID to use for licensing (optional)
size = 'web' # str | The size of the video to license (optional) (default to web)
search_id = 'search_id_example' # str | The Search ID that led to this licensing event (optional)

try:
    # License videos
    api_response = api_instance.license_videos(body, subscription_id=subscription_id, size=size, search_id=search_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->license_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LicenseVideoRequest**](LicenseVideoRequest.md)| List of videos to request licenses for and information about each license transaction; these values override the defaults in the query parameters | 
 **subscription_id** | **str**| The subscription ID to use for licensing | [optional] 
 **size** | **str**| The size of the video to license | [optional] [default to web]
 **search_id** | **str**| The Search ID that led to this licensing event | [optional] 

### Return type

[**LicenseVideoResultDataList**](LicenseVideoResultDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_clipbox**
> rename_clipbox(id, body)

Rename video collections

This endpoint sets a new name for a collection.

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
api_instance = shutterstock_api.VideosApi(shutterstock_api.ApiClient(configuration))
id = '\"17555176\"' # str | The ID of the collection to rename
body = shutterstock_api.CollectionUpdateRequest() # CollectionUpdateRequest | The new name for the collection

try:
    # Rename video collections
    api_instance.rename_clipbox(id, body)
except ApiException as e:
    print("Exception when calling VideosApi->rename_clipbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the collection to rename | 
 **body** | [**CollectionUpdateRequest**](CollectionUpdateRequest.md)| The new name for the collection | 

### Return type

void (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_videos**
> VideoSearchResults search_videos(added_date=added_date, added_date_start=added_date_start, added_date_end=added_date_end, aspect_ratio=aspect_ratio, category=category, contributor=contributor, duration=duration, duration_from=duration_from, duration_to=duration_to, fps=fps, fps_from=fps_from, fps_to=fps_to, language=language, license=license, model=model, page=page, per_page=per_page, people_age=people_age, people_ethnicity=people_ethnicity, people_gender=people_gender, people_number=people_number, people_model_released=people_model_released, query=query, resolution=resolution, safe=safe, sort=sort, view=view)

Search for videos

This endpoint searches for videos. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the `query` parameter by prefixing the term with NOT.

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
api_instance = shutterstock_api.VideosApi(shutterstock_api.ApiClient(configuration))
added_date = '2013-10-20' # date | Show videos added on the specified date, in the format YYYY-MM-DD (optional)
added_date_start = '2013-10-20' # date | Show videos added on or after the specified date, in the format YYYY-MM-DD (optional)
added_date_end = '2013-10-20' # date | Show videos added before the specified date, in the format YYYY-MM-DD (optional)
aspect_ratio = 'aspect_ratio_example' # str | Show videos with the specified aspect ratio (optional)
category = 'category_example' # str | Show videos with the specified Shutterstock-defined category; specify a category name or ID (optional)
contributor = ['contributor_example'] # list[str] | Show videos with the specified artist names or IDs (optional)
duration = 56 # int | (Deprecated; use duration_from and duration_to instead) Show videos with the specified duration (seconds) (optional)
duration_from = 56 # int | Show videos with the specified duration or longer (seconds) (optional)
duration_to = 56 # int | Show videos with the specified duration or shorter (seconds) (optional)
fps = 8.14 # float | (Deprecated; use fps_from and fps_to instead) Show videos with the specified frames per second (optional)
fps_from = 8.14 # float | Show videos with the specified frames per second or more (optional)
fps_to = 8.14 # float | Show videos with the specified frames per second or fewer (optional)
language = 'language_example' # str | Set query and result language (uses Accept-Language header if not set) (optional)
license = ['[ \"commercial\", \"editorial\" ]'] # list[str] | Show only videos with the specified license or licenses (optional)
model = ['[ \"442583\", \"434750\" ]'] # list[str] | Show videos with each of the specified models (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page (optional) (default to 20)
people_age = 'people_age_example' # str | Show videos that feature people of the specified age range (optional)
people_ethnicity = 'people_ethnicity_example' # str | Show videos with people of the specified ethnicity (optional)
people_gender = 'people_gender_example' # str | Show videos with people with the specified gender (optional)
people_number = 56 # int | Show videos with the specified number of people (optional)
people_model_released = true # bool | Show only videos of people with a signed model release (optional)
query = 'query_example' # str | One or more search terms separated by spaces; you can use NOT to filter out videos that match a term (optional)
resolution = 'resolution_example' # str | Show videos with the specified resolution (optional)
safe = true # bool | Enable or disable safe search (optional) (default to true)
sort = 'popular' # str | Sort by one of these categories (optional) (default to popular)
view = 'minimal' # str | Amount of detail to render in the response (optional) (default to minimal)

try:
    # Search for videos
    api_response = api_instance.search_videos(added_date=added_date, added_date_start=added_date_start, added_date_end=added_date_end, aspect_ratio=aspect_ratio, category=category, contributor=contributor, duration=duration, duration_from=duration_from, duration_to=duration_to, fps=fps, fps_from=fps_from, fps_to=fps_to, language=language, license=license, model=model, page=page, per_page=per_page, people_age=people_age, people_ethnicity=people_ethnicity, people_gender=people_gender, people_number=people_number, people_model_released=people_model_released, query=query, resolution=resolution, safe=safe, sort=sort, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->search_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **added_date** | **date**| Show videos added on the specified date, in the format YYYY-MM-DD | [optional] 
 **added_date_start** | **date**| Show videos added on or after the specified date, in the format YYYY-MM-DD | [optional] 
 **added_date_end** | **date**| Show videos added before the specified date, in the format YYYY-MM-DD | [optional] 
 **aspect_ratio** | **str**| Show videos with the specified aspect ratio | [optional] 
 **category** | **str**| Show videos with the specified Shutterstock-defined category; specify a category name or ID | [optional] 
 **contributor** | [**list[str]**](str.md)| Show videos with the specified artist names or IDs | [optional] 
 **duration** | **int**| (Deprecated; use duration_from and duration_to instead) Show videos with the specified duration (seconds) | [optional] 
 **duration_from** | **int**| Show videos with the specified duration or longer (seconds) | [optional] 
 **duration_to** | **int**| Show videos with the specified duration or shorter (seconds) | [optional] 
 **fps** | **float**| (Deprecated; use fps_from and fps_to instead) Show videos with the specified frames per second | [optional] 
 **fps_from** | **float**| Show videos with the specified frames per second or more | [optional] 
 **fps_to** | **float**| Show videos with the specified frames per second or fewer | [optional] 
 **language** | **str**| Set query and result language (uses Accept-Language header if not set) | [optional] 
 **license** | [**list[str]**](str.md)| Show only videos with the specified license or licenses | [optional] 
 **model** | [**list[str]**](str.md)| Show videos with each of the specified models | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 20]
 **people_age** | **str**| Show videos that feature people of the specified age range | [optional] 
 **people_ethnicity** | **str**| Show videos with people of the specified ethnicity | [optional] 
 **people_gender** | **str**| Show videos with people with the specified gender | [optional] 
 **people_number** | **int**| Show videos with the specified number of people | [optional] 
 **people_model_released** | **bool**| Show only videos of people with a signed model release | [optional] 
 **query** | **str**| One or more search terms separated by spaces; you can use NOT to filter out videos that match a term | [optional] 
 **resolution** | **str**| Show videos with the specified resolution | [optional] 
 **safe** | **bool**| Enable or disable safe search | [optional] [default to true]
 **sort** | **str**| Sort by one of these categories | [optional] [default to popular]
 **view** | **str**| Amount of detail to render in the response | [optional] [default to minimal]

### Return type

[**VideoSearchResults**](VideoSearchResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

