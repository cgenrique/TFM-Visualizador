import os
import webbrowser

import folium
from branca.element import Template, MacroElement

COLORES_CLUSTER = {
    0: "#66c2a5",   # verde
    1: "#8da0cb",   # azul
    2: "#bdbdbd",   # gris
    3: "#ffd92f"    # amarillo
}

def añadir_controles_exportacion(m, titulo):

    nombre_archivo = (
        titulo.replace(" ", "_")
        .replace("á", "a")
        .replace("é", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ú", "u")
        .replace("Á", "A")
        .replace("É", "E")
        .replace("Í", "I")
        .replace("Ó", "O")
        .replace("Ú", "U")
        .replace("ñ", "n")
        .replace("Ñ", "N")
        .replace("(", "")
        .replace(")", "")
        .replace("%", "porcentaje")
        .replace("€", "euros")
    )

    template = f"""
    {{% macro html(this, kwargs) %}}

    <div id="exportPanel" style="
        position: fixed;
        top: 80px;
        right: 10px;
        z-index: 9999;
        background: white;
        padding: 8px;
        border: 2px solid grey;
        border-radius: 6px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        font-family: Arial, sans-serif;
        font-size: 13px;
    ">

        <button onclick="descargarHTML()" style="width:150px;">
            Exportar mapa (.html)
        </button>

    </div>

    <script>

    function descargarHTML() {{

        // Ocultar panel de exportación
        const panel = document.getElementById("exportPanel");
        if (panel) panel.style.display = "none";

        // Ocultar controles y leyendas
        const controles = document.querySelectorAll(".legend, .leaflet-control");

        controles.forEach(el => {{
            if (el.id !== "exportPanel") {{
                el.dataset.display = el.style.display;
                el.style.display = "none";
            }}
        }});

        const contenido = document.documentElement.outerHTML;

        // Restaurar controles
        controles.forEach(el => {{
            if (el.id !== "exportPanel") {{
                el.style.display = el.dataset.display || "";
            }}
        }});

        if (panel) panel.style.display = "block";

        const blob = new Blob([contenido], {{ type: "text/html" }});

        const enlace = document.createElement("a");

        enlace.href = URL.createObjectURL(blob);
        enlace.download = "Mapa_{nombre_archivo}_2025.html";

        enlace.click();

        URL.revokeObjectURL(enlace.href);
    }}

    </script>

    {{% endmacro %}}
    """

    macro = MacroElement()
    macro._template = Template(template)

    m.get_root().add_child(macro)

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

    if variable == "Cluster":

        def estilo(feature):

            cluster = feature["properties"]["Cluster"]

            return {
                "fillColor": COLORES_CLUSTER.get(cluster, "#ffffff"),
                "color": "black",
                "weight": 1,
                "fillOpacity": 0.8
            }

        folium.GeoJson(
            gdf,
            style_function=estilo
        ).add_to(m)

        añadir_leyenda_clusters(m)

    else:

        if variable == "Densidad_Poblacion":

            folium.Choropleth(
                geo_data=gdf,
                data=gdf,
                columns=["name", variable],
                key_on="feature.properties.name",
                fill_color=colores,
                bins=[0, 50, 100, 200, 400, 1000, 8000],
                fill_opacity=0.8,
                line_opacity=0.8,
                legend_name=f"{titulo} (2025)"
            ).add_to(m)

        else:

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

    añadir_controles_exportacion(m, titulo)
    
    m.save(ruta)

    webbrowser.open_new_tab(
        "file://" + os.path.realpath(ruta)
    )

def añadir_leyenda_clusters(m):

    template = """
    {% macro html(this, kwargs) %}

    <div style="
        position: fixed;
        bottom: 40px;
        left: 40px;
        width: 190px;
        background-color: white;
        border:2px solid grey;
        border-radius:8px;
        z-index:9999;
        font-size:14px;
        padding:12px;
        box-shadow:2px 2px 8px rgba(0,0,0,0.3);
    ">

    <b>Tipologías territoriales</b>
    <hr style="margin:6px 0;">

    <div><span style="color:#66c2a5;">&#9632;</span> <b>Cluster 0</b><br>
    <small>Alta renta y empleo · Población envejecida · Baja densidad</small></div>

    <div style="margin-top:8px;">
    <span style="color:#8da0cb;">&#9632;</span> <b>Cluster 1</b><br>
    <small>Mayor desempleo y pobreza · Renta baja · Crecimiento moderado</small></div>

    <div style="margin-top:8px;">
    <span style="color:#bdbdbd;">&#9632;</span> <b>Cluster 2</b><br>
    <small>Ceuta y Melilla · Muy alta densidad · Desempleo elevado</small></div>

    <div style="margin-top:8px;">
    <span style="color:#ffd92f;">&#9632;</span> <b>Cluster 3</b><br>
    <small>Alta renta y PIB · Bajo desempleo · Grandes áreas urbanas</small></div>

    </div>

    {% endmacro %}
    """

    macro = MacroElement()
    macro._template = Template(template)

    m.get_root().add_child(macro)

def mapa_vacio():

    m = folium.Map(
        location=[40.2,-3.5],
        zoom_start=6,
        tiles="CartoDB positron"
    )

    m.save("mapas/index.html")