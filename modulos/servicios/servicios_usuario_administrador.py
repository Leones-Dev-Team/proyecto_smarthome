# modulos/servicios/servicio_usuario_administrador.py

import logging
from typing import Dict, Optional
from modulos.repositorio.repositorio_usuarios import crear_usuario
from modulos.servicios.servicios_hogares import buscar_hogar_por_id


# Simulación de base de datos en memoria
_usuarios: Dict[str, dict] = {}

def registrar_usuario(nombre: str, contraseña: str, id_hogar: str, correo_electronico: str, telefono: str, edad: int) -> Optional[dict]:
    """
    Registra un nuevo usuario administrador validando el hogar.

    Args:
        nombre (str): Nombre de usuario.
        contraseña (str): Contraseña del usuario.
        id_hogar (str): ID del hogar asociado.
        correo_electronico (str): Correo electrónico.
        telefono (str): Teléfono.
        edad (int): Edad del usuario.

    Returns:
        dict: Usuario registrado, o None si hubo error.
    """
    nombre = nombre.lower()
    if not buscar_hogar_por_id(id_hogar):
        return None
    if nombre in _usuarios:
        return None
    usuario = {
        "nombre": nombre,
        "contraseña": contraseña,
        "id_hogar": id_hogar,
        "mail": correo_electronico,
        "telefono": telefono,
        "edad": edad,
        "rol": "administrador"
    }
    _usuarios[nombre] = usuario
    return usuario

def cambiar_rol(nombre: str, nuevo_rol: str) -> bool:
    """
    Cambia el rol de un usuario si existe y el rol es válido.

    Args:
        nombre (str): Nombre de usuario.
        nuevo_rol (str): 'estandar' o 'administrador'.

    Returns:
        bool: True si se cambió, False si no.
    """
    nombre = nombre.lower()
    if nombre in _usuarios and nuevo_rol in ["estandar", "administrador"]:
        _usuarios[nombre]["rol"] = nuevo_rol
        return True
    return False

def listar_usuarios() -> list:
    """
    Lista todos los usuarios registrados.

    Returns:
        list: Lista de diccionarios de usuarios.
    """
    return list(_usuarios.values())

def obtener_usuario(nombre: str) -> Optional[dict]:
    """
    Obtiene la información de un usuario por nombre.

    Args:
        nombre (str): Nombre de usuario.

    Returns:
        dict: Datos del usuario, o None si no existe.
    """
    nombre = nombre.lower()
    return _usuarios.get(nombre)
