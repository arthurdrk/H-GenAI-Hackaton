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

class Papi(object):
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
        'code_national_papi': 'str',
        'libelle_papi': 'str',
        'liste_libelle_risque': 'list[RisqueGaspar]',
        'libelle_bassin_risques': 'str',
        'date_labellisation': 'date',
        'date_signature': 'date',
        'date_fin_realisation': 'date',
        'code_insee': 'str',
        'libelle_commune': 'str'
    }

    attribute_map = {
        'code_national_papi': 'code_national_papi',
        'libelle_papi': 'libelle_papi',
        'liste_libelle_risque': 'liste_libelle_risque',
        'libelle_bassin_risques': 'libelle_bassin_risques',
        'date_labellisation': 'date_labellisation',
        'date_signature': 'date_signature',
        'date_fin_realisation': 'date_fin_realisation',
        'code_insee': 'code_insee',
        'libelle_commune': 'libelle_commune'
    }

    def __init__(self, code_national_papi=None, libelle_papi=None, liste_libelle_risque=None, libelle_bassin_risques=None, date_labellisation=None, date_signature=None, date_fin_realisation=None, code_insee=None, libelle_commune=None):  # noqa: E501
        """Papi - a model defined in Swagger"""  # noqa: E501
        self._code_national_papi = None
        self._libelle_papi = None
        self._liste_libelle_risque = None
        self._libelle_bassin_risques = None
        self._date_labellisation = None
        self._date_signature = None
        self._date_fin_realisation = None
        self._code_insee = None
        self._libelle_commune = None
        self.discriminator = None
        if code_national_papi is not None:
            self.code_national_papi = code_national_papi
        if libelle_papi is not None:
            self.libelle_papi = libelle_papi
        if liste_libelle_risque is not None:
            self.liste_libelle_risque = liste_libelle_risque
        if libelle_bassin_risques is not None:
            self.libelle_bassin_risques = libelle_bassin_risques
        if date_labellisation is not None:
            self.date_labellisation = date_labellisation
        if date_signature is not None:
            self.date_signature = date_signature
        if date_fin_realisation is not None:
            self.date_fin_realisation = date_fin_realisation
        if code_insee is not None:
            self.code_insee = code_insee
        if libelle_commune is not None:
            self.libelle_commune = libelle_commune

    @property
    def code_national_papi(self):
        """Gets the code_national_papi of this Papi.  # noqa: E501

        Identifiant unique du PAPI  # noqa: E501

        :return: The code_national_papi of this Papi.  # noqa: E501
        :rtype: str
        """
        return self._code_national_papi

    @code_national_papi.setter
    def code_national_papi(self, code_national_papi):
        """Sets the code_national_papi of this Papi.

        Identifiant unique du PAPI  # noqa: E501

        :param code_national_papi: The code_national_papi of this Papi.  # noqa: E501
        :type: str
        """

        self._code_national_papi = code_national_papi

    @property
    def libelle_papi(self):
        """Gets the libelle_papi of this Papi.  # noqa: E501

        Libellé du PAPI  # noqa: E501

        :return: The libelle_papi of this Papi.  # noqa: E501
        :rtype: str
        """
        return self._libelle_papi

    @libelle_papi.setter
    def libelle_papi(self, libelle_papi):
        """Sets the libelle_papi of this Papi.

        Libellé du PAPI  # noqa: E501

        :param libelle_papi: The libelle_papi of this Papi.  # noqa: E501
        :type: str
        """

        self._libelle_papi = libelle_papi

    @property
    def liste_libelle_risque(self):
        """Gets the liste_libelle_risque of this Papi.  # noqa: E501

        Détail du risque gaspar  # noqa: E501

        :return: The liste_libelle_risque of this Papi.  # noqa: E501
        :rtype: list[RisqueGaspar]
        """
        return self._liste_libelle_risque

    @liste_libelle_risque.setter
    def liste_libelle_risque(self, liste_libelle_risque):
        """Sets the liste_libelle_risque of this Papi.

        Détail du risque gaspar  # noqa: E501

        :param liste_libelle_risque: The liste_libelle_risque of this Papi.  # noqa: E501
        :type: list[RisqueGaspar]
        """

        self._liste_libelle_risque = liste_libelle_risque

    @property
    def libelle_bassin_risques(self):
        """Gets the libelle_bassin_risques of this Papi.  # noqa: E501

        Libellé bassin de risque  # noqa: E501

        :return: The libelle_bassin_risques of this Papi.  # noqa: E501
        :rtype: str
        """
        return self._libelle_bassin_risques

    @libelle_bassin_risques.setter
    def libelle_bassin_risques(self, libelle_bassin_risques):
        """Sets the libelle_bassin_risques of this Papi.

        Libellé bassin de risque  # noqa: E501

        :param libelle_bassin_risques: The libelle_bassin_risques of this Papi.  # noqa: E501
        :type: str
        """

        self._libelle_bassin_risques = libelle_bassin_risques

    @property
    def date_labellisation(self):
        """Gets the date_labellisation of this Papi.  # noqa: E501

        Date de labellisation du PAPI  # noqa: E501

        :return: The date_labellisation of this Papi.  # noqa: E501
        :rtype: date
        """
        return self._date_labellisation

    @date_labellisation.setter
    def date_labellisation(self, date_labellisation):
        """Sets the date_labellisation of this Papi.

        Date de labellisation du PAPI  # noqa: E501

        :param date_labellisation: The date_labellisation of this Papi.  # noqa: E501
        :type: date
        """

        self._date_labellisation = date_labellisation

    @property
    def date_signature(self):
        """Gets the date_signature of this Papi.  # noqa: E501

        Date de signature du PAPI  # noqa: E501

        :return: The date_signature of this Papi.  # noqa: E501
        :rtype: date
        """
        return self._date_signature

    @date_signature.setter
    def date_signature(self, date_signature):
        """Sets the date_signature of this Papi.

        Date de signature du PAPI  # noqa: E501

        :param date_signature: The date_signature of this Papi.  # noqa: E501
        :type: date
        """

        self._date_signature = date_signature

    @property
    def date_fin_realisation(self):
        """Gets the date_fin_realisation of this Papi.  # noqa: E501

        Date de fin de réalisation du PAPI  # noqa: E501

        :return: The date_fin_realisation of this Papi.  # noqa: E501
        :rtype: date
        """
        return self._date_fin_realisation

    @date_fin_realisation.setter
    def date_fin_realisation(self, date_fin_realisation):
        """Sets the date_fin_realisation of this Papi.

        Date de fin de réalisation du PAPI  # noqa: E501

        :param date_fin_realisation: The date_fin_realisation of this Papi.  # noqa: E501
        :type: date
        """

        self._date_fin_realisation = date_fin_realisation

    @property
    def code_insee(self):
        """Gets the code_insee of this Papi.  # noqa: E501

        Identifiant unique INSEE de la commune  # noqa: E501

        :return: The code_insee of this Papi.  # noqa: E501
        :rtype: str
        """
        return self._code_insee

    @code_insee.setter
    def code_insee(self, code_insee):
        """Sets the code_insee of this Papi.

        Identifiant unique INSEE de la commune  # noqa: E501

        :param code_insee: The code_insee of this Papi.  # noqa: E501
        :type: str
        """

        self._code_insee = code_insee

    @property
    def libelle_commune(self):
        """Gets the libelle_commune of this Papi.  # noqa: E501

        Libellé de la commune  # noqa: E501

        :return: The libelle_commune of this Papi.  # noqa: E501
        :rtype: str
        """
        return self._libelle_commune

    @libelle_commune.setter
    def libelle_commune(self, libelle_commune):
        """Sets the libelle_commune of this Papi.

        Libellé de la commune  # noqa: E501

        :param libelle_commune: The libelle_commune of this Papi.  # noqa: E501
        :type: str
        """

        self._libelle_commune = libelle_commune

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
        if issubclass(Papi, dict):
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
        if not isinstance(other, Papi):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
