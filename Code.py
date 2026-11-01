import streamlit as st

st.write("Emotion, premier test sur streamlit")


st.title("Mon appli")

# Lien dans la page principale
st.markdown("Source des données : [data.gouv.fr](https://www.data.gouv.fr)")

# Bouton-lien bien visible
st.link_button("Ouvrir le site", "https://www.data.gouv.fr")

# Lien dans la barre latérale
st.sidebar.markdown("### Liens utiles")
st.sidebar.markdown("- [Wikipédia](https://fr.wikipedia.org)")
st.sidebar.link_button("GitHub du projet", "https://github.com/ton-compte/ton-depot")
