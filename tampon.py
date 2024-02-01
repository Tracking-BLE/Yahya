import json
import http.client

"""
Connexion au serveur OVH 
Parametre :
- hote : juleshaag.fr
- port : 80
- fichier : /trackingble2024/JSON/index.php
"""
def connexion():
    # Connexion au serveur
    server_host = "juleshaag.fr"
    server_port = 80
    endpoint = "/trackingble2024/JSON/index.php"
    conn = http.client.HTTPConnection(server_host, server_port)
    return conn, endpoint


def lire():
    # Ouvrir le fichier en mode lecture
    with open("C:/Users/yahya/OneDrive/Documents/JSON/test.json") as f:
        data = json.load(f)
    return data

data = lire()

# Appeler la fonction de connexion
conn, endpoint = connexion()

# Envoyer une requete POST a l'endpoint specifie avec les donnees JSON
headers = {"Content-type": "application/json"}
conn.request("POST", endpoint, body=json.dumps(data), headers=headers)

# Recuperer la reponse du serveur
response = conn.getresponse()

# Afficher la reponse
print(response.read().decode())

# Fermer la connexion
conn.close()
