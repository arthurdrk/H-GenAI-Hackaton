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

class ZonageSismique(object):
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
        'code_insee': 'str',
        'libelle_commune': 'str',
        'code_zone': 'str',
        'zone_sismicite': 'str'
    }

    attribute_map = {
        'code_insee': 'code_insee',
        'libelle_commune': 'libelle_commune',
        'code_zone': 'code_zone',
        'zone_sismicite': 'zone_sismicite'
    }

    def __init__(self, code_insee=None, libelle_commune=None, code_zone=None, zone_sismicite=None):  # noqa: E501
        """ZonageSismique - a model defined in Swagger"""  # noqa: E501
        self._code_insee = None
        self._libelle_commune = None
        self._code_zone = None
        self._zone_sismicite = None
        self.discriminator = None
        if code_insee is not None:
            self.code_insee = code_insee
        if libelle_commune is not None:
            self.libelle_commune = libelle_commune
        if code_zone is not None:
            self.code_zone = code_zone
        if zone_sismicite is not None:
            self.zone_sismicite = zone_sismicite

    @property
    def code_insee(self):
        """Gets the code_insee of this ZonageSismique.  # noqa: E501

        Identifiant unique INSEE de la commune  # noqa: E501

        :return: The code_insee of this ZonageSismique.  # noqa: E501
        :rtype: str
        """
        return self._code_insee

    @code_insee.setter
    def code_insee(self, code_insee):
        """Sets the code_insee of this ZonageSismique.

        Identifiant unique INSEE de la commune  # noqa: E501

        :param code_insee: The code_insee of this ZonageSismique.  # noqa: E501
        :type: str
        """

        self._code_insee = code_insee

    @property
    def libelle_commune(self):
        """Gets the libelle_commune of this ZonageSismique.  # noqa: E501

        Libellé de la commune  # noqa: E501

        :return: The libelle_commune of this ZonageSismique.  # noqa: E501
        :rtype: str
        """
        return self._libelle_commune

    @libelle_commune.setter
    def libelle_commune(self, libelle_commune):
        """Sets the libelle_commune of this ZonageSismique.

        Libellé de la commune  # noqa: E501

        :param libelle_commune: The libelle_commune of this ZonageSismique.  # noqa: E501
        :type: str
        """

        self._libelle_commune = libelle_commune

    @property
    def code_zone(self):
        """Gets the code_zone of this ZonageSismique.  # noqa: E501

        Code du zonage sismique  # noqa: E501

        :return: The code_zone of this ZonageSismique.  # noqa: E501
        :rtype: str
        """
        return self._code_zone

    @code_zone.setter
    def code_zone(self, code_zone):
        """Sets the code_zone of this ZonageSismique.

        Code du zonage sismique  # noqa: E501

        :param code_zone: The code_zone of this ZonageSismique.  # noqa: E501
        :type: str
        """

        self._code_zone = code_zone

    @property
    def zone_sismicite(self):
        """Gets the zone_sismicite of this ZonageSismique.  # noqa: E501

        Libellé du zonage sismique  # noqa: E501

        :return: The zone_sismicite of this ZonageSismique.  # noqa: E501
        :rtype: str
        """
        return self._zone_sismicite

    @zone_sismicite.setter
    def zone_sismicite(self, zone_sismicite):
        """Sets the zone_sismicite of this ZonageSismique.

        Libellé du zonage sismique  # noqa: E501

        :param zone_sismicite: The zone_sismicite of this ZonageSismique.  # noqa: E501
        :type: str
        """

        self._zone_sismicite = zone_sismicite

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
        if issubclass(ZonageSismique, dict):
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
        if not isinstance(other, ZonageSismique):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
