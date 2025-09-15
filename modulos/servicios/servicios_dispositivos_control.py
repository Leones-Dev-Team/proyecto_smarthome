# servicios_dispositivos_control.py
from typing import Optional, Tuple
from datetime import datetime
from modulos.repositorios import repositorio_dispositivos_control as rdc
from modulos.repositorios import repositorio_hogares as rh
import uuid


def crear_dispositivo_control(
    id_hogar: str,
    nombre: str,
    tipo: str,
    estado: str
) -> Tuple[dict, int]:
    """
    Crea un nuevo dispositivo de control asociado a un hogar.
    Estado debe ser 'encendido' o 'apagado'.
    """
    if not all(isinstance(v, str) and v.strip() for v in (id_hogar, nombre, tipo, estado)):
        return {"error": "Datos invalido o vacio."}, 400

    if estado not in ("encendido", "apagado"):
        return {"error": "Estado invalido. Use 'encendido' o 'apagado'."}, 400

    if not rh.existe_hogar(id_hogar):
        return {"error": f"El hogar con ID '{id_hogar}' no existe."}, 404

    try:
        ahora = datetime.now().isoformat()
        nuevo_control = rdc.crear_control(
            id_control=str(uuid.uuid4()),
            id_usuario_conectado=None,
            hora_de_conexion=ahora if estado == "encendido" else None,
            dispositivos_activos=[] if estado == "encendido" else [],
            dispositivos_apagados=[] if estado == "apagado" else [],
            dispositivos_en_ahorro_de_energia=[],
            registro_actividad=[{
                "accion": f"crear_control_{estado}",
                "fecha": ahora
            }],
            otros={
                "id_hogar": id_hogar,
                "nombre": nombre,
                "tipo": tipo,
                "estado": estado
            }
        )
        return nuevo_control, 201
    except ValueError as e:
        return {"error": str(e)}, 400


def listar_dispositivos_control() -> dict:
    """Retorna todos los dispositivos de control."""
    return rdc.listar_controles()


def buscar_dispositivo_control_por_id(id_control: str) -> Optional[dict]:
    """Busca un dispositivo de control por su ID."""
    return rdc.obtener_control(id_control)


def obtener_estado_dispositivo(id_control: str) -> Tuple[object, int]:
    """Obtiene el estado de un dispositivo de control."""
    control = rdc.obtener_control(id_control)
    if control:
        return control.get("otros", {}).get("estado"), 200
    return {"error": "Dispositivo no encontrado."}, 404


def actualizar_estado_dispositivo(id_control: str, nuevo_estado: str, origen: Optional[str] = None) -> Tuple[dict, int]:
    """
    Actualiza el estado de un dispositivo de control, ajusta hora_de_conexion
    y registra la acción en el historial.
    """
    if not isinstance(id_control, str) or not id_control.strip():
        return {"error": "ID de control invalido."}, 400
    if nuevo_estado not in ("encendido", "apagado"):
        return {"error": "Estado invalido. Use 'encendido' o 'apagado'."}, 400

    control = rdc.obtener_control(id_control)
    if not control:
        return {"error": "Dispositivo no encontrado."}, 404

    control["otros"]["estado"] = nuevo_estado
    control["hora_de_conexion"] = datetime.now(
    ).isoformat() if nuevo_estado == "encendido" else None
    if "registro_actividad" in control and isinstance(control["registro_actividad"], list):
        control["registro_actividad"].append({
            "accion": origen if origen else f"cambiar_estado_{nuevo_estado}",
            "fecha": datetime.now().isoformat()
        })
    return control, 200


def eliminar_dispositivo_control(id_control: str) -> bool:
    """Elimina un dispositivo de control por su ID."""
    return rdc.eliminar_control(id_control)
