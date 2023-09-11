import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Style CSS pour la boîte "amazing"
box_style = """
    background-color: #3c4963;
    padding: 5px;
    border-radius: 5px;
    text-align: left;
    width: 200px; /* Largeur minimale pour minimiser la taille de la boîte */
"""

# Affichage de la boîte "amazing" avec nom et prénom en haut à gauche
st.sidebar.markdown(
    f'<div style="{box_style}">'
    '<h5 style="color: #ffffff;">Nom : CHARET</h3>'
    '<h5 style="color: #ffffff;">Prénom : Mohamed</h3>'
    '<h5 style="color: #ffffff;">Filière : Actuariat-Finance</h3>'
    '</div>',
    unsafe_allow_html=True
)

st.title("Analyse d'Assurance")

# Section de sélection du fichier Excel avec plusieurs feuilles
st.sidebar.header('Sélectionnez le fichier Excel avec plusieurs feuilles')
uploaded_file = st.sidebar.file_uploader("Chargez le fichier Excel avec plusieurs feuilles", type=["xlsx"])

data = None  # Initialisation de la variable data

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1]  # Obtenir l'extension du fichier

    if file_extension == "xlsx":
        xls = pd.ExcelFile(uploaded_file)  # Ouvrir le fichier Excel avec plusieurs feuilles
        sheet_names = xls.sheet_names  # Obtenir les noms des feuilles de calcul

        # Demander à l'utilisateur de sélectionner une feuille de calcul dans la barre latérale
        selected_sheet = st.sidebar.selectbox("Sélectionnez la feuille de calcul à analyser", sheet_names)

        # Charger les données depuis la feuille de calcul sélectionnée
        data = pd.read_excel(xls, sheet_name=selected_sheet)

# Section pour choisir entre l'analyse exploratoire et le calcul de provisions
st.header('Choisissez une option :')
selected_option = st.radio("", ["Analyse Exploratoire", "Calcul de Provisions (Chain-Ladder)"])

# Si l'utilisateur choisit l'analyse exploratoire
if selected_option == "Analyse Exploratoire" and data is not None:
    st.write("Aperçu des données :")
    st.write(data.head())

    st.write("Statistiques descriptives :")
    st.write(data.describe())

    selected_variable = st.selectbox("Sélectionnez la variable pour l'histogramme", data.columns)

    st.write(f"Histogramme de {selected_variable} :")
    fig, ax = plt.subplots()
    ax.hist(data[selected_variable], bins=30)
    st.pyplot(fig)

# Si l'utilisateur choisit le calcul de provisions par la méthode de Chain-Ladder
if selected_option == "Calcul de Provisions (Chain-Ladder)" and data is not None:
    # Ici, vous pouvez mettre le code pour effectuer le calcul de provisions selon la méthode de Chain-Ladder.
    # Par exemple, vous pouvez utiliser la méthode que j'ai mentionnée précédemment pour calculer les provisions.
    st.write("Vous avez choisi de calculer les provisions par la méthode de Chain-Ladder.")
    # Ajoutez votre code de calcul de provisions ici
