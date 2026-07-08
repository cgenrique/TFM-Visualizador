import tkinter as tk
from tkinter import ttk

from config import VARIABLES, PALETAS
from datos import cargar_datos
from mapas import crear_mapa, mapa_vacio

# =====================================================
# CARGAR DATOS
# =====================================================

gdf = cargar_datos()

# =====================================================
# FUNCIONES
# =====================================================

def generar():

    nombre = combo.get()

    variable, titulo = VARIABLES[nombre]

    colores = PALETAS[
        combo_colores.get()
    ]

    crear_mapa(
        gdf,
        variable,
        titulo,
        colores
    )


def cerrar():

    mapa_vacio()

    ventana.destroy()

def actualizar_colores(event=None):

    if combo.get() == "Tipologías territoriales (K-Means)":

        combo_colores.configure(state="normal")
        combo_colores["values"] = ["Multicolor (Clusters)"]
        combo_colores.current(0)
        combo_colores.configure(state="disabled")

    else:

        combo_colores.configure(state="readonly")

        combo_colores["values"] = [
            "Azules",
            "Verdes",
            "Rojos",
            "Naranjas",
            "Morados",
            "Marrones",
            "Azul verdoso",
            "Rosa",
            "Grises"
        ]

        combo_colores.current(0)
    if combo.get() == "Tipologías territoriales (K-Means)":

        combo_colores["values"] = ["Multicolor (Clusters)"]
        combo_colores.current(0)

    else:

        combo_colores["values"] = [
            "Azules",
            "Verdes",
            "Rojos",
            "Naranjas",
            "Morados",
            "Marrones",
            "Azul verdoso",
            "Rosa",
            "Grises"
        ]

        combo_colores.current(0)


# =====================================================
# INTERFAZ
# =====================================================

ventana = tk.Tk()

ventana.title("Visualizador TFM")

ventana.resizable(False, False)

titulo = tk.Label(
    ventana,
    text="Visualizador de indicadores socioeconómicos",
    font=("Arial", 13, "bold")
)

titulo.pack(padx=20, pady=(15, 5))

subtitulo = tk.Label(
    ventana,
    text="España · Datos 2025",
    font=("Arial", 9)
)

subtitulo.pack(padx=20, pady=(0, 15))

tk.Label(
    ventana,
    text="Seleccione un indicador:"
).pack(padx=20)

combo = ttk.Combobox(
    ventana,
    values=list(VARIABLES.keys()),
    width=35,
    state="readonly"
)

combo.current(0)

combo.pack(padx=20, pady=(5, 15))

combo.bind(
    "<<ComboboxSelected>>",
    actualizar_colores
)

tk.Label(
    ventana,
    text="Escala de colores:"
).pack()

combo_colores = ttk.Combobox(
    ventana,
    values=list(PALETAS.keys()),
    width=35,
    state="readonly"
)

combo_colores.current(0)

combo_colores.pack(padx=20, pady=(5, 20))

boton = tk.Button(
    ventana,
    text="Generar mapa",
    command=generar,
    width=20,
    height=2
)

boton.pack(padx=20, pady=(0, 8))

boton_salir = tk.Button(
    ventana,
    text="Salir",
    command=cerrar,
    width=20
)

boton_salir.pack(padx=20, pady=(0, 15))

ventana.protocol(
    "WM_DELETE_WINDOW",
    cerrar
)

actualizar_colores()
ventana.mainloop()