# servicio_usuarios.py

from modulos.repositorio import repositorio_usuarios as repo


def registrar_usuario(nombre, contraseña):
    """
    Crea un nuevo usuario estandar si no existe.
    Devuelve True si se registro, False si ya existia.
    """
    nombre = nombre.lower()
    if repo.existe_usuario(nombre):
        return False
    repo.crear_usuario(nombre, contraseña, rol="estandar")
    return True


def iniciar_sesion(nombre, contraseña):
    """
    Verifica credenciales. Devuelve (usuario, rol) si es correcto,
    o (None, None) si falla.
    """
    nombre = nombre.lower()
    usuario = repo.obtener_usuario(nombre)
    if usuario and usuario["contraseña"] == contraseña:
        return nombre, usuario["rol"]
    return None, None


def cambiar_rol(nombre, nuevo_rol):
    """
    Cambia el rol de un usuario existente.
    Devuelve True si se cambio, False si no existe o el rol es invalido.
    """
    nombre = nombre.lower()
    if not repo.existe_usuario(nombre):
        return False
    if nuevo_rol not in repo.ROLES_VALIDOS:
        return False
    repo.actualizar_rol(nombre, nuevo_rol)
    return True


def obtener_info_usuario(nombre):
    """
    Devuelve un diccionario con los datos del usuario (sin contraseña),
    o None si no existe.
    """
    nombre = nombre.lower()
    usuario = repo.obtener_usuario(nombre)
    if usuario:
        return {"nombre": nombre, "rol": usuario["rol"]}
    return None
