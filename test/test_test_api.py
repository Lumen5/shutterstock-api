# coding: utf-8

"""
    Shutterstock API Reference

    The Shutterstock API provides access to Shutterstock's library of media, as well as information about customers' accounts and the contributors that provide the media.  # noqa: E501

    OpenAPI spec version: 1.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import shutterstock_api
from shutterstock_api.api.test_api import TestApi  # noqa: E501
from shutterstock_api.rest import ApiException


class TestTestApi(unittest.TestCase):
    """TestApi unit test stubs"""

    def setUp(self):
        self.api = shutterstock_api.api.test_api.TestApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_echo(self):
        """Test case for echo

        Echo text  # noqa: E501
        """
        pass

    def test_validate(self):
        """Test case for validate

        Validate input  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
