# coding: utf-8

"""
    Shutterstock API Reference

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.  # noqa: E501

    OpenAPI spec version: 1.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from shutterstock_api.models.url import Url  # noqa: F401,E501


class LicenseAudioResult(object):
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
        'audio_id': 'str',
        'download': 'Url',
        'error': 'str'
    }

    attribute_map = {
        'audio_id': 'audio_id',
        'download': 'download',
        'error': 'error'
    }

    def __init__(self, audio_id=None, download=None, error=None):  # noqa: E501
        """LicenseAudioResult - a model defined in Swagger"""  # noqa: E501

        self._audio_id = None
        self._download = None
        self._error = None
        self.discriminator = None

        self.audio_id = audio_id
        if download is not None:
            self.download = download
        if error is not None:
            self.error = error

    @property
    def audio_id(self):
        """Gets the audio_id of this LicenseAudioResult.  # noqa: E501

        ID of the track that was licensed  # noqa: E501

        :return: The audio_id of this LicenseAudioResult.  # noqa: E501
        :rtype: str
        """
        return self._audio_id

    @audio_id.setter
    def audio_id(self, audio_id):
        """Sets the audio_id of this LicenseAudioResult.

        ID of the track that was licensed  # noqa: E501

        :param audio_id: The audio_id of this LicenseAudioResult.  # noqa: E501
        :type: str
        """
        if audio_id is None:
            raise ValueError("Invalid value for `audio_id`, must not be `None`")  # noqa: E501

        self._audio_id = audio_id

    @property
    def download(self):
        """Gets the download of this LicenseAudioResult.  # noqa: E501


        :return: The download of this LicenseAudioResult.  # noqa: E501
        :rtype: Url
        """
        return self._download

    @download.setter
    def download(self, download):
        """Sets the download of this LicenseAudioResult.


        :param download: The download of this LicenseAudioResult.  # noqa: E501
        :type: Url
        """

        self._download = download

    @property
    def error(self):
        """Gets the error of this LicenseAudioResult.  # noqa: E501

        Error information if applicable  # noqa: E501

        :return: The error of this LicenseAudioResult.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this LicenseAudioResult.

        Error information if applicable  # noqa: E501

        :param error: The error of this LicenseAudioResult.  # noqa: E501
        :type: str
        """

        self._error = error

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
        if issubclass(LicenseAudioResult, dict):
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
        if not isinstance(other, LicenseAudioResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
