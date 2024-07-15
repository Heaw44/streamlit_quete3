import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

url = 'https://raw.githubusercontent.com/Heaw44/streamlit_quete3/main/credentials.csv'
# Lire le fichier CSV depuis l'URL
try:
    df = pd.read_csv(url, delimiter=';')
    # st.write(df.head())  # Afficher les premières lignes pour vérifier le contenu

    try:
        # Convertir le DataFrame au format souhaité
        lesDonneesDesComptes = {'usernames': {}}

        for index, row in df.iterrows():
            user_dict = {
                'name': row['name'],
                'password': row['password'],
                'email': row['email'],
                'failed_login_attemps': row['failed_login_attemps'],
                'logged_in': row['logged_in'],
                'role': row['role']
            }
            lesDonneesDesComptes['usernames'][row['name']] = user_dict

        # Afficher le dictionnaire pour vérifier le résultat
        # st.write(lesDonneesDesComptes)

    except Exception as e:
        st.error(f"Erreur lors de la création du dictionnaire: {e}")

except Exception as e:
    st.error(f"Erreur lors de la lecture du fichier CSV: {e}")


authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

name, authentication_status, username = authenticator.login()


if st.session_state["authentication_status"]:

    with st.sidebar:
        st.write(f"Bienvenue {name}")
        # Define the menu options
        options = ["Accueil \U0001F60A", "Les photos de mon chat \U0001F431"]

        # Create the option menu
        selection = option_menu("", options,
                    icons=['house', 'gear'], menu_icon="cast", default_index=0)
                
        # Le bouton de déconnexion
        authenticator.logout("Déconnexion", "sidebar")


    ## page d'accueil
    if selection == "Accueil \U0001F60A":
        st.markdown("# Bienvenue sur ma page :smile:")
        st.image("https://www.theatreinparis.com/uploads/images/article/clapping-header.jpg")

    ## page photos animaux
    
    elif selection == "Les photos de mon chat \U0001F431":
        st.markdown("# Bienvenue dans l'album de mon chat :cat:")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("https://cdn.pixabay.com/photo/2017/05/29/15/34/kitten-2354016_1280.jpg")

        with col2:
            st.image("https://images.pexels.com/photos/2071882/pexels-photo-2071882.jpeg?cs=srgb&dl=brown-tabby-cat-2071882.jpg&fm=jpg")

        with col3:
            st.image("https://www.wallpaperflare.com/static/260/510/512/muzzle-cat-whiskers-eyes-wallpaper.jpg")

    


elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')