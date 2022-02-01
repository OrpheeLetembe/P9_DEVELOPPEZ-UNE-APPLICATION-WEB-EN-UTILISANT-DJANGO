# P9_DEVELOPPEZ-UNE-APPLICATION-WEB-EN-UTILISANT-DJANGO

La startup LITReview souhaite développer et commercialiser une application web permettant à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.

Un utilisateur devra pouvoir :

-	Se connecter et s’inscrire, le site ne doit pas être accessible à un utilisateur non connecté
-	Consulter un flux contenant les derniers tickets et les commentaires des utilisateurs qu'il suit, classés par ordre chronologique, les plus récents en premier ; 
-	Créer de nouveaux tickets pour demander une critique sur un livre/article ;
-	Créer des critiques en réponse à des tickets ;
-	Créer des critiques qui ne sont pas en réponse à un ticket. Dans le cadre d'un processus en une étape, l'utilisateur créera un ticket puis un commentaire en réponse à son propre ticket ;
-	Voir, modifier et supprimer ses propres tickets et commentaires ; 
-	Suivre les autres utilisateurs en entrant leur nom d'utilisateur ;
-	Voir qui il suit et suivre qui il veut ; 
-	Cesser de suivre un utilisateur.

# Installation et exécution de l'application 

1	Cloner ce dépôt de code à l'aide de la commande ‘$ git clone clone https://github.com/OrpheeLetembe/P9_DEVELOPPEZ-UNE-APPLICATION-WEB-EN-UTILISANT-DJANGO.git’ (vous pouvez également télécharger le code [en temps qu'archive zip] https://github.com/OrpheeLetembe/P9_DEVELOPPEZ-UNE-APPLICATION-WEB-EN-UTILISANT-DJANGO/archive/refs/heads/main.zip

2	 Rendez-vous depuis un terminal à la racine du répertoire litreview 

3	Créer un environnement virtuel pour le projet avec la commande :

-`$ python -m venv env` sous windows 
- `$ python3 -m venv env` sous macos ou linux.

4	Activez l'environnement virtuel avec la commande

-`$ env\Scripts\activate` sous windows 
-`$ source env/bin/activate` sous macos ou linux.

5	Installez les dépendances du projet avec la commande `$ pip install -r requirements.txt`

6	Créer un super utilisateur avec la commande ‘$ python manage.py createsuperuser et suivez les instructions

7	 Démarrer le serveur avec `$ python manage.py runserver`

Les étapes 1 à 6 ne sont requises que pour l'installation initiale. Pour les lancements ultérieurs du serveur de l'application, il suffit d'exécuter les étapes 4 et 7 à partir du répertoire racine du projet.


## Connexion à l'application

Lorsque le serveur fonctionne, après l'étape 7 de la procédure, l’application peut être accessible via url http://localhost:8000/. Ce dernier ouvrira un navigateur qui vous présentera la page d’accueil de l’application permettant la connexion de l’utilisateur et un lien vers l’interface de création de compte.
Vous trouverez dans le tableau ‘Comptes utilisateurs’ ci-dessous les identifiants des utilisateurs déjà enregistrés.
Comptes utilisateurs

Nom d’utilisateur	  Mot de passe
Alex	               dafp1982
Aurore	             ldau2015
Davis	               r7dY98CYf
Jean	               gb63nHQ4f
Léon	               kLjaeF29
Lyn	                 97N5UHihg
Malick	             vr9K6t5EK
Orphée	             kstr571jt
Rose	               2qVG7si2V


## Interface d’administration

L’interface d’administration de l’application est accessible via l’url http://localhost:8000/admin. Vous serrez alors diriger vers la page de connexion de l’administrateur. Vous pouvez ainsi avoir accès à l’interface d’administration après la saisie des identifiants de super utilisateur précédemment créer(étape 6).
