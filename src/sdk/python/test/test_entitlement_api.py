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
from OsduClient.api.entitlement_api import EntitlementApi  # noqa: E501
from OsduClient.rest import ApiException


class TestEntitlementApi(unittest.TestCase):
    """EntitlementApi unit test stubs"""

    def setUp(self):
        self.api = OsduClient.api.entitlement_api.EntitlementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_member_using_post(self):
        """Test case for add_member_using_post

        Add Member to Group  # noqa: E501
        """
        pass

    def test_create_group_using_post(self):
        """Test case for create_group_using_post

        Create a Group  # noqa: E501
        """
        pass

    def test_delete_group_using_delete(self):
        """Test case for delete_group_using_delete

        Delete a Group  # noqa: E501
        """
        pass

    def test_delete_member_using_delete(self):
        """Test case for delete_member_using_delete

        Delete a User  # noqa: E501
        """
        pass

    def test_delete_member_using_delete1(self):
        """Test case for delete_member_using_delete1

        Remove Member from Group  # noqa: E501
        """
        pass

    def test_list_group_members_using_get(self):
        """Test case for list_group_members_using_get

        List Group Members  # noqa: E501
        """
        pass

    def test_list_groups_on_behalf_of_using_get(self):
        """Test case for list_groups_on_behalf_of_using_get

        List Assigned Groups for User  # noqa: E501
        """
        pass

    def test_list_groups_using_get(self):
        """Test case for list_groups_using_get

        List Assigned Groups  # noqa: E501
        """
        pass

    def test_update_group_using_patch(self):
        """Test case for update_group_using_patch

        Updates Items in Group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()