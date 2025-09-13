# repositorio_hogares.py

_hogares = {}

def crear_hogar(
    id_hogar,
    ubicacion=None,
    tipo_de_vivienda=None,
    tiempo_de_conexion=0,
    registro_actividad=None
):
    """
    Agrega un nuevo hogar al repositorio.
    """
    if registro_actividad is None:
        registro_actividad = []
    _hogares[id_hogar] = {
        "ubicacion": ubicacion,
        "tipo_de_vivienda": tipo_de_vivienda,
        "tiempo_de_conexion": tiempo_de_conexion,
        "registro_actividad": registro_actividad
    }

def obtener_hogar(id_hogar):
    """
    Obtiene un hogar por su ID.
    """
    return _hogares.get(id_hogar)

def listar_hogares():
    """
    Devuelve todos los hogares registrados.
    """
    return dict(_hogares)

def existe_hogar(id_hogar):
    """
    Verifica si existe un hogar por su ID.
    """
    return id_hogar in _hogares

def buscar_hogares_por_ubicacion(ubicacion):
    """
    Devuelve una lista de hogares que coinciden con la ubicación dada.
    """
    return [
        hogar for hogar in _hogares.values()
        if hogar["ubicacion"] == ubicacion
    ]