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

class FamilleRisques(object):
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
        'code_risque': 'str',
        'libelle_risque': 'str',
        'classes_alea': 'list[Risque]'
    }

    attribute_map = {
        'code_risque': 'code_risque',
        'libelle_risque': 'libelle_risque',
        'classes_alea': 'classes_alea'
    }

    def __init__(self, code_risque=None, libelle_risque=None, classes_alea=None):  # noqa: E501
        """FamilleRisques - a model defined in Swagger"""  # noqa: E501
        self._code_risque = None
        self._libelle_risque = None
        self._classes_alea = None
        self.discriminator = None
        if code_risque is not None:
            self.code_risque = code_risque
        if libelle_risque is not None:
            self.libelle_risque = libelle_risque
        if classes_alea is not None:
            self.classes_alea = classes_alea

    @property
    def code_risque(self):
        """Gets the code_risque of this FamilleRisques.  # noqa: E501

        Code d'un risque PPR  # noqa: E501

        :return: The code_risque of this FamilleRisques.  # noqa: E501
        :rtype: str
        """
        return self._code_risque

    @code_risque.setter
    def code_risque(self, code_risque):
        """Sets the code_risque of this FamilleRisques.

        Code d'un risque PPR  # noqa: E501

        :param code_risque: The code_risque of this FamilleRisques.  # noqa: E501
        :type: str
        """

        self._code_risque = code_risque

    @property
    def libelle_risque(self):
        """Gets the libelle_risque of this FamilleRisques.  # noqa: E501

        Libellé d'un risque PPR  # noqa: E501

        :return: The libelle_risque of this FamilleRisques.  # noqa: E501
        :rtype: str
        """
        return self._libelle_risque

    @libelle_risque.setter
    def libelle_risque(self, libelle_risque):
        """Sets the libelle_risque of this FamilleRisques.

        Libellé d'un risque PPR  # noqa: E501

        :param libelle_risque: The libelle_risque of this FamilleRisques.  # noqa: E501
        :type: str
        """

        self._libelle_risque = libelle_risque

    @property
    def classes_alea(self):
        """Gets the classes_alea of this FamilleRisques.  # noqa: E501

        Classe d'un risque d'alea  # noqa: E501

        :return: The classes_alea of this FamilleRisques.  # noqa: E501
        :rtype: list[Risque]
        """
        return self._classes_alea

    @classes_alea.setter
    def classes_alea(self, classes_alea):
        """Sets the classes_alea of this FamilleRisques.

        Classe d'un risque d'alea  # noqa: E501

        :param classes_alea: The classes_alea of this FamilleRisques.  # noqa: E501
        :type: list[Risque]
        """

        self._classes_alea = classes_alea

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
        if issubclass(FamilleRisques, dict):
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
        if not isinstance(other, FamilleRisques):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
