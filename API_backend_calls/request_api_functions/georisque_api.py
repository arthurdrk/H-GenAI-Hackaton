import requests

BASE_URL = "https://georisques.gouv.fr/api"


def call_georisques_api(endpoint: str, **params):
    """
    Appelle un endpoint spécifique de l'API Géorisques avec les paramètres fournis.

    :param endpoint: Chemin de l'endpoint (ex: "/v1/zonage_sismique").
    :param params: Paramètres de requête optionnels sous forme de dictionnaire.
    :return: Résultat JSON de la requête ou message d'erreur.
    """
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Erreur {response.status_code}: {response.text}"}


# 🔹 Fonctions spécifiques pour chaque endpoint :
def get_zonage_sismique(latlon=None, code_insee=None, rayon=1000, page=1, page_size=10):
    if latlon!=None and code_insee!=None:
        return {"error": "Veuillez spécifier soit 'latlon' soit 'code_insee', pas les deux."}
    return call_georisques_api("/v1/zonage_sismique", latlon=latlon, code_insee=code_insee, rayon=rayon, page=page, page_size=page_size)


def get_tri_zonage(latlon, code=None):
    return call_georisques_api("/v1/tri_zonage", latlon=latlon, code=code)


def get_ssp(latlon=None, code_insee=None, rayon=1000, page=1, page_size=10):
    if latlon!=None and code_insee!=None:
        return {"error": "Veuillez spécifier soit 'latlon' soit 'code_insee', pas les deux."}
    return call_georisques_api("/v1/ssp", latlon=latlon, code_insee=code_insee, rayon=rayon, page=page, page_size=page_size)


def get_risques(latlon=None, code_insee=None, rayon=1000, page=1, page_size=10):
    if latlon!=None and code_insee!=None:
        return {"error": "Veuillez spécifier soit 'latlon' soit 'code_insee', pas les deux."}
    return call_georisques_api("/v1/gaspar/risques", latlon=latlon, code_insee=code_insee, rayon=rayon, page=page, page_size=page_size)


def get_radon(code_insee, page=1, page_size=10):
    return call_georisques_api("/v1/radon", code_insee=code_insee, page=page, page_size=page_size)


def get_papi(latlon=None, code_insee=None, rayon=1000, page=1, page_size=10):
    if latlon!=None and code_insee!=None:
        return {"error": "Veuillez spécifier soit 'latlon' soit 'code_insee', pas les deux."}
    return call_georisques_api("/v1/gaspar/papi", latlon=latlon, code_insee=code_insee, rayon=rayon, page=page, page_size=page_size)


def get_tim(latlon=None, code_insee=None, rayon=1000, page=1, page_size=10):
    if latlon!=None and code_insee!=None:
        return {"error": "Veuillez spécifier soit 'latlon' soit 'code_insee', pas les deux."}
    return call_georisques_api("/v1/gaspar/tim", latlon=latlon, code_insee=code_insee, rayon=rayon, page=page, page_size=page_size)


def get_catnat(latlon=None, code_insee=None, rayon=1000, page=1, page_size=10):
    if latlon!=None and code_insee!=None:
        return {"error": "Veuillez spécifier soit 'latlon' soit 'code_insee', pas les deux."}
    return call_georisques_api("/v1/gaspar/catnat", latlon=latlon, code_insee=code_insee, rayon=rayon, page=page, page_size=page_size)


def get_azi(latlon=None, code_insee=None, rayon=1000, page=1, page_size=10):
    if latlon!=None and code_insee!=None:
        return {"error": "Veuillez spécifier soit 'latlon' soit 'code_insee', pas les deux."}
    return call_georisques_api("/v1/gaspar/azi", latlon=latlon, code_insee=code_insee, rayon=rayon, page=page, page_size=page_size)


def get_rga(latlon=None):
    return call_georisques_api("/v1/rga", latlon=latlon)


def get_rapport_risque(code_insee=None, latlon=None, adresse=None):
    if latlon!=None and code_insee!=None:
        return {"error": "Veuillez spécifier soit 'latlon' soit 'code_insee', pas les deux."}
    return call_georisques_api("/v1/resultats_rapport_risque", code_insee=code_insee, latlon=latlon, adresse=adresse)


def get_rapport_pdf(code_insee=None, latlon=None, adresse=None):
    if latlon!=None and code_insee!=None:
        return {"error": "Veuillez spécifier soit 'latlon' soit 'code_insee', pas les deux."}
    return call_georisques_api("/v1/rapport_pdf", code_insee=code_insee, latlon=latlon, adresse=adresse)


def get_mvt(latlon=None, code_insee=None, rayon=1000, page=1, page_size=10):
    if latlon!=None and code_insee!=None:
        return {"error": "Veuillez spécifier soit 'latlon' soit 'code_insee', pas les deux."}
    return call_georisques_api("/v1/mvt", latlon=latlon, code_insee=code_insee, rayon=rayon, page=page, page_size=page_size)


def get_installations_classees(latlon=None, code_insee=None, rayon=1000, page=1, page_size=10):
    if latlon!=None and code_insee!=None:
        return {"error": "Veuillez spécifier soit 'latlon' soit 'code_insee', pas les deux."}
    return call_georisques_api("/v1/installations_classees", latlon=latlon, code_insee=code_insee, rayon=rayon, page=page, page_size=page_size)


def get_cavites(latlon=None, code_insee=None, rayon=1000, page=1, page_size=10):
    if latlon!=None and code_insee!=None:
        return {"error": "Veuillez spécifier soit 'latlon' soit 'code_insee', pas les deux."}
    return call_georisques_api("/v1/cavites", latlon=latlon, code_insee=code_insee, rayon=rayon, page=page, page_size=page_size)


# 🔹 Exemples d'utilisation :
if __name__ == "__main__":
    print("📍 Exemple : Recherche de zonage sismique à Paris (48.8566, 2.3522)")
    print(get_zonage_sismique(latlon="2.3522,48.8566"))

    print("\n🌊 Exemple : Recherche TRI à Marseille (5.3698, 43.2965)")
    print(get_tri_zonage(latlon="5.3698,43.2965"))

    print("\n🛑 Exemple : Recherche des risques à Lyon (4.8357, 45.7640)")
    print(get_risques(latlon="4.8357,45.7640"))


# Mettre des seuils, dans la DB, les plus grosses, qui produit le plus, (sinon moyens moindres)
# La performance : pas crucial, on veut pas une réponse en 30 secodnes
# Il n'y aura pas 150 utilisaterus en mm temps
# Territoire type, risque, retrecissement gonflement argile, risque transition (? risques physiques), stress hydrique, 

