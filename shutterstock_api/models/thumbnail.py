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


class Thumbnail(object):
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
        'height': 'int',
        'url': 'str',
        'width': 'int'
    }

    attribute_map = {
        'height': 'height',
        'url': 'url',
        'width': 'width'
    }

    def __init__(self, height=None, url=None, width=None):  # noqa: E501
        """Thumbnail - a model defined in Swagger"""  # noqa: E501

        self._height = None
        self._url = None
        self._width = None
        self.discriminator = None

        self.height = height
        self.url = url
        self.width = width

    @property
    def height(self):
        """Gets the height of this Thumbnail.  # noqa: E501

        Height in pixels of the image thumbnail  # noqa: E501

        :return: The height of this Thumbnail.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Thumbnail.

        Height in pixels of the image thumbnail  # noqa: E501

        :param height: The height of this Thumbnail.  # noqa: E501
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def url(self):
        """Gets the url of this Thumbnail.  # noqa: E501

        Direct URL to the image  # noqa: E501

        :return: The url of this Thumbnail.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Thumbnail.

        Direct URL to the image  # noqa: E501

        :param url: The url of this Thumbnail.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def width(self):
        """Gets the width of this Thumbnail.  # noqa: E501

        Width in pixels of the image thumbnail  # noqa: E501

        :return: The width of this Thumbnail.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Thumbnail.

        Width in pixels of the image thumbnail  # noqa: E501

        :param width: The width of this Thumbnail.  # noqa: E501
        :type: int
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

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
        if issubclass(Thumbnail, dict):
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
        if not isinstance(other, Thumbnail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
