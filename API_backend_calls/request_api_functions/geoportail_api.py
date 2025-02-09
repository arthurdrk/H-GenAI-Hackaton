import requests

BASE_URL = "https://apicarto.ign.fr/api/gpu"

def call_geoportail_api(endpoint: str, **params):
    """
    Effectue une requête GET à un endpoint spécifique de l'API Géoportail Urbanisme.

    :param endpoint: Endpoint de l'API (ex: "/municipality").
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

def get_municipality(geom=None, insee=None):
    """
    Récupère les informations d'une commune.
    
    :param geom: Géométrie GeoJSON pour la recherche.
    :param insee: Code INSEE de la commune.
    :return: Données GeoJSON des communes trouvées.
    """
    return call_geoportail_api("/municipality", geom=geom, insee=insee)

def get_document(geom=None, partition=None):
    """
    Récupère l'emprise d'un document d'urbanisme (PLU, POS, CC, PSMV).
    
    :param geom: Géométrie GeoJSON pour la recherche.
    :param partition: Partition GPU du document.
    :return: Données GeoJSON des documents intersectant la géométrie.
    """
    return call_geoportail_api("/document", geom=geom, partition=partition)

def get_zone_urba(geom=None, partition=None):
    """
    Récupère les zonages d’un document d’urbanisme.
    
    :param geom: Géométrie GeoJSON pour la recherche.
    :param partition: Partition GPU du document.
    :return: Données GeoJSON des zonages intersectant la géométrie.
    """
    return call_geoportail_api("/zone-urba", geom=geom, partition=partition)

def get_secteur_cc(geom=None, partition=None):
    """
    Récupère les secteurs d’une carte communale.
    """
    return call_geoportail_api("/secteur-cc", geom=geom, partition=partition)

def get_prescription_surf(geom=None, partition=None):
    """
    Récupère les prescriptions surfaciques d’un document d’urbanisme.
    """
    return call_geoportail_api("/prescription-surf", geom=geom, partition=partition)

def get_prescription_lin(geom=None, partition=None):
    """
    Récupère les prescriptions linéaires d’un document d’urbanisme.
    """
    return call_geoportail_api("/prescription-lin", geom=geom, partition=partition)

def get_prescription_pct(geom=None, partition=None):
    """
    Récupère les prescriptions ponctuelles d’un document d’urbanisme.
    """
    return call_geoportail_api("/prescription-pct", geom=geom, partition=partition)

def get_info_surf(geom=None, partition=None):
    """
    Récupère les informations surfaciques d’un document d’urbanisme.
    """
    return call_geoportail_api("/info-surf", geom=geom, partition=partition)

def get_info_lin(geom=None, partition=None):
    """
    Récupère les informations linéaires d’un document d’urbanisme.
    """
    return call_geoportail_api("/info-lin", geom=geom, partition=partition)

def get_info_pct(geom=None, partition=None):
    """
    Récupère les informations ponctuelles d’un document d’urbanisme.
    """
    return call_geoportail_api("/info-pct", geom=geom, partition=partition)

def get_acte_sup(partition=None):
    """
    Récupère les actes des servitudes d’utilité publique.
    """
    return call_geoportail_api("/acte-sup", partition=partition)

def get_assiette_sup_s(geom=None, partition=None, categorie=None):
    """
    Récupère les assiettes surfaciques des servitudes d’utilité publique.
    """
    return call_geoportail_api("/assiette-sup-s", geom=geom, partition=partition, categorie=categorie)

def get_assiette_sup_l(geom=None, partition=None, categorie=None):
    """
    Récupère les assiettes linéaires des servitudes d’utilité publique.
    """
    return call_geoportail_api("/assiette-sup-l", geom=geom, partition=partition, categorie=categorie)

def get_assiette_sup_p(geom=None, partition=None, categorie=None):
    """
    Récupère les assiettes ponctuelles des servitudes d’utilité publique.
    """
    return call_geoportail_api("/assiette-sup-p", geom=geom, partition=partition, categorie=categorie)

def get_generateur_sup_s(geom=None, partition=None, categorie=None):
    """
    Récupère les générateurs surfaciques des servitudes d’utilité publique.
    """
    return call_geoportail_api("/generateur-sup-s", geom=geom, partition=partition, categorie=categorie)

def get_generateur_sup_l(geom=None, partition=None, categorie=None):
    """
    Récupère les générateurs linéaires des servitudes d’utilité publique.
    """
    return call_geoportail_api("/generateur-sup-l", geom=geom, partition=partition, categorie=categorie)

def get_generateur_sup_p(geom=None, partition=None, categorie=None):
    """
    Récupère les générateurs ponctuels des servitudes d’utilité publique.
    """
    return call_geoportail_api("/generateur-sup-p", geom=geom, partition=partition, categorie=categorie)

# 🔹 Exemples d'utilisation :
if __name__ == "__main__":
    print("📍 Exemple : Recherche de la commune de Rennes")
    print(get_municipality(geom='{"type": "Point","coordinates":[-1.691634,48.104237]}'))

    print("\n📜 Exemple : Recherche d'un document d'urbanisme")
    print(get_document(geom='{"type": "Point","coordinates":[-1.691634,48.104237]}'))

    print("\n🏗️ Exemple : Recherche d'un zonage d'urbanisme")
    print(get_zone_urba(geom='{"type": "Point","coordinates":[-1.691634,48.104237]}'))
