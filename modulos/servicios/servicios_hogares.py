# modulos/servicios/servicios_hogares.py
import uuid

# Simulación de una base de datos o almacenamiento en memoria.
_hogares = []

def crear_hogar(nombre_hogar: str, direccion: str):
    """
    Crea un nuevo hogar y lo agrega a la lista de hogares.

    Args:
        nombre_hogar (str): El nombre del hogar.
        direccion (str): La dirección física del hogar.

    Returns:
        tuple: Un diccionario con los datos del nuevo hogar y un código de estado (201).
               En caso de error, retorna un diccionario con un mensaje de error y un
               código de estado (400).
    """
    if not isinstance(nombre_hogar, str) or not isinstance(direccion, str):
        return {"error": "Tipos de datos incorrectos para nombre_hogar o direccion."}, 400
    
    nuevo_hogar = {
        "id_hogar": str(uuid.uuid4()),
        "nombre": nombre_hogar,
        "direccion": direccion
    }
    _hogares.append(nuevo_hogar)
    print(f"Hogar creado: {nuevo_hogar}")
    return nuevo_hogar, 201

def listar_hogares():
    """
    Retorna una lista de todos los hogares registrados.

    Returns:
        list: Una lista de diccionarios, donde cada diccionario representa un hogar.
    """
    return _hogares

def buscar_hogar_por_id(id_hogar: str):
    """
    Busca un hogar por su ID único.

    Args:
        id_hogar (str): El ID del hogar a buscar.

    Returns:
        dict or None: El diccionario del hogar si se encuentra, de lo contrario None.
    """
    for hogar in _hogares:
        if hogar.get("id_hogar") == id_hogar:
            return hogar
    return None
