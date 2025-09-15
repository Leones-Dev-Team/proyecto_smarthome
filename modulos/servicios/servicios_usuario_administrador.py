# servicio_usuario_administrador.py
from typing import Optional, Tuple
from datetime import datetime
from modulos.repositorios import repositorio_usuarios as ru
from modulos.repositorios import repositorio_hogares as rh


def registrar_usuario(
    nombre: str,
    contrasena: str,
    id_hogar: str,
    correo_electronico: str,
    telefono: str,
    edad: int
) -> Optional[dict]:
    """
    Registra un nuevo usuario administrador validando el hogar y los datos.
    """
    if not isinstance(nombre, str) or not nombre.strip():
        return None
    if not isinstance(contrasena, str) or not contrasena.strip():
        return None
    if not isinstance(id_hogar, str) or not id_hogar.strip():
        return None
    if not isinstance(correo_electronico, str) or not correo_electronico.strip():
        return None
    if not isinstance(telefono, str) or not telefono.strip():
        return None
    try:
        edad = int(edad)
        if edad < 0:
            return None
    except (ValueError, TypeError):
        return None

    nombre = nombre.lower()

    if ru.existe_usuario(nombre):
        return None

    if not rh.existe_hogar(id_hogar):
        return None

    ahora = datetime.now().isoformat()
    usuario = ru.crear_usuario(
        nombre=nombre,
        contrasena=contrasena,
        rol="administrador",
        id_hogar=id_hogar,
        edad=edad,
        mail=correo_electronico,
        telefono=telefono,
        tiempo_de_conexion=0,
        registro_actividad=[{
            "accion": "crear_usuario_administrador",
            "fecha": ahora
        }]
    )
    return usuario


def cambiar_rol(nombre: str, nuevo_rol: str) -> bool:
    """
    Cambia el rol de un usuario si existe y el rol es valido.
    """
    try:
        ru.actualizar_rol(nombre.lower(), nuevo_rol)
        return True
    except ValueError:
        return False


def listar_usuarios() -> dict:
    """
    Lista todos los usuarios registrados.
    """
    return ru.listar_usuarios()


def obtener_usuario(nombre: str) -> Optional[dict]:
    """
    Obtiene la informacion de un usuario por nombre.
    """
    return ru.obtener_usuario(nombre.lower())


def iniciar_sesion(nombre: str, contrasena: str) -> Tuple[Optional[dict], Optional[str]]:
    """
    Inicia sesion exclusivamente para usuarios con rol 'administrador'.
    Devuelve (usuario, rol) si es correcto; en caso contrario (None, None).
    """
    if not isinstance(nombre, str) or not nombre.strip():
        return (None, None)
    if not isinstance(contrasena, str) or not contrasena.strip():
        return (None, None)

    nombre_norm = nombre.strip().lower()
    usuario = ru.obtener_usuario(nombre_norm)
    if usuario and usuario.get("contrasena") == contrasena and usuario.get("rol") == "administrador":
        return (usuario, usuario.get("rol"))
    return (None, None)
