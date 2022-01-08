# coding: utf-8

"""
    self-managed-osdu

    Rest API Documentation for Self Managed OSDU  # noqa: E501

    OpenAPI spec version: 0.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from OsduClient.configuration import Configuration


class SearchCursorQueryResponse(object):
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
        'cursor': 'str',
        'results': 'list[dict(str, object)]',
        'total_count': 'int'
    }

    attribute_map = {
        'cursor': 'cursor',
        'results': 'results',
        'total_count': 'totalCount'
    }

    def __init__(self, cursor=None, results=None, total_count=None, _configuration=None):  # noqa: E501
        """SearchCursorQueryResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cursor = None
        self._results = None
        self._total_count = None
        self.discriminator = None

        if cursor is not None:
            self.cursor = cursor
        if results is not None:
            self.results = results
        if total_count is not None:
            self.total_count = total_count

    @property
    def cursor(self):
        """Gets the cursor of this SearchCursorQueryResponse.  # noqa: E501


        :return: The cursor of this SearchCursorQueryResponse.  # noqa: E501
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this SearchCursorQueryResponse.


        :param cursor: The cursor of this SearchCursorQueryResponse.  # noqa: E501
        :type: str
        """

        self._cursor = cursor

    @property
    def results(self):
        """Gets the results of this SearchCursorQueryResponse.  # noqa: E501


        :return: The results of this SearchCursorQueryResponse.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this SearchCursorQueryResponse.


        :param results: The results of this SearchCursorQueryResponse.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._results = results

    @property
    def total_count(self):
        """Gets the total_count of this SearchCursorQueryResponse.  # noqa: E501


        :return: The total_count of this SearchCursorQueryResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this SearchCursorQueryResponse.


        :param total_count: The total_count of this SearchCursorQueryResponse.  # noqa: E501
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
        if issubclass(SearchCursorQueryResponse, dict):
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
        if not isinstance(other, SearchCursorQueryResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchCursorQueryResponse):
            return True

        return self.to_dict() != other.to_dict()
