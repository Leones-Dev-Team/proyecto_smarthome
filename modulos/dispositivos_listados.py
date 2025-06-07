# --- MÓDULO DE DISPOSITIVOS ---
# Este archivo define una lista de dispositivos reutilizable por todo el sistema.
# Es un prototipo inicial. En el futuro, estos datos se cargarán desde una base de datos.

"""
Este módulo contiene la lista inicial de dispositivos.
Actualmente es un prototipo para pruebas, en el futuro se integrará con base de datos.
"""

dispositivos = [
    {
        "id": "a123",
        "tipo": "luz",
        "estado": "encendido",
        "es_esencial": True
    },
    {
        "id": "b456",
        "tipo": "cámara",
        "estado": "apagado",
        "es_esencial": False
    },
    {
        "id": "c789",
        "tipo": "sensor de movimiento",
        "estado": "encendido",
        "es_esencial": False
    }
]
