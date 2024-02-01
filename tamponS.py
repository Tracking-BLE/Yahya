import json
import http.server

def ecire(data):
    # Ouvre le fichier en ecriture
    with open("C:/Users/yahya/OneDrive/Documents/JSON/test.json", "w") as g:
        json.dump(data, g)

# Definir le port sur lequel le serveur ecoutera
PORT = 8888
server_address = ("", PORT)

# Creer une instance de HTTPServer
server = http.server.HTTPServer

# Utiliser CGIHTTPRequestHandler comme gestionnaire de requetes
handler = http.server.CGIHTTPRequestHandler

# Definir les repertoires CGI (dans ce cas, tous les repertoires)
handler.cgi_directories = ["/"]

# Afficher un message indiquant le port sur lequel le serveur est actif
print("Serveur actif sur le port :", PORT)

# Creer et lancer le serveur
httpd = server(server_address, handler)
httpd.serve_forever()

# Modifier le fichier JSON avec une chaine de caracteres JSON
data = {'gateway 1': 
            {'Beacon 1': {'major': '0001', 'minor': '0004', 'RSSI': '-20'}, 
             'Beacon 2': {'major': '0001', 'minor': '004F', 'RSSI': '-45'}},
         'gateway 2': 
            {'Beacon 3': {'major': '0001', 'minor': '0004', 'RSSI': '-35'},
             'Beacon 4': {'major': '0001', 'minor': '00FF', 'RSSI': '-10'}}}

ecire(data)
