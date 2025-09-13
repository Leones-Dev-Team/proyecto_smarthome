# repositorio_dispositivos.py

# Base de datos en memoria para dispositivos

_dispositivos = {}

def crear_dispositivo(
    id_dispositivo,
    id_usuario_conectado=None,
    ubicacion=None,
    hora_de_conexion=None,
    nombre_dispositivo=None,
    tipo_dispositivo=None,
    marca_dispositivo=None,
    consumo_energetico=None
):
    """
    Crea un nuevo dispositivo con los campos indicados.
    """
    _dispositivos[id_dispositivo] = {
        "id_usuario_conectado": id_usuario_conectado,
        "ubicacion": ubicacion,
        "hora_de_conexion": hora_de_conexion,
        "nombre_dispositivo": nombre_dispositivo,
        "tipo_dispositivo": tipo_dispositivo,
        "marca_dispositivo": marca_dispositivo,
        "consumo_energetico": consumo_energetico
    }

def obtener_dispositivo(id_dispositivo):
    return _dispositivos.get(id_dispositivo)

def listar_dispositivos():
    return dict(_dispositivos)

def obtener_dispositivo_por_id(dispositivos, dispositivo_id):
    """
    Busca un dispositivo por su ID. Devuelve el diccionario o None.
    """
    for dispositivo in dispositivos:
        if dispositivo['id'] == dispositivo_id:
            return dispositivo
    return None