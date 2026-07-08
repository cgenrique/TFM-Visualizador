import os
import webbrowser

import folium

def crear_mapa(
    gdf,
    variable,
    titulo,
    colores
):

    m = folium.Map(
        location=[40.2,-3.5],
        zoom_start=6,
        tiles="CartoDB positron"
    )

    folium.Choropleth(
        geo_data=gdf,
        data=gdf,
        columns=["name", variable],
        key_on="feature.properties.name",
        fill_color=colores,
        fill_opacity=0.8,
        line_opacity=0.8,
        legend_name=f"{titulo} (2025)"
    ).add_to(m)

    folium.GeoJson(
        gdf,
        tooltip=folium.GeoJsonTooltip(
            fields=[
                "name",
                "Poblacion",
                variable
            ],
            aliases=[
                "Comunidad",
                "Población (2025)",
                f"{titulo} (2025)"
            ],
            localize=True,
            sticky=False
        )
    ).add_to(m)

    os.makedirs("mapas", exist_ok=True)

    ruta = "mapas/index.html"

    m.save(ruta)

    webbrowser.open_new_tab(
        "file://" + os.path.realpath(ruta)
    )


def mapa_vacio():

    m = folium.Map(
        location=[40.2,-3.5],
        zoom_start=6,
        tiles="CartoDB positron"
    )

    m.save("mapas/index.html")