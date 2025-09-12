# servicio_dispositivos.py

from modulos.repositorio import repositorio_dispositivos as repo


def listar_dispositivos(dispositivos):
    """
    Devuelve la lista de dispositivos registrados.
    """
    return dispositivos


def agregar_dispositivo(dispositivos, nuevo_dispositivo):
    """
    Agrega un nuevo dispositivo si el ID no existe.
    Devuelve True si se agrego, False si ya existe.
    """
    if repo.obtener_dispositivo_por_id(dispositivos, nuevo_dispositivo['id']):
        return False
    dispositivos.append(nuevo_dispositivo)
    return True


def eliminar_dispositivo(dispositivos, dispositivo_id):
    """
    Elimina un dispositivo por ID. Devuelve True si se elimino, False si no existe.
    """
    dispositivo = repo.obtener_dispositivo_por_id(dispositivos, dispositivo_id)
    if dispositivo:
        dispositivos.remove(dispositivo)
        return True
    return False


def buscar_dispositivo(dispositivos, dispositivo_id):
    """
    Devuelve el dispositivo si existe, None si no.
    """
    return repo.obtener_dispositivo_por_id(dispositivos, dispositivo_id)


def activar_modo_ahorro(dispositivos):
    """
    Apaga todos los dispositivos no esenciales que esten encendidos.
    Devuelve la cantidad de dispositivos apagados.
    """
    apagados = 0
    for dispositivo in dispositivos:
        if not dispositivo.get("es_esencial", False) and dispositivo.get("estado") == "encendido":
            dispositivo["estado"] = "apagado"
            apagados += 1
    return apagados
