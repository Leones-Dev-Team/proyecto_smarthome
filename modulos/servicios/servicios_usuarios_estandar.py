# Servicios para gestión de usuarios estándar
from typing import Dict, Tuple, Optional
from modulos.servicios.servicios_hogares import existe_hogar

# Simulación de base de datos en memoria
_usuarios_estandar: Dict[str, dict] = {}

def registrar_usuario(nombre: str, contraseña: str, id_hogar: str, edad: int, mail: str, telefono: str) -> bool:
    """
    Registra un nuevo usuario estándar si el nombre no existe y el hogar es válido.

    Args:
        nombre (str): Nombre de usuario.
        contraseña (str): Contraseña del usuario.
        id_hogar (str): ID del hogar asociado.
        edad (int): Edad del usuario.
        mail (str): Correo electrónico.
        telefono (str): Teléfono.

    Returns:
        bool: True si se registró, False si ya existe o el hogar no existe.
    """
    nombre = nombre.lower()
    if nombre in _usuarios_estandar or not existe_hogar(id_hogar):
        return False
    _usuarios_estandar[nombre] = {
        "nombre": nombre,
        "contraseña": contraseña,
        "id_hogar": id_hogar,
        "edad": edad,
        "mail": mail,
        "telefono": telefono,
        "rol": "estandar"
    }
    return True

def iniciar_sesion(nombre: str, contraseña: str) -> Tuple[Optional[dict], Optional[str]]:
    """
    Verifica usuario y contraseña. Devuelve usuario y rol si es correcto.

    Args:
        nombre (str): Nombre de usuario.
        contraseña (str): Contraseña.

    Returns:
        tuple: (usuario dict, rol str) si es correcto, (None, None) si no.
    """
    if nombre is not None:
        nombre = nombre.lower()
    usuario = _usuarios_estandar.get(nombre)
    if usuario and usuario["contraseña"] == contraseña:
        return usuario, usuario["rol"]
    return None, None

def obtener_info_usuario(nombre: str) -> Optional[dict]:
    """
    Devuelve la información del usuario estándar.

    Args:
        nombre (str): Nombre de usuario.

    Returns:
        dict: Datos del usuario, o None si no existe.
    """
    nombre = nombre.lower()
    return _usuarios_estandar.get(nombre)

def listar_usuarios_estandar() -> Dict[str, dict]:
    """
    Devuelve todos los usuarios estándar registrados.

    Returns:
        dict: Diccionario de usuarios, clave es el nombre de usuario.
    """
    return dict(_usuarios_estandar)