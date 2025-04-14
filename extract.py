import geopandas as gpd
import pandas as pd
import requests
import os

# URL du fichier GeoJSON
url = "https://www.data.gouv.fr/fr/datasets/r/ad4bb2f6-0f40-46d2-a636-8d2604532f74"
local_geojson = "bdnb_capvm.geojson"
output_csv = "bdnb_capvm.csv"

# Étape 1 : Télécharger le fichier GeoJSON
print("⬇ Téléchargement du fichier GeoJSON...")
with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open(local_geojson, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
print("✅ Téléchargement terminé.")

# Étape 2 : Lire le fichier GeoJSON avec GeoPandas
print("📖 Lecture du fichier GeoJSON...")
gdf = gpd.read_file(local_geojson)

# Étape 3 : Supprimer la colonne 'geometry' pour un CSV plus léger
df = gdf.drop(columns='geometry', errors='ignore')

# Étape 4 : Exporter en CSV
df.to_csv(output_csv, index=False)
print(f"✔ Fichier CSV exporté : {output_csv} ({len(df)} lignes)")

# Optionnel : supprimer le fichier GeoJSON temporaire
os.remove(local_geojson)
