# coding: utf-8

"""
    Shutterstock API Reference

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.  # noqa: E501

    OpenAPI spec version: 1.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from shutterstock_api.models.album import Album  # noqa: F401,E501
from shutterstock_api.models.artist import Artist  # noqa: F401,E501
from shutterstock_api.models.audio_assets import AudioAssets  # noqa: F401,E501
from shutterstock_api.models.contributor import Contributor  # noqa: F401,E501
from shutterstock_api.models.model_release import ModelRelease  # noqa: F401,E501


class Audio(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'added_date': 'date',
        'affiliate_url': 'str',
        'album': 'Album',
        'artists': 'list[Artist]',
        'assets': 'AudioAssets',
        'bpm': 'int',
        'contributor': 'Contributor',
        'deleted_time': 'datetime',
        'description': 'str',
        'duration': 'int',
        'genres': 'list[str]',
        'id': 'str',
        'instruments': 'list[str]',
        'is_adult': 'bool',
        'is_instrumental': 'bool',
        'isrc': 'str',
        'keywords': 'list[str]',
        'language': 'str',
        'lyrics': 'str',
        'media_type': 'str',
        'model_releases': 'list[ModelRelease]',
        'moods': 'list[str]',
        'published_time': 'datetime',
        'recording_version': 'str',
        'releases': 'list[str]',
        'similar_artists': 'list[Artist]',
        'submitted_time': 'datetime',
        'title': 'str',
        'updated_time': 'datetime',
        'vocal_description': 'str',
        'url': 'str'
    }

    attribute_map = {
        'added_date': 'added_date',
        'affiliate_url': 'affiliate_url',
        'album': 'album',
        'artists': 'artists',
        'assets': 'assets',
        'bpm': 'bpm',
        'contributor': 'contributor',
        'deleted_time': 'deleted_time',
        'description': 'description',
        'duration': 'duration',
        'genres': 'genres',
        'id': 'id',
        'instruments': 'instruments',
        'is_adult': 'is_adult',
        'is_instrumental': 'is_instrumental',
        'isrc': 'isrc',
        'keywords': 'keywords',
        'language': 'language',
        'lyrics': 'lyrics',
        'media_type': 'media_type',
        'model_releases': 'model_releases',
        'moods': 'moods',
        'published_time': 'published_time',
        'recording_version': 'recording_version',
        'releases': 'releases',
        'similar_artists': 'similar_artists',
        'submitted_time': 'submitted_time',
        'title': 'title',
        'updated_time': 'updated_time',
        'vocal_description': 'vocal_description',
        'url': 'url'
    }

    def __init__(self, added_date=None, affiliate_url=None, album=None, artists=None, assets=None, bpm=None, contributor=None, deleted_time=None, description=None, duration=None, genres=None, id=None, instruments=None, is_adult=None, is_instrumental=None, isrc=None, keywords=None, language=None, lyrics=None, media_type=None, model_releases=None, moods=None, published_time=None, recording_version=None, releases=None, similar_artists=None, submitted_time=None, title=None, updated_time=None, vocal_description=None, url=None):  # noqa: E501
        """Audio - a model defined in Swagger"""  # noqa: E501

        self._added_date = None
        self._affiliate_url = None
        self._album = None
        self._artists = None
        self._assets = None
        self._bpm = None
        self._contributor = None
        self._deleted_time = None
        self._description = None
        self._duration = None
        self._genres = None
        self._id = None
        self._instruments = None
        self._is_adult = None
        self._is_instrumental = None
        self._isrc = None
        self._keywords = None
        self._language = None
        self._lyrics = None
        self._media_type = None
        self._model_releases = None
        self._moods = None
        self._published_time = None
        self._recording_version = None
        self._releases = None
        self._similar_artists = None
        self._submitted_time = None
        self._title = None
        self._updated_time = None
        self._vocal_description = None
        self._url = None
        self.discriminator = None

        if added_date is not None:
            self.added_date = added_date
        if affiliate_url is not None:
            self.affiliate_url = affiliate_url
        if album is not None:
            self.album = album
        if artists is not None:
            self.artists = artists
        if assets is not None:
            self.assets = assets
        if bpm is not None:
            self.bpm = bpm
        self.contributor = contributor
        if deleted_time is not None:
            self.deleted_time = deleted_time
        if description is not None:
            self.description = description
        if duration is not None:
            self.duration = duration
        if genres is not None:
            self.genres = genres
        self.id = id
        if instruments is not None:
            self.instruments = instruments
        if is_adult is not None:
            self.is_adult = is_adult
        if is_instrumental is not None:
            self.is_instrumental = is_instrumental
        if isrc is not None:
            self.isrc = isrc
        if keywords is not None:
            self.keywords = keywords
        if language is not None:
            self.language = language
        if lyrics is not None:
            self.lyrics = lyrics
        self.media_type = media_type
        if model_releases is not None:
            self.model_releases = model_releases
        if moods is not None:
            self.moods = moods
        if published_time is not None:
            self.published_time = published_time
        if recording_version is not None:
            self.recording_version = recording_version
        if releases is not None:
            self.releases = releases
        if similar_artists is not None:
            self.similar_artists = similar_artists
        if submitted_time is not None:
            self.submitted_time = submitted_time
        if title is not None:
            self.title = title
        if updated_time is not None:
            self.updated_time = updated_time
        if vocal_description is not None:
            self.vocal_description = vocal_description
        if url is not None:
            self.url = url

    @property
    def added_date(self):
        """Gets the added_date of this Audio.  # noqa: E501

        Date this track was added to the Shutterstock library, in the format: YYYY-MM-DD  # noqa: E501

        :return: The added_date of this Audio.  # noqa: E501
        :rtype: date
        """
        return self._added_date

    @added_date.setter
    def added_date(self, added_date):
        """Sets the added_date of this Audio.

        Date this track was added to the Shutterstock library, in the format: YYYY-MM-DD  # noqa: E501

        :param added_date: The added_date of this Audio.  # noqa: E501
        :type: date
        """

        self._added_date = added_date

    @property
    def affiliate_url(self):
        """Gets the affiliate_url of this Audio.  # noqa: E501

        Affiliate referral link; appears only for registered affiliate partners  # noqa: E501

        :return: The affiliate_url of this Audio.  # noqa: E501
        :rtype: str
        """
        return self._affiliate_url

    @affiliate_url.setter
    def affiliate_url(self, affiliate_url):
        """Sets the affiliate_url of this Audio.

        Affiliate referral link; appears only for registered affiliate partners  # noqa: E501

        :param affiliate_url: The affiliate_url of this Audio.  # noqa: E501
        :type: str
        """

        self._affiliate_url = affiliate_url

    @property
    def album(self):
        """Gets the album of this Audio.  # noqa: E501


        :return: The album of this Audio.  # noqa: E501
        :rtype: Album
        """
        return self._album

    @album.setter
    def album(self, album):
        """Sets the album of this Audio.


        :param album: The album of this Audio.  # noqa: E501
        :type: Album
        """

        self._album = album

    @property
    def artists(self):
        """Gets the artists of this Audio.  # noqa: E501

        List of artists  # noqa: E501

        :return: The artists of this Audio.  # noqa: E501
        :rtype: list[Artist]
        """
        return self._artists

    @artists.setter
    def artists(self, artists):
        """Sets the artists of this Audio.

        List of artists  # noqa: E501

        :param artists: The artists of this Audio.  # noqa: E501
        :type: list[Artist]
        """

        self._artists = artists

    @property
    def assets(self):
        """Gets the assets of this Audio.  # noqa: E501


        :return: The assets of this Audio.  # noqa: E501
        :rtype: AudioAssets
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this Audio.


        :param assets: The assets of this Audio.  # noqa: E501
        :type: AudioAssets
        """

        self._assets = assets

    @property
    def bpm(self):
        """Gets the bpm of this Audio.  # noqa: E501

        BPM (beats per minute) of this track  # noqa: E501

        :return: The bpm of this Audio.  # noqa: E501
        :rtype: int
        """
        return self._bpm

    @bpm.setter
    def bpm(self, bpm):
        """Sets the bpm of this Audio.

        BPM (beats per minute) of this track  # noqa: E501

        :param bpm: The bpm of this Audio.  # noqa: E501
        :type: int
        """

        self._bpm = bpm

    @property
    def contributor(self):
        """Gets the contributor of this Audio.  # noqa: E501


        :return: The contributor of this Audio.  # noqa: E501
        :rtype: Contributor
        """
        return self._contributor

    @contributor.setter
    def contributor(self, contributor):
        """Sets the contributor of this Audio.


        :param contributor: The contributor of this Audio.  # noqa: E501
        :type: Contributor
        """
        if contributor is None:
            raise ValueError("Invalid value for `contributor`, must not be `None`")  # noqa: E501

        self._contributor = contributor

    @property
    def deleted_time(self):
        """Gets the deleted_time of this Audio.  # noqa: E501


        :return: The deleted_time of this Audio.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_time

    @deleted_time.setter
    def deleted_time(self, deleted_time):
        """Sets the deleted_time of this Audio.


        :param deleted_time: The deleted_time of this Audio.  # noqa: E501
        :type: datetime
        """

        self._deleted_time = deleted_time

    @property
    def description(self):
        """Gets the description of this Audio.  # noqa: E501

        Description of this track  # noqa: E501

        :return: The description of this Audio.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Audio.

        Description of this track  # noqa: E501

        :param description: The description of this Audio.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def duration(self):
        """Gets the duration of this Audio.  # noqa: E501

        Duration of this track in seconds  # noqa: E501

        :return: The duration of this Audio.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Audio.

        Duration of this track in seconds  # noqa: E501

        :param duration: The duration of this Audio.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def genres(self):
        """Gets the genres of this Audio.  # noqa: E501

        List of all genres for this track  # noqa: E501

        :return: The genres of this Audio.  # noqa: E501
        :rtype: list[str]
        """
        return self._genres

    @genres.setter
    def genres(self, genres):
        """Sets the genres of this Audio.

        List of all genres for this track  # noqa: E501

        :param genres: The genres of this Audio.  # noqa: E501
        :type: list[str]
        """

        self._genres = genres

    @property
    def id(self):
        """Gets the id of this Audio.  # noqa: E501

        Shutterstock ID of this track  # noqa: E501

        :return: The id of this Audio.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Audio.

        Shutterstock ID of this track  # noqa: E501

        :param id: The id of this Audio.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def instruments(self):
        """Gets the instruments of this Audio.  # noqa: E501

        List of all instruments that appear in this track  # noqa: E501

        :return: The instruments of this Audio.  # noqa: E501
        :rtype: list[str]
        """
        return self._instruments

    @instruments.setter
    def instruments(self, instruments):
        """Sets the instruments of this Audio.

        List of all instruments that appear in this track  # noqa: E501

        :param instruments: The instruments of this Audio.  # noqa: E501
        :type: list[str]
        """

        self._instruments = instruments

    @property
    def is_adult(self):
        """Gets the is_adult of this Audio.  # noqa: E501

        Whether or not this track contains adult content  # noqa: E501

        :return: The is_adult of this Audio.  # noqa: E501
        :rtype: bool
        """
        return self._is_adult

    @is_adult.setter
    def is_adult(self, is_adult):
        """Sets the is_adult of this Audio.

        Whether or not this track contains adult content  # noqa: E501

        :param is_adult: The is_adult of this Audio.  # noqa: E501
        :type: bool
        """

        self._is_adult = is_adult

    @property
    def is_instrumental(self):
        """Gets the is_instrumental of this Audio.  # noqa: E501

        Whether or not this track is purely instrumental (lacking lyrics)  # noqa: E501

        :return: The is_instrumental of this Audio.  # noqa: E501
        :rtype: bool
        """
        return self._is_instrumental

    @is_instrumental.setter
    def is_instrumental(self, is_instrumental):
        """Sets the is_instrumental of this Audio.

        Whether or not this track is purely instrumental (lacking lyrics)  # noqa: E501

        :param is_instrumental: The is_instrumental of this Audio.  # noqa: E501
        :type: bool
        """

        self._is_instrumental = is_instrumental

    @property
    def isrc(self):
        """Gets the isrc of this Audio.  # noqa: E501

          # noqa: E501

        :return: The isrc of this Audio.  # noqa: E501
        :rtype: str
        """
        return self._isrc

    @isrc.setter
    def isrc(self, isrc):
        """Sets the isrc of this Audio.

          # noqa: E501

        :param isrc: The isrc of this Audio.  # noqa: E501
        :type: str
        """

        self._isrc = isrc

    @property
    def keywords(self):
        """Gets the keywords of this Audio.  # noqa: E501

        List of all keywords for this track  # noqa: E501

        :return: The keywords of this Audio.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this Audio.

        List of all keywords for this track  # noqa: E501

        :param keywords: The keywords of this Audio.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def language(self):
        """Gets the language of this Audio.  # noqa: E501

        Language of this track's lyrics  # noqa: E501

        :return: The language of this Audio.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Audio.

        Language of this track's lyrics  # noqa: E501

        :param language: The language of this Audio.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def lyrics(self):
        """Gets the lyrics of this Audio.  # noqa: E501

        Lyrics of this track  # noqa: E501

        :return: The lyrics of this Audio.  # noqa: E501
        :rtype: str
        """
        return self._lyrics

    @lyrics.setter
    def lyrics(self, lyrics):
        """Sets the lyrics of this Audio.

        Lyrics of this track  # noqa: E501

        :param lyrics: The lyrics of this Audio.  # noqa: E501
        :type: str
        """

        self._lyrics = lyrics

    @property
    def media_type(self):
        """Gets the media_type of this Audio.  # noqa: E501

        Media type of this track; should always be \"audio\"  # noqa: E501

        :return: The media_type of this Audio.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this Audio.

        Media type of this track; should always be \"audio\"  # noqa: E501

        :param media_type: The media_type of this Audio.  # noqa: E501
        :type: str
        """
        if media_type is None:
            raise ValueError("Invalid value for `media_type`, must not be `None`")  # noqa: E501

        self._media_type = media_type

    @property
    def model_releases(self):
        """Gets the model_releases of this Audio.  # noqa: E501

        List of all model releases for this track  # noqa: E501

        :return: The model_releases of this Audio.  # noqa: E501
        :rtype: list[ModelRelease]
        """
        return self._model_releases

    @model_releases.setter
    def model_releases(self, model_releases):
        """Sets the model_releases of this Audio.

        List of all model releases for this track  # noqa: E501

        :param model_releases: The model_releases of this Audio.  # noqa: E501
        :type: list[ModelRelease]
        """

        self._model_releases = model_releases

    @property
    def moods(self):
        """Gets the moods of this Audio.  # noqa: E501

        List of all moods of this track  # noqa: E501

        :return: The moods of this Audio.  # noqa: E501
        :rtype: list[str]
        """
        return self._moods

    @moods.setter
    def moods(self, moods):
        """Sets the moods of this Audio.

        List of all moods of this track  # noqa: E501

        :param moods: The moods of this Audio.  # noqa: E501
        :type: list[str]
        """

        self._moods = moods

    @property
    def published_time(self):
        """Gets the published_time of this Audio.  # noqa: E501

        Time this track was published, in the format YYYY-MM-DDThh:mm:ssZ  # noqa: E501

        :return: The published_time of this Audio.  # noqa: E501
        :rtype: datetime
        """
        return self._published_time

    @published_time.setter
    def published_time(self, published_time):
        """Sets the published_time of this Audio.

        Time this track was published, in the format YYYY-MM-DDThh:mm:ssZ  # noqa: E501

        :param published_time: The published_time of this Audio.  # noqa: E501
        :type: datetime
        """

        self._published_time = published_time

    @property
    def recording_version(self):
        """Gets the recording_version of this Audio.  # noqa: E501

        Recording version of this track  # noqa: E501

        :return: The recording_version of this Audio.  # noqa: E501
        :rtype: str
        """
        return self._recording_version

    @recording_version.setter
    def recording_version(self, recording_version):
        """Sets the recording_version of this Audio.

        Recording version of this track  # noqa: E501

        :param recording_version: The recording_version of this Audio.  # noqa: E501
        :type: str
        """

        self._recording_version = recording_version

    @property
    def releases(self):
        """Gets the releases of this Audio.  # noqa: E501

        List of all releases of this track  # noqa: E501

        :return: The releases of this Audio.  # noqa: E501
        :rtype: list[str]
        """
        return self._releases

    @releases.setter
    def releases(self, releases):
        """Sets the releases of this Audio.

        List of all releases of this track  # noqa: E501

        :param releases: The releases of this Audio.  # noqa: E501
        :type: list[str]
        """

        self._releases = releases

    @property
    def similar_artists(self):
        """Gets the similar_artists of this Audio.  # noqa: E501

        List of all similar artists of this track  # noqa: E501

        :return: The similar_artists of this Audio.  # noqa: E501
        :rtype: list[Artist]
        """
        return self._similar_artists

    @similar_artists.setter
    def similar_artists(self, similar_artists):
        """Sets the similar_artists of this Audio.

        List of all similar artists of this track  # noqa: E501

        :param similar_artists: The similar_artists of this Audio.  # noqa: E501
        :type: list[Artist]
        """

        self._similar_artists = similar_artists

    @property
    def submitted_time(self):
        """Gets the submitted_time of this Audio.  # noqa: E501

        Time this track was submitted, in the format YYYY-MM-DDThh:mm:ssZ  # noqa: E501

        :return: The submitted_time of this Audio.  # noqa: E501
        :rtype: datetime
        """
        return self._submitted_time

    @submitted_time.setter
    def submitted_time(self, submitted_time):
        """Sets the submitted_time of this Audio.

        Time this track was submitted, in the format YYYY-MM-DDThh:mm:ssZ  # noqa: E501

        :param submitted_time: The submitted_time of this Audio.  # noqa: E501
        :type: datetime
        """

        self._submitted_time = submitted_time

    @property
    def title(self):
        """Gets the title of this Audio.  # noqa: E501

        Title of this track  # noqa: E501

        :return: The title of this Audio.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Audio.

        Title of this track  # noqa: E501

        :param title: The title of this Audio.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def updated_time(self):
        """Gets the updated_time of this Audio.  # noqa: E501

        Time this track was last updated, in the format YYYY-MM-DDThh:mm:ssZ  # noqa: E501

        :return: The updated_time of this Audio.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this Audio.

        Time this track was last updated, in the format YYYY-MM-DDThh:mm:ssZ  # noqa: E501

        :param updated_time: The updated_time of this Audio.  # noqa: E501
        :type: datetime
        """

        self._updated_time = updated_time

    @property
    def vocal_description(self):
        """Gets the vocal_description of this Audio.  # noqa: E501

        Vocal description of this track  # noqa: E501

        :return: The vocal_description of this Audio.  # noqa: E501
        :rtype: str
        """
        return self._vocal_description

    @vocal_description.setter
    def vocal_description(self, vocal_description):
        """Sets the vocal_description of this Audio.

        Vocal description of this track  # noqa: E501

        :param vocal_description: The vocal_description of this Audio.  # noqa: E501
        :type: str
        """

        self._vocal_description = vocal_description

    @property
    def url(self):
        """Gets the url of this Audio.  # noqa: E501

        Link to track information page; included only for certain accounts  # noqa: E501

        :return: The url of this Audio.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Audio.

        Link to track information page; included only for certain accounts  # noqa: E501

        :param url: The url of this Audio.  # noqa: E501
        :type: str
        """

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Audio, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Audio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
