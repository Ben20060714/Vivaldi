"""
VIVALDI - Assistant IA personnel pour l'informatique, la programmation et la science.
Projet #VIVALDI
"""

import sys
import platform
import datetime
import requests
import subprocess
import os

# --- Présentation ---
INTRO = """
╔════════════════════════════════════════════════════╗
║                   VIVALDI                          ║
║  Assistant IA personnel pour l'informatique, la    ║
║  programmation et la science.                      ║
╚════════════════════════════════════════════════════╝
"""

# --- Commandes disponibles ---
COMMANDS = {
    "help": "Afficher les commandes disponibles",
    "about": "Informations supplementaires",
    "sysinfo": "Afficher les infos système",
    "datetime": "Afficher la date et l'heure actuelles",
    "python": "Exécuter du code Python simple",
    "wt": "Ouvrir le terminal windows",
    "cmd": "Ouvrir l'invite de commande",
    "powershell": "Exécuter powershell natif",
    "doc": "Rechercher dans la documentation Python (via API)",
    "science": "Accéder à des infos scientifiques (via API)",
    "ask": "Poser une question technique ou scientifique",
    "exit": "Quitter VIVALDI"
}

# --- Fonctions principales ---
def show_help():
    print("\nCommandes disponibles :")
    for cmd, desc in COMMANDS.items():
        print(f"  - {cmd:<10} : {desc}")
    print()

def show_infs():
    print("\nNom du projet : VIVALDI", "\nVersion : 3.0", "\nAuteur : Ben-kail Azad")
    print()

def start_terminal():
    subprocess.run("wt", shell=True)

def start_cmd():
    subprocess.run("start cmd", shell=True)

def start_powershell():
    subprocess.run("start powershell", shell=True)

def show_sysinfo():
    print("\n[ Informations système ]")
    print(f"OS         : {platform.system()} {platform.release()}")
    print(f"Machine    : {platform.machine()}")
    print(f"Python     : {platform.python_version()}")
    print()

def show_datetime():
    now = datetime.datetime.now()
    print(f"\nDate et heure actuelles : {now.strftime('%A %d %B %Y, %H:%M:%S')}\n")

def ask_question():
    question = input("Pose ta question : ").strip()
    if not question:
        print("# Veuillez entrer une question.")
        return

    print("\n# Recherche en cours...")
    try:
        url = "https://api.duckduckgo.com/"
        params = {
            "q": question,
            "format": "json",
            "no_redirect": 1,
            "no_html": 1,
            "skip_disambig": 1
        }
        headers = {"User-Agent": "VIVALDI/3.0"}
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        abstract = data.get("Abstract", "").strip()
        related = data.get("RelatedTopics", [])

        if abstract:
            print(f"\n# Résumé :\n{abstract}\n")
        elif related:
            print("\n# Résumé indirect :")
            printed = 0
            for topic in related:
                if printed >= 3:
                    break
                if "Text" in topic and topic["Text"]:
                    print(f"- {topic['Text']}")
                    printed += 1
                elif "Topics" in topic and isinstance(topic["Topics"], list):
                    for subtopic in topic["Topics"]:
                        if printed >= 3:
                            break
                        if "Text" in subtopic and subtopic["Text"]:
                            print(f"- {subtopic['Text']}")
                            printed += 1
            print()
        else:
            print("Aucune réponse claire trouvée. Essaie une autre formulation.")
    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête : {e}")
    except ValueError as e:
        print(f"Erreur lors du traitement de la réponse : {e}")

def run_python():
    print("\n[ Mode Python interactif ] Tapez 'exit()' pour quitter.")
    while True:
        try:
            code = input(">>> ")
            if code.strip() == "exit()":
                break
            exec(code, globals())
        except Exception as e:
            print(f"Erreur : {e}")

def search_python_doc():
    query = input("Mot-clé ou fonction Python : ").strip()
    url = f"https://docs.python.org/3/search.html?q={query}&check_keywords=yes&area=default"
    print(f"\n# Documentation Python : {url}\n")

def fetch_science_info():
    topic = input("Sujet scientifique (ex: gravité, ADN, énergie) : ").strip()
    if not topic:
        print("# Veuillez entrer un sujet.")
        return

    try:
        url = "https://api.duckduckgo.com/"
        params = {
            "q": topic,
            "format": "json",
            "no_redirect": 1,
            "no_html": 1,
            "skip_disambig": 1
        }
        headers = {"User-Agent": "VIVALDI/3.0"}
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        abstract = data.get("Abstract", "").strip()
        if abstract:
            print(f"\n# Résumé scientifique :\n{abstract}\n")
        else:
            print("Aucune information trouvée. Essaie un autre sujet ou reformule.")
    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête : {e}")
    except ValueError as e:
        print(f"Erreur lors du traitement de la réponse : {e}")
"""
def run_antivirus_module(module_name="VIVALDI_SECURE_CORE", path_to_monitor="~/", sensitivity=70):
    print(f"[VIVALDI] Lancement du module antivirus : {module_name}")
    print(f"[VIVALDI] Surveillance active dans le dossier {path_to_monitor}...")

    subprocess.run([
        "python3", f"{module_name}.py",
        "--path", path_to_monitor,
        "--sensitivity", str(sensitivity)
    ])
"""
# --- Boucle principale ---
def main():
    print(INTRO)
    show_help()

    while True:
        try:
            cmd = input("VIVALDI > ").strip().lower()
            if cmd == "help":
                show_help()
            elif cmd == "sysinfo":
                show_sysinfo()
            elif cmd == "datetime":
                show_datetime()
            elif cmd == "python":
                run_python()
            elif cmd == "wt":
                start_terminal()
            elif cmd == "cmd":
                start_cmd()
            elif cmd == "powershell":
                start_powershell()
            elif cmd == "about":
                show_infs()
            elif cmd == "ask":
                ask_question()
            elif cmd == "doc":
                search_python_doc()
            elif cmd == "science":
                fetch_science_info()
            elif cmd == "exit":
                print("DESTRUCTION...")
                break
            else:
                print("Commande inconnue. Tapez 'help' pour la liste.")
        except KeyboardInterrupt:
            print("\nInterruption. Tapez 'exit' pour quitter.")
        except Exception as e:
            print(f"Erreur inattendue : {e}")

if __name__ == "__main__":
    main()

# BEN-KAIL AZAD