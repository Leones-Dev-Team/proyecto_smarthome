# modulos/servicios/servicio_usuarios.py

import logging
from modulos.repositorio.repositorio_usuarios import crear_usuario
from modulos.servicios.servicios_hogares import buscar_hogar_por_id

def registrar_usuario(nombre, apellido, id_hogar, correo_electronico):
    """Registra un nuevo usuario con la validación de id_hogar."""

    # Validar que el id_hogar exista
    if not buscar_hogar_por_id(id_hogar):
        raise ValueError(f"El hogar con ID {id_hogar} no existe.")

    # Validaciones de tipo de datos
    if not isinstance(nombre, str):
        raise TypeError("El nombre debe ser una cadena de texto.")
    if not isinstance(apellido, str):
        raise TypeError("El apellido debe ser una cadena de texto.")
    if not isinstance(id_hogar, str):
        raise TypeError("El ID del hogar debe ser una cadena de texto (UUID).")
    if not isinstance(correo_electronico, str):
        raise TypeError("El correo electrónico debe ser una cadena de texto.")

    try:
        usuario = crear_usuario(nombre, apellido, id_hogar, correo_electronico)
        return usuario
    except Exception as e:
        # Mejor manejo de errores usando logging
        logging.error(f"Error al registrar usuario: {e}")
        return None