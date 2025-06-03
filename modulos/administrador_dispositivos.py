#modulos/administrador_dispositivos.py

def _get_dispositivo_by_id(dispositivos, dispositivo_id):
    """
    Función auxiliar para encontrar un dispositivo por su ID.
    """
    for dispositivo in dispositivos:
        if dispositivo['id'] == dispositivo_id:
            return dispositivo
    return None

# Funcion para listar los dispositivos actuales con sus atributos y estado actual
def listar_dispositivos(dispositivos):
    if not dispositivos:
        print("No hay dispositivos registrados.")
        return

    print("\n--- Dispositivos Actuales ---")
    for dispositivo in dispositivos:
        print(f"ID: {dispositivo['id']}, Tipo: {dispositivo['tipo']}, Estado: {dispositivo['estado']}, Esencial: {'Sí' if dispositivo.get('es_esencial') else 'No'}")

# Funcion para agregar dispositivos indicando su tipo
def agregar_dispositivo(dispositivos, nuevo_dispositivo):
    # Validación básica.
    while not nuevo_dispositivo.get("tipo"):
        print("Error: El tipo de dispositivo no puede estar vacío.")
        nuevo_dispositivo["tipo"] = input("Tipo (luz, camara, etc.): ").strip()

    # Permite validar y establecer estado de dispositivo
    estado = input("Estado (encendido/apagado): ").lower().strip()
    while estado not in ["encendido", "apagado"]:
        print("Error: El estado debe ser 'encendido' o 'apagado'.")
        estado = input("Estado (encendido/apagado): ").lower().strip()
    nuevo_dispositivo["estado"] = estado

    # Permite validar y establecer es_esencial
    es_esencial_input = input("¿Es esencial? (si/no): ").lower().strip()
    nuevo_dispositivo["es_esencial"] = es_esencial_input == "si"

    dispositivos.append(nuevo_dispositivo)
    print(f"Dispositivo '{nuevo_dispositivo['tipo']}' con ID '{nuevo_dispositivo['id']}' agregado exitosamente.")

# Funcion para eliminar dispositivos
def eliminar_dispositivo(dispositivos, dispositivo_id):
    dispositivo = _get_dispositivo_by_id(dispositivos, dispositivo_id)
    if dispositivo:
        dispositivos.remove(dispositivo)
        print(f"Dispositivo con ID '{dispositivo_id}' eliminado.")
    else:
        print("Dispositivo no encontrado.")

# Funcion para buscar un dispositivo
def buscar_dispositivo(dispositivos, dispositivo_id):
    dispositivo = _get_dispositivo_by_id(dispositivos, dispositivo_id)
    if dispositivo:
        print(f"\n--- Dispositivo Encontrado ---")
        print(f"ID: {dispositivo['id']}")
        print(f"Tipo: {dispositivo['tipo']}")
        print(f"Estado: {dispositivo['estado']}")
        print(f"Esencial: {'Sí' if dispositivo.get('es_esencial') else 'No'}")
        return dispositivo
    else:
        print("Dispositivo no encontrado.")
        return None
