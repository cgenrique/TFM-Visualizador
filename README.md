# TFM-Visualizador

Aplicación desarrollada como complemento del Trabajo Fin de Máster
**"Análisis computacional de la desigualdad socioeconómica en España por
regiones"**.

Permite visualizar de forma interactiva distintos indicadores
socioeconómicos de las comunidades autónomas españolas mediante mapas
coropléticos generados con **GeoPandas** y **Folium**.

## Características

-   Interfaz gráfica desarrollada con Tkinter.
-   Mapas interactivos en HTML.
-   Selección de distintos indicadores socioeconómicos.
-   Selección de paletas de colores.
-   Tooltips con información resumida por comunidad autónoma.
-   Exportación automática del mapa a `mapas/index.html`.

## Estructura del proyecto

``` text
TFM-Visualizador/
│
├── app.py
├── config.py
├── datos.py
├── mapas.py
├── requirements.txt
├── README.md
│
├── datos/
│   └── ccaa.csv
│
└── mapas/
    └── index.html
```

## Requisitos

-   Python 3.10 o superior

## Instalación

Clonar el repositorio:

``` bash
git clone <URL_DEL_REPOSITORIO>
cd TFM-Visualizador
```

Crear un entorno virtual:

### Windows

``` bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

Instalar las dependencias:

``` bash
pip install -r requirements.txt
```

## Ejecución

Con el entorno virtual activado:

``` bash
python app.py
```

Seleccione el indicador y la escala de colores deseados y pulse
**Generar mapa**. El mapa se abrirá automáticamente en el navegador
predeterminado.

## Tecnologías utilizadas

-   Python
-   Pandas
-   GeoPandas
-   Folium
-   Tkinter

## Autor

Enrique Camacho García

Universidad de Granada Trabajo Fin de Máster
