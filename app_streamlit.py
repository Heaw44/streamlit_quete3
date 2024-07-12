import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu


## identifiants
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
                'name': 'nicolas',
                'password': 'Worn434Raft',
                'email': 'rob.nicolas44@gmail.com',
                'failed_login_attemps': 0, # Sera géré automatiquement
                'logged_in': False, # Sera géré automatiquement
                'role': 'utilisateur'
        },
        'root': {
                'name': 'root',
                'password': 'rootMDP',
                'email': 'admin@gmail.com',
                'failed_login_attemps': 0, # Sera géré automatiquement
                'logged_in': False, # Sera géré automatiquement
                'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

name, authentication_status, username = authenticator.login()


if st.session_state["authentication_status"]:

    with st.sidebar:
        selection = option_menu("Accueil", ["Accueil", 'Les photos de mon chat'], 
            icons=['house', 'gear'], menu_icon="cast", default_index=1)
        
        # Le bouton de déconnexion
        authenticator.logout("Déconnexion", "sidebar")


    ## page d'accueil
    if selection == "Accueil":
        st.title("Bienvenue sur ma page")
        st.image("https://www.theatreinparis.com/uploads/images/article/clapping-header.jpg")

    ## page photos animaux
    elif selection == "Les photos de mon chat":
        st.title(f"Bienvenue dans l'album de mon chat {name}")
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