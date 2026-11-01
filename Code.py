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

import requests
import pandas as pd
import streamlit as st

BASE = "https://opendata.agenceore.fr/api/explore/v2.1/catalog/datasets"
DATASET = "consommation-annuelle-d-electricite-et-gaz-par-commune"

@st.cache_data(ttl=3600)
def conso_commune(commune: str) -> pd.DataFrame:
    r = requests.get(
        f"{BASE}/{DATASET}/records",
        params={
            "where": f'nom_commune="{commune}"',   # adapte au nom exact de la colonne
            "limit": 100,
            "order_by": "annee",
        },
        timeout=30,
    )
    r.raise_for_status()
    return pd.DataFrame(r.json()["results"])

commune = st.text_input("Commune", "Rennes")
if commune:
    df = conso_commune(commune)
    st.dataframe(df)
