# modulos/servicios/servicios_hogares.py
import uuid
from typing import Dict

# Simulación de una base de datos en memoria (diccionario)
_hogares = {}


def crear_hogar(id_hogar: str, ubicacion: str, tipo_de_vivienda: str) -> tuple:
    """
    Crea un nuevo hogar y lo agrega al diccionario de hogares.

    Args:
        id_hogar (str): El ID único del hogar.
        ubicacion (str): La ubicación física del hogar.
        tipo_de_vivienda (str): El tipo de vivienda (casa, departamento, etc.).

    Returns:
        tuple: Un diccionario con los datos del nuevo hogar y un código de estado (201).
            En caso de error, retorna un diccionario con un mensaje de error y un
            código de estado (400 o 409).
    """
    if not isinstance(id_hogar, str) or not isinstance(ubicacion, str) or not isinstance(tipo_de_vivienda, str):
        return {"error": "Tipos de datos incorrectos."}, 400

    if id_hogar in _hogares:
        return {"error": "Ya existe un hogar con ese ID."}, 409

    nuevo_hogar = {
        "id_hogar": id_hogar,
        "ubicacion": ubicacion,
        "tipo_de_vivienda": tipo_de_vivienda,
        "tiempo_de_conexion": 0  # Valor inicial, puede actualizarse luego
    }
    _hogares[id_hogar] = nuevo_hogar
    return nuevo_hogar, 201


def existe_hogar(id_hogar: str) -> bool:
    """
    Verifica si existe un hogar con el ID dado.

    Args:
        id_hogar (str): El ID del hogar a verificar.

    Returns:
        bool: True si existe, False si no.
    """
    return id_hogar in _hogares


def listar_hogares() -> Dict[str, dict]:
    """
    Retorna un diccionario de todos los hogares registrados.

    Returns:
        dict: Diccionario de hogares, clave es el id_hogar.
    """
    return dict(_hogares)


def buscar_hogar_por_id(id_hogar: str):
    """
    Busca un hogar por su ID único.

    Args:
        id_hogar (str): El ID del hogar a buscar.

    Returns:
        dict or None: El diccionario del hogar si se encuentra, de lo contrario None.
    """
    return _hogares.get(id_hogar)
