# modo_ahorro_energia.py

def activar_modo_ahorro(dispositivos):
    """
    Funcion que activa el modo ahorro de energia apagando todos los dispositivos
    que no estan marcados como esenciales.
    """
    if not dispositivos:
        print("No hay dispositivos registrados.")
        return

    # Inicializa contador de dispositivos apagados
    dispositivos_apagados = 0

    # Itera sobre cada dispositivo en la lista
    for dispositivo in dispositivos:
        # Comprueba si el dispositivo NO es esencial y si esta encendido:
        if not dispositivo.get("es_esencial", False) and dispositivo.get("estado") == "encendido":
            dispositivo["estado"] = "apagado"   # Cambia el estado a apagado
            dispositivos_apagados += 1   # Incrementa el contador

    # Informa al usuario del resultado de la operacion
    if dispositivos_apagados == 0:
        print("Todos los dispositivos no esenciales ya estaban apagados.")
    else:
        print(f"{dispositivos_apagados} dispositivo(s) no esenciales fueron apagados para ahorrar energia.")
