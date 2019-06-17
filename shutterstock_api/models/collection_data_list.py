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

from shutterstock_api.models.collection import Collection  # noqa: F401,E501
from shutterstock_api.models.error import Error  # noqa: F401,E501


class CollectionDataList(object):
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
        'data': 'list[Collection]',
        'errors': 'list[Error]',
        'message': 'str',
        'page': 'int',
        'per_page': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'data': 'data',
        'errors': 'errors',
        'message': 'message',
        'page': 'page',
        'per_page': 'per_page',
        'total_count': 'total_count'
    }

    def __init__(self, data=None, errors=None, message=None, page=None, per_page=None, total_count=None):  # noqa: E501
        """CollectionDataList - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._errors = None
        self._message = None
        self._page = None
        self._per_page = None
        self._total_count = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if errors is not None:
            self.errors = errors
        if message is not None:
            self.message = message
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page
        if total_count is not None:
            self.total_count = total_count

    @property
    def data(self):
        """Gets the data of this CollectionDataList.  # noqa: E501

        Collections  # noqa: E501

        :return: The data of this CollectionDataList.  # noqa: E501
        :rtype: list[Collection]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CollectionDataList.

        Collections  # noqa: E501

        :param data: The data of this CollectionDataList.  # noqa: E501
        :type: list[Collection]
        """

        self._data = data

    @property
    def errors(self):
        """Gets the errors of this CollectionDataList.  # noqa: E501

        Error list; appears only if there was an error  # noqa: E501

        :return: The errors of this CollectionDataList.  # noqa: E501
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this CollectionDataList.

        Error list; appears only if there was an error  # noqa: E501

        :param errors: The errors of this CollectionDataList.  # noqa: E501
        :type: list[Error]
        """

        self._errors = errors

    @property
    def message(self):
        """Gets the message of this CollectionDataList.  # noqa: E501

        Server-generated message, if any  # noqa: E501

        :return: The message of this CollectionDataList.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CollectionDataList.

        Server-generated message, if any  # noqa: E501

        :param message: The message of this CollectionDataList.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def page(self):
        """Gets the page of this CollectionDataList.  # noqa: E501

        The current page of results  # noqa: E501

        :return: The page of this CollectionDataList.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this CollectionDataList.

        The current page of results  # noqa: E501

        :param page: The page of this CollectionDataList.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def per_page(self):
        """Gets the per_page of this CollectionDataList.  # noqa: E501

        The number of results per page  # noqa: E501

        :return: The per_page of this CollectionDataList.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this CollectionDataList.

        The number of results per page  # noqa: E501

        :param per_page: The per_page of this CollectionDataList.  # noqa: E501
        :type: int
        """

        self._per_page = per_page

    @property
    def total_count(self):
        """Gets the total_count of this CollectionDataList.  # noqa: E501

        The total number of results across all pages  # noqa: E501

        :return: The total_count of this CollectionDataList.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this CollectionDataList.

        The total number of results across all pages  # noqa: E501

        :param total_count: The total_count of this CollectionDataList.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if issubclass(CollectionDataList, dict):
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
        if not isinstance(other, CollectionDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
