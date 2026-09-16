# VIVALDI

VIVALDI est un assistant en ligne de commande écrit en Python. Il fournit des outils simples pour l'informatique, la programmation et la recherche d'informations scientifiques.

## Fonctionnalités

- Affichage des informations système et de la date/heure ;
- exécution de code Python dans un mode interactif ;
- ouverture de Windows Terminal, de l'invite de commande ou de PowerShell ;
- accès rapide à la documentation Python ;
- recherche de réponses techniques et d'informations scientifiques via l'API DuckDuckGo ;
- interface interactive avec commandes intégrées.

## Prérequis

- Python 3 ;
- une connexion Internet pour les commandes `ask` et `science` ;
- Windows pour les commandes `wt`, `cmd` et `powershell` ;
- le paquet Python `requests`.

## Installation

Clonez le projet ou placez `Vivaldi.py` dans le dossier de votre choix, puis installez la dépendance :

```bash
python -m pip install requests
```

Sous certains systèmes, la commande peut être :

```bash
python3 -m pip install requests
```

## Lancement

Depuis le dossier contenant `Vivaldi.py` :

```bash
python Vivaldi.py
```

L'application affiche ensuite l'invite interactive :

```text
VIVALDI >
```

## Commandes disponibles

| Commande | Description |
| --- | --- |
| `help` | Affiche la liste des commandes disponibles. |
| `about` | Affiche le nom du projet, sa version et son auteur. |
| `sysinfo` | Affiche le système d'exploitation, la machine et la version de Python. |
| `datetime` | Affiche la date et l'heure actuelles. |
| `python` | Ouvre un mode Python interactif. Utilisez `exit()` pour en sortir. |
| `wt` | Ouvre Windows Terminal. |
| `cmd` | Ouvre l'invite de commande Windows. |
| `powershell` | Ouvre PowerShell. |
| `doc` | Demande un mot-clé et affiche un lien vers la recherche correspondante dans la documentation Python. |
| `science` | Recherche un sujet scientifique via l'API DuckDuckGo. |
| `ask` | Recherche une réponse technique ou générale via l'API DuckDuckGo. |
| `exit` | Quitte VIVALDI. |

## Exemple d'utilisation

```text
VIVALDI > sysinfo

[ Informations système ]
OS         : Windows 11
Machine    : AMD64
Python     : 3.x.x

VIVALDI > ask
Pose ta question : Qu'est-ce que Python ?

VIVALDI > exit
DESTRUCTION...
```

## Connexion et erreurs réseau

Les commandes `ask` et `science` envoient la requête à `https://api.duckduckgo.com/` et attendent une réponse pendant 10 secondes au maximum. Une connexion Internet est donc nécessaire. En cas de problème réseau ou de réponse JSON invalide, VIVALDI affiche un message d'erreur sans arrêter l'application.

La commande `doc` ne consulte pas directement l'API : elle construit et affiche un lien vers la page de recherche de la documentation officielle Python.

## Attention à la sécurité

Le mode `python` utilise `exec()` pour exécuter le code saisi. Il permet donc d'exécuter des opérations arbitraires avec les droits de l'utilisateur courant. N'exécutez pas de code provenant d'une source non fiable.

Les commandes `wt`, `cmd` et `powershell` lancent également des programmes du système et sont principalement destinées à Windows.

## Informations du projet

- **Nom :** VIVALDI
- **Version indiquée dans le programme :** 3.0
- **Auteur :** Ben-kail Azad
- **Fichier principal :** `Vivaldi.py`
