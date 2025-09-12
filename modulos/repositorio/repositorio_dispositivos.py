# repositorio_dispositivos.py

def obtener_dispositivo_por_id(dispositivos, dispositivo_id):
    """
    Busca un dispositivo por su ID. Devuelve el diccionario o None.
    """
    for dispositivo in dispositivos:
        if dispositivo['id'] == dispositivo_id:
            return dispositivo
    return None
