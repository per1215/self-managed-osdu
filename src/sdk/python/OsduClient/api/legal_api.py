# coding: utf-8

"""
    self-managed-osdu

    Rest API Documentation for Self Managed OSDU  # noqa: E501

    OpenAPI spec version: 0.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from OsduClient.api_client import ApiClient


class LegalApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_legal_tag(self, osdu_account_id, **kwargs):  # noqa: E501
        """Creates the LegalTag for the given 'name'.  # noqa: E501

        This allows for the creation of your LegalTag. There can only be 1 LegalTag per 'name'. A LegalTag must be created before you can start ingesting data for that name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_legal_tag(osdu_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str osdu_account_id: Users account e.g. OSDU (required)
        :param LegalTagDto body:
        :param str osdu_on_behalf_of: User's email or auth token
        :return: LegalTagDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_legal_tag_with_http_info(osdu_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_legal_tag_with_http_info(osdu_account_id, **kwargs)  # noqa: E501
            return data

    def create_legal_tag_with_http_info(self, osdu_account_id, **kwargs):  # noqa: E501
        """Creates the LegalTag for the given 'name'.  # noqa: E501

        This allows for the creation of your LegalTag. There can only be 1 LegalTag per 'name'. A LegalTag must be created before you can start ingesting data for that name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_legal_tag_with_http_info(osdu_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str osdu_account_id: Users account e.g. OSDU (required)
        :param LegalTagDto body:
        :param str osdu_on_behalf_of: User's email or auth token
        :return: LegalTagDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['osdu_account_id', 'body', 'osdu_on_behalf_of']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_legal_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'osdu_account_id' is set
        if self.api_client.client_side_validation and ('osdu_account_id' not in params or
                                                       params['osdu_account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `osdu_account_id` when calling `create_legal_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'osdu_account_id' in params:
            header_params['OSDU-Account-Id'] = params['osdu_account_id']  # noqa: E501
        if 'osdu_on_behalf_of' in params:
            header_params['OSDU-On-Behalf-Of'] = params['osdu_on_behalf_of']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/legal/v1/legaltags', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LegalTagDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_legal_tag(self, data_partition_id, name, **kwargs):  # noqa: E501
        """Delete Legal Tag  # noqa: E501

        This allows for the deletion of your LegalTag using the 'name' associated with it.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_legal_tag(data_partition_id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Partition Id (required)
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_legal_tag_with_http_info(data_partition_id, name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_legal_tag_with_http_info(data_partition_id, name, **kwargs)  # noqa: E501
            return data

    def delete_legal_tag_with_http_info(self, data_partition_id, name, **kwargs):  # noqa: E501
        """Delete Legal Tag  # noqa: E501

        This allows for the deletion of your LegalTag using the 'name' associated with it.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_legal_tag_with_http_info(data_partition_id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Partition Id (required)
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_partition_id', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_legal_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_partition_id' is set
        if self.api_client.client_side_validation and ('data_partition_id' not in params or
                                                       params['data_partition_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data_partition_id` when calling `delete_legal_tag`")  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in params or
                                                       params['name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `name` when calling `delete_legal_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'data_partition_id' in params:
            header_params['data-partition-id'] = params['data_partition_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/legal/v1/legaltags/{name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_legal_tag(self, data_partition_id, name, **kwargs):  # noqa: E501
        """Gets a LegalTag for the given 'name'.  # noqa: E501

        This allows for the retrieval of your LegalTag using the 'name' associated with it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_legal_tag(data_partition_id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Partition Id (required)
        :param str name: (required)
        :return: LegalTagDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_legal_tag_with_http_info(data_partition_id, name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_legal_tag_with_http_info(data_partition_id, name, **kwargs)  # noqa: E501
            return data

    def get_legal_tag_with_http_info(self, data_partition_id, name, **kwargs):  # noqa: E501
        """Gets a LegalTag for the given 'name'.  # noqa: E501

        This allows for the retrieval of your LegalTag using the 'name' associated with it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_legal_tag_with_http_info(data_partition_id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Partition Id (required)
        :param str name: (required)
        :return: LegalTagDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_partition_id', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_legal_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_partition_id' is set
        if self.api_client.client_side_validation and ('data_partition_id' not in params or
                                                       params['data_partition_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data_partition_id` when calling `get_legal_tag`")  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in params or
                                                       params['name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `name` when calling `get_legal_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'data_partition_id' in params:
            header_params['data-partition-id'] = params['data_partition_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/legal/v1/legaltags/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LegalTagDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_legal_tag_properties(self, data_partition_id, **kwargs):  # noqa: E501
        """Gets LegalTag property values.  # noqa: E501

        This allows for the retrieval of allowed values for LegalTag properties.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_legal_tag_properties(data_partition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Partition Id (required)
        :return: LegalTagPropertyValues
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_legal_tag_properties_with_http_info(data_partition_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_legal_tag_properties_with_http_info(data_partition_id, **kwargs)  # noqa: E501
            return data

    def get_legal_tag_properties_with_http_info(self, data_partition_id, **kwargs):  # noqa: E501
        """Gets LegalTag property values.  # noqa: E501

        This allows for the retrieval of allowed values for LegalTag properties.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_legal_tag_properties_with_http_info(data_partition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Partition Id (required)
        :return: LegalTagPropertyValues
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_partition_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_legal_tag_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_partition_id' is set
        if self.api_client.client_side_validation and ('data_partition_id' not in params or
                                                       params['data_partition_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data_partition_id` when calling `get_legal_tag_properties`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'data_partition_id' in params:
            header_params['data-partition-id'] = params['data_partition_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/legal/v1/legaltags:properties', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LegalTagPropertyValues',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_legal_tags(self, osdu_account_id, **kwargs):  # noqa: E501
        """Retrieves the LegalTags for the given names.  # noqa: E501

        This allows for the retrieval of your LegalTags using the 'name' associated with it. A maximum of 25 can be retrieved at once.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_legal_tags(osdu_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str osdu_account_id: Users account e.g. OSDU (required)
        :param LegalTagRequest body:
        :param str osdu_on_behalf_of: User's email or auth token
        :return: LegalTagDtos
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_legal_tags_with_http_info(osdu_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_legal_tags_with_http_info(osdu_account_id, **kwargs)  # noqa: E501
            return data

    def get_legal_tags_with_http_info(self, osdu_account_id, **kwargs):  # noqa: E501
        """Retrieves the LegalTags for the given names.  # noqa: E501

        This allows for the retrieval of your LegalTags using the 'name' associated with it. A maximum of 25 can be retrieved at once.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_legal_tags_with_http_info(osdu_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str osdu_account_id: Users account e.g. OSDU (required)
        :param LegalTagRequest body:
        :param str osdu_on_behalf_of: User's email or auth token
        :return: LegalTagDtos
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['osdu_account_id', 'body', 'osdu_on_behalf_of']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_legal_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'osdu_account_id' is set
        if self.api_client.client_side_validation and ('osdu_account_id' not in params or
                                                       params['osdu_account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `osdu_account_id` when calling `get_legal_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'osdu_account_id' in params:
            header_params['OSDU-Account-Id'] = params['osdu_account_id']  # noqa: E501
        if 'osdu_on_behalf_of' in params:
            header_params['OSDU-On-Behalf-Of'] = params['osdu_on_behalf_of']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/legal/v1/legaltags:batchRetrieve', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LegalTagDtos',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_legal_tags(self, osdu_account_id, **kwargs):  # noqa: E501
        """Gets all LegalTags.  # noqa: E501

        This allows for the retrieval of all LegalTags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_legal_tags(osdu_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str osdu_account_id: Users account e.g. OSDU (required)
        :param bool valid: If true returns only valid LegalTags, if false returns only invalid LegalTags.  Default value is true.
        :param str osdu_on_behalf_of: User's email or auth token
        :return: LegalTagDtos
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_legal_tags_with_http_info(osdu_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_legal_tags_with_http_info(osdu_account_id, **kwargs)  # noqa: E501
            return data

    def list_legal_tags_with_http_info(self, osdu_account_id, **kwargs):  # noqa: E501
        """Gets all LegalTags.  # noqa: E501

        This allows for the retrieval of all LegalTags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_legal_tags_with_http_info(osdu_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str osdu_account_id: Users account e.g. OSDU (required)
        :param bool valid: If true returns only valid LegalTags, if false returns only invalid LegalTags.  Default value is true.
        :param str osdu_on_behalf_of: User's email or auth token
        :return: LegalTagDtos
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['osdu_account_id', 'valid', 'osdu_on_behalf_of']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_legal_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'osdu_account_id' is set
        if self.api_client.client_side_validation and ('osdu_account_id' not in params or
                                                       params['osdu_account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `osdu_account_id` when calling `list_legal_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'valid' in params:
            query_params.append(('valid', params['valid']))  # noqa: E501

        header_params = {}
        if 'osdu_account_id' in params:
            header_params['OSDU-Account-Id'] = params['osdu_account_id']  # noqa: E501
        if 'osdu_on_behalf_of' in params:
            header_params['OSDU-On-Behalf-Of'] = params['osdu_on_behalf_of']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/legal/v1/legaltags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LegalTagDtos',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_legal_tag(self, osdu_account_id, **kwargs):  # noqa: E501
        """Updates the LegalTag for the given 'name'.  # noqa: E501

        This allows to update certain properties of your LegalTag using the 'name' associated with it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_legal_tag(osdu_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str osdu_account_id: Users account e.g. OSDU (required)
        :param LegalTagUpdateDto body:
        :param str osdu_on_behalf_of: User's email or auth token
        :return: LegalTagDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_legal_tag_with_http_info(osdu_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_legal_tag_with_http_info(osdu_account_id, **kwargs)  # noqa: E501
            return data

    def update_legal_tag_with_http_info(self, osdu_account_id, **kwargs):  # noqa: E501
        """Updates the LegalTag for the given 'name'.  # noqa: E501

        This allows to update certain properties of your LegalTag using the 'name' associated with it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_legal_tag_with_http_info(osdu_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str osdu_account_id: Users account e.g. OSDU (required)
        :param LegalTagUpdateDto body:
        :param str osdu_on_behalf_of: User's email or auth token
        :return: LegalTagDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['osdu_account_id', 'body', 'osdu_on_behalf_of']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_legal_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'osdu_account_id' is set
        if self.api_client.client_side_validation and ('osdu_account_id' not in params or
                                                       params['osdu_account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `osdu_account_id` when calling `update_legal_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'osdu_account_id' in params:
            header_params['OSDU-Account-Id'] = params['osdu_account_id']  # noqa: E501
        if 'osdu_on_behalf_of' in params:
            header_params['OSDU-On-Behalf-Of'] = params['osdu_on_behalf_of']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/legal/v1/legaltags', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LegalTagDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def validate_legal_tags(self, osdu_account_id, **kwargs):  # noqa: E501
        """Retrieves the invalid LegalTag names with reasons for the given names.  # noqa: E501

        This allows for the retrieval of the reason why your LegalTag is not valid. A maximum of 25 can be retrieved at once.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_legal_tags(osdu_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str osdu_account_id: Users account e.g. OSDU (required)
        :param LegalTagRequest body:
        :param str osdu_on_behalf_of: User's email or auth token
        :return: LegalTagInvalidResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.validate_legal_tags_with_http_info(osdu_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.validate_legal_tags_with_http_info(osdu_account_id, **kwargs)  # noqa: E501
            return data

    def validate_legal_tags_with_http_info(self, osdu_account_id, **kwargs):  # noqa: E501
        """Retrieves the invalid LegalTag names with reasons for the given names.  # noqa: E501

        This allows for the retrieval of the reason why your LegalTag is not valid. A maximum of 25 can be retrieved at once.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_legal_tags_with_http_info(osdu_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str osdu_account_id: Users account e.g. OSDU (required)
        :param LegalTagRequest body:
        :param str osdu_on_behalf_of: User's email or auth token
        :return: LegalTagInvalidResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['osdu_account_id', 'body', 'osdu_on_behalf_of']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate_legal_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'osdu_account_id' is set
        if self.api_client.client_side_validation and ('osdu_account_id' not in params or
                                                       params['osdu_account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `osdu_account_id` when calling `validate_legal_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'osdu_account_id' in params:
            header_params['OSDU-Account-Id'] = params['osdu_account_id']  # noqa: E501
        if 'osdu_on_behalf_of' in params:
            header_params['OSDU-On-Behalf-Of'] = params['osdu_on_behalf_of']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/legal/v1/legaltags:validate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LegalTagInvalidResponseList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
