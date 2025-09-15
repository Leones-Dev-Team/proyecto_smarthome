# repositorio_dispositivos.py
from typing import Optional
from modulos.datos.datos_dispositivos import dispositivos as dispositivos_iniciales

# Base de datos en memoria para dispositivos
_dispositivos: dict[str, dict] = {}

# --- Inicializacion de datos por defecto ---
for disp in dispositivos_iniciales:
    _dispositivos[disp["id_dispositivo"]] = disp
# --- Fin inicializacion ---


def crear_dispositivo(
    id_dispositivo: str,
    id_usuario_conectado: Optional[str] = None,
    ubicacion: Optional[str] = None,
    hora_de_conexion: Optional[str] = None,
    nombre_dispositivo: Optional[str] = None,
    tipo_dispositivo: Optional[str] = None,
    marca_dispositivo: Optional[str] = None,
    consumo_energetico: Optional[float] = None,
    estado: str = "apagado",
    es_esencial: bool = False
) -> dict:
    """Crea un nuevo dispositivo validando datos y evitando duplicados."""
    if not isinstance(id_dispositivo, str) or not id_dispositivo.strip():
        raise ValueError("El ID del dispositivo no puede estar vacio.")

    if id_dispositivo in _dispositivos:
        raise ValueError(
            f"Ya existe un dispositivo con ID '{id_dispositivo}'.")

    if estado not in ("encendido", "apagado"):
        raise ValueError("El estado debe ser 'encendido' o 'apagado'.")

    if consumo_energetico is not None:
        try:
            consumo_energetico = float(consumo_energetico)
        except (ValueError, TypeError):
            raise ValueError("El consumo energetico debe ser un numero.")

    _dispositivos[id_dispositivo] = {
        "id_dispositivo": id_dispositivo,
        "id_usuario_conectado": id_usuario_conectado,
        "ubicacion": ubicacion,
        "hora_de_conexion": hora_de_conexion,
        "nombre_dispositivo": nombre_dispositivo,
        "tipo_dispositivo": tipo_dispositivo,
        "marca_dispositivo": marca_dispositivo,
        "consumo_energetico": consumo_energetico if consumo_energetico is not None else 0.0,
        "estado": estado,
        "es_esencial": bool(es_esencial),
        "registro_actividad": []
    }
    return _dispositivos[id_dispositivo]


def obtener_dispositivo(id_dispositivo: str) -> Optional[dict]:
    return _dispositivos.get(id_dispositivo)


def listar_dispositivos() -> dict[str, dict]:
    return dict(_dispositivos)


def existe_dispositivo(id_dispositivo: str) -> bool:
    return id_dispositivo in _dispositivos


def eliminar_dispositivo(id_dispositivo: str) -> bool:
    if id_dispositivo in _dispositivos:
        del _dispositivos[id_dispositivo]
        return True
    return False
