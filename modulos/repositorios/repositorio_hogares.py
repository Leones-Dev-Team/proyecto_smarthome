# repositorio_hogares.py
from typing import Optional
from modulos.datos.datos_hogares import hogares as hogares_iniciales

_hogares: dict[str, dict] = {}

# --- Inicializacion de datos por defecto ---
for hogar in hogares_iniciales:
    _hogares[hogar["id_hogar"]] = hogar
# --- Fin inicializacion ---


def crear_hogar(
    id_hogar: str,
    ubicacion: Optional[str] = None,
    tipo_de_vivienda: Optional[str] = None,
    tiempo_de_conexion: int = 0,
    registro_actividad: Optional[list] = None
) -> dict:
    """
    Agrega un nuevo hogar al repositorio.
    """
    if not isinstance(id_hogar, str) or not id_hogar.strip():
        raise ValueError("El ID del hogar no puede estar vacio.")

    if id_hogar in _hogares:
        raise ValueError(f"Ya existe un hogar con ID '{id_hogar}'.")

    if ubicacion is not None and not isinstance(ubicacion, str):
        raise ValueError("La ubicacion debe ser una cadena de texto o None.")

    if tipo_de_vivienda is not None and not isinstance(tipo_de_vivienda, str):
        raise ValueError(
            "El tipo de vivienda debe ser una cadena de texto o None.")

    try:
        tiempo_de_conexion = int(tiempo_de_conexion)
        if tiempo_de_conexion < 0:
            raise ValueError
    except (ValueError, TypeError):
        raise ValueError(
            "El tiempo de conexion debe ser un numero entero no negativo.")

    if registro_actividad is None or not isinstance(registro_actividad, list):
        registro_actividad = []

    _hogares[id_hogar] = {
        "id_hogar": id_hogar,
        "ubicacion": ubicacion,
        "tipo_de_vivienda": tipo_de_vivienda,
        "tiempo_de_conexion": tiempo_de_conexion,
        "registro_actividad": registro_actividad
    }
    return _hogares[id_hogar]


def obtener_hogar(id_hogar: str) -> Optional[dict]:
    """Obtiene un hogar por su ID."""
    return _hogares.get(id_hogar)


def listar_hogares() -> dict[str, dict]:
    """Devuelve todos los hogares registrados."""
    return dict(_hogares)


def existe_hogar(id_hogar: str) -> bool:
    """Verifica si existe un hogar por su ID."""
    return id_hogar in _hogares


def buscar_hogares_por_ubicacion(ubicacion: str) -> list[dict]:
    """Devuelve una lista de hogares que coinciden con la ubicacion dada."""
    return [
        hogar for hogar in _hogares.values()
        if hogar.get("ubicacion") == ubicacion
    ]


def eliminar_hogar(id_hogar: str) -> bool:
    """Elimina un hogar por su ID."""
    if id_hogar in _hogares:
        del _hogares[id_hogar]
        return True
    return False
