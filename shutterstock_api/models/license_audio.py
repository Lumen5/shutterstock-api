# coding: utf-8

"""
    Shutterstock API Reference

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.  # noqa: E501

    OpenAPI spec version: 1.0.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LicenseAudio(object):
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
        'license': 'str',
        'search_id': 'str'
    }

    attribute_map = {
        'audio_id': 'audio_id',
        'license': 'license',
        'search_id': 'search_id'
    }

    def __init__(self, audio_id=None, license=None, search_id=None):  # noqa: E501
        """LicenseAudio - a model defined in Swagger"""  # noqa: E501

        self._audio_id = None
        self._license = None
        self._search_id = None
        self.discriminator = None

        self.audio_id = audio_id
        if license is not None:
            self.license = license
        if search_id is not None:
            self.search_id = search_id

    @property
    def audio_id(self):
        """Gets the audio_id of this LicenseAudio.  # noqa: E501

        ID of the track being licensed  # noqa: E501

        :return: The audio_id of this LicenseAudio.  # noqa: E501
        :rtype: str
        """
        return self._audio_id

    @audio_id.setter
    def audio_id(self, audio_id):
        """Sets the audio_id of this LicenseAudio.

        ID of the track being licensed  # noqa: E501

        :param audio_id: The audio_id of this LicenseAudio.  # noqa: E501
        :type: str
        """
        if audio_id is None:
            raise ValueError("Invalid value for `audio_id`, must not be `None`")  # noqa: E501

        self._audio_id = audio_id

    @property
    def license(self):
        """Gets the license of this LicenseAudio.  # noqa: E501

        Type of license  # noqa: E501

        :return: The license of this LicenseAudio.  # noqa: E501
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this LicenseAudio.

        Type of license  # noqa: E501

        :param license: The license of this LicenseAudio.  # noqa: E501
        :type: str
        """
        allowed_values = ["audio_standard", "audio_enhanced", "audio_platform", "premier_music_basic", "premier_music_extended", "premier_music_pro", "premier_music_comp"]  # noqa: E501
        if license not in allowed_values:
            raise ValueError(
                "Invalid value for `license` ({0}), must be one of {1}"  # noqa: E501
                .format(license, allowed_values)
            )

        self._license = license

    @property
    def search_id(self):
        """Gets the search_id of this LicenseAudio.  # noqa: E501

        ID of the search that led to this licensing event  # noqa: E501

        :return: The search_id of this LicenseAudio.  # noqa: E501
        :rtype: str
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id):
        """Sets the search_id of this LicenseAudio.

        ID of the search that led to this licensing event  # noqa: E501

        :param search_id: The search_id of this LicenseAudio.  # noqa: E501
        :type: str
        """

        self._search_id = search_id

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
        if issubclass(LicenseAudio, dict):
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
        if not isinstance(other, LicenseAudio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
