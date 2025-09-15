# ui_hogares.py
from modulos.ui.ui_utils import obtener_input, pausar_pantalla
from modulos.servicios import servicios_hogares as sh


def agregar_hogar():
    """Agrega un nuevo hogar validando duplicados y tipos de datos."""
    print("\n--- Agregar Hogar ---")
    nuevo_id = (obtener_input("ID del hogar: ") or "").strip()
    if not nuevo_id:
        print("El ID del hogar no puede estar vacío.")
        pausar_pantalla()
        return

    if sh.existe_hogar(nuevo_id):
        print("Ya existe un hogar con ese ID. Intenta con otro.")
        pausar_pantalla()
        return

    ubicacion = (obtener_input("Ubicación: ") or "").strip()
    if not ubicacion:
        print("La ubicación no puede estar vacía.")
        pausar_pantalla()
        return

    tipo_de_vivienda = (obtener_input(
        "Tipo de vivienda (casa/departamento/etc.): ") or "").strip()
    if not tipo_de_vivienda:
        print("El tipo de vivienda no puede estar vacío.")
        pausar_pantalla()
        return

    resultado, status = sh.crear_hogar(
        id_hogar=nuevo_id,
        ubicacion=ubicacion,
        tipo_de_vivienda=tipo_de_vivienda
    )

    if status == 201:
        print("Hogar agregado con éxito.")
    else:
        print(
            f"Error al agregar hogar: {resultado.get('error', 'desconocido')}")
    pausar_pantalla()


def listar_hogares():
    """Lista todos los hogares registrados usando el servicio."""
    print("\n--- Lista de Hogares ---")
    hogares = sh.listar_hogares()

    if not hogares:
        print("No hay hogares registrados.")
    else:
        for id_hogar, h in hogares.items():
            print(
                f"ID: {id_hogar}, "
                f"Ubicación: {h.get('ubicacion', '-')}, "
                f"Tipo: {h.get('tipo_de_vivienda', '-')}, "
                f"Tiempo conexión: {h.get('tiempo_de_conexion', 0)} min, "
                f"Registro actividad: {h.get('registro_actividad', [])}"
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
        opcion = (obtener_input("Elige una opción: ") or "").strip()

        if opcion == "1":
            agregar_hogar()
        elif opcion == "2":
            listar_hogares()
        elif opcion == "0":
            print("Saliendo del menú de hogares...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            pausar_pantalla()
