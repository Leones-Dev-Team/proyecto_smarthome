# Funcion para listar los dispositivos actuales con sus atributos y estado actual
def listar_dispositivos(dispositivos):
    if not dispositivos:
        print("No hay dispositivos registrados.")
    for dispositivo in dispositivos:
        print(
            f"ID: {dispositivo['id']}, Tipo: {dispositivo['tipo']}, Estado: {dispositivo['estado']}")


# Funcion para agregar dispositivos indicando su tipo
def agregar_dispositivo(dispositivos, nuevo_dispositivo):
    dispositivos.append(nuevo_dispositivo)
    print(f"Dispositivo {nuevo_dispositivo['tipo']} agregado.")


# Funcion para eliminar dispositivos
def eliminar_dispositivo(dispositivos, dispositivo_id):
    for i, dispositivo in enumerate(dispositivos):
        if dispositivo['id'] == dispositivo_id:
            del dispositivos[i]
            print(f"Dispositivo {dispositivo_id} eliminado.")
            return
    print("Dispositivo no encontrado.")


# Funcion para buscar un dispositivo
def buscar_dispositivo(dispositivos, dispositivo_id):
    for dispositivo in dispositivos:
        if dispositivo['id'] == dispositivo_id:
            return dispositivo
    return None
