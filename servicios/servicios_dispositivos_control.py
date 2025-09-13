# modulos/servicios/servicios_dispositivos_control.py
import uuid
from .servicios_hogares import buscar_hogar_por_id

# Simulación de una base de datos o almacenamiento en memoria.
_dispositivos_control = []

def crear_dispositivo_control(id_hogar: str, nombre: str, tipo: str, estado: bool):
    """
    Crea un nuevo dispositivo de control asociado a un hogar.

    Args:
        id_hogar (str): El ID del hogar al que pertenece el dispositivo de control.
        nombre (str): El nombre del dispositivo.
        tipo (str): El tipo de dispositivo (ej. "altavoz", "termostato").
        estado (bool): El estado inicial del dispositivo (ej. True para encendido).

    Returns:
        tuple: Un diccionario con los datos del nuevo dispositivo y un código de estado (201).
               En caso de error, retorna un diccionario con un mensaje de error y un
               código de estado (400 o 404).
    """
    # 1. Validaciones de tipo de dato
    if not isinstance(id_hogar, str) or not isinstance(nombre, str) or not isinstance(tipo, str) or not isinstance(estado, bool):
        return {"error": "Tipos de datos incorrectos."}, 400
    
    # 2. Validar que el id_hogar exista
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
    print(f"Dispositivo de control creado: {nuevo_dispositivo}")
    return nuevo_dispositivo, 201

def listar_dispositivos_control():
    """
    Retorna una lista de todos los dispositivos de control.

    Returns:
        list: Una lista de diccionarios, donde cada diccionario representa un dispositivo.
    """
    return _dispositivos_control

def buscar_dispositivo_control_por_id(id_dispositivo: str):
    for dispositivo in _dispositivos_control:
        if dispositivo.get("id_dispositivo_control") == id_dispositivo:
            return dispositivo
    return None