import requests

BASE_URL = "https://hubeau.eaufrance.fr/api/v1/qualite_nappes"

def call_hubeau_api(endpoint: str, **params):
    """
    Effectue une requête GET vers un endpoint spécifique de l'API Hub'Eau - Qualité des nappes.

    :param endpoint: Chemin de l'endpoint (ex: "/analyses").
    :param params: Paramètres optionnels sous forme de dictionnaire.
    :return: Résultat JSON de la requête ou message d'erreur.
    """
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Erreur {response.status_code}: {response.text}"}

# 🔹 Fonctions spécifiques pour chaque endpoint :

def get_analyses(bbox=None, bss_id=None, code_insee=None, date_debut=None, date_fin=None, page=1, size=20):
    """
    Récupère les mesures de qualité des nappes d'eau souterraines.

    :param bbox: Emprise spatiale (format : minLon,minLat,maxLon,maxLat).
    :param bss_id: Code(s) national de la station.
    :param code_insee: Code INSEE de la commune.
    :param date_debut: Date de début du prélèvement (format yyyy-MM-dd).
    :param date_fin: Date de fin du prélèvement (format yyyy-MM-dd).
    :param page: Numéro de la page.
    :param size: Nombre maximal de résultats par page.
    :return: Données JSON des analyses de qualité des nappes.
    """
    return call_hubeau_api("/analyses", bbox=bbox, bss_id=bss_id, code_insee_actuel=code_insee, 
                           date_debut_prelevement=date_debut, date_fin_prelevement=date_fin, page=page, size=size)

def get_analyses_csv(**params):
    """
    Récupère les mesures de qualité des nappes au format CSV.

    :param params: Même structure que `get_analyses()`.
    :return: Contenu CSV en texte brut.
    """
    return call_hubeau_api("/analyses.csv", **params)

def get_stations(bbox=None, code_commune=None, code_masse_eau=None, date_min_maj=None, date_max_maj=None, page=1, size=20):
    """
    Récupère la liste des stations de mesure des nappes d'eau souterraines.

    :param bbox: Emprise spatiale (format : minLon,minLat,maxLon,maxLat).
    :param code_commune: Code(s) INSEE de la commune.
    :param code_masse_eau: Code(s) masse d'eau.
    :param date_min_maj: Date min de mise à jour (format yyyy-MM-dd).
    :param date_max_maj: Date max de mise à jour (format yyyy-MM-dd).
    :param page: Numéro de la page.
    :param size: Nombre maximal de résultats par page.
    :return: Données JSON des stations de mesure.
    """
    return call_hubeau_api("/stations", bbox=bbox, code_commune=code_commune, code_masse_eau_rap=code_masse_eau, 
                           date_min_maj=date_min_maj, date_max_maj=date_max_maj, page=page, size=size)

def get_stations_csv(**params):
    """
    Récupère la liste des stations de mesure au format CSV.

    :param params: Même structure que `get_stations()`.
    :return: Contenu CSV en texte brut.
    """
    return call_hubeau_api("/stations.csv", **params)

# 🔹 Exemples d'utilisation :
if __name__ == "__main__":
    print("📍 Exemple : Recherche des analyses de qualité pour une zone géographique")
    print(get_analyses(bbox="1.6194,47.7965,2.1910,47.9988", date_debut="2023-01-01", date_fin="2023-12-31"))

    print("\n🛠️ Exemple : Recherche des stations de mesure en région parisienne")
    print(get_stations(code_commune="75056", date_min_maj="2023-01-01"))
