# coding: utf-8

"""
    Services API Géorisques

    Description de l'API de Géorisques  # noqa: E501

    OpenAPI spec version: 1.9.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from GeorisqueApi.api_client import ApiClient


class TRIZonageRglementaireApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def recherche_tri_zonage(self, latlon, **kwargs):  # noqa: E501
        """Lister les Territoires à  Risques importants d'Inondation (TRI) recensés sur l'adresse concernée  # noqa: E501

        Ce service permet de lister les Territoires à  Risques importants d'Inondation (TRI) recensés sur l'adresse concernée, suivant une latitude et une longitude.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.recherche_tri_zonage(latlon, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str latlon: Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 (required)
        :param str code: Code risque TRI - possibilité de mettre une liste entre virgules
        :return: NoPaginatedResponseTriZonageDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.recherche_tri_zonage_with_http_info(latlon, **kwargs)  # noqa: E501
        else:
            (data) = self.recherche_tri_zonage_with_http_info(latlon, **kwargs)  # noqa: E501
            return data

    def recherche_tri_zonage_with_http_info(self, latlon, **kwargs):  # noqa: E501
        """Lister les Territoires à  Risques importants d'Inondation (TRI) recensés sur l'adresse concernée  # noqa: E501

        Ce service permet de lister les Territoires à  Risques importants d'Inondation (TRI) recensés sur l'adresse concernée, suivant une latitude et une longitude.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.recherche_tri_zonage_with_http_info(latlon, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str latlon: Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 (required)
        :param str code: Code risque TRI - possibilité de mettre une liste entre virgules
        :return: NoPaginatedResponseTriZonageDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['latlon', 'code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method recherche_tri_zonage" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'latlon' is set
        if ('latlon' not in params or
                params['latlon'] is None):
            raise ValueError("Missing the required parameter `latlon` when calling `recherche_tri_zonage`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'latlon' in params:
            query_params.append(('latlon', params['latlon']))  # noqa: E501
        if 'code' in params:
            query_params.append(('code', params['code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/tri_zonage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NoPaginatedResponseTriZonageDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
