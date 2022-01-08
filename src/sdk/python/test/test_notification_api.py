# coding: utf-8

"""
    self-managed-osdu

    Rest API Documentation for Self Managed OSDU  # noqa: E501

    OpenAPI spec version: 0.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import OsduClient
from OsduClient.api.notification_api import NotificationApi  # noqa: E501
from OsduClient.rest import ApiException


class TestNotificationApi(unittest.TestCase):
    """NotificationApi unit test stubs"""

    def setUp(self):
        self.api = OsduClient.api.notification_api.NotificationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_record_changed_using_post(self):
        """Test case for record_changed_using_post

        Notifies subscribers that records have changed  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
