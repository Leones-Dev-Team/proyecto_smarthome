# repositorio_usuarios.py

# Base de datos en memoria (puede cambiarse a BD real en el futuro)
_usuarios = {
    "admin": {"contraseña": "adminpass", "rol": "administrador"}
}

# Roles válidos en el sistema
ROLES_VALIDOS = {"administrador", "estandar"}


def obtener_usuario(nombre):
    """
    Devuelve el diccionario de datos de un usuario por su nombre,
    o None si no existe.
    """
    return _usuarios.get(nombre)


def existe_usuario(nombre):
    """
    Devuelve True si el usuario existe, False si no.
    """
    return nombre in _usuarios


def crear_usuario(nombre, contraseña, rol="estandar"):
    """
    Crea un nuevo usuario con el rol indicado.
    """
    _usuarios[nombre] = {"contraseña": contraseña, "rol": rol}


def actualizar_rol(nombre, nuevo_rol):
    """
    Cambia el rol de un usuario existente.
    """
    _usuarios[nombre]["rol"] = nuevo_rol


def listar_usuarios():
    """
    Devuelve una copia del diccionario de usuarios.
    Esto evita que se modifique el original desde fuera.
    """
    return dict(_usuarios)
