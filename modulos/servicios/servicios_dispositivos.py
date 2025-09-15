# servicios_dispositivos.py
from typing import Optional
from datetime import datetime
from modulos.repositorios import repositorio_dispositivos as rd


def agregar_dispositivo(
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
) -> bool:
    """Agrega un nuevo dispositivo validando datos y evitando duplicados."""
    if not isinstance(id_dispositivo, str) or not id_dispositivo.strip():
        return False
    if estado not in ("encendido", "apagado"):
        return False

    if consumo_energetico is not None:
        try:
            consumo_energetico = float(consumo_energetico)
        except (ValueError, TypeError):
            return False

    try:
        rd.crear_dispositivo(
            id_dispositivo=id_dispositivo,
            id_usuario_conectado=id_usuario_conectado,
            ubicacion=ubicacion,
            hora_de_conexion=hora_de_conexion,
            nombre_dispositivo=nombre_dispositivo,
            tipo_dispositivo=tipo_dispositivo,
            marca_dispositivo=marca_dispositivo,
            consumo_energetico=consumo_energetico if consumo_energetico is not None else 0.0,
            estado=estado,
            es_esencial=es_esencial
        )
        return True
    except ValueError:
        return False


def listar_dispositivos() -> dict:
    """Devuelve todos los dispositivos registrados."""
    return rd.listar_dispositivos()


def eliminar_dispositivo(id_dispositivo: str) -> bool:
    """Elimina un dispositivo por su ID."""
    return rd.eliminar_dispositivo(id_dispositivo)


def buscar_dispositivo(id_dispositivo: str) -> Optional[dict]:
    """Busca un dispositivo por su ID."""
    return rd.obtener_dispositivo(id_dispositivo)


def actualizar_estado_dispositivo(id_dispositivo: str, nuevo_estado: str, origen: Optional[str] = None) -> bool:
    """
    Actualiza el estado de un dispositivo, ajusta hora_de_conexion
    y registra la accion en el historial.
    El parametro 'origen' permite especificar el motivo de la accion.
    """
    if nuevo_estado not in ("encendido", "apagado"):
        return False
    dispositivo = rd.obtener_dispositivo(id_dispositivo)
    if not dispositivo:
        return False

    dispositivo["estado"] = nuevo_estado
    dispositivo["hora_de_conexion"] = datetime.now(
    ).isoformat() if nuevo_estado == "encendido" else None

    if "registro_actividad" in dispositivo and isinstance(dispositivo["registro_actividad"], list):
        dispositivo["registro_actividad"].append({
            "accion": origen if origen else f"cambiar_estado_{nuevo_estado}",
            "fecha": datetime.now().isoformat()
        })
    return True
