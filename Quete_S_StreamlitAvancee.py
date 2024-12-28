import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import pandas as pd
# import seaborn as sns
# import plotly.express as px
# import matplotlib.pyplot as plt

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
                                                    'password': 'utilisateurMDP',
                                                    'email': 'utilisateur@gmail.com',
                                                    'failed_login_attemps': 0, # Sera géré automatiquement
                                                    'logged_in': False, # Sera géré automatiquement
                                                    'role': 'utilisateur'},
                                      'root': {'name': 'root',
                                              'password': 'rootMDP',
                                              'email': 'admin@gmail.com',
                                              'failed_login_attemps': 0, # Sera géré automatiquement
                                              'logged_in': False, # Sera géré automatiquement
                                              'role': 'administrateur'}}}

authenticator = Authenticate(lesDonneesDesComptes, # Les données des comptes
                             "cookie name", # Le nom du cookie, un str quelconque
                             "cookie key", # La clé du cookie, un str quelconque
                             30,) # Le nombre de jours avant que le cookie expire 
                          
authenticator.login()

# Gérer la bare des taches (sidebar):
def accueil():
  with st.sidebar:
    authenticator.logout("Déconnexion")
    st.title("Bienvenu root")
    selection = option_menu(menu_title=None, options = ["Accueil", "Les photos de mes chats"])
      # On indique au programme quoi faire en fonction du choix


  if selection == "Accueil":
    st.title("Bienvenue sur ma page")
    st.image("https://www.code-couleur.com/images/listing/rose-lilas.jpg")

  elif selection == "Les photos de mes chats":
      st.write("Bienvenue dans l'album de mes chats")
      col1, col2, col3 = st.columns(3)

      with col1:
        st.header("Chat noir")
        st.image("https://www.code-couleur.com/images/listing/listing2020/chat-noir.jpg")

      with col2:
        st.header("Chat blanc")
        st.image("https://www.code-couleur.com/images/listing/listing2020/chat-blanc.jpg")

      with col3:
        st.header("Chat bicol")
        st.image("https://www.code-couleur.com/images/listing/listing2020/chat-siamois.jpg")


if st.session_state["authentication_status"]:
  accueil()
elif st.session_state["authentication_status"] is False:
    st.error("L'identifiant ou le mot de passe est/sont incorrecte(s)")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')



## Reste à traiter le point du fichier csv avec les colonnes : 
# name, password, email, failed_login_attemps, logged_in et role
#  lien pour les chats : https://www.code-couleur.com/chats/
