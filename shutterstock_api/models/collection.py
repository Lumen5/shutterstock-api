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

from shutterstock_api.models.collection_item import CollectionItem  # noqa: F401,E501


class Collection(object):
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
        'cover_item': 'CollectionItem',
        'created_time': 'datetime',
        'id': 'str',
        'items_updated_time': 'datetime',
        'name': 'str',
        'share_code': 'str',
        'share_url': 'str',
        'total_item_count': 'int',
        'updated_time': 'datetime'
    }

    attribute_map = {
        'cover_item': 'cover_item',
        'created_time': 'created_time',
        'id': 'id',
        'items_updated_time': 'items_updated_time',
        'name': 'name',
        'share_code': 'share_code',
        'share_url': 'share_url',
        'total_item_count': 'total_item_count',
        'updated_time': 'updated_time'
    }

    def __init__(self, cover_item=None, created_time=None, id=None, items_updated_time=None, name=None, share_code=None, share_url=None, total_item_count=None, updated_time=None):  # noqa: E501
        """Collection - a model defined in Swagger"""  # noqa: E501

        self._cover_item = None
        self._created_time = None
        self._id = None
        self._items_updated_time = None
        self._name = None
        self._share_code = None
        self._share_url = None
        self._total_item_count = None
        self._updated_time = None
        self.discriminator = None

        if cover_item is not None:
            self.cover_item = cover_item
        if created_time is not None:
            self.created_time = created_time
        self.id = id
        if items_updated_time is not None:
            self.items_updated_time = items_updated_time
        self.name = name
        if share_code is not None:
            self.share_code = share_code
        if share_url is not None:
            self.share_url = share_url
        self.total_item_count = total_item_count
        if updated_time is not None:
            self.updated_time = updated_time

    @property
    def cover_item(self):
        """Gets the cover_item of this Collection.  # noqa: E501


        :return: The cover_item of this Collection.  # noqa: E501
        :rtype: CollectionItem
        """
        return self._cover_item

    @cover_item.setter
    def cover_item(self, cover_item):
        """Sets the cover_item of this Collection.


        :param cover_item: The cover_item of this Collection.  # noqa: E501
        :type: CollectionItem
        """

        self._cover_item = cover_item

    @property
    def created_time(self):
        """Gets the created_time of this Collection.  # noqa: E501

        When the collection was created  # noqa: E501

        :return: The created_time of this Collection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Collection.

        When the collection was created  # noqa: E501

        :param created_time: The created_time of this Collection.  # noqa: E501
        :type: datetime
        """

        self._created_time = created_time

    @property
    def id(self):
        """Gets the id of this Collection.  # noqa: E501

        The collection ID  # noqa: E501

        :return: The id of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Collection.

        The collection ID  # noqa: E501

        :param id: The id of this Collection.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def items_updated_time(self):
        """Gets the items_updated_time of this Collection.  # noqa: E501

        The last time this collection's items were updated  # noqa: E501

        :return: The items_updated_time of this Collection.  # noqa: E501
        :rtype: datetime
        """
        return self._items_updated_time

    @items_updated_time.setter
    def items_updated_time(self, items_updated_time):
        """Sets the items_updated_time of this Collection.

        The last time this collection's items were updated  # noqa: E501

        :param items_updated_time: The items_updated_time of this Collection.  # noqa: E501
        :type: datetime
        """

        self._items_updated_time = items_updated_time

    @property
    def name(self):
        """Gets the name of this Collection.  # noqa: E501

        The name of the collection  # noqa: E501

        :return: The name of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Collection.

        The name of the collection  # noqa: E501

        :param name: The name of this Collection.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def share_code(self):
        """Gets the share_code of this Collection.  # noqa: E501

        A code that can be used to share the collection (optional)  # noqa: E501

        :return: The share_code of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._share_code

    @share_code.setter
    def share_code(self, share_code):
        """Sets the share_code of this Collection.

        A code that can be used to share the collection (optional)  # noqa: E501

        :param share_code: The share_code of this Collection.  # noqa: E501
        :type: str
        """

        self._share_code = share_code

    @property
    def share_url(self):
        """Gets the share_url of this Collection.  # noqa: E501

        The browser URL that can be used to share the collection (optional)  # noqa: E501

        :return: The share_url of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._share_url

    @share_url.setter
    def share_url(self, share_url):
        """Sets the share_url of this Collection.

        The browser URL that can be used to share the collection (optional)  # noqa: E501

        :param share_url: The share_url of this Collection.  # noqa: E501
        :type: str
        """

        self._share_url = share_url

    @property
    def total_item_count(self):
        """Gets the total_item_count of this Collection.  # noqa: E501

        The number of items in the collection  # noqa: E501

        :return: The total_item_count of this Collection.  # noqa: E501
        :rtype: int
        """
        return self._total_item_count

    @total_item_count.setter
    def total_item_count(self, total_item_count):
        """Sets the total_item_count of this Collection.

        The number of items in the collection  # noqa: E501

        :param total_item_count: The total_item_count of this Collection.  # noqa: E501
        :type: int
        """
        if total_item_count is None:
            raise ValueError("Invalid value for `total_item_count`, must not be `None`")  # noqa: E501

        self._total_item_count = total_item_count

    @property
    def updated_time(self):
        """Gets the updated_time of this Collection.  # noqa: E501

        The last time the collection was update (other than changes to the items in it)  # noqa: E501

        :return: The updated_time of this Collection.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this Collection.

        The last time the collection was update (other than changes to the items in it)  # noqa: E501

        :param updated_time: The updated_time of this Collection.  # noqa: E501
        :type: datetime
        """

        self._updated_time = updated_time

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
        if issubclass(Collection, dict):
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
        if not isinstance(other, Collection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
