# ui_hogares.py

from modulos.ui.ui_utils import obtener_input, pausar_pantalla
from modulos.repositorios import repositorio_hogares


def agregar_hogar():
    """Agrega un nuevo hogar (validando duplicados con el repositorio)."""
    print("\n--- Agregar Hogar ---")
    nuevo_id = obtener_input("ID del hogar: ")

    if repositorio_hogares.existe_hogar(nuevo_id):
        print("Ya existe un hogar con ese ID. Intenta con otro.")
        pausar_pantalla()
        return

    ubicacion = obtener_input("Ubicación: ")
    tipo_vivienda = obtener_input("Tipo de vivienda (casa/departamento/etc.): ")

    repositorio_hogares.crear_hogar(
        id_hogar=nuevo_id,
        ubicacion=ubicacion,
        tipo_de_vivienda=tipo_vivienda
    )

    print("Hogar agregado con éxito.")
    pausar_pantalla()


def listar_hogares():
    """Lista todos los hogares registrados desde el repositorio."""
    print("\n--- Lista de Hogares ---")
    hogares = repositorio_hogares.listar_hogares()

    if not hogares:
        print("No hay hogares registrados.")
    else:
        for id_hogar, h in hogares.items():
            print(
                f"ID: {id_hogar}, "
                f"Ubicación: {h['ubicacion']}, "
                f"Tipo: {h['tipo_de_vivienda']}, "
                f"Tiempo conexión: {h['tiempo_de_conexion']} min"
            )
    pausar_pantalla()


def menu_principal_hogares():
    """Menú principal de hogares."""
    while True:
        print("""
        --- Menú de Hogares ---
        1. Agregar hogar
        2. Listar hogares
        0. Volver al menú global
        """)
        opcion = obtener_input("Elige una opción: ")

        if opcion == "1":
            agregar_hogar()
        elif opcion == "2":
            listar_hogares()
        elif opcion == "0":
            print("Saliendo del menú de
