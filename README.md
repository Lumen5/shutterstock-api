# shutterstock-api
The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.6
- Package version: 0.2.2
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import shutterstock_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import shutterstock_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.shutterstock.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AudioApi* | [**add_soundbox_items**](docs/AudioApi.md#add_soundbox_items) | **POST** /v2/audio/collections/{id}/items | Add audio tracks to collections
*AudioApi* | [**create_soundbox**](docs/AudioApi.md#create_soundbox) | **POST** /v2/audio/collections | Create audio collections
*AudioApi* | [**delete_soundbox**](docs/AudioApi.md#delete_soundbox) | **DELETE** /v2/audio/collections/{id} | Delete audio collections
*AudioApi* | [**delete_soundbox_items**](docs/AudioApi.md#delete_soundbox_items) | **DELETE** /v2/audio/collections/{id}/items | Remove audio tracks from collections
*AudioApi* | [**download_tracks**](docs/AudioApi.md#download_tracks) | **POST** /v2/audio/licenses/{id}/downloads | Download audio tracks
*AudioApi* | [**get_audio_license_list**](docs/AudioApi.md#get_audio_license_list) | **GET** /v2/audio/licenses | List audio licenses
*AudioApi* | [**get_soundbox**](docs/AudioApi.md#get_soundbox) | **GET** /v2/audio/collections/{id} | Get the details of audio collections
*AudioApi* | [**get_soundbox_items**](docs/AudioApi.md#get_soundbox_items) | **GET** /v2/audio/collections/{id}/items | Get the contents of audio collections
*AudioApi* | [**get_soundbox_list**](docs/AudioApi.md#get_soundbox_list) | **GET** /v2/audio/collections | List audio collections
*AudioApi* | [**get_track**](docs/AudioApi.md#get_track) | **GET** /v2/audio/{id} | Get details about audio tracks
*AudioApi* | [**get_track_list**](docs/AudioApi.md#get_track_list) | **GET** /v2/audio | List audio tracks
*AudioApi* | [**license_track**](docs/AudioApi.md#license_track) | **POST** /v2/audio/licenses | License audio tracks
*AudioApi* | [**rename_soundbox**](docs/AudioApi.md#rename_soundbox) | **POST** /v2/audio/collections/{id} | Rename audio collections
*AudioApi* | [**search_audio**](docs/AudioApi.md#search_audio) | **GET** /v2/audio/search | Search for tracks
*ContributorsApi* | [**get_contributor**](docs/ContributorsApi.md#get_contributor) | **GET** /v2/contributors/{contributor_id} | Get details about a single contributor
*ContributorsApi* | [**get_contributor_collection_items**](docs/ContributorsApi.md#get_contributor_collection_items) | **GET** /v2/contributors/{contributor_id}/collections/{id}/items | Get the items in contributors&#39; collections
*ContributorsApi* | [**get_contributor_collections**](docs/ContributorsApi.md#get_contributor_collections) | **GET** /v2/contributors/{contributor_id}/collections/{id} | Get details about contributors&#39; collections
*ContributorsApi* | [**get_contributor_collections_list**](docs/ContributorsApi.md#get_contributor_collections_list) | **GET** /v2/contributors/{contributor_id}/collections | List contributors&#39; collections
*ContributorsApi* | [**get_contributor_list**](docs/ContributorsApi.md#get_contributor_list) | **GET** /v2/contributors | Get details about multiple contributors
*EditorialApi* | [**get_editorial_image**](docs/EditorialApi.md#get_editorial_image) | **GET** /v2/editorial/{id} | Get editorial content details
*EditorialApi* | [**get_editorial_livefeed**](docs/EditorialApi.md#get_editorial_livefeed) | **GET** /v2/editorial/livefeeds/{id} | Get editorial livefeed
*EditorialApi* | [**get_editorial_livefeed_items**](docs/EditorialApi.md#get_editorial_livefeed_items) | **GET** /v2/editorial/livefeeds/{id}/items | Get editorial livefeed items
*EditorialApi* | [**get_editorial_livefeed_list**](docs/EditorialApi.md#get_editorial_livefeed_list) | **GET** /v2/editorial/livefeeds | Get editorial livefeed list
*EditorialApi* | [**license_editorial_image**](docs/EditorialApi.md#license_editorial_image) | **POST** /v2/editorial/licenses | License editorial content
*EditorialApi* | [**search_editorial**](docs/EditorialApi.md#search_editorial) | **GET** /v2/editorial/search | Search editorial content
*ImagesApi* | [**add_lightbox_items**](docs/ImagesApi.md#add_lightbox_items) | **POST** /v2/images/collections/{id}/items | Add images to collections
*ImagesApi* | [**create_lightbox**](docs/ImagesApi.md#create_lightbox) | **POST** /v2/images/collections | Create image collections
*ImagesApi* | [**delete_lightbox**](docs/ImagesApi.md#delete_lightbox) | **DELETE** /v2/images/collections/{id} | Delete image collections
*ImagesApi* | [**delete_lightbox_items**](docs/ImagesApi.md#delete_lightbox_items) | **DELETE** /v2/images/collections/{id}/items | Remove images from collections
*ImagesApi* | [**download_image**](docs/ImagesApi.md#download_image) | **POST** /v2/images/licenses/{id}/downloads | Download images
*ImagesApi* | [**get_featured_lightbox**](docs/ImagesApi.md#get_featured_lightbox) | **GET** /v2/images/collections/featured/{id} | Get the details of featured image collections
*ImagesApi* | [**get_featured_lightbox_items**](docs/ImagesApi.md#get_featured_lightbox_items) | **GET** /v2/images/collections/featured/{id}/items | Get the contents of featured image collections
*ImagesApi* | [**get_featured_lightbox_list**](docs/ImagesApi.md#get_featured_lightbox_list) | **GET** /v2/images/collections/featured | List featured image collections
*ImagesApi* | [**get_image**](docs/ImagesApi.md#get_image) | **GET** /v2/images/{id} | Get details about images
*ImagesApi* | [**get_image_categories**](docs/ImagesApi.md#get_image_categories) | **GET** /v2/images/categories | List image categories
*ImagesApi* | [**get_image_license_list**](docs/ImagesApi.md#get_image_license_list) | **GET** /v2/images/licenses | List image licenses
*ImagesApi* | [**get_image_list**](docs/ImagesApi.md#get_image_list) | **GET** /v2/images | List images
*ImagesApi* | [**get_image_recommendations**](docs/ImagesApi.md#get_image_recommendations) | **GET** /v2/images/recommendations | List recommended images
*ImagesApi* | [**get_lightbox**](docs/ImagesApi.md#get_lightbox) | **GET** /v2/images/collections/{id} | Get the details of image collections
*ImagesApi* | [**get_lightbox_items**](docs/ImagesApi.md#get_lightbox_items) | **GET** /v2/images/collections/{id}/items | Get the contents of image collections
*ImagesApi* | [**get_lightbox_list**](docs/ImagesApi.md#get_lightbox_list) | **GET** /v2/images/collections | List image collections
*ImagesApi* | [**get_similar_images**](docs/ImagesApi.md#get_similar_images) | **GET** /v2/images/{id}/similar | List similar images
*ImagesApi* | [**get_updated_images**](docs/ImagesApi.md#get_updated_images) | **GET** /v2/images/updated | List updated images
*ImagesApi* | [**license_images**](docs/ImagesApi.md#license_images) | **POST** /v2/images/licenses | License images
*ImagesApi* | [**rename_lightbox**](docs/ImagesApi.md#rename_lightbox) | **POST** /v2/images/collections/{id} | Rename image collections
*ImagesApi* | [**search_images**](docs/ImagesApi.md#search_images) | **GET** /v2/images/search | Search for images
*ImagesApi* | [**upload_ephemeral_image**](docs/ImagesApi.md#upload_ephemeral_image) | **POST** /v2/images | Upload images
*TestApi* | [**echo**](docs/TestApi.md#echo) | **GET** /v2/test | Echo text
*TestApi* | [**validate**](docs/TestApi.md#validate) | **GET** /v2/test/validate | Validate input
*UsersApi* | [**create_user**](docs/UsersApi.md#create_user) | **POST** /v2/user | Register user
*UsersApi* | [**get_access_token**](docs/UsersApi.md#get_access_token) | **GET** /v2/user/access_token | Get access token details
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /v2/user | Get user details
*UsersApi* | [**get_user_subsciption_list**](docs/UsersApi.md#get_user_subsciption_list) | **GET** /v2/user/subscriptions | List user subscriptions
*VideosApi* | [**add_clipbox_items**](docs/VideosApi.md#add_clipbox_items) | **POST** /v2/videos/collections/{id}/items | Add videos to collections
*VideosApi* | [**create_clipbox**](docs/VideosApi.md#create_clipbox) | **POST** /v2/videos/collections | Create video collections
*VideosApi* | [**delete_clipbox**](docs/VideosApi.md#delete_clipbox) | **DELETE** /v2/videos/collections/{id} | Delete video collections
*VideosApi* | [**delete_clipbox_items**](docs/VideosApi.md#delete_clipbox_items) | **DELETE** /v2/videos/collections/{id}/items | Remove videos from collections
*VideosApi* | [**download_videos**](docs/VideosApi.md#download_videos) | **POST** /v2/videos/licenses/{id}/downloads | Download videos
*VideosApi* | [**get_clipbox**](docs/VideosApi.md#get_clipbox) | **GET** /v2/videos/collections/{id} | Get the details of video collections
*VideosApi* | [**get_clipbox_items**](docs/VideosApi.md#get_clipbox_items) | **GET** /v2/videos/collections/{id}/items | Get the contents of video collections
*VideosApi* | [**get_clipbox_list**](docs/VideosApi.md#get_clipbox_list) | **GET** /v2/videos/collections | List video collections
*VideosApi* | [**get_similar_videos**](docs/VideosApi.md#get_similar_videos) | **GET** /v2/videos/{id}/similar | List similar videos
*VideosApi* | [**get_updated_videos**](docs/VideosApi.md#get_updated_videos) | **GET** /v2/videos/updated | List updated videos
*VideosApi* | [**get_video**](docs/VideosApi.md#get_video) | **GET** /v2/videos/{id} | Get details about videos
*VideosApi* | [**get_video_categories**](docs/VideosApi.md#get_video_categories) | **GET** /v2/videos/categories | List video categories
*VideosApi* | [**get_video_license_list**](docs/VideosApi.md#get_video_license_list) | **GET** /v2/videos/licenses | List video licenses
*VideosApi* | [**get_video_list**](docs/VideosApi.md#get_video_list) | **GET** /v2/videos | List videos
*VideosApi* | [**license_videos**](docs/VideosApi.md#license_videos) | **POST** /v2/videos/licenses | License videos
*VideosApi* | [**rename_clipbox**](docs/VideosApi.md#rename_clipbox) | **POST** /v2/videos/collections/{id} | Rename video collections
*VideosApi* | [**search_videos**](docs/VideosApi.md#search_videos) | **GET** /v2/videos/search | Search for videos


## Documentation For Models

 - [AccessTokenDetails](docs/AccessTokenDetails.md)
 - [Album](docs/Album.md)
 - [Allotment](docs/Allotment.md)
 - [Artist](docs/Artist.md)
 - [Audio](docs/Audio.md)
 - [AudioAssetDetails](docs/AudioAssetDetails.md)
 - [AudioAssets](docs/AudioAssets.md)
 - [AudioDataList](docs/AudioDataList.md)
 - [AudioSearchResults](docs/AudioSearchResults.md)
 - [Category](docs/Category.md)
 - [CategoryDataList](docs/CategoryDataList.md)
 - [Collection](docs/Collection.md)
 - [CollectionCreateRequest](docs/CollectionCreateRequest.md)
 - [CollectionCreateResponse](docs/CollectionCreateResponse.md)
 - [CollectionDataList](docs/CollectionDataList.md)
 - [CollectionItem](docs/CollectionItem.md)
 - [CollectionItemDataList](docs/CollectionItemDataList.md)
 - [CollectionItemRequest](docs/CollectionItemRequest.md)
 - [CollectionUpdateRequest](docs/CollectionUpdateRequest.md)
 - [Contributor](docs/Contributor.md)
 - [ContributorProfile](docs/ContributorProfile.md)
 - [ContributorProfileDataList](docs/ContributorProfileDataList.md)
 - [ContributorProfileSocialMedia](docs/ContributorProfileSocialMedia.md)
 - [Cookie](docs/Cookie.md)
 - [DownloadHistory](docs/DownloadHistory.md)
 - [DownloadHistoryDataList](docs/DownloadHistoryDataList.md)
 - [DownloadHistoryFormatDetails](docs/DownloadHistoryFormatDetails.md)
 - [DownloadHistoryMediaDetails](docs/DownloadHistoryMediaDetails.md)
 - [DownloadHistoryUserDetails](docs/DownloadHistoryUserDetails.md)
 - [EditorialAssets](docs/EditorialAssets.md)
 - [EditorialCategory](docs/EditorialCategory.md)
 - [EditorialContent](docs/EditorialContent.md)
 - [EditorialContentDataList](docs/EditorialContentDataList.md)
 - [EditorialCoverItem](docs/EditorialCoverItem.md)
 - [EditorialLivefeed](docs/EditorialLivefeed.md)
 - [EditorialLivefeedList](docs/EditorialLivefeedList.md)
 - [EditorialSearchResults](docs/EditorialSearchResults.md)
 - [Error](docs/Error.md)
 - [FeaturedCollection](docs/FeaturedCollection.md)
 - [FeaturedCollectionCoverItem](docs/FeaturedCollectionCoverItem.md)
 - [FeaturedCollectionDataList](docs/FeaturedCollectionDataList.md)
 - [Image](docs/Image.md)
 - [ImageAssets](docs/ImageAssets.md)
 - [ImageCreateRequest](docs/ImageCreateRequest.md)
 - [ImageCreateResponse](docs/ImageCreateResponse.md)
 - [ImageDataList](docs/ImageDataList.md)
 - [ImageSearchResults](docs/ImageSearchResults.md)
 - [ImageSizeDetails](docs/ImageSizeDetails.md)
 - [LicenseAudio](docs/LicenseAudio.md)
 - [LicenseAudioRequest](docs/LicenseAudioRequest.md)
 - [LicenseAudioResult](docs/LicenseAudioResult.md)
 - [LicenseAudioResultDataList](docs/LicenseAudioResultDataList.md)
 - [LicenseEditorialContent](docs/LicenseEditorialContent.md)
 - [LicenseEditorialContentRequest](docs/LicenseEditorialContentRequest.md)
 - [LicenseEditorialContentResult](docs/LicenseEditorialContentResult.md)
 - [LicenseEditorialContentResultDataList](docs/LicenseEditorialContentResultDataList.md)
 - [LicenseFormat](docs/LicenseFormat.md)
 - [LicenseImage](docs/LicenseImage.md)
 - [LicenseImageRequest](docs/LicenseImageRequest.md)
 - [LicenseImageResult](docs/LicenseImageResult.md)
 - [LicenseImageResultDataList](docs/LicenseImageResultDataList.md)
 - [LicenseRequestMetadata](docs/LicenseRequestMetadata.md)
 - [LicenseVideo](docs/LicenseVideo.md)
 - [LicenseVideoRequest](docs/LicenseVideoRequest.md)
 - [LicenseVideoResult](docs/LicenseVideoResult.md)
 - [LicenseVideoResultDataList](docs/LicenseVideoResultDataList.md)
 - [Model](docs/Model.md)
 - [ModelRelease](docs/ModelRelease.md)
 - [Price](docs/Price.md)
 - [Recommendation](docs/Recommendation.md)
 - [RecommendationDataList](docs/RecommendationDataList.md)
 - [RedownloadImage](docs/RedownloadImage.md)
 - [RedownloadVideo](docs/RedownloadVideo.md)
 - [Subscription](docs/Subscription.md)
 - [SubscriptionDataList](docs/SubscriptionDataList.md)
 - [SubscriptionMetadata](docs/SubscriptionMetadata.md)
 - [TestEcho](docs/TestEcho.md)
 - [TestValidate](docs/TestValidate.md)
 - [TestValidateHeader](docs/TestValidateHeader.md)
 - [TestValidateQuery](docs/TestValidateQuery.md)
 - [Thumbnail](docs/Thumbnail.md)
 - [UpdatedMedia](docs/UpdatedMedia.md)
 - [UpdatedMediaDataList](docs/UpdatedMediaDataList.md)
 - [Url](docs/Url.md)
 - [Urls](docs/Urls.md)
 - [UserDetails](docs/UserDetails.md)
 - [UserPostRequest](docs/UserPostRequest.md)
 - [UserPostResponse](docs/UserPostResponse.md)
 - [Video](docs/Video.md)
 - [VideoAssets](docs/VideoAssets.md)
 - [VideoDataList](docs/VideoDataList.md)
 - [VideoSearchResults](docs/VideoSearchResults.md)
 - [VideoSizeDetails](docs/VideoSizeDetails.md)


## Documentation For Authorization


## basic

- **Type**: HTTP basic authentication

## customer_accessCode

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://accounts.shutterstock.com/oauth/authorize
- **Scopes**: 
 - **licenses.create**: Grant the ability to download and license media on behalf of the user.
 - **purchases.view**: Grant read-only access to a user's purchase history.
 - **licenses.view**: Grant read-only access to a user's licenses.
 - **collections.edit**: Grant the ability to create new collections, edit a collection, and modify the contents of a collection
 - **collections.view**: Grant read-only access to a collection and its contents.
 - **user.view**: Grants read-only access to a user's basic account information (includes username, id, first and last name). If email is the same as username, it also implies user.email


## Author



