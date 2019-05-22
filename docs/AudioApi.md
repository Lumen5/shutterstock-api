# shutterstock_api.AudioApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_soundbox_items**](AudioApi.md#add_soundbox_items) | **POST** /v2/audio/collections/{id}/items | Add audio tracks to collections
[**create_soundbox**](AudioApi.md#create_soundbox) | **POST** /v2/audio/collections | Create audio collections
[**delete_soundbox**](AudioApi.md#delete_soundbox) | **DELETE** /v2/audio/collections/{id} | Delete audio collections
[**delete_soundbox_items**](AudioApi.md#delete_soundbox_items) | **DELETE** /v2/audio/collections/{id}/items | Remove audio tracks from collections
[**download_tracks**](AudioApi.md#download_tracks) | **POST** /v2/audio/licenses/{id}/downloads | Download audio tracks
[**get_audio_license_list**](AudioApi.md#get_audio_license_list) | **GET** /v2/audio/licenses | List audio licenses
[**get_soundbox**](AudioApi.md#get_soundbox) | **GET** /v2/audio/collections/{id} | Get the details of audio collections
[**get_soundbox_items**](AudioApi.md#get_soundbox_items) | **GET** /v2/audio/collections/{id}/items | Get the contents of audio collections
[**get_soundbox_list**](AudioApi.md#get_soundbox_list) | **GET** /v2/audio/collections | List audio collections
[**get_track**](AudioApi.md#get_track) | **GET** /v2/audio/{id} | Get details about audio tracks
[**get_track_list**](AudioApi.md#get_track_list) | **GET** /v2/audio | List audio tracks
[**license_track**](AudioApi.md#license_track) | **POST** /v2/audio/licenses | License audio tracks
[**rename_soundbox**](AudioApi.md#rename_soundbox) | **POST** /v2/audio/collections/{id} | Rename audio collections
[**search_audio**](AudioApi.md#search_audio) | **GET** /v2/audio/search | Search for tracks


# **add_soundbox_items**
> add_soundbox_items(id, body)

Add audio tracks to collections

This endpoint adds one or more tracks to a collection by track IDs.

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
api_instance = shutterstock_api.AudioApi(shutterstock_api.ApiClient(configuration))
id = '\"48433115\"' # str | Collection ID
body = shutterstock_api.CollectionItemRequest() # CollectionItemRequest | List of items to add to collection

try:
    # Add audio tracks to collections
    api_instance.add_soundbox_items(id, body)
except ApiException as e:
    print("Exception when calling AudioApi->add_soundbox_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **body** | [**CollectionItemRequest**](CollectionItemRequest.md)| List of items to add to collection | 

### Return type

void (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_soundbox**
> CollectionCreateResponse create_soundbox(body)

Create audio collections

This endpoint creates one or more collections (soundboxes). To add tracks, use `POST /audio/collections/{id}/items`.

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
api_instance = shutterstock_api.AudioApi(shutterstock_api.ApiClient(configuration))
body = shutterstock_api.CollectionCreateRequest() # CollectionCreateRequest | Collection metadata

try:
    # Create audio collections
    api_response = api_instance.create_soundbox(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->create_soundbox: %s\n" % e)
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

# **delete_soundbox**
> delete_soundbox(id)

Delete audio collections

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
api_instance = shutterstock_api.AudioApi(shutterstock_api.ApiClient(configuration))
id = '\"48433111\"' # str | Collection ID

try:
    # Delete audio collections
    api_instance.delete_soundbox(id)
except ApiException as e:
    print("Exception when calling AudioApi->delete_soundbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 

### Return type

void (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_soundbox_items**
> delete_soundbox_items(id, item_id=item_id)

Remove audio tracks from collections

This endpoint removes one or more tracks from a collection.

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
api_instance = shutterstock_api.AudioApi(shutterstock_api.ApiClient(configuration))
id = '\"48433119\"' # str | Collection ID
item_id = ['[ \"76688182\", \"40005859\" ]'] # list[str] | One or more item IDs to remove from the collection (optional)

try:
    # Remove audio tracks from collections
    api_instance.delete_soundbox_items(id, item_id=item_id)
except ApiException as e:
    print("Exception when calling AudioApi->delete_soundbox_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **item_id** | [**list[str]**](str.md)| One or more item IDs to remove from the collection | [optional] 

### Return type

void (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_tracks**
> Url download_tracks(id)

Download audio tracks

This endpoint redownloads tracks that you have already received a license for.

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
api_instance = shutterstock_api.AudioApi(shutterstock_api.ApiClient(configuration))
id = '\"i1188641348\"' # str | License ID

try:
    # Download audio tracks
    api_response = api_instance.download_tracks(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->download_tracks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| License ID | 

### Return type

[**Url**](Url.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audio_license_list**
> DownloadHistoryDataList get_audio_license_list(audio_id=audio_id)

List audio licenses

This endpoint lists existing licenses. You can filter the results according to the track ID to see if you have an existing license for a specific track.

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
api_instance = shutterstock_api.AudioApi(shutterstock_api.ApiClient(configuration))
audio_id = '\"1\"' # str | Show licenses for the specified track ID (optional)

try:
    # List audio licenses
    api_response = api_instance.get_audio_license_list(audio_id=audio_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->get_audio_license_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audio_id** | **str**| Show licenses for the specified track ID | [optional] 

### Return type

[**DownloadHistoryDataList**](DownloadHistoryDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_soundbox**
> Collection get_soundbox(id)

Get the details of audio collections

This endpoint gets more detailed information about a collection, including the number of items in it and when it was last updated. To get the tracks in collections, use `GET /audio/collections/{id}/items`.

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
api_instance = shutterstock_api.AudioApi(shutterstock_api.ApiClient(configuration))
id = '\"48433107\"' # str | Collection ID

try:
    # Get the details of audio collections
    api_response = api_instance.get_soundbox(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->get_soundbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 

### Return type

[**Collection**](Collection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_soundbox_items**
> CollectionItemDataList get_soundbox_items(id, page=page, per_page=per_page, sort=sort)

Get the contents of audio collections

This endpoint lists the IDs of tracks in a collection and the date that each was added.

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
api_instance = shutterstock_api.AudioApi(shutterstock_api.ApiClient(configuration))
id = '\"48433113\"' # str | Collection ID
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Number of results per page (optional) (default to 100)
sort = 'oldest' # str | Sort order (optional) (default to oldest)

try:
    # Get the contents of audio collections
    api_response = api_instance.get_soundbox_items(id, page=page, per_page=per_page, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->get_soundbox_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
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

# **get_soundbox_list**
> CollectionDataList get_soundbox_list(page=page, per_page=per_page)

List audio collections

This endpoint lists your collections of audio tracks and their basic attributes.

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
api_instance = shutterstock_api.AudioApi(shutterstock_api.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Number of results per page (optional) (default to 100)

try:
    # List audio collections
    api_response = api_instance.get_soundbox_list(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->get_soundbox_list: %s\n" % e)
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

# **get_track**
> Audio get_track(id, view=view)

Get details about audio tracks

This endpoint shows information about a track, including its genres, instruments, and other attributes.

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
api_instance = shutterstock_api.AudioApi(shutterstock_api.ApiClient(configuration))
id = '\"442583\"' # str | Audio track ID
view = 'full' # str | Amount of detail to render in the response (optional) (default to full)

try:
    # Get details about audio tracks
    api_response = api_instance.get_track(id, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->get_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Audio track ID | 
 **view** | **str**| Amount of detail to render in the response | [optional] [default to full]

### Return type

[**Audio**](Audio.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_track_list**
> AudioDataList get_track_list(id, view=view)

List audio tracks

This endpoint lists information about one or more audio tracks, including the description and publication date.

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
api_instance = shutterstock_api.AudioApi(shutterstock_api.ApiClient(configuration))
id = ['[ \"442583\", \"434750\" ]'] # list[str] | One or more audio IDs
view = 'minimal' # str | Amount of detail to render in the response (optional) (default to minimal)

try:
    # List audio tracks
    api_response = api_instance.get_track_list(id, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->get_track_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| One or more audio IDs | 
 **view** | **str**| Amount of detail to render in the response | [optional] [default to minimal]

### Return type

[**AudioDataList**](AudioDataList.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_track**
> LicenseAudioResultDataList license_track(body, license=license, search_id=search_id)

License audio tracks

This endpoint gets licenses for one or more tracks.

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
api_instance = shutterstock_api.AudioApi(shutterstock_api.ApiClient(configuration))
body = shutterstock_api.LicenseAudioRequest() # LicenseAudioRequest | Tracks to license
license = 'audio_standard' # str | License type (optional) (default to audio_standard)
search_id = 'search_id_example' # str | The ID of the search that led to licensing this track (optional)

try:
    # License audio tracks
    api_response = api_instance.license_track(body, license=license, search_id=search_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->license_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LicenseAudioRequest**](LicenseAudioRequest.md)| Tracks to license | 
 **license** | **str**| License type | [optional] [default to audio_standard]
 **search_id** | **str**| The ID of the search that led to licensing this track | [optional] 

### Return type

[**LicenseAudioResultDataList**](LicenseAudioResultDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_soundbox**
> rename_soundbox(id, body)

Rename audio collections

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
api_instance = shutterstock_api.AudioApi(shutterstock_api.ApiClient(configuration))
id = '\"48433107\"' # str | Collection ID
body = shutterstock_api.CollectionUpdateRequest() # CollectionUpdateRequest | Collection changes

try:
    # Rename audio collections
    api_instance.rename_soundbox(id, body)
except ApiException as e:
    print("Exception when calling AudioApi->rename_soundbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **body** | [**CollectionUpdateRequest**](CollectionUpdateRequest.md)| Collection changes | 

### Return type

void (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_audio**
> AudioSearchResults search_audio(artists=artists, bpm=bpm, bpm_from=bpm_from, bpm_to=bpm_to, duration=duration, duration_from=duration_from, duration_to=duration_to, genre=genre, is_instrumental=is_instrumental, instruments=instruments, moods=moods, page=page, per_page=per_page, query=query, sort=sort, sort_order=sort_order, vocal_description=vocal_description, view=view)

Search for tracks

This endpoint searches for tracks. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter.

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
api_instance = shutterstock_api.AudioApi(shutterstock_api.ApiClient(configuration))
artists = ['artists_example'] # list[str] | Show tracks with one of the specified artist names or IDs (optional)
bpm = 56 # int | (Deprecated; use bpm_from and bpm_to instead) Show tracks with the specified beats per minute (optional)
bpm_from = 56 # int | Show tracks with the specified beats per minute or faster (optional)
bpm_to = 56 # int | Show tracks with the specified beats per minute or slower (optional)
duration = 56 # int | Show tracks with the specified duration (seconds) (optional)
duration_from = 56 # int | Show tracks with the specified duration or longer (seconds) (optional)
duration_to = 56 # int | Show tracks with the specified duration or shorter (seconds) (optional)
genre = ['[ \"Classical\", \"Holiday\" ]'] # list[str] | Show tracks with each of the specified genres (optional)
is_instrumental = true # bool | Show instrumental music only (optional)
instruments = ['[ \"Trumpet\", \"Percussion\" ]'] # list[str] | Show tracks with each of the specified instruments (optional)
moods = ['[ \"Confident\", \"Playful\" ]'] # list[str] | Show tracks with each of the specified moods (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 20 # int | Number of results per page (optional) (default to 20)
query = '\"drum\"' # str | One or more search terms separated by spaces (optional)
sort = 'sort_example' # str | Sort by (optional)
sort_order = 'desc' # str | Sort order, asc or desc (optional) (default to desc)
vocal_description = 'vocal_description_example' # str | Show tracks with the specified vocal description (male, female) (optional)
view = 'minimal' # str | Amount of detail to render in the response (optional) (default to minimal)

try:
    # Search for tracks
    api_response = api_instance.search_audio(artists=artists, bpm=bpm, bpm_from=bpm_from, bpm_to=bpm_to, duration=duration, duration_from=duration_from, duration_to=duration_to, genre=genre, is_instrumental=is_instrumental, instruments=instruments, moods=moods, page=page, per_page=per_page, query=query, sort=sort, sort_order=sort_order, vocal_description=vocal_description, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudioApi->search_audio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artists** | [**list[str]**](str.md)| Show tracks with one of the specified artist names or IDs | [optional] 
 **bpm** | **int**| (Deprecated; use bpm_from and bpm_to instead) Show tracks with the specified beats per minute | [optional] 
 **bpm_from** | **int**| Show tracks with the specified beats per minute or faster | [optional] 
 **bpm_to** | **int**| Show tracks with the specified beats per minute or slower | [optional] 
 **duration** | **int**| Show tracks with the specified duration (seconds) | [optional] 
 **duration_from** | **int**| Show tracks with the specified duration or longer (seconds) | [optional] 
 **duration_to** | **int**| Show tracks with the specified duration or shorter (seconds) | [optional] 
 **genre** | [**list[str]**](str.md)| Show tracks with each of the specified genres | [optional] 
 **is_instrumental** | **bool**| Show instrumental music only | [optional] 
 **instruments** | [**list[str]**](str.md)| Show tracks with each of the specified instruments | [optional] 
 **moods** | [**list[str]**](str.md)| Show tracks with each of the specified moods | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Number of results per page | [optional] [default to 20]
 **query** | **str**| One or more search terms separated by spaces | [optional] 
 **sort** | **str**| Sort by | [optional] 
 **sort_order** | **str**| Sort order, asc or desc | [optional] [default to desc]
 **vocal_description** | **str**| Show tracks with the specified vocal description (male, female) | [optional] 
 **view** | **str**| Amount of detail to render in the response | [optional] [default to minimal]

### Return type

[**AudioSearchResults**](AudioSearchResults.md)

### Authorization

[basic](../README.md#basic), [customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

