# IA_P08_front


## Application Streamlit de Segmentation d'Image
Cette application Streamlit permet aux utilisateurs de charger une image, de l'envoyer à une API de segmentation d'image, et d'afficher le masque de segmentation prédit. Elle offre également la possibilité de comparer le masque prédit avec un masque réel, si disponible.
Fonctionnalités

Interface utilisateur avec Streamlit
Chargement d'images à segmenter
Chargement optionnel d'un masque réel pour comparaison
Envoi d'images à une API de segmentation
Affichage des résultats : image originale, masque réel (si fourni), et masque prédit

# Prérequis

Python 3.x
pip (gestionnaire de paquets Python)

# Installation

Clonez ce dépôt ou téléchargez le script.
Installez les dépendances nécessaires :
Copypip install streamlit requests pillow numpy


# Configuration
Assurez-vous de définir correctement l'URL de l'API dans le script :
pythonCopyurl = 'https://p08.azurewebsites.net/predict_mask'
Remplacez cette URL par celle de votre API de segmentation si nécessaire.
Utilisation

Lancez l'application Streamlit :
Copystreamlit run nom_du_script.py

Ouvrez votre navigateur à l'adresse indiquée par Streamlit (généralement http://localhost:8501).
Utilisez l'interface pour :

Charger une image à segmenter
Charger un masque réel (optionnel)
Cliquer sur "Prédire le mask" pour envoyer l'image à l'API et afficher les résultats



# Structure du code

get_predicted_mask(image_path) : Envoie l'image à l'API et récupère le masque prédit.
display_images(original_image, real_mask, predicted_mask) : Affiche l'image originale, le masque réel (si disponible) et le masque prédit.
Le reste du script gère l'interface utilisateur Streamlit et le flux de l'application.

# Remarques

L'application sauvegarde temporairement l'image chargée sous le nom "temp_image.png" avant de l'envoyer à l'API.
Assurez-vous que l'API est accessible et fonctionne correctement pour obtenir des résultats.
Les types d'images supportés sont PNG, JPG et JPEG.

# Dépannage

Si vous rencontrez des erreurs liées à l'API, vérifiez que l'URL est correcte et que l'API est opérationnelle.
En cas de problèmes de chargement d'image, assurez-vous que le format est pris en charge.

# Contribuer
Les contributions à ce projet sont les bienvenues. N'hésitez pas à ouvrir une issue ou à soumettre une pull request.
