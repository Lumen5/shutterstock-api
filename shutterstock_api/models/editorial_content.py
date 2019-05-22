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

from shutterstock_api.models.editorial_assets import EditorialAssets  # noqa: F401,E501
from shutterstock_api.models.editorial_category import EditorialCategory  # noqa: F401,E501


class EditorialContent(object):
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
        'aspect': 'float',
        'assets': 'EditorialAssets',
        'byline': 'str',
        'caption': 'str',
        'categories': 'list[EditorialCategory]',
        'date_taken': 'date',
        'description': 'str',
        'id': 'str',
        'keywords': 'list[str]',
        'title': 'str'
    }

    attribute_map = {
        'aspect': 'aspect',
        'assets': 'assets',
        'byline': 'byline',
        'caption': 'caption',
        'categories': 'categories',
        'date_taken': 'date_taken',
        'description': 'description',
        'id': 'id',
        'keywords': 'keywords',
        'title': 'title'
    }

    def __init__(self, aspect=None, assets=None, byline=None, caption=None, categories=None, date_taken=None, description=None, id=None, keywords=None, title=None):  # noqa: E501
        """EditorialContent - a model defined in Swagger"""  # noqa: E501

        self._aspect = None
        self._assets = None
        self._byline = None
        self._caption = None
        self._categories = None
        self._date_taken = None
        self._description = None
        self._id = None
        self._keywords = None
        self._title = None
        self.discriminator = None

        if aspect is not None:
            self.aspect = aspect
        if assets is not None:
            self.assets = assets
        if byline is not None:
            self.byline = byline
        if caption is not None:
            self.caption = caption
        if categories is not None:
            self.categories = categories
        if date_taken is not None:
            self.date_taken = date_taken
        if description is not None:
            self.description = description
        self.id = id
        if keywords is not None:
            self.keywords = keywords
        if title is not None:
            self.title = title

    @property
    def aspect(self):
        """Gets the aspect of this EditorialContent.  # noqa: E501


        :return: The aspect of this EditorialContent.  # noqa: E501
        :rtype: float
        """
        return self._aspect

    @aspect.setter
    def aspect(self, aspect):
        """Sets the aspect of this EditorialContent.


        :param aspect: The aspect of this EditorialContent.  # noqa: E501
        :type: float
        """

        self._aspect = aspect

    @property
    def assets(self):
        """Gets the assets of this EditorialContent.  # noqa: E501


        :return: The assets of this EditorialContent.  # noqa: E501
        :rtype: EditorialAssets
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this EditorialContent.


        :param assets: The assets of this EditorialContent.  # noqa: E501
        :type: EditorialAssets
        """

        self._assets = assets

    @property
    def byline(self):
        """Gets the byline of this EditorialContent.  # noqa: E501


        :return: The byline of this EditorialContent.  # noqa: E501
        :rtype: str
        """
        return self._byline

    @byline.setter
    def byline(self, byline):
        """Sets the byline of this EditorialContent.


        :param byline: The byline of this EditorialContent.  # noqa: E501
        :type: str
        """

        self._byline = byline

    @property
    def caption(self):
        """Gets the caption of this EditorialContent.  # noqa: E501


        :return: The caption of this EditorialContent.  # noqa: E501
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """Sets the caption of this EditorialContent.


        :param caption: The caption of this EditorialContent.  # noqa: E501
        :type: str
        """

        self._caption = caption

    @property
    def categories(self):
        """Gets the categories of this EditorialContent.  # noqa: E501

        List of categories  # noqa: E501

        :return: The categories of this EditorialContent.  # noqa: E501
        :rtype: list[EditorialCategory]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this EditorialContent.

        List of categories  # noqa: E501

        :param categories: The categories of this EditorialContent.  # noqa: E501
        :type: list[EditorialCategory]
        """

        self._categories = categories

    @property
    def date_taken(self):
        """Gets the date_taken of this EditorialContent.  # noqa: E501


        :return: The date_taken of this EditorialContent.  # noqa: E501
        :rtype: date
        """
        return self._date_taken

    @date_taken.setter
    def date_taken(self, date_taken):
        """Sets the date_taken of this EditorialContent.


        :param date_taken: The date_taken of this EditorialContent.  # noqa: E501
        :type: date
        """

        self._date_taken = date_taken

    @property
    def description(self):
        """Gets the description of this EditorialContent.  # noqa: E501


        :return: The description of this EditorialContent.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EditorialContent.


        :param description: The description of this EditorialContent.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this EditorialContent.  # noqa: E501


        :return: The id of this EditorialContent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EditorialContent.


        :param id: The id of this EditorialContent.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def keywords(self):
        """Gets the keywords of this EditorialContent.  # noqa: E501


        :return: The keywords of this EditorialContent.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this EditorialContent.


        :param keywords: The keywords of this EditorialContent.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def title(self):
        """Gets the title of this EditorialContent.  # noqa: E501


        :return: The title of this EditorialContent.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this EditorialContent.


        :param title: The title of this EditorialContent.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(EditorialContent, dict):
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
        if not isinstance(other, EditorialContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
