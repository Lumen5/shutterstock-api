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
from shutterstock_api.api.audio_api import AudioApi  # noqa: E501
from shutterstock_api.rest import ApiException


class TestAudioApi(unittest.TestCase):
    """AudioApi unit test stubs"""

    def setUp(self):
        self.api = shutterstock_api.api.audio_api.AudioApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_soundbox_items(self):
        """Test case for add_soundbox_items

        Add audio tracks to collections  # noqa: E501
        """
        pass

    def test_create_soundbox(self):
        """Test case for create_soundbox

        Create audio collections  # noqa: E501
        """
        pass

    def test_delete_soundbox(self):
        """Test case for delete_soundbox

        Delete audio collections  # noqa: E501
        """
        pass

    def test_delete_soundbox_items(self):
        """Test case for delete_soundbox_items

        Remove audio tracks from collections  # noqa: E501
        """
        pass

    def test_download_tracks(self):
        """Test case for download_tracks

        Download audio tracks  # noqa: E501
        """
        pass

    def test_get_audio_license_list(self):
        """Test case for get_audio_license_list

        List audio licenses  # noqa: E501
        """
        pass

    def test_get_soundbox(self):
        """Test case for get_soundbox

        Get the details of audio collections  # noqa: E501
        """
        pass

    def test_get_soundbox_items(self):
        """Test case for get_soundbox_items

        Get the contents of audio collections  # noqa: E501
        """
        pass

    def test_get_soundbox_list(self):
        """Test case for get_soundbox_list

        List audio collections  # noqa: E501
        """
        pass

    def test_get_track(self):
        """Test case for get_track

        Get details about audio tracks  # noqa: E501
        """
        pass

    def test_get_track_list(self):
        """Test case for get_track_list

        List audio tracks  # noqa: E501
        """
        pass

    def test_license_track(self):
        """Test case for license_track

        License audio tracks  # noqa: E501
        """
        pass

    def test_rename_soundbox(self):
        """Test case for rename_soundbox

        Rename audio collections  # noqa: E501
        """
        pass

    def test_search_audio(self):
        """Test case for search_audio

        Search for tracks  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
