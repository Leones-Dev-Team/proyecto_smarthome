# repositorio_usuarios.py
import uuid
from typing import Optional
from modulos.repositorios import repositorio_hogares as rh
from modulos.datos.datos_usuarios import usuarios as usuarios_iniciales

ROLES_VALIDOS = ("administrador", "estandar")
_usuarios: dict[str, dict] = {}

# --- Inicializacion de datos por defecto ---
# Crear hogares de los usuarios iniciales si no existen
for usr in usuarios_iniciales:
    id_hogar = usr.get("id_hogar")
    if id_hogar and not rh.existe_hogar(id_hogar):
        rh._hogares[id_hogar] = {
            "direccion": None,
            "propietario": usr["usuario"],
            "dispositivos": [],
            "usuarios": [usr["usuario"]],
            "tiempo_de_conexion": 0,
            "registro_actividad": []
        }
    _usuarios[usr["usuario"]] = {
        "id_usuario": str(uuid.uuid4()),
        "nombre": usr["usuario"],
        "contrasena": usr["contrasena"],
        "rol": usr["rol"],
        "id_hogar": usr.get("id_hogar"),
        "edad": usr.get("edad"),
        "mail": usr.get("mail"),
        "telefono": usr.get("telefono"),
        "tiempo_de_conexion": usr.get("tiempo_de_conexion", 0),
        "registro_actividad": usr.get("registro_actividad", [])
    }


def existe_usuario(nombre: str) -> bool:
    """Devuelve True si el usuario existe, False si no."""
    return nombre in _usuarios


def crear_usuario(
    nombre: str,
    contrasena: str,
    rol: str = "estandar",
    id_hogar: Optional[str] = None,
    edad: Optional[int] = None,
    mail: Optional[str] = None,
    telefono: Optional[str] = None,
    tiempo_de_conexion: int = 0,
    registro_actividad: Optional[list] = None
) -> dict:
    """
    Crea un nuevo usuario con los campos indicados, validando datos y claves foraneas.
    """
    if not isinstance(nombre, str) or not nombre.strip():
        raise ValueError("El nombre del usuario no puede estar vacio.")

    if not isinstance(contrasena, str) or not contrasena.strip():
        raise ValueError("La contrasena no puede estar vacia.")

    if existe_usuario(nombre):
        raise ValueError(f"El usuario '{nombre}' ya existe.")

    if rol not in ROLES_VALIDOS:
        raise ValueError(
            f"El rol '{rol}' no es valido. Roles permitidos: {ROLES_VALIDOS}")

    if id_hogar is not None:
        if not isinstance(id_hogar, str) or not id_hogar.strip():
            raise ValueError("El ID de hogar debe ser una cadena no vacia.")
        if not rh.existe_hogar(id_hogar):
            raise ValueError(f"El hogar con ID '{id_hogar}' no existe.")

    if edad is not None:
        try:
            edad = int(edad)
            if edad < 0:
                raise ValueError
        except (ValueError, TypeError):
            raise ValueError("La edad debe ser un numero entero no negativo.")

    if tiempo_de_conexion is not None:
        try:
            tiempo_de_conexion = int(tiempo_de_conexion)
            if tiempo_de_conexion < 0:
                raise ValueError
        except (ValueError, TypeError):
            raise ValueError(
                "El tiempo de conexion debe ser un numero entero no negativo.")

    if registro_actividad is None or not isinstance(registro_actividad, list):
        registro_actividad = []

    usuario = {
        "id_usuario": str(uuid.uuid4()),
        "nombre": nombre,
        "contrasena": contrasena,
        "rol": rol,
        "id_hogar": id_hogar,
        "edad": edad,
        "mail": mail,
        "telefono": telefono,
        "tiempo_de_conexion": tiempo_de_conexion,
        "registro_actividad": registro_actividad
    }
    _usuarios[nombre] = usuario
    return usuario


def obtener_usuario(nombre: str) -> Optional[dict]:
    """Devuelve el diccionario de datos de un usuario por su nombre, o None si no existe."""
    return _usuarios.get(nombre)


def actualizar_rol(nombre: str, nuevo_rol: str) -> None:
    """Cambia el rol de un usuario existente."""
    if not existe_usuario(nombre):
        raise ValueError(f"El usuario '{nombre}' no existe.")

    if nuevo_rol not in ROLES_VALIDOS:
        raise ValueError(
            f"El rol '{nuevo_rol}' no es valido. Roles permitidos: {ROLES_VALIDOS}")

    _usuarios[nombre]["rol"] = nuevo_rol


def listar_usuarios() -> dict[str, dict]:
    """Devuelve una copia del diccionario de usuarios."""
    return dict(_usuarios)


def eliminar_usuario(nombre: str) -> bool:
    """Elimina un usuario por su nombre."""
    if nombre in _usuarios:
        del _usuarios[nombre]
        return True
    return False
