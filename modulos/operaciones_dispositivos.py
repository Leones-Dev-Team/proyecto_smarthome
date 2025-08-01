# Modulo que contiene la logica detras de la interfaz del menu para la gestion de dispositivos inteligentes

def obtener_dispositivo_por_id(dispositivos, dispositivo_id):
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
        print(
            f"ID: {dispositivo['id']}, Tipo: {dispositivo['tipo']}, Estado: {dispositivo['estado']}, Esencial: {'Sí' if dispositivo.get('es_esencial') else 'No'}")


# Funcion para agregar dispositivos indicando su tipo
def agregar_dispositivo(dispositivos):
    """
    Agrega un nuevo dispositivo a la lista, validando que el ID sea unico.
    Solicita al usuario el ID, tipo, estado y si es esencial.
    """
    nuevo_dispositivo = {}

    # Solicitar y validar ID unico
    while True:
        dispositivo_id = input(
            "Ingrese el ID del dispositivo (debe ser unico): ").strip()
        if not dispositivo_id:
            print("Error: El ID del dispositivo no puede estar vacio.")
        elif obtener_dispositivo_por_id(dispositivos, dispositivo_id):
            print(
                f"Error: Ya existe un dispositivo con el ID '{dispositivo_id}'. Por favor, ingrese un ID diferente.")
        else:
            nuevo_dispositivo["id"] = dispositivo_id
            break

    # Validacion basica para el tipo
    while True:
        tipo = input("Tipo (luz, camara, etc.): ").strip()
        if not tipo:
            print("Error: El tipo de dispositivo no puede estar vacio.")
        else:
            nuevo_dispositivo["tipo"] = tipo
            break

    # Permite validar y establecer estado de dispositivo
    estado = input("Estado (encendido/apagado): ").lower().strip()
    while estado not in ["encendido", "apagado"]:
        print("Error: El estado debe ser 'encendido' o 'apagado'.")
        estado = input("Estado (encendido/apagado): ").lower().strip()
    nuevo_dispositivo["estado"] = estado

    # Permite validar y establecer si el dispositivo es_esencial
    es_esencial_input = ""
    intentos = 0  # Inicializa contador intentos

    while es_esencial_input not in ["si", "no"]:
        if intentos > 0:
            print('Error. Debe responder "si" o "no. Intente nuevamente.')

        es_esencial_input = input("¿Es esencial? (si/no): ").lower().strip()
        intentos += 1

    # Permitir salida despues de varios intentos fallidos
    if intentos >= 3 and es_esencial_input not in ["si", "no"]:
        print("Demasiados intentos fallidos. Cancelando operacion.")
        return  # Sale de la funcion al haber muchos errores

    nuevo_dispositivo["es_esencial"] = es_esencial_input == "si"

    dispositivos.append(nuevo_dispositivo)
    print(
        f"Dispositivo '{nuevo_dispositivo['tipo']}' con ID '{nuevo_dispositivo['id']}' agregado exitosamente.")


# Funcion para eliminar dispositivos
def eliminar_dispositivo(dispositivos, dispositivo_id):
    """
    Elimina un dispositivo de la lista por su ID.
    """
    dispositivo = obtener_dispositivo_por_id(dispositivos, dispositivo_id)

    if dispositivo:
        dispositivos.remove(dispositivo)
        print(f"Dispositivo con ID '{dispositivo_id}' eliminado.")
    else:
        print("Dispositivo no encontrado.")


# Funcion para buscar un dispositivo
def buscar_dispositivo(dispositivos, dispositivo_id):
    """
    Busca y muestra la información de un dispositivo por su ID.
    """
    dispositivo = obtener_dispositivo_por_id(dispositivos, dispositivo_id)

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
