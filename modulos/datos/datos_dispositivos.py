# datos_dispositivos.py
"""
Este modulo contiene la lista inicial de dispositivos.
Actualmente es un prototipo para pruebas, en el futuro se integrara con base de datos.
"""

dispositivos = [
    {
        "id_dispositivo": "a123",
        "nombre_dispositivo": None,
        "tipo_dispositivo": "luz",
        "marca_dispositivo": None,
        "consumo_energetico": 0.0,
        "estado": "encendido",
        "es_esencial": True,
        "id_usuario_conectado": None,
        "ubicacion": None,
        "tiempo_de_conexion": 0,
        "registro_actividad": []
    },
    {
        "id_dispositivo": "b456",
        "nombre_dispositivo": None,
        "tipo_dispositivo": "camara",
        "marca_dispositivo": None,
        "consumo_energetico": 0.0,
        "estado": "apagado",
        "es_esencial": False,
        "id_usuario_conectado": None,
        "ubicacion": None,
        "tiempo_de_conexion": 0,
        "registro_actividad": []
    },
    {
        "id_dispositivo": "c789",
        "nombre_dispositivo": None,
        "tipo_dispositivo": "sensor de movimiento",
        "marca_dispositivo": None,
        "consumo_energetico": 0.0,
        "estado": "encendido",
        "es_esencial": False,
        "id_usuario_conectado": None,
        "ubicacion": None,
        "tiempo_de_conexion": 0,
        "registro_actividad": []
    }
]
