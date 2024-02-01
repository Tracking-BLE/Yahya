    <?php
    // Recuperer les donnees POST envoyees par le script Python
    $data = file_get_contents('php://input');

    // Decodez les donnees JSON
    $data_decoded = json_decode($data);

    // Renvoyer la reponse au script Python
    echo "valider";
    ?>
