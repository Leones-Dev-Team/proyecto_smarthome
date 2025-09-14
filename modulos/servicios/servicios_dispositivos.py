# Módulo de servicios para la gestión de dispositivos.
# Este archivo contiene las funciones que permiten agregar, listar y buscar dispositivos.
import uuid
from .servicios_usuarios import buscar_usuario_por_id
from .servicios_historial import agregar_evento_historial

# Simulación de una base de datos en memoria para los dispositivos.
_dispositivos = []


def agregar_dispositivo(id_usuario_conectado: str, nombre: str, tipo: str, estado: bool):
    """
    Agrega un nuevo dispositivo y lo asocia a un usuario existente.

    Args:
        id_usuario_conectado (str): El ID del usuario al que se asocia el dispositivo.
        nombre (str): El nombre del dispositivo.
        tipo (str): El tipo de dispositivo (ej. "luz", "puerta").
        estado (bool): El estado inicial del dispositivo (ej. True para encendido).

    Returns:
        tuple: Un diccionario con los datos del nuevo dispositivo y un código de estado (201).
            En caso de error, retorna un diccionario con un mensaje de error y un
            código de estado (400 o 404).
    """
    # 1. Validaciones de tipo de dato
    if not isinstance(id_usuario_conectado, str) or not isinstance(nombre, str) or not isinstance(tipo, str) or not isinstance(estado, bool):
        return {"error": "Tipos de datos incorrectos."}, 400

    # 2. Validar que el id_usuario_conectado exista
    usuario_existente = buscar_usuario_por_id(id_usuario_conectado)
    if not usuario_existente:
        return {"error": "El 'id_usuario_conectado' no existe."}, 404

    # Generar ID único para el dispositivo
    nuevo_dispositivo = {
        "id_dispositivo": str(uuid.uuid4()),
        "id_usuario_conectado": id_usuario_conectado,
        "nombre": nombre,
        "tipo": tipo,
        "estado": estado
    }

    _dispositivos.append(nuevo_dispositivo)
    print(f"Dispositivo agregado: {nuevo_dispositivo}")

    # Registrar el evento en el historial.
    agregar_evento_historial(
        id_usuario_conectado,
        "dispositivo",
        f"Se agregó un nuevo dispositivo: {nombre} ({tipo})."
    )

    return nuevo_dispositivo, 201


def listar_dispositivos():
    """
    Retorna una lista de todos los dispositivos registrados.

    Returns:
        list: Una lista de diccionarios, donde cada diccionario representa un dispositivo.
    """
    return _dispositivos


def buscar_dispositivo_por_id(id_dispositivo: str):
    """
    Busca un dispositivo por su ID único.

    Args:
        id_dispositivo (str): El ID del dispositivo a buscar.

    Returns:
        dict or None: El diccionario del dispositivo si se encuentra, de lo contrario None.
    """
    for dispositivo in _dispositivos:
        if dispositivo.get("id_dispositivo") == id_dispositivo:
            return dispositivo
    return None
