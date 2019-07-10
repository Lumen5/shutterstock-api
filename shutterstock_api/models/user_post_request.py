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


class UserPostRequest(object):
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
        'email': 'str',
        'password': 'str',
        'username': 'str'
    }

    attribute_map = {
        'email': 'email',
        'password': 'password',
        'username': 'username'
    }

    def __init__(self, email=None, password=None, username=None):  # noqa: E501
        """UserPostRequest - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._password = None
        self._username = None
        self.discriminator = None

        self.email = email
        self.password = password
        if username is not None:
            self.username = username

    @property
    def email(self):
        """Gets the email of this UserPostRequest.  # noqa: E501

        Email address for the new user  # noqa: E501

        :return: The email of this UserPostRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserPostRequest.

        Email address for the new user  # noqa: E501

        :param email: The email of this UserPostRequest.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def password(self):
        """Gets the password of this UserPostRequest.  # noqa: E501

        Password for the new user  # noqa: E501

        :return: The password of this UserPostRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserPostRequest.

        Password for the new user  # noqa: E501

        :param password: The password of this UserPostRequest.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def username(self):
        """Gets the username of this UserPostRequest.  # noqa: E501

        User name for the new user  # noqa: E501

        :return: The username of this UserPostRequest.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserPostRequest.

        User name for the new user  # noqa: E501

        :param username: The username of this UserPostRequest.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(UserPostRequest, dict):
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
        if not isinstance(other, UserPostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
