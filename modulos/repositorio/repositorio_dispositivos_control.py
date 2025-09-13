# repositorio_dispositivos_control.py

_dispositivos_control = {}

def crear_control(
    id_control,
    id_usuario_conectado=None,
    hora_de_conexion=None,
    dispositivos_activos=None,
    dispositivos_apagados=None,
    dispositivos_en_ahorro_de_energia=None,
    registro_actividad=None,
    otros=None
):
    """
    Agrega un nuevo registro de control de dispositivos.
    """
    if dispositivos_activos is None:
        dispositivos_activos = []
    if dispositivos_apagados is None:
        dispositivos_apagados = []
    if dispositivos_en_ahorro_de_energia is None:
        dispositivos_en_ahorro_de_energia = []
    if registro_actividad is None:
        registro_actividad = []
    _dispositivos_control[id_control] = {
        "id_usuario_conectado": id_usuario_conectado,
        "hora_de_conexion": hora_de_conexion,
        "dispositivos_activos": dispositivos_activos,
        "dispositivos_apagados": dispositivos_apagados,
        "dispositivos_en_ahorro_de_energia": dispositivos_en_ahorro_de_energia,
        "registro_actividad": registro_actividad,
        "otros": otros
    }

def obtener_control(id_control):
    return _dispositivos_control.get(id_control)

def listar_controles():
    return dict(_dispositivos_control)

def existe_control(id_control):
    return id_control in _dispositivos_control