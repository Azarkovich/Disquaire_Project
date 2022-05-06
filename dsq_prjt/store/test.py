import json

chemin = "ynb/Documents/fichier.json"

with open(chemin, "w") as f:
    json.dump("Bonjour", f)
