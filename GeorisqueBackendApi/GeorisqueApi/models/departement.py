# coding: utf-8

"""
    Services API Géorisques

    Description de l'API de Géorisques  # noqa: E501

    OpenAPI spec version: 1.9.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Departement(object):
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
        'code': 'str',
        'nom': 'str'
    }

    attribute_map = {
        'code': 'code',
        'nom': 'nom'
    }

    def __init__(self, code=None, nom=None):  # noqa: E501
        """Departement - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._nom = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if nom is not None:
            self.nom = nom

    @property
    def code(self):
        """Gets the code of this Departement.  # noqa: E501


        :return: The code of this Departement.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Departement.


        :param code: The code of this Departement.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def nom(self):
        """Gets the nom of this Departement.  # noqa: E501


        :return: The nom of this Departement.  # noqa: E501
        :rtype: str
        """
        return self._nom

    @nom.setter
    def nom(self, nom):
        """Sets the nom of this Departement.


        :param nom: The nom of this Departement.  # noqa: E501
        :type: str
        """

        self._nom = nom

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
        if issubclass(Departement, dict):
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
        if not isinstance(other, Departement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
