# datos_usuarios.py
"""
Este modulo contiene la lista inicial de usuarios.
Actualmente es un prototipo para pruebas, en el futuro se integrara con base de datos.
"""

usuarios = [
    {
        "usuario": "admin",
        "contrasena": "adminpass",
        "rol": "administrador",
        "id_hogar": "hogar_admin",
        "edad": 35,
        "mail": "admin@smarthome.com",
        "telefono": None,
        "tiempo_de_conexion": 0,
        "registro_actividad": []
    },
    {
        "usuario": "juan",
        "contrasena": "1234",
        "rol": "estandar",
        "id_hogar": "hogar_juan",
        "edad": 28,
        "mail": "juan@example.com",
        "telefono": "123456789",
        "tiempo_de_conexion": 0,
        "registro_actividad": []
    }
]
