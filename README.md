## H-GenAI-Hackaton

Nom de l'équipe : **GEN'SAE**  
Membres : Titouan CONSTANCE, Arthur DE ROUCK, Yann GAUTIER, Valentin GENAY, Quentin GOUIFFES, Alexandre HOUARD  
Cas d'usage : **Sfil 2**  
> _Figure 1 : Notre équipe (Slide Executive Summary)_
<img width="476" alt="gensae" src="https://github.com/user-attachments/assets/b7d89183-b44e-4d7f-a888-795390c68234" />

### Solution proposée
Nous avons développé un **portail interactif** combiné à un **agent conversationnel** capable d'exploiter les données publiques (INSEE, DGFIP) et internes à Sfil. Ce portail permet aux utilisateurs de formuler des requêtes afin de **rechercher, croiser et analyser** les informations disponibles. 

Les résultats sont présentés sous forme de **visualisations interactives** telles que des cartes géographiques ou des graphiques dynamiques. L'application s'appuie largement sur **l'API d'Amazon Bedrock**.

> _Figure 2 : Présentation du projet (Slide Executive Summary)_
<img width="475" alt="summary" src="https://github.com/user-attachments/assets/fadd2dab-632d-4bc7-bb51-1157513fa3ee" />



### Utilisation
L'utilisateur fait sa requête à **chatbot_lib**. Ce dernier affiche :
- Une **synthèse des risques encourus** pour la communauté locale demandée, avec une **visualisation des risques**.
- Dans un autre onglet, des **informations pertinentes** relatives au risque et à la communauté locale demandés.

> _Figure 3 : Expérience utilisateur (Slide User Journey Case 1)_
<img width="469" alt="UI" src="https://github.com/user-attachments/assets/e26408f7-6d7a-4e55-aa76-35be24e76dac" />


### Architecture du projet
L'architecture repose sur un **système modulaire**, intégrant des services de traitement de données, un chatbot intelligent et des visualisations interactives.
<img width="476" alt="architecture" src="https://github.com/user-attachments/assets/52174c21-5db5-457c-a215-57b3698e604b" />

> _Figure 4 : Schéma technique de l'architecture (Slide Architecture)_

### Points forts de notre outil
✅ Simple d'utilisation  
✅ Informations fiables et sourcées  
✅ Peu énergivore  
✅ Visualisation claire des données  

### Business Model
Notre modèle économique repose sur l'intégration de notre outil dans le **processus décisionnel de Sfil**, avec des options d'expansion vers d'autres collectivités locales.

> _Figure 5 : Stratégie de monétisation (Slide Business Model)_
<img width="476" alt="business model" src="https://github.com/user-attachments/assets/9be3def7-b240-49ae-abf0-6ef0424d6c24" />

---
📌 **Projet développé par l'équipe GEN'SAE**

