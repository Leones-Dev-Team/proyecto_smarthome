# modulos/servicios/servicios_dispositivos_control.py
import uuid
from modulos.servicios.servicios_hogares import buscar_hogar_por_id

# Simulación de una base de datos en memoria
_dispositivos_control = []


def crear_dispositivo_control(id_hogar: str, nombre: str, tipo: str, estado: bool):
    """
    Crea un nuevo dispositivo de control asociado a un hogar.

    Args:
        id_hogar (str): El ID del hogar al que pertenece el dispositivo de control.
        nombre (str): El nombre del dispositivo.
        tipo (str): El tipo de dispositivo (ej. "sensor", "termostato", "hub").
        estado (bool): El estado inicial del dispositivo (True para encendido, False para apagado).

    Returns:
        tuple: Un diccionario con los datos del nuevo dispositivo y un código de estado (201).
            En caso de error, retorna un diccionario con un mensaje de error y un
            código de estado (400 o 404).
    """
    # Validaciones de tipo de dato
    if not isinstance(id_hogar, str) or not isinstance(nombre, str) or not isinstance(tipo, str) or not isinstance(estado, bool):
        return {"error": "Tipos de datos incorrectos."}, 400

    # Validar que el id_hogar exista usando el servicio correspondiente
    hogar_existente = buscar_hogar_por_id(id_hogar)
    if not hogar_existente:
        return {"error": "El 'id_hogar' proporcionado no existe."}, 404

    nuevo_dispositivo = {
        "id_dispositivo_control": str(uuid.uuid4()),
        "id_hogar": id_hogar,
        "nombre": nombre,
        "tipo": tipo,
        "estado": estado
    }
    _dispositivos_control.append(nuevo_dispositivo)
    return nuevo_dispositivo, 201


def listar_dispositivos_control():
    """
    Retorna una lista de todos los dispositivos de control.

    Returns:
        list: Una lista de diccionarios, donde cada diccionario representa un dispositivo.
    """
    return list(_dispositivos_control)  # Devuelve una copia para evitar modificaciones externas


def buscar_dispositivo_control_por_id(id_dispositivo: str):
    """
    Busca un dispositivo de control por su ID único.

    Args:
        id_dispositivo (str): El ID del dispositivo de control a buscar.

    Returns:
        dict or None: El diccionario del dispositivo si se encuentra, de lo contrario None.
    """
    for dispositivo in _dispositivos_control:
        if dispositivo.get("id_dispositivo_control") == id_dispositivo:
            return dispositivo
    return None


def obtener_estado_dispositivo(id_dispositivo: str):
    """
    Obtiene el estado (encendido/apagado) de un dispositivo de control por su ID.

    Args:
        id_dispositivo (str): El ID del dispositivo de control.

    Returns:
        tuple: Estado del dispositivo (True/False) y código de estado (200/404).
    """
    dispositivo = buscar_dispositivo_control_por_id(id_dispositivo)
    if dispositivo:
        return dispositivo["estado"], 200
    return {"error": "Dispositivo no encontrado."}, 404


def actualizar_estado_dispositivo(id_dispositivo: str, nuevo_estado: bool):
    """
    Actualiza el estado de un dispositivo de control.

    Args:
        id_dispositivo (str): El ID del dispositivo de control.
        nuevo_estado (bool): El nuevo estado (True/False).

    Returns:
        tuple: Diccionario actualizado y código de estado (200/404).
    """
    dispositivo = buscar_dispositivo_control_por_id(id_dispositivo)
    if dispositivo:
        dispositivo["estado"] = nuevo_estado
        return dispositivo, 200
    return {"error": "Dispositivo no encontrado."}, 404
