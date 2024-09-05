import requests
import cv2
import numpy as np
import streamlit as st
from PIL import Image
import io

# Fonction pour envoyer l'image à l'API et récupérer le masque prédit
def get_predicted_mask(image_path):
    with open(image_path, 'rb') as img_file:
        image_data = {'image': img_file}
        # Envoyer la requête à l'API
        r = requests.post(url, files=image_data)
        if r.status_code == 200:
            # Convertir la réponse en tableau numpy (image du mask prédit)
            img_array = cv2.imdecode(np.frombuffer(r.content, np.uint8), cv2.IMREAD_UNCHANGED)
            return img_array
        else:
            st.error(f"Erreur API: {r.status_code}")
            return None

# Afficher l'image et les masques sur l'interface Streamlit
def display_images(original_image, real_mask, predicted_mask):
    st.image(original_image, caption='Image Originale', use_column_width=True)
    
    if real_mask is not None:
        st.image(real_mask, caption='Mask Réel', use_column_width=True, clamp=True, channels="GRAY")
    
    if predicted_mask is not None:
        predicted_mask_rgb = cv2.cvtColor(predicted_mask, cv2.COLOR_BGR2RGB)
        st.image(predicted_mask_rgb, caption='Mask Prédit', use_column_width=True)

# URL de l'API
url = 'https://p08.azurewebsites.net/predict_mask'

# Interface Streamlit
st.title("Segmentation d'image avec API")

# Charger l'image à partir de l'interface utilisateur Streamlit
uploaded_image = st.file_uploader("Charger une image", type=["png", "jpg", "jpeg"])

# Option pour charger un masque réel (facultatif)
uploaded_mask = st.file_uploader("Charger un mask réel (optionnel)", type=["png"])

if uploaded_image is not None:
    # Lire l'image originale en tant qu'image PIL
    original_image = Image.open(uploaded_image)
    
    # Convertir l'image PIL en numpy array pour OpenCV
    original_image_cv = np.array(original_image)

    # Convertir l'image en format BGR si elle est en RGB (pour compatibilité OpenCV)
    if original_image_cv.shape[2] == 3:  # Vérifie s'il y a 3 canaux (RGB)
        original_image_cv = cv2.cvtColor(original_image_cv, cv2.COLOR_RGB2BGR)

    # Afficher l'image originale
    st.write("Image originale chargée :")
    st.image(original_image, caption="Image originale", use_column_width=True)

    # Si un masque réel est fourni, on le charge
    real_mask = None
    if uploaded_mask is not None:
        real_mask = Image.open(uploaded_mask).convert('L')  # Convertir en niveaux de gris
        real_mask = np.array(real_mask)
        st.write("Mask réel chargé :")
        st.image(real_mask, caption="Mask Réel", use_column_width=True, clamp=True)

    # Demander l'envoi à l'API
    if st.button("Prédire le mask"):
        st.write("Envoi de l'image à l'API pour la segmentation...")
        # Sauvegarder temporairement l'image
        with open("temp_image.png", "wb") as f:
            f.write(uploaded_image.getbuffer())
        
        # Appel à l'API pour obtenir le masque prédit
        predicted_mask = get_predicted_mask("temp_image.png")
        
        if predicted_mask is not None:
            # Afficher les résultats
            display_images(original_image, real_mask, predicted_mask)
        else:
            st.error("Échec de la prédiction du masque.")