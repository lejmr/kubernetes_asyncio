# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.24.2
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from kubernetes_asyncio.client.configuration import Configuration


class EventsV1EventSeries(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'count': 'int',
        'last_observed_time': 'datetime'
    }

    attribute_map = {
        'count': 'count',
        'last_observed_time': 'lastObservedTime'
    }

    def __init__(self, count=None, last_observed_time=None, local_vars_configuration=None):  # noqa: E501
        """EventsV1EventSeries - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._last_observed_time = None
        self.discriminator = None

        self.count = count
        self.last_observed_time = last_observed_time

    @property
    def count(self):
        """Gets the count of this EventsV1EventSeries.  # noqa: E501

        count is the number of occurrences in this series up to the last heartbeat time.  # noqa: E501

        :return: The count of this EventsV1EventSeries.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this EventsV1EventSeries.

        count is the number of occurrences in this series up to the last heartbeat time.  # noqa: E501

        :param count: The count of this EventsV1EventSeries.  # noqa: E501
        :type count: int
        """
        if self.local_vars_configuration.client_side_validation and count is None:  # noqa: E501
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def last_observed_time(self):
        """Gets the last_observed_time of this EventsV1EventSeries.  # noqa: E501

        lastObservedTime is the time when last Event from the series was seen before last heartbeat.  # noqa: E501

        :return: The last_observed_time of this EventsV1EventSeries.  # noqa: E501
        :rtype: datetime
        """
        return self._last_observed_time

    @last_observed_time.setter
    def last_observed_time(self, last_observed_time):
        """Sets the last_observed_time of this EventsV1EventSeries.

        lastObservedTime is the time when last Event from the series was seen before last heartbeat.  # noqa: E501

        :param last_observed_time: The last_observed_time of this EventsV1EventSeries.  # noqa: E501
        :type last_observed_time: datetime
        """
        if self.local_vars_configuration.client_side_validation and last_observed_time is None:  # noqa: E501
            raise ValueError("Invalid value for `last_observed_time`, must not be `None`")  # noqa: E501

        self._last_observed_time = last_observed_time

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventsV1EventSeries):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventsV1EventSeries):
            return True

        return self.to_dict() != other.to_dict()
