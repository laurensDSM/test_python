#Dit is de main.py
from github import Github
import importlib
import json
import os
from importlib import import_module
import socket
import datetime
import random
def create_directory_in_logs(directory_name):
    """Deze functie zal een map aanmaken in de map logs op basis van de hostname + datum """
    logs_directory = "logs"
    new_directory_path = os.path.join(logs_directory, directory_name)

    # Controleer of de logs-map bestaat
    if not os.path.exists(logs_directory):
        print(f"De map '{logs_directory}' bestaat niet.")
        return

    # Controleer of de nieuwe map al bestaat
    if os.path.exists(new_directory_path):
        return

    # Maak de nieuwe map aan binnen de logs-map
    os.makedirs(new_directory_path)
    print(f"De map '{new_directory_path}' is succesvol aangemaakt.")


def generate_unique_id():
    """Deze functie zal unique id maken op basis van de hostname + datum + een random nummer"""
    hostname = socket.gethostname()
    current_day = datetime.date.today().strftime('%Y%m%d')
    number = int(random.uniform(1, 2000))
    unique_id = f"{hostname}_{current_day}_{number}"

    return unique_id

def main():
    github = Github('https://github.com/laurensDSM/test_python.git')
    print(github.check_update())
    id = generate_unique_id()
    create_directory_in_logs(id)
    config_path = "config/config.txt"  # Het pad naar het configuratiebestand

    try:
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
            
            module_name = config[0]["module_name"]
            class_name = config[0]["class_name"]

            # Bepaal het pad naar de module
            module_path = f"modules.{module_name}"

            # Importeer de module
            module = import_module(module_path)

            # Instantieer de klasse
            my_class = getattr(module, class_name)()

            # Gebruik de klasse
            my_class.log_text(id)

    except FileNotFoundError:
        print("Het configuratiebestand kon niet worden gevonden.")
    except json.JSONDecodeError:
        print("Het configuratiebestand bevat geen geldige JSON-indeling.")
    except IOError:
        print("Er is een fout opgetreden bij het openen van het configuratiebestand.")



    print(github.send_logs_to_github())




if __name__ == "__main__":
    main()

