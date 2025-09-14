# ui_dispositivos_control.py

import re
from modulos.ui.ui_utils import obtener_input, pausar_pantalla
from repositorio_dispositivos_control import (
    crear_control,
    obtener_control,
    listar_controles,
    existe_control
)


def validar_hora(hora):
    """Valida que la hora esté en formato HH:MM."""
    return re.match(r'^([01]\d|2[0-3]):([0-5]\d)$', hora) is not None


def agregar_dispositivo_control():
    """Agrega un nuevo dispositivo de control usando el repositorio."""
    print("\n--- Agregar Dispositivo de Control ---")
    nuevo_id = obtener_input("ID del dispositivo de control: ")

    # Validar ID único
    if existe_control(nuevo_id):
        print("Ya existe un dispositivo con ese ID. Intenta con otro.")
        pausar_pantalla()
        return

    tipo = obtener_input("Tipo de dispositivo de control (ej: sensor, termostato, hub): ")
    ubicacion = obtener_input("Ubicación: ")
    id_usuario_conectado = obtener_input("ID del usuario conectado: ")
    hora_conexion = obtener_input("Hora de conexión (HH:MM): ")

    # Validaciones básicas
    if not nuevo_id or not tipo or not ubicacion or not id_usuario_conectado or not hora_conexion:
        print("Todos los campos son obligatorios.")
        pausar_pantalla()
        return

    if not validar_hora(hora_conexion):
        print("Formato de hora inválido. Debe ser HH:MM (ej: 14:30).")
        pausar_pantalla()
        return

    # Crear registro en el repositorio
    crear_control(
        id_control=nuevo_id,
        id_usuario_conectado=id_usuario_conectado,
        hora_de_conexion=hora_conexion
    )

    print("Dispositivo de control agregado con éxito.")
    pausar_pantalla()


def listar_dispositivos_control():
    """Lista todos los dispositivos de control registrados en el repositorio."""
    print("\n--- Lista de Dispositivos de Control ---")
    controles = listar_controles()
    if not controles:
        print("No hay dispositivos de control registrados.")
    else:
        for id_control, datos in controles.items():
            print(
                f"ID: {id_control}, Usuario: {datos['id_usuario_conectado']}, "
                f"Hora conexión: {datos['hora_de_conexion']}, "
                f"Activos: {len(datos['dispositivos_activos'])}, "
                f"Apagados: {len(datos['dispositivos_apagados'])}, "
                f"Ahorro energía: {len(datos['dispositivos_en_ahorro_de_energia'])}"
            )
    pausar_pantalla()


def menu_principal_dispositivos_control():
    """Menú principal para gestionar dispositivos de control."""
    while True:
        print("""
        --- Menú de Dispositivos de Control ---
        1. Agregar dispositivo de control
        2. Listar dispositivos de control
        0. Volver al menú anterior
        """)
        opcion = obtener_input("Elige una opción: ")

        if opcion == "1":
            agregar_dispositivo_control()
        elif opcion == "2":
            listar_dispositivos_control()
        elif opcion == "0":
            print("Saliendo del menú de dispositivos de control.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            pausar_pantalla()
