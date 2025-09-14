# repositorio_usuarios.py

# Base de datos en memoria (puede cambiarse a BD real en el futuro)

from typing import Optional

_usuarios = {
    "admin": {
        "contraseña": "adminpass",
        "rol": "administrador",
        "id_hogar": None,
        "edad": None,
        "mail": None,
        "telefono": None,
        "tiempo_de_conexion": 0,
        "registro_actividad": []
    }
}

# Roles válidos en el sistema
ROLES_VALIDOS = {"administrador", "estandar"}


def obtener_usuario(nombre: str) -> dict | None:
    """
    Devuelve el diccionario de datos de un usuario por su nombre,
    o None si no existe.

    Args:
        nombre (str): El nombre del usuario.

    Returns:
        dict | None: El diccionario de datos del usuario o None si no se encuentra.
    """
    return _usuarios.get(nombre)


def existe_usuario(nombre: str) -> bool:
    """
    Devuelve True si el usuario existe, False si no.

    Args:
        nombre (str): El nombre del usuario a verificar.

    Returns:
        bool: True si el usuario existe, False en caso contrario.
    """
    return nombre in _usuarios


def crear_usuario(
    nombre: str,
    contraseña: str,
    rol: str = "estandar",
    id_hogar=None,
    edad=None,
    mail=None,
    telefono=None,
    tiempo_de_conexion: int = 0,
    registro_actividad: Optional[list] = None
) -> None:
    """
    Crea un nuevo usuario con los campos indicados.

    Args:
        nombre (str): El nombre único del usuario.
        contraseña (str): La contraseña del usuario.
        rol (str): El rol del usuario, debe ser "administrador" o "estandar".
        ... (otros campos)
    """
    if not isinstance(nombre, str) or not nombre.strip():
        raise ValueError("El nombre del usuario no puede estar vacío.")

    if existe_usuario(nombre):
        raise ValueError(f"El usuario '{nombre}' ya existe.")

    if rol not in ROLES_VALIDOS:
        raise ValueError(
            f"El rol '{rol}' no es válido. Los roles permitidos son: {ROLES_VALIDOS}")

    if registro_actividad is None:
        registro_actividad = []

    _usuarios[nombre] = {
        "contraseña": contraseña,
        "rol": rol,
        "id_hogar": id_hogar,
        "edad": edad,
        "mail": mail,
        "telefono": telefono,
        "tiempo_de_conexion": tiempo_de_conexion,
        "registro_actividad": registro_actividad
    }


def actualizar_rol(nombre: str, nuevo_rol: str) -> None:
    """
    Cambia el rol de un usuario existente.

    Args:
        nombre (str): El nombre del usuario.
        nuevo_rol (str): El nuevo rol, debe ser "administrador" o "estandar".
    """
    if not existe_usuario(nombre):
        raise ValueError(f"El usuario '{nombre}' no existe.")

    if nuevo_rol not in ROLES_VALIDOS:
        raise ValueError(
            f"El rol '{nuevo_rol}' no es válido. Los roles permitidos son: {ROLES_VALIDOS}")

    _usuarios[nombre]["rol"] = nuevo_rol


def listar_usuarios() -> dict:
    """
    Devuelve una copia del diccionario de usuarios.
    Esto evita que se modifique el original desde fuera.
    """
    return _usuarios.copy()
