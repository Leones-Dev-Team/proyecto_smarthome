# servicios_hogares.py
from typing import Tuple, Optional
from datetime import datetime
from modulos.repositorios import repositorio_hogares as rh


def crear_hogar(id_hogar: str, ubicacion: str, tipo_de_vivienda: str) -> Tuple[dict, int]:
    """
    Crea un nuevo hogar validando datos y evitando duplicados.
    Devuelve (resultado, status_code).
    """
    if not all(isinstance(v, str) and v.strip() for v in (id_hogar, ubicacion, tipo_de_vivienda)):
        return {"error": "Datos invalidos o vacios."}, 400

    if rh.existe_hogar(id_hogar):
        return {"error": "Ya existe un hogar con ese ID."}, 409

    try:
        ahora = datetime.now().isoformat()
        nuevo_hogar = rh.crear_hogar(
            id_hogar=id_hogar,
            ubicacion=ubicacion,
            tipo_de_vivienda=tipo_de_vivienda,
            tiempo_de_conexion=0,
            registro_actividad=[{
                "accion": "crear_hogar",
                "fecha": ahora
            }]
        )
        return nuevo_hogar, 201
    except ValueError as e:
        return {"error": str(e)}, 400


def existe_hogar(id_hogar: str) -> bool:
    """Verifica si existe un hogar con el ID dado."""
    return rh.existe_hogar(id_hogar)


def listar_hogares() -> dict:
    """Retorna un diccionario de todos los hogares registrados."""
    return rh.listar_hogares()


def buscar_hogar_por_id(id_hogar: str) -> Optional[dict]:
    """Busca un hogar por su ID unico."""
    return rh.obtener_hogar(id_hogar)


def eliminar_hogar(id_hogar: str) -> bool:
    """Elimina un hogar por su ID."""
    return rh.eliminar_hogar(id_hogar)
