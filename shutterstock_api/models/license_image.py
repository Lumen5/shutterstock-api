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

from shutterstock_api.models.cookie import Cookie  # noqa: F401,E501
from shutterstock_api.models.license_request_metadata import LicenseRequestMetadata  # noqa: F401,E501


class LicenseImage(object):
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
        'auth_cookie': 'Cookie',
        'editorial_acknowledgement': 'bool',
        'format': 'str',
        'image_id': 'str',
        'metadata': 'LicenseRequestMetadata',
        'price': 'float',
        'search_id': 'str',
        'show_modal': 'bool',
        'size': 'str',
        'subscription_id': 'str',
        'verification_code': 'str'
    }

    attribute_map = {
        'auth_cookie': 'auth_cookie',
        'editorial_acknowledgement': 'editorial_acknowledgement',
        'format': 'format',
        'image_id': 'image_id',
        'metadata': 'metadata',
        'price': 'price',
        'search_id': 'search_id',
        'show_modal': 'show_modal',
        'size': 'size',
        'subscription_id': 'subscription_id',
        'verification_code': 'verification_code'
    }

    def __init__(self, auth_cookie=None, editorial_acknowledgement=None, format=None, image_id=None, metadata=None, price=None, search_id=None, show_modal=None, size=None, subscription_id=None, verification_code=None):  # noqa: E501
        """LicenseImage - a model defined in Swagger"""  # noqa: E501

        self._auth_cookie = None
        self._editorial_acknowledgement = None
        self._format = None
        self._image_id = None
        self._metadata = None
        self._price = None
        self._search_id = None
        self._show_modal = None
        self._size = None
        self._subscription_id = None
        self._verification_code = None
        self.discriminator = None

        if auth_cookie is not None:
            self.auth_cookie = auth_cookie
        if editorial_acknowledgement is not None:
            self.editorial_acknowledgement = editorial_acknowledgement
        if format is not None:
            self.format = format
        self.image_id = image_id
        if metadata is not None:
            self.metadata = metadata
        if price is not None:
            self.price = price
        if search_id is not None:
            self.search_id = search_id
        if show_modal is not None:
            self.show_modal = show_modal
        if size is not None:
            self.size = size
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if verification_code is not None:
            self.verification_code = verification_code

    @property
    def auth_cookie(self):
        """Gets the auth_cookie of this LicenseImage.  # noqa: E501

        Cookie object  # noqa: E501

        :return: The auth_cookie of this LicenseImage.  # noqa: E501
        :rtype: Cookie
        """
        return self._auth_cookie

    @auth_cookie.setter
    def auth_cookie(self, auth_cookie):
        """Sets the auth_cookie of this LicenseImage.

        Cookie object  # noqa: E501

        :param auth_cookie: The auth_cookie of this LicenseImage.  # noqa: E501
        :type: Cookie
        """

        self._auth_cookie = auth_cookie

    @property
    def editorial_acknowledgement(self):
        """Gets the editorial_acknowledgement of this LicenseImage.  # noqa: E501

        Set to true to acknowledge the editorial agreement  # noqa: E501

        :return: The editorial_acknowledgement of this LicenseImage.  # noqa: E501
        :rtype: bool
        """
        return self._editorial_acknowledgement

    @editorial_acknowledgement.setter
    def editorial_acknowledgement(self, editorial_acknowledgement):
        """Sets the editorial_acknowledgement of this LicenseImage.

        Set to true to acknowledge the editorial agreement  # noqa: E501

        :param editorial_acknowledgement: The editorial_acknowledgement of this LicenseImage.  # noqa: E501
        :type: bool
        """

        self._editorial_acknowledgement = editorial_acknowledgement

    @property
    def format(self):
        """Gets the format of this LicenseImage.  # noqa: E501

        Image format to download  # noqa: E501

        :return: The format of this LicenseImage.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this LicenseImage.

        Image format to download  # noqa: E501

        :param format: The format of this LicenseImage.  # noqa: E501
        :type: str
        """
        allowed_values = ["jpg", "eps"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def image_id(self):
        """Gets the image_id of this LicenseImage.  # noqa: E501

        Image ID  # noqa: E501

        :return: The image_id of this LicenseImage.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this LicenseImage.

        Image ID  # noqa: E501

        :param image_id: The image_id of this LicenseImage.  # noqa: E501
        :type: str
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def metadata(self):
        """Gets the metadata of this LicenseImage.  # noqa: E501


        :return: The metadata of this LicenseImage.  # noqa: E501
        :rtype: LicenseRequestMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this LicenseImage.


        :param metadata: The metadata of this LicenseImage.  # noqa: E501
        :type: LicenseRequestMetadata
        """

        self._metadata = metadata

    @property
    def price(self):
        """Gets the price of this LicenseImage.  # noqa: E501

        For revenue-sharing transactions, the final cost to the end customer  # noqa: E501

        :return: The price of this LicenseImage.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this LicenseImage.

        For revenue-sharing transactions, the final cost to the end customer  # noqa: E501

        :param price: The price of this LicenseImage.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def search_id(self):
        """Gets the search_id of this LicenseImage.  # noqa: E501

        ID of the search that led to this licensing transaction  # noqa: E501

        :return: The search_id of this LicenseImage.  # noqa: E501
        :rtype: str
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id):
        """Sets the search_id of this LicenseImage.

        ID of the search that led to this licensing transaction  # noqa: E501

        :param search_id: The search_id of this LicenseImage.  # noqa: E501
        :type: str
        """

        self._search_id = search_id

    @property
    def show_modal(self):
        """Gets the show_modal of this LicenseImage.  # noqa: E501

        (Deprecated)  # noqa: E501

        :return: The show_modal of this LicenseImage.  # noqa: E501
        :rtype: bool
        """
        return self._show_modal

    @show_modal.setter
    def show_modal(self, show_modal):
        """Sets the show_modal of this LicenseImage.

        (Deprecated)  # noqa: E501

        :param show_modal: The show_modal of this LicenseImage.  # noqa: E501
        :type: bool
        """

        self._show_modal = show_modal

    @property
    def size(self):
        """Gets the size of this LicenseImage.  # noqa: E501

        Image size to download  # noqa: E501

        :return: The size of this LicenseImage.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this LicenseImage.

        Image size to download  # noqa: E501

        :param size: The size of this LicenseImage.  # noqa: E501
        :type: str
        """
        allowed_values = ["small", "medium", "huge", "vector"]  # noqa: E501
        if size not in allowed_values:
            raise ValueError(
                "Invalid value for `size` ({0}), must be one of {1}"  # noqa: E501
                .format(size, allowed_values)
            )

        self._size = size

    @property
    def subscription_id(self):
        """Gets the subscription_id of this LicenseImage.  # noqa: E501

        ID of the subscription to use for the download.  # noqa: E501

        :return: The subscription_id of this LicenseImage.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this LicenseImage.

        ID of the subscription to use for the download.  # noqa: E501

        :param subscription_id: The subscription_id of this LicenseImage.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def verification_code(self):
        """Gets the verification_code of this LicenseImage.  # noqa: E501

        (Deprecated)  # noqa: E501

        :return: The verification_code of this LicenseImage.  # noqa: E501
        :rtype: str
        """
        return self._verification_code

    @verification_code.setter
    def verification_code(self, verification_code):
        """Sets the verification_code of this LicenseImage.

        (Deprecated)  # noqa: E501

        :param verification_code: The verification_code of this LicenseImage.  # noqa: E501
        :type: str
        """

        self._verification_code = verification_code

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
        if issubclass(LicenseImage, dict):
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
        if not isinstance(other, LicenseImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
