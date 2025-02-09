import requests

BASE_URL = "https://hubeau.eaufrance.fr/api/v0/indicateurs_services"

def call_hubeau_api(endpoint: str, **params):
    """
    Effectue une requête GET vers un endpoint spécifique de l'API Hub'Eau.

    :param endpoint: Chemin de l'endpoint (ex: "/communes").
    :param params: Paramètres optionnels de la requête sous forme de dictionnaire.
    :return: Résultat JSON de la requête ou message d'erreur.
    """
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Erreur {response.status_code}: {response.text}"}

# 🔹 Fonctions spécifiques pour chaque endpoint :

def get_services_par_commune(annee=None, code_commune=None, code_departement=None, detail_service=False, fields=None, format="json", page=1, size=20, type_service=None):
    """
    Récupère les indicateurs de performance des services d'eau et d'assainissement pour une ou plusieurs communes.

    :param annee: Année (4 chiffres).
    :param code_commune: Code(s) INSEE de la commune (séparés par des virgules si plusieurs).
    :param code_departement: Code INSEE du département.
    :param detail_service: Détail par service (booléen).
    :param fields: Liste des champs souhaités dans la réponse.
    :param format: Format de réponse (json ou geojson).
    :param page: Numéro de la page.
    :param size: Nombre maximum de résultats par page.
    :param type_service: Type de service (AEP, AC, ANC).
    :return: Données JSON des services d'eau et d'assainissement.
    """
    return call_hubeau_api("/communes", annee=annee, code_commune=code_commune, code_departement=code_departement,
                           detail_service=detail_service, fields=fields, format=format, page=page, size=size,
                           type_service=type_service)

def get_services_par_commune_csv(**params):
    """
    Récupère les indicateurs de performance au format CSV.

    :param params: Même structure que `get_services_par_commune`.
    :return: Contenu CSV en texte brut.
    """
    return call_hubeau_api("/communes.csv", **params)

def get_services_par_indicateur(annee=None, code_indicateur="D102.0", fields=None, format="json", page=1, size=20):
    """
    Récupère la liste des valeurs des indicateurs de performance par service.

    :param annee: Année (4 chiffres).
    :param code_indicateur: Code de l'indicateur (ex: "D102.0").
    :param fields: Liste des champs souhaités dans la réponse.
    :param format: Format de réponse (json).
    :param page: Numéro de la page.
    :param size: Nombre maximum de résultats par page.
    :return: Données JSON des indicateurs par service.
    """
    return call_hubeau_api("/indicateurs", annee=annee, code_indicateur=code_indicateur,
                           fields=fields, format=format, page=page, size=size)

def get_services_par_indicateur_csv(**params):
    """
    Récupère les indicateurs de performance par service au format CSV.

    :param params: Même structure que `get_services_par_indicateur`.
    :return: Contenu CSV en texte brut.
    """
    return call_hubeau_api("/indicateurs.csv", **params)

def get_services_par_service(annee=None, code_commune=None, code_departement=None, fields=None, format="json", page=1, size=20, type_service=None):
    """
    Récupère les indicateurs de performance des services publics d'eau et d'assainissement par service.

    :param annee: Année (4 chiffres).
    :param code_commune: Code(s) INSEE de la commune.
    :param code_departement: Code INSEE du département.
    :param fields: Liste des champs souhaités dans la réponse.
    :param format: Format de réponse (json).
    :param page: Numéro de la page.
    :param size: Nombre maximum de résultats par page.
    :param type_service: Type de service (AEP, AC, ANC).
    :return: Données JSON des services publics d'eau et d'assainissement.
    """
    return call_hubeau_api("/services", annee=annee, code_commune=code_commune, code_departement=code_departement,
                           fields=fields, format=format, page=page, size=size, type_service=type_service)

def get_services_par_service_csv(**params):
    """
    Récupère les indicateurs des services publics d'eau et d'assainissement au format CSV.

    :param params: Même structure que `get_services_par_service`.
    :return: Contenu CSV en texte brut.
    """
    return call_hubeau_api("/services.csv", **params)

# 🔹 Exemples d'utilisation :
if __name__ == "__main__":
    print("📍 Exemple : Recherche des services d'eau pour la commune 75056 (Paris)")
    print(get_services_par_commune(code_commune="75056", annee=2023))

    print("\n💧 Exemple : Recherche des indicateurs pour l'indicateur D102.0")
    print(get_services_par_indicateur(code_indicateur="D102.0", annee=2023))

    print("\n🏢 Exemple : Recherche des services par département 75")
    print(get_services_par_service(code_departement="75", annee=2023))
