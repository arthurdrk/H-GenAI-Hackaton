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


class TIMApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def recherche_risques3(self, **kwargs):  # noqa: E501
        """Lister les dossier de Transmission d'Information au Maire (TIM) recensés sur le territoire concerné  # noqa: E501

        Ce service permet de lister les dossier de Transmission d'Information au Maire (TIM) recensés sur le territoire concerné, suivant une emprise spatiale définie, à  savoir un rayon de recherche pour un point défini, une ou plusieurs communes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.recherche_risques3(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int rayon: Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à  10 000 mètres. Par défaut le rayon de recherche est fixé à  1000 mètres.
        :param str latlon: Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572
        :param str code_insee: Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee=45234,45100, le nombre maximum de code est 10. Ce type de recherche ne peut pas être combinée avec une recherche au rayon.
        :param int page: Numéro de la page
        :param int page_size: Taille des pages
        :return: PaginatedResponseTim
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.recherche_risques3_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.recherche_risques3_with_http_info(**kwargs)  # noqa: E501
            return data

    def recherche_risques3_with_http_info(self, **kwargs):  # noqa: E501
        """Lister les dossier de Transmission d'Information au Maire (TIM) recensés sur le territoire concerné  # noqa: E501

        Ce service permet de lister les dossier de Transmission d'Information au Maire (TIM) recensés sur le territoire concerné, suivant une emprise spatiale définie, à  savoir un rayon de recherche pour un point défini, une ou plusieurs communes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.recherche_risques3_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int rayon: Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à  10 000 mètres. Par défaut le rayon de recherche est fixé à  1000 mètres.
        :param str latlon: Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572
        :param str code_insee: Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee=45234,45100, le nombre maximum de code est 10. Ce type de recherche ne peut pas être combinée avec une recherche au rayon.
        :param int page: Numéro de la page
        :param int page_size: Taille des pages
        :return: PaginatedResponseTim
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rayon', 'latlon', 'code_insee', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method recherche_risques3" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'rayon' in params:
            query_params.append(('rayon', params['rayon']))  # noqa: E501
        if 'latlon' in params:
            query_params.append(('latlon', params['latlon']))  # noqa: E501
        if 'code_insee' in params:
            query_params.append(('code_insee', params['code_insee']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

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
            '/v1/gaspar/tim', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedResponseTim',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
