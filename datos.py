import pandas as pd
import geopandas as gpd

from config import EQUIVALENCIAS


def cargar_datos():

    df = pd.read_csv("datos/ccaa.csv")

    df["Nombre_GEO"] = (
        df["Nombre_Completo"]
        .replace(EQUIVALENCIAS)
    )

    url = "https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/spain-communities.geojson"

    gdf = gpd.read_file(url)

    gdf = gdf.merge(
        df,
        left_on="name",
        right_on="Nombre_GEO",
        how="left"
    )

    return gdf[[
        "name",
        "geometry",
        "Poblacion",
        "PIB_Per_Capita",
        "Paro_medio",
        "Tasa_Riesgo_Pobreza",
        "Porcentaje_Mayores_65",
        "Renta_Media_Hogar",
        "Esperanza_Vida",
        "Tasa_Dependencia",
        "Densidad_Poblacion",
        "Cluster"
    ]].copy()