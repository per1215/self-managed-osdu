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


class FileLegal(object):
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
        'legaltags': 'list[str]',
        'other_relevant_data_countries': 'list[str]',
        'status': 'str'
    }

    attribute_map = {
        'legaltags': 'legaltags',
        'other_relevant_data_countries': 'otherRelevantDataCountries',
        'status': 'status'
    }

    def __init__(self, legaltags=None, other_relevant_data_countries=None, status=None, _configuration=None):  # noqa: E501
        """FileLegal - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._legaltags = None
        self._other_relevant_data_countries = None
        self._status = None
        self.discriminator = None

        if legaltags is not None:
            self.legaltags = legaltags
        if other_relevant_data_countries is not None:
            self.other_relevant_data_countries = other_relevant_data_countries
        if status is not None:
            self.status = status

    @property
    def legaltags(self):
        """Gets the legaltags of this FileLegal.  # noqa: E501

        The list of legal tags, see compliance API.  # noqa: E501

        :return: The legaltags of this FileLegal.  # noqa: E501
        :rtype: list[str]
        """
        return self._legaltags

    @legaltags.setter
    def legaltags(self, legaltags):
        """Sets the legaltags of this FileLegal.

        The list of legal tags, see compliance API.  # noqa: E501

        :param legaltags: The legaltags of this FileLegal.  # noqa: E501
        :type: list[str]
        """

        self._legaltags = legaltags

    @property
    def other_relevant_data_countries(self):
        """Gets the other_relevant_data_countries of this FileLegal.  # noqa: E501

        The list of other relevant data countries using the ISO 2-letter codes, see compliance API.  # noqa: E501

        :return: The other_relevant_data_countries of this FileLegal.  # noqa: E501
        :rtype: list[str]
        """
        return self._other_relevant_data_countries

    @other_relevant_data_countries.setter
    def other_relevant_data_countries(self, other_relevant_data_countries):
        """Sets the other_relevant_data_countries of this FileLegal.

        The list of other relevant data countries using the ISO 2-letter codes, see compliance API.  # noqa: E501

        :param other_relevant_data_countries: The other_relevant_data_countries of this FileLegal.  # noqa: E501
        :type: list[str]
        """

        self._other_relevant_data_countries = other_relevant_data_countries

    @property
    def status(self):
        """Gets the status of this FileLegal.  # noqa: E501

        The legal status.  # noqa: E501

        :return: The status of this FileLegal.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FileLegal.

        The legal status.  # noqa: E501

        :param status: The status of this FileLegal.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(FileLegal, dict):
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
        if not isinstance(other, FileLegal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileLegal):
            return True

        return self.to_dict() != other.to_dict()
