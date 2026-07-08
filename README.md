# TFM-Visualizador

Aplicación desarrollada como complemento del Trabajo Fin de Máster **"Análisis computacional de la desigualdad socioeconómica en España por regiones"**, realizado en la Universidad de Granada.

La herramienta permite visualizar de forma interactiva distintos indicadores socioeconómicos de las comunidades autónomas españolas mediante mapas coropléticos generados con **GeoPandas** y **Folium**. Además, incorpora la representación de las tipologías territoriales obtenidas mediante un análisis de **K-Means**, permitiendo explorar los principales patrones territoriales identificados durante la investigación.

---

## Características

- Interfaz gráfica desarrollada con **Tkinter**.
- Mapas interactivos en formato HTML.
- Visualización de indicadores socioeconómicos oficiales.
- Selección de distintas paletas de colores.
- Visualización de las tipologías territoriales obtenidas mediante K-Means.
- Tooltips con información resumida por comunidad autónoma.
- Exportación automática del mapa a `mapas/index.html`.

---
## Datos

Los datos utilizados en la aplicación proceden de **fuentes estadísticas oficiales**, principalmente del **Instituto Nacional de Estadística (INE)**.

El conjunto de datos integra indicadores demográficos, económicos y sociales correspondientes, siempre que ha sido posible, al año **2025** o, cuando no existía información disponible para dicho año, a la última actualización oficial publicada.

---

## Documentación

Además de la aplicación, este repositorio incluye la documentación empleada para desarrollar el análisis del Trabajo Fin de Máster.

La carpeta [`docs/`](docs/) contiene los **notebooks de Jupyter** utilizados durante todo el proceso de análisis y preparación de datos:

- Análisis por comunidades autónomas.
- Análisis complementario por provincias.
- Comparación territorial entre España e Italia.

Cada notebook recoge el flujo completo de trabajo, desde la preparación de los datos hasta los análisis estadísticos y la generación de los resultados utilizados en la memoria.

---

## Estructura del proyecto

``` text
TFM-Visualizador/
│
├── app.py
├── config.py
├── datos.py
├── mapas.py
├── requirements.txt
├── LICENSE
├── README.md
│
├── datos/
│   └── ccaa.csv
│
├── docs/
│   ├── README.md
│   └── notebooks/
│       ├── OperacionesCCAA.ipynb
│       ├── OperacionesProvincias.ipynb
│       └── OperacionesItalia.ipynb
│
└── mapas/
    └── index.html
```

---

## Requisitos

-   Python 3.10 o superior

---

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

---

## Ejecución

Con el entorno virtual activado:

``` bash
python app.py
```

Seleccione el indicador y la escala de colores deseados y pulse
**Generar mapa**. El mapa se abrirá automáticamente en el navegador
predeterminado.

---

## Tecnologías utilizadas

-   Python
-   Pandas
-   GeoPandas
-   Folium
-   Tkinter

---

## Autor

*Enrique Camacho García*

Máster Universitario en Ingeniería Informática  
Universidad de Granada
