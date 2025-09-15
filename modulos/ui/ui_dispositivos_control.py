# ui_dispositivos_control.py
from modulos.ui.ui_utils import obtener_input, pausar_pantalla
from modulos.servicios import servicios_dispositivos_control as sdc


def agregar_dispositivo_control():
    """Agrega un nuevo dispositivo de control usando el servicio."""
    print("\n--- Agregar Dispositivo de Control ---")

    id_hogar = (obtener_input("ID del hogar al que pertenece: ") or "").strip()
    nombre = (obtener_input("Nombre del dispositivo: ") or "").strip()
    tipo = (obtener_input(
        "Tipo de dispositivo (ej: sensor, termostato, hub): ") or "").strip()
    estado = (obtener_input("Estado (encendido/apagado): ")
              or "").lower().strip()

    resultado, status = sdc.crear_dispositivo_control(
        id_hogar=id_hogar,
        nombre=nombre,
        tipo=tipo,
        estado=estado
    )

    if status == 201:
        print(f"Dispositivo agregado con éxito: {resultado}")
    else:
        print(
            f"Error al agregar dispositivo: {resultado.get('error', 'desconocido')}")
    pausar_pantalla()


def listar_dispositivos_control():
    """Lista todos los dispositivos de control registrados."""
    print("\n--- Lista de Dispositivos de Control ---")
    controles = sdc.listar_dispositivos_control()
    if not controles:
        print("No hay dispositivos de control registrados.")
    else:
        for c in controles.values():
            otros = c.get("otros", {})
            print(
                f"ID: {c.get('id_control', '-')}, "
                f"Hogar: {otros.get('id_hogar', '-')}, "
                f"Nombre: {otros.get('nombre', '-')}, "
                f"Tipo: {otros.get('tipo', '-')}, "
                f"Estado: {otros.get('estado', '-')}"
            )
    pausar_pantalla()


def buscar_dispositivo_control():
    """Busca un dispositivo de control por ID."""
    id_dispositivo = (obtener_input(
        "ID del dispositivo a buscar: ") or "").strip()
    dispositivo = sdc.buscar_dispositivo_control_por_id(id_dispositivo)
    if dispositivo:
        otros = dispositivo.get("otros", {})
        print(
            f"ID: {dispositivo.get('id_control', '-')}, "
            f"Hogar: {otros.get('id_hogar', '-')}, "
            f"Nombre: {otros.get('nombre', '-')}, "
            f"Tipo: {otros.get('tipo', '-')}, "
            f"Estado: {otros.get('estado', '-')}"
        )
    else:
        print("No se encontró el dispositivo.")
    pausar_pantalla()


def menu_principal_dispositivos_control():
    """Menú principal para gestionar dispositivos de control."""
    while True:
        print("""
        --- Menú de Dispositivos de Control ---
        1. Agregar dispositivo de control
        2. Listar dispositivos de control
        3. Buscar dispositivo de control
        0. Volver al menú anterior
        """)
        opcion = (obtener_input("Elige una opción: ") or "").strip()

        if opcion == "1":
            agregar_dispositivo_control()
        elif opcion == "2":
            listar_dispositivos_control()
        elif opcion == "3":
            buscar_dispositivo_control()
        elif opcion == "0":
            print("Saliendo del menú de dispositivos de control.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            pausar_pantalla()
