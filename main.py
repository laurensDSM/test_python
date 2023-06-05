#Dit is de main.py
from github import Github
import importlib
import json
import os

def main():
#  github = Github('https://github.com/laurensDSM/test_python.git')
#   print(github.check_update())
    config_path = "config/config.txt"  # Het pad naar het configuratiebestand

    try:
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
            
            module_name = config[0]["module_name"]
            class_name = config[0]["class_name"]

            # Importeer de module
            module = __import__(module_name)

            # Instantieer de klasse
            my_class = getattr(module, class_name)()

            # Gebruik de klasse
            my_class.log_text()

                    
    except FileNotFoundError:
        print("Het configuratiebestand kon niet worden gevonden.")
    except json.JSONDecodeError:
        print("Het configuratiebestand bevat geen geldige JSON-indeling.")
    except IOError:
        print("Er is een fout opgetreden bij het openen van het configuratiebestand.")


if __name__ == "__main__":
    main()

