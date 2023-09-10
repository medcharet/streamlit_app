import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Analyse d'Assurance")
st.header('chargement de la base de donnée')
# Section de chargement des données
uploaded_file = st.file_uploader("Chargez la base de données CSV ou Excel", type=["csv", "xlsx"])

data = None  # Initialisation de la variable data

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1]  # Obtenir l'extension du fichier

    if file_extension == "csv":
        data = pd.read_csv(uploaded_file)  # Charger les données depuis le fichier CSV
    elif file_extension == "xlsx":
        data = pd.read_excel(uploaded_file)  # Charger les données depuis le fichier Excel

# Afficher les 5 premières lignes du DataFrame si data est défini
if data is not None:
    st.write("Aperçu des données :")
    st.write(data.head())

    # Afficher des statistiques descriptives
    st.write("Statistiques descriptives :")
    st.write(data.describe())

    # Sélection de la variable pour l'histogramme
    selected_variable = st.selectbox("Sélectionnez la variable pour l'histogramme", data.columns)

    # Créer un histogramme interactif de la variable sélectionnée avec Matplotlib et afficher avec st.pyplot()
    st.write(f"Histogramme de {selected_variable} :")
    fig, ax = plt.subplots()
    ax.hist(data[selected_variable], bins=30)
    st.pyplot(fig)  # Utilisez st.pyplot() pour afficher le graphique dans Streamlit
