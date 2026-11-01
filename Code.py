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

# À adapter avec les vrais noms de champs (voir ?limit=3 dans le navigateur)
CHAMP_COMMUNE = "nom_commune"
CHAMP_ANNEE = "annee"

@st.cache_data(ttl=3600)
def chercher(commune: str) -> pd.DataFrame:
    commune = commune.replace('"', "")  # évite de casser la requête
    r = requests.get(
        f"{BASE}/{DATASET}/records",
        params={
            "where": f'{CHAMP_COMMUNE}="{commune}"',
            "order_by": CHAMP_ANNEE,
            "limit": 100,
        },
        timeout=30,
    )
    r.raise_for_status()
    return pd.DataFrame(r.json()["results"])

st.title("Consommation énergétique de ma commune")

with st.form("recherche"):
    nom = st.text_input("Nom de votre commune")
    valide = st.form_submit_button("Voir les données")

if valide:
    if not nom.strip():
        st.warning("Merci de saisir un nom de commune.")
    else:
        try:
            df = chercher(nom.strip())
        except requests.RequestException:
            st.error("Impossible de joindre le service de données. Réessayez plus tard.")
        else:
            if df.empty:
                st.info("Aucune donnée trouvée. Vérifiez l'orthographe (accents, tirets).")
            else:
                st.subheader(nom.strip())

commune = st.text_input("Commune", "Rennes")
if commune:
    df = chercher=(commune)
    st.dataframe(df)
