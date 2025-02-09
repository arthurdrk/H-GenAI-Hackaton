# coding: utf-8

"""
    Services API Géorisques

    Description de l'API de Géorisques  # noqa: E501

    OpenAPI spec version: 1.9.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import GeorisqueApi
from GeorisqueApi.api.mvt_api import MVTApi  # noqa: E501
from GeorisqueApi.rest import ApiException


class TestMVTApi(unittest.TestCase):
    """MVTApi unit test stubs"""

    def setUp(self):
        self.api = MVTApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_recherche_risques1(self):
        """Test case for recherche_risques1

        Cette interface est conçue pour diffuser les données sur le mouvement de terrain.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
