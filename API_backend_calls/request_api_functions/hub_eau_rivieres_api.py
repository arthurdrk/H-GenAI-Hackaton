import requests

BASE_URL = "https://hubeau.eaufrance.fr/api/v2/qualite_rivieres"

def call_hubeau_api(endpoint: str, **params):
    """
    Effectue une requête GET vers un endpoint spécifique de l'API Hub'Eau - Qualité des rivières.

    :param endpoint: Chemin de l'endpoint (ex: "/analyse_pc").
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

def get_analyse_pc(bbox=None, code_commune=None, code_cours_eau=None, date_debut=None, date_fin=None, page=1, size=20):
    """
    Récupère les analyses physico-chimiques des cours d'eau.

    :param bbox: Emprise spatiale (format : minLon,minLat,maxLon,maxLat).
    :param code_commune: Code(s) INSEE de la commune.
    :param code_cours_eau: Code(s) du cours d'eau.
    :param date_debut: Date de début de prélèvement (format yyyy-MM-dd).
    :param date_fin: Date de fin de prélèvement (format yyyy-MM-dd).
    :param page: Numéro de la page.
    :param size: Nombre maximal de résultats par page.
    :return: Données JSON des analyses physico-chimiques.
    """
    return call_hubeau_api("/analyse_pc", bbox=bbox, code_commune=code_commune, code_cours_eau=code_cours_eau, 
                           date_debut_prelevement=date_debut, date_fin_prelevement=date_fin, page=page, size=size)

def get_analyse_pc_csv(**params):
    """
    Récupère les analyses physico-chimiques au format CSV.

    :param params: Même structure que `get_analyse_pc()`.
    :return: Contenu CSV en texte brut.
    """
    return call_hubeau_api("/analyse_pc.csv", **params)

def get_condition_environnementale(bbox=None, code_commune=None, code_cours_eau=None, date_debut=None, date_fin=None, page=1, size=20):
    """
    Récupère les conditions environnementales physico-chimiques des cours d'eau.

    :param bbox: Emprise spatiale (format : minLon,minLat,maxLon,maxLat).
    :param code_commune: Code(s) INSEE de la commune.
    :param code_cours_eau: Code(s) du cours d'eau.
    :param date_debut: Date de début de prélèvement (format yyyy-MM-dd).
    :param date_fin: Date de fin de prélèvement (format yyyy-MM-dd).
    :param page: Numéro de la page.
    :param size: Nombre maximal de résultats par page.
    :return: Données JSON des conditions environnementales.
    """
    return call_hubeau_api("/condition_environnementale_pc", bbox=bbox, code_commune=code_commune, code_cours_eau=code_cours_eau, 
                           date_debut_prelevement=date_debut, date_fin_prelevement=date_fin, page=page, size=size)

def get_condition_environnementale_csv(**params):
    """
    Récupère les conditions environnementales physico-chimiques au format CSV.

    :param params: Même structure que `get_condition_environnementale()`.
    :return: Contenu CSV en texte brut.
    """
    return call_hubeau_api("/condition_environnementale_pc.csv", **params)

# 🔹 Exemples d'utilisation :
if __name__ == "__main__":
    print("📍 Exemple : Recherche des analyses physico-chimiques pour une zone géographique")
    print(get_analyse_pc(bbox="1.6194,47.7965,2.1910,47.9988", date_debut="2023-01-01", date_fin="2023-12-31"))

    print("\n💧 Exemple : Recherche des conditions environnementales en région parisienne")
    print(get_condition_environnementale(code_commune="75056", date_debut="2023-01-01"))
