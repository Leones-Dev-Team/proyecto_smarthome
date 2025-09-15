from modulos.servicios import servicios_dispositivos as sd


def activar_modo_ahorro() -> int:
    """
    Apaga todos los dispositivos no esenciales que estén encendidos
    usando la lógica centralizada de servicios_dispositivos.
    Registra la acción como 'modo_ahorro_apagar' en el historial.
    """
    dispositivos = sd.listar_dispositivos()
    apagados = 0

    for d in dispositivos.values():
        if not d.get("es_esencial", False) and d.get("estado") == "encendido":
            if sd.actualizar_estado_dispositivo(d["id_dispositivo"], "apagado", origen="modo_ahorro_apagar"):
                apagados += 1

    return apagados
