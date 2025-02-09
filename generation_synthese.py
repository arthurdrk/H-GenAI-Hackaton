from appel_knowledge_basis import retrieve_info_from_rag

def risque_collectivite(collectivite, risque):
    prompt = f""" A l'aide de ta base de connaissance, analyse dans tous les documents les risques encourue par {collectivite}
    et les alentours. Si cette collectivité n'est pas présente dans ta base de connaissance, ne me donne pas d'info supplémentaire
    et préviens moi seulement de l'absence de cette collectivité.
    Etape 1 : évalue le niveau de risque brut sur la collectivite de {collectivite} et les alentours, comme la commune, 
    le département, ou la région, pour le risque {risque}. 
    Etape 2 : fais des comparaison entre la région ou est situé {collectivite} et le reste de la France pour le risque {risque}.
    Etape 3 : fais une description d'évènement passé lié au risque {risque} sur la collectivité de {collectivite} ou les alentours, et 
    tout en restant modéré, donne une estimation de la probabilité de ce type d'évènement dans le futur.
    
    Il est tres important que tu ne donne aucune information qui ne soit pas explicitement écrite, ou logiquement déduite des ressource que tu
    possède. Si tu ne possède pas une information, soit tu n'en parle pas, soit tu précise l'absence d'information à ce sujet. Si tu as accès au nom
    complet de la source de l'information, donne la moi. TOUTE LES SOURCE DE LA FORME "(source 1)" NE DOiVENT PAS ÊTRE PRECISE . Il est important de respecter 
    l'ordre des étapes que je t'ai donné mais ne reprécise pas dans ton rendu les étapes que je t'ai donné.
    """
    output = retrieve_info_from_rag(prompt)
    print(output)
    return output

risque_collectivite('Avignon', 'climatique')

def connaissce_adaptation_risque(collectivite, risque):
    prompt = f""" 
    A l'aide de ta base de connaissance, analyse dans tous les documents les mesures de prévention mise en place par {collectivite}
    pour faire face au risque {risque}.
    Tu dois découper ta sortie pour chaque sous risque lié au risque {risque}. A chaque fois, tu dois dire à quel point {collectivite} a bien analysé le
    risque qu'il encourais en essayant de citer au mieux les sources de ta base de connaissance, tu dois ensuite montrer les actions mises en place par {collectivite}
    pour faire face à ce risque en essayant de citer au mieux les sources de ta base de connaissance. Finalement essaye d'évaluer la pertinence de ces actions.
    
    
    Il est tres important que tu ne donne aucune information qui ne soit pas explicitement écrite, ou logiquement déduite des ressource que tu
    possède. Si tu ne possède pas une information, soit tu n'en parle pas, soit tu précise l'absence d'information à ce sujet. Si tu as accès au nom
    complet de la source de l'information, donne la moi. TOUTE LES SOURCE DE LA FORME "(source 1)" NE DOiVENT PAS ÊTRE PRECISE . Il est important de respecter 
    l'ordre des étapes que je t'ai donné mais ne reprécise pas dans ton rendu les étapes que je t'ai donné.
    """
    output = retrieve_info_from_rag(prompt)
    print(output)
    return output
    
# connaissce_adaptation_risque('Avignon', 'climatique')

def conclusion_preliminaire(collectivite, risque):
    prompt = f""" 
    A l'aide de ta base de connaissance, analyse dans tous les documents les risques mesures de prévention mise en place par {collectivite}
    pour faire face au risque {risque}.
    
    Etape 1 : Reprécise les risques encourus par {collectivite} et les alentours pour le risque {risque} et à quel point ils sont présent.
    Etape 2 : Reprécise si le risques est bien identifié par la collectivité
    Etape 3 : Reprécise si la collectivité à bien menée ou prévue de mener des actions d'adaptation
    
    Il est tres important que tu ne donne aucune information qui ne soit pas explicitement écrite, ou logiquement déduite des ressource que tu
    possède. Si tu ne possède pas une information, soit tu n'en parle pas, soit tu précise l'absence d'information à ce sujet. Si tu as accès au nom
    complet de la source de l'information, donne la moi. TOUTE LES SOURCE DE LA FORME "(source 1)" NE DOiVENT PAS ÊTRE PRECISE . Il est important de respecter 
    l'ordre des étapes que je t'ai donné mais ne reprécise pas dans ton rendu les étapes que je t'ai donné.
    """
    output = retrieve_info_from_rag(prompt)
    print(output)
    return output

# conclusion_preliminaire('Avignon', 'climatique')