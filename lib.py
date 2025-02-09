from __future__ import print_function
import time
import GeorisqueApi
from GeorisqueApi.rest import ApiException
from pprint import pprint
import json

def GetRapportRisquesJSON(code_insee):
    api_instance = GeorisqueApi.RapportPDFEtJSONApi()
    # Résultats du rapport des risques près de chez moi
    api_response = api_instance.generate_rapport_risque_json(code_insee=code_insee)
    return api_response

def GetCatastropheNaturelles(code_insee,rayon,latlon):
    api_instance = GeorisqueApi.CATNATApi()
    api_response = api_instance.recherche_cat_nat(code_insee= code_insee)
    return api_response

def GetDICRIM(code_insee):
    api_instance = GeorisqueApi.DICRIMApi()
    api_response = api_instance.recherche_risques6(code_insee=code_insee)
    return api_response

def ListeRisques(code_insee):
    api_instance = GeorisqueApi.RisquesApi()
    api_response = api_instance.recherche_risques4(code_insee=code_insee)
    return api_response

def GetInfoVille(code_insee):
    InfoVille = dict()
    InfoVille["RapportRisqueJson"] = GetRapportRisquesJSON(code_insee).to_dict()
    InfoVille["DICRIM"] = GetDICRIM(code_insee).to_dict()
    InfoVille["ListeRisques"] = ListeRisques(code_insee).to_dict()
    InfoVille["CatastropheNaturelles"] = GetCatastropheNaturelles(code_insee, 10, "46.603354,1.888334").to_dict()
    return InfoVille
