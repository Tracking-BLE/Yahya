<?php

// URL du serveur Python
$pythonServerUrl = 'http://192.168.134.172:8888'; // Mettez l'URL correcte de votre serveur Python

// Données à envoyer au serveur Python (peut être vide si vous n'envoyez pas de données)
$data = array(
    'key1' => 'value1',
    'key2' => 'value2'
);

// Convertir les données en format JSON
$jsonData = json_encode($data);

// Options pour la requête HTTP
$options = array(
    'http' => array(
        'header'  => "Content-type: application/json\r\n",
        'method'  => 'POST',
        'content' => $jsonData
    )
);

// Créer le contexte de la requête HTTP
$context  = stream_context_create($options);

// Envoyer la requête POST au serveur Python
$response = file_get_contents($pythonServerUrl, false, $context);

// Afficher la réponse du serveur Python
echo $response;

?>
