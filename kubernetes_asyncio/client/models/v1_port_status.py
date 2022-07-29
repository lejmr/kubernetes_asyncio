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


class V1PortStatus(object):
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
        'error': 'str',
        'port': 'int',
        'protocol': 'str'
    }

    attribute_map = {
        'error': 'error',
        'port': 'port',
        'protocol': 'protocol'
    }

    def __init__(self, error=None, port=None, protocol=None, local_vars_configuration=None):  # noqa: E501
        """V1PortStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._error = None
        self._port = None
        self._protocol = None
        self.discriminator = None

        if error is not None:
            self.error = error
        self.port = port
        self.protocol = protocol

    @property
    def error(self):
        """Gets the error of this V1PortStatus.  # noqa: E501

        Error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use   CamelCase names - cloud provider specific error values must have names that comply with the   format foo.example.com/CamelCase.  # noqa: E501

        :return: The error of this V1PortStatus.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this V1PortStatus.

        Error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use   CamelCase names - cloud provider specific error values must have names that comply with the   format foo.example.com/CamelCase.  # noqa: E501

        :param error: The error of this V1PortStatus.  # noqa: E501
        :type error: str
        """

        self._error = error

    @property
    def port(self):
        """Gets the port of this V1PortStatus.  # noqa: E501

        Port is the port number of the service port of which status is recorded here  # noqa: E501

        :return: The port of this V1PortStatus.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this V1PortStatus.

        Port is the port number of the service port of which status is recorded here  # noqa: E501

        :param port: The port of this V1PortStatus.  # noqa: E501
        :type port: int
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this V1PortStatus.  # noqa: E501

        Protocol is the protocol of the service port of which status is recorded here The supported values are: \"TCP\", \"UDP\", \"SCTP\"    # noqa: E501

        :return: The protocol of this V1PortStatus.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this V1PortStatus.

        Protocol is the protocol of the service port of which status is recorded here The supported values are: \"TCP\", \"UDP\", \"SCTP\"    # noqa: E501

        :param protocol: The protocol of this V1PortStatus.  # noqa: E501
        :type protocol: str
        """
        if self.local_vars_configuration.client_side_validation and protocol is None:  # noqa: E501
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

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
        if not isinstance(other, V1PortStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1PortStatus):
            return True

        return self.to_dict() != other.to_dict()
