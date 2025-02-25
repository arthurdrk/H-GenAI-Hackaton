# coding: utf-8

# flake8: noqa
"""
    Services API Géorisques

    Description de l'API de Géorisques  # noqa: E501

    OpenAPI spec version: 1.9.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from GeorisqueApi.models.adresse_dto import AdresseDto
from GeorisqueApi.models.azi import Azi
from GeorisqueApi.models.casias_dto import CasiasDto
from GeorisqueApi.models.cat_nat import CatNat
from GeorisqueApi.models.cavites import Cavites
from GeorisqueApi.models.commune_dto import CommuneDto
from GeorisqueApi.models.commune_model import CommuneModel
from GeorisqueApi.models.coordonnees import Coordonnees
from GeorisqueApi.models.crs import Crs
from GeorisqueApi.models.departement import Departement
from GeorisqueApi.models.dicrim import Dicrim
from GeorisqueApi.models.etat_ppr import EtatPPR
from GeorisqueApi.models.ex_basol_dto import ExBasolDto
from GeorisqueApi.models.famille_risques import FamilleRisques
from GeorisqueApi.models.feature import Feature
from GeorisqueApi.models.feature_collection import FeatureCollection
from GeorisqueApi.models.geo_json_object import GeoJsonObject
from GeorisqueApi.models.geometry_collection import GeometryCollection
from GeorisqueApi.models.inspection import Inspection
from GeorisqueApi.models.installation_classee import InstallationClassee
from GeorisqueApi.models.lex_scenario import LexScenario
from GeorisqueApi.models.lex_type import LexType
from GeorisqueApi.models.line_string import LineString
from GeorisqueApi.models.lng_lat_alt import LngLatAlt
from GeorisqueApi.models.metadata_fichier import MetadataFichier
from GeorisqueApi.models.multi_line_string import MultiLineString
from GeorisqueApi.models.multi_point import MultiPoint
from GeorisqueApi.models.multi_polygon import MultiPolygon
from GeorisqueApi.models.mvt import Mvt
from GeorisqueApi.models.no_paginated_response_tri_zonage_dto import NoPaginatedResponseTriZonageDto
from GeorisqueApi.models.old_model import OldModel
from GeorisqueApi.models.one_of_casias_dto_geom import OneOfCasiasDtoGeom
from GeorisqueApi.models.one_of_ex_basol_dto_geom import OneOfExBasolDtoGeom
from GeorisqueApi.models.one_of_ppr_geom_perimetre import OneOfPPRGeomPerimetre
from GeorisqueApi.models.one_of_ppr_geom_zonage import OneOfPPRGeomZonage
from GeorisqueApi.models.one_of_sis_dto_geom import OneOfSisDtoGeom
from GeorisqueApi.models.one_of_sup_dto_geom import OneOfSupDtoGeom
from GeorisqueApi.models.ppr import PPR
from GeorisqueApi.models.paginated_response_azi import PaginatedResponseAzi
from GeorisqueApi.models.paginated_response_casias_dto import PaginatedResponseCasiasDto
from GeorisqueApi.models.paginated_response_cat_nat import PaginatedResponseCatNat
from GeorisqueApi.models.paginated_response_cavites import PaginatedResponseCavites
from GeorisqueApi.models.paginated_response_dicrim import PaginatedResponseDicrim
from GeorisqueApi.models.paginated_response_etat_ppr import PaginatedResponseEtatPPR
from GeorisqueApi.models.paginated_response_ex_basol_dto import PaginatedResponseExBasolDto
from GeorisqueApi.models.paginated_response_famille_risques import PaginatedResponseFamilleRisques
from GeorisqueApi.models.paginated_response_installation_classee import PaginatedResponseInstallationClassee
from GeorisqueApi.models.paginated_response_mvt import PaginatedResponseMvt
from GeorisqueApi.models.paginated_response_ppr import PaginatedResponsePPR
from GeorisqueApi.models.paginated_response_papi import PaginatedResponsePapi
from GeorisqueApi.models.paginated_response_radon import PaginatedResponseRadon
from GeorisqueApi.models.paginated_response_risques import PaginatedResponseRisques
from GeorisqueApi.models.paginated_response_sis_dto import PaginatedResponseSisDto
from GeorisqueApi.models.paginated_response_sup_dto import PaginatedResponseSupDto
from GeorisqueApi.models.paginated_response_tim import PaginatedResponseTim
from GeorisqueApi.models.paginated_response_tri import PaginatedResponseTri
from GeorisqueApi.models.paginated_response_zonage_sismique import PaginatedResponseZonageSismique
from GeorisqueApi.models.papi import Papi
from GeorisqueApi.models.point import Point
from GeorisqueApi.models.polygon import Polygon
from GeorisqueApi.models.radon import Radon
from GeorisqueApi.models.rapport_risques_json_dto import RapportRisquesJsonDto
from GeorisqueApi.models.region import Region
from GeorisqueApi.models.risque import Risque
from GeorisqueApi.models.risque_dto import RisqueDto
from GeorisqueApi.models.risque_gaspar import RisqueGaspar
from GeorisqueApi.models.risques import Risques
from GeorisqueApi.models.risques_naturels_dto import RisquesNaturelsDto
from GeorisqueApi.models.risques_technologiques_dto import RisquesTechnologiquesDto
from GeorisqueApi.models.rubrique_ic import RubriqueIC
from GeorisqueApi.models.sis_dto import SisDto
from GeorisqueApi.models.ssp import Ssp
from GeorisqueApi.models.sup_dto import SupDto
from GeorisqueApi.models.tim import Tim
from GeorisqueApi.models.tri import Tri
from GeorisqueApi.models.tri_zonage_dto import TriZonageDto
from GeorisqueApi.models.zonage_argile import ZonageArgile
from GeorisqueApi.models.zonage_sismique import ZonageSismique
