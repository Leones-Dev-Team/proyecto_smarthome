# Módulo de servicios para la gestión de dispositivos.
# Este archivo contiene las funciones que permiten agregar, listar y buscar dispositivos.
import uuid
from typing import Dict, Any

# Simulación de una base de datos en memoria para los dispositivos.
_dispositivos = {}

def agregar_dispositivo(dispositivos: Dict[str, dict], nuevo: dict) -> bool:
    """
    Agrega un nuevo dispositivo al diccionario si el ID no existe.

    Args:
        dispositivos (dict): Diccionario de dispositivos.
        nuevo (dict): Diccionario con los datos del nuevo dispositivo.

    Returns:
        bool: True si se agregó, False si el ID ya existe.
    """
    id_disp = nuevo.get('id_dispositivo')
    if not id_disp or id_disp in dispositivos:
        return False
    # Generar un UUID si el ID no es válido (opcional)
    # id_disp = id_disp or str(uuid.uuid4())
    dispositivos[id_disp] = nuevo
    _dispositivos[id_disp] = nuevo
    return True

def listar_dispositivos() -> Dict[str, dict]:
    """
    Devuelve todos los dispositivos registrados.

    Returns:
        dict: Diccionario de dispositivos, clave es el id_dispositivo.
    """
    return dict(_dispositivos)

def eliminar_dispositivo(dispositivos: Dict[str, dict], id_dispositivo: str) -> bool:
    """
    Elimina un dispositivo por su ID.

    Args:
        dispositivos (dict): Diccionario de dispositivos.
        id_dispositivo (str): ID del dispositivo a eliminar.

    Returns:
        bool: True si se eliminó, False si no se encontró.
    """
    if id_dispositivo in dispositivos:
        dispositivos.pop(id_dispositivo)
        _dispositivos.pop(id_dispositivo, None)
        return True
    return False

def buscar_dispositivo(dispositivos: Dict[str, dict], id_dispositivo: str) -> dict:
    """
    Busca un dispositivo por su ID.

    Args:
        dispositivos (dict): Diccionario de dispositivos.
        id_dispositivo (str): ID del dispositivo a buscar.

    Returns:
        dict or None: Diccionario del dispositivo si existe, None si no.
    """
    return dispositivos.get(id_dispositivo)

def actualizar_estado_dispositivo(id_dispositivo: str, nuevo_estado: str) -> bool:
    """
    Actualiza el estado de un dispositivo.

    Args:
        id_dispositivo (str): ID del dispositivo.
        nuevo_estado (str): 'encendido' o 'apagado'.

    Returns:
        bool: True si se actualizó, False si no existe o estado inválido.
    """
    dispositivo = _dispositivos.get(id_dispositivo)
    if dispositivo and nuevo_estado in ['encendido', 'apagado']:
        dispositivo['estado'] = nuevo_estado
        return True
    return False

def activar_modo_ahorro(dispositivos: Dict[str, dict]) -> int:
    """
    Apaga todos los dispositivos no esenciales.

    Args:
        dispositivos (dict): Diccionario de dispositivos.

    Returns:
        int: Número de dispositivos apagados.
    """
    apagados = 0
    for d in dispositivos.values():
        if not d.get('es_esencial', False) and d.get('estado') == 'encendido':
            d['estado'] = 'apagado'
            apagados += 1
    return apagados