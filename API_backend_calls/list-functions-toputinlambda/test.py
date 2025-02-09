from __future__ import print_function
import time
import GeorisqueApi
from GeorisqueApi.rest import ApiException
from pprint import pprint
import streamlit as st

#
# pip install git+https://github.com/vorpax/python-client-generated--1- (Pour installer l'API de Georisques, si besoin)

# L'objectif : lister les calls api necessaires pour la 1ère étape de la réponse.


def GetRapportRisquesJSON(code_insee):
    api_instance = GeorisqueApi.RapportPDFEtJSONApi()
    # Résultats du rapport des risques près de chez moi
    api_response = api_instance.generate_rapport_risque_json(code_insee=code_insee)
    return api_response

def GetRapportRisquesPDF(code_insee):
    api_instance = GeorisqueApi.RapportPDFEtJSONApi()
    # Résultats du rapport des risques près de chez moi
    api_response = api_instance.generate_rapport_risque(code_insee=code_insee)
    return api_response

def GetCatastropheNaturelles(code_insee,rayon,latlon):
    api_instance = GeorisqueApi.CATNATApi()
    api_response = api_instance.recherche_cat_nat(rayon=rayon, latlon=latlon, code_insee= code_insee)
    




print()
RapportRisqueJson= GetRapportRisquesJSON("86194")
#RapportRisquePdf= GetRapportRisquesPDF("86194")





print("done")
