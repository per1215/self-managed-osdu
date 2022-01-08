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


class DeliveryAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def returns_delivery_instructions_for_file_s_using_sr_ns(self, data_partition_id, **kwargs):  # noqa: E501
        """returns_delivery_instructions_for_file_s_using_sr_ns  # noqa: E501

        Returns delivery instructions for File(s) using SRNs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.returns_delivery_instructions_for_file_s_using_sr_ns(data_partition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Specifies the data partition to use. This should either be the partition name or crm account ID associated with the partition. (required)
        :param FileDeliveryGetFileSignedURLRequest body:
        :return: FileDeliveryGetFileSignedURLResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.returns_delivery_instructions_for_file_s_using_sr_ns_with_http_info(data_partition_id, **kwargs)  # noqa: E501
        else:
            (data) = self.returns_delivery_instructions_for_file_s_using_sr_ns_with_http_info(data_partition_id, **kwargs)  # noqa: E501
            return data

    def returns_delivery_instructions_for_file_s_using_sr_ns_with_http_info(self, data_partition_id, **kwargs):  # noqa: E501
        """returns_delivery_instructions_for_file_s_using_sr_ns  # noqa: E501

        Returns delivery instructions for File(s) using SRNs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.returns_delivery_instructions_for_file_s_using_sr_ns_with_http_info(data_partition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Specifies the data partition to use. This should either be the partition name or crm account ID associated with the partition. (required)
        :param FileDeliveryGetFileSignedURLRequest body:
        :return: FileDeliveryGetFileSignedURLResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_partition_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method returns_delivery_instructions_for_file_s_using_sr_ns" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_partition_id' is set
        if self.api_client.client_side_validation and ('data_partition_id' not in params or
                                                       params['data_partition_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data_partition_id` when calling `returns_delivery_instructions_for_file_s_using_sr_ns`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'data_partition_id' in params:
            header_params['data-partition-id'] = params['data_partition_id']  # noqa: E501

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
            '/api/file/v2/delivery/getFileSignedUrl', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FileDeliveryGetFileSignedURLResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
