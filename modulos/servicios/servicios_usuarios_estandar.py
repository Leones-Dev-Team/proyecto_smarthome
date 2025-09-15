# servicios_usuarios_estandar.py
from typing import Optional, Tuple
from datetime import datetime
from modulos.repositorios import repositorio_usuarios as ru
from modulos.repositorios import repositorio_hogares as rh


def registrar_usuario(
    nombre: str,
    contrasena: str,
    id_hogar: str,
    edad: int,
    mail: Optional[str] = None,
    telefono: Optional[str] = None
) -> bool:
    """
    Registra un nuevo usuario estandar si el nombre no existe y el hogar es valido.
    """
    if not isinstance(nombre, str) or not nombre.strip():
        return False
    if not isinstance(contrasena, str) or not contrasena.strip():
        return False
    if not isinstance(id_hogar, str) or not id_hogar.strip():
        return False
    try:
        edad = int(edad)
        if edad < 0:
            return False
    except (ValueError, TypeError):
        return False
    if mail is not None and (not isinstance(mail, str) or not mail.strip()):
        return False
    if telefono is not None and (not isinstance(telefono, str) or not telefono.strip()):
        return False

    nombre = nombre.lower()

    if ru.existe_usuario(nombre):
        return False

    if not rh.existe_hogar(id_hogar):
        return False

    ahora = datetime.now().isoformat()
    ru.crear_usuario(
        nombre=nombre,
        contrasena=contrasena,
        rol="estandar",
        id_hogar=id_hogar,
        edad=edad,
        mail=mail,
        telefono=telefono,
        tiempo_de_conexion=0,
        registro_actividad=[{
            "accion": "crear_usuario_estandar",
            "fecha": ahora
        }]
    )
    return True


def iniciar_sesion(nombre: str, contrasena: str) -> Tuple[Optional[dict], Optional[str]]:
    """
    Verifica usuario y contrasena. Devuelve usuario y rol si es correcto.
    """
    if nombre is not None:
        nombre = nombre.lower()

    usuario = ru.obtener_usuario(nombre)
    if usuario and usuario.get("contrasena") == contrasena:
        return usuario, usuario.get("rol")
    return None, None


def obtener_info_usuario(nombre: str) -> Optional[dict]:
    """
    Devuelve la informacion del usuario estandar.
    """
    nombre = nombre.lower()
    return ru.obtener_usuario(nombre)


def listar_usuarios_estandar() -> dict:
    """
    Devuelve todos los usuarios estandar registrados.
    """
    return {
        nombre: datos
        for nombre, datos in ru.listar_usuarios().items()
        if datos.get("rol") == "estandar"
    }
