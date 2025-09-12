# ui_hogares.py

from modulos.ui.ui_utils import obtener_input, pausar_pantalla

# Nota: esta lista se eliminará cuando Jonny cree repositorio_hogares.
hogares = []


def agregar_hogar():
    """Agrega un nuevo hogar a la lista de hogares."""
    print("\n--- Agregar Hogar ---")
    nuevo_id = obtener_input("ID del hogar: ")

    # Validar que el ID no esté duplicado
    for h in hogares:
        if h["id_hogar"] == nuevo_id:
            print("Ya existe un hogar con ese ID. Intenta con otro.")
            pausar_pantalla()
            return

    ubicacion = obtener_input("Ubicación: ")
    tipo_vivienda = obtener_input("Tipo de vivienda (casa/departamento/etc.): ")

    if not nuevo_id or not ubicacion or not tipo_vivienda:
        print("Todos los campos son obligatorios.")
        pausar_pantalla()
        return

    nuevo = {
        "id_hogar": nuevo_id,
        "ubicacion": ubicacion,
        "tipo_de_vivienda": tipo_vivienda,
    }
    hogares.append(nuevo)
    print("Hogar agregado con éxito.")
    pausar_pantalla()


def listar_hogares():
    """Muestra todos los hogares registrados."""
    print("\n--- Lista de Hogares ---")
    if not hogares:
        print("No hay hogares registrados.")
    else:
        for h in hogares:
            print(f"ID: {h['id_hogar']}, Ubicación: {h['ubicacion']}, Tipo: {h['tipo_de_vivienda']}")
    pausar_pantalla()


def menu_principal_hogares():
    """Menú principal para gestionar hogares."""
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
            print("Saliendo del menú de hogares.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
