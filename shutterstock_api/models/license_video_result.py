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

from shutterstock_api.models.price import Price  # noqa: F401,E501
from shutterstock_api.models.url import Url  # noqa: F401,E501


class LicenseVideoResult(object):
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
        'allotment_charge': 'int',
        'download': 'Url',
        'error': 'str',
        'price': 'Price',
        'video_id': 'str'
    }

    attribute_map = {
        'allotment_charge': 'allotment_charge',
        'download': 'download',
        'error': 'error',
        'price': 'price',
        'video_id': 'video_id'
    }

    def __init__(self, allotment_charge=None, download=None, error=None, price=None, video_id=None):  # noqa: E501
        """LicenseVideoResult - a model defined in Swagger"""  # noqa: E501

        self._allotment_charge = None
        self._download = None
        self._error = None
        self._price = None
        self._video_id = None
        self.discriminator = None

        if allotment_charge is not None:
            self.allotment_charge = allotment_charge
        if download is not None:
            self.download = download
        if error is not None:
            self.error = error
        if price is not None:
            self.price = price
        self.video_id = video_id

    @property
    def allotment_charge(self):
        """Gets the allotment_charge of this LicenseVideoResult.  # noqa: E501

        Number of allotments that this licensing event used  # noqa: E501

        :return: The allotment_charge of this LicenseVideoResult.  # noqa: E501
        :rtype: int
        """
        return self._allotment_charge

    @allotment_charge.setter
    def allotment_charge(self, allotment_charge):
        """Sets the allotment_charge of this LicenseVideoResult.

        Number of allotments that this licensing event used  # noqa: E501

        :param allotment_charge: The allotment_charge of this LicenseVideoResult.  # noqa: E501
        :type: int
        """

        self._allotment_charge = allotment_charge

    @property
    def download(self):
        """Gets the download of this LicenseVideoResult.  # noqa: E501


        :return: The download of this LicenseVideoResult.  # noqa: E501
        :rtype: Url
        """
        return self._download

    @download.setter
    def download(self, download):
        """Sets the download of this LicenseVideoResult.


        :param download: The download of this LicenseVideoResult.  # noqa: E501
        :type: Url
        """

        self._download = download

    @property
    def error(self):
        """Gets the error of this LicenseVideoResult.  # noqa: E501

        Potential error that occurred during licensing  # noqa: E501

        :return: The error of this LicenseVideoResult.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this LicenseVideoResult.

        Potential error that occurred during licensing  # noqa: E501

        :param error: The error of this LicenseVideoResult.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def price(self):
        """Gets the price of this LicenseVideoResult.  # noqa: E501

        Wholesale price information; only for rev-share partners only  # noqa: E501

        :return: The price of this LicenseVideoResult.  # noqa: E501
        :rtype: Price
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this LicenseVideoResult.

        Wholesale price information; only for rev-share partners only  # noqa: E501

        :param price: The price of this LicenseVideoResult.  # noqa: E501
        :type: Price
        """

        self._price = price

    @property
    def video_id(self):
        """Gets the video_id of this LicenseVideoResult.  # noqa: E501

        ID of the video that was licensed  # noqa: E501

        :return: The video_id of this LicenseVideoResult.  # noqa: E501
        :rtype: str
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """Sets the video_id of this LicenseVideoResult.

        ID of the video that was licensed  # noqa: E501

        :param video_id: The video_id of this LicenseVideoResult.  # noqa: E501
        :type: str
        """
        if video_id is None:
            raise ValueError("Invalid value for `video_id`, must not be `None`")  # noqa: E501

        self._video_id = video_id

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
        if issubclass(LicenseVideoResult, dict):
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
        if not isinstance(other, LicenseVideoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
