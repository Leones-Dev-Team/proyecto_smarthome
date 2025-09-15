# repositorio_dispositivos_control.py
from typing import Optional

# Base de datos en memoria para dispositivos de control
_dispositivos_control: dict[str, dict] = {}


def crear_control(
    id_control: str,
    id_usuario_conectado: Optional[str] = None,
    hora_de_conexion: Optional[str] = None,
    dispositivos_activos: Optional[list] = None,
    dispositivos_apagados: Optional[list] = None,
    dispositivos_en_ahorro_de_energia: Optional[list] = None,
    registro_actividad: Optional[list] = None,
    otros: Optional[dict] = None
) -> dict:
    """Agrega un nuevo registro de control de dispositivos."""
    if not isinstance(id_control, str) or not id_control.strip():
        raise ValueError("El ID de control no puede estar vacio.")

    if id_control in _dispositivos_control:
        raise ValueError(f"Ya existe un control con ID '{id_control}'.")

    _dispositivos_control[id_control] = {
        "id_control": id_control,
        "id_usuario_conectado": id_usuario_conectado,
        "hora_de_conexion": hora_de_conexion,
        "dispositivos_activos": dispositivos_activos if isinstance(dispositivos_activos, list) else [],
        "dispositivos_apagados": dispositivos_apagados if isinstance(dispositivos_apagados, list) else [],
        "dispositivos_en_ahorro_de_energia": dispositivos_en_ahorro_de_energia if isinstance(dispositivos_en_ahorro_de_energia, list) else [],
        "registro_actividad": registro_actividad if isinstance(registro_actividad, list) else [],
        "otros": otros if isinstance(otros, dict) else {}
    }
    return _dispositivos_control[id_control]


def obtener_control(id_control: str) -> Optional[dict]:
    return _dispositivos_control.get(id_control)


def listar_controles() -> dict[str, dict]:
    return dict(_dispositivos_control)


def existe_control(id_control: str) -> bool:
    return id_control in _dispositivos_control


def eliminar_control(id_control: str) -> bool:
    if id_control in _dispositivos_control:
        del _dispositivos_control[id_control]
        return True
    return False
