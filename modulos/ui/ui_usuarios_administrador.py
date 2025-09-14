# ui_usuarios_administrador.py

from modulos.servicios import servicios_usuarios_administrador as sa
from modulos.datos.datos_dispositivos import dispositivos
from modulos.ui.ui_dispositivos import menu_principal_dispositivos
from modulos.ui.ui_utils import obtener_input, pausar_pantalla


def menu_administrador(nombre_usuario):
    """Muestra opciones para usuarios administradores."""
    while True:
        print(f"\n--- Menú Administrador ({nombre_usuario}) ---")
        print("""
        1. Consultar automatizaciones activas
        2. Gestionar dispositivos
        3. Modificar rol de un usuario
        4. Listar usuarios
        0. Cerrar sesión
        """)
        opcion = obtener_input("Elige una opción: ")

        if opcion == '1':
            print("\n--- Automatizaciones Activas ---\nMostrando automatizaciones en curso...")
            pausar_pantalla()

        elif opcion == '2':
            # Se pasa el mismo menú admin como "volver_a" para regresar luego
            menu_principal_dispositivos(dispositivos, volver_a=menu_administrador)

        elif opcion == '3':
            usuario_a_modificar = obtener_input("Usuario para cambiar su rol: ").lower()
            nuevo_rol = obtener_input("Nuevo rol (estandar/administrador): ").lower()
            if sa.cambiar_rol(usuario_a_modificar, nuevo_rol):
                print(f"¡Rol de '{usuario_a_modificar}' cambiado a '{nuevo_rol}'! ")
            else:
                print("Usuario no encontrado o rol inválido.")
            pausar_pantalla()

        elif opcion == '4':
            print("\n--- Lista de Usuarios ---")
            for u in sa.listar_usuarios():
                print(f"Usuario: {u['nombre']}, Rol: {u['rol']}, Hogar: {u['id_hogar']}")
            pausar_pantalla()

        elif opcion == '0':
            print(f"Cerrando sesión de {nombre_usuario}. ")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


def menu_principal_usuarios_administrador():
    """Menú principal de gestión de usuarios administradores."""
    nombre_admin = obtener_input("Ingresa tu nombre de usuario administrador: ").lower()
    menu_administrador(nombre_admin)
