# Modulo que contiene la interfaz menu para gestionar usuarios y la logica detras de dicha interfaz
# Tambien brinda acceso a la interfaz de dispositivos y al modo ahorro
from modulos.gestion_dispositivos import mostrar_menu
from modulos.datos_dispositivos import dispositivos

# Empieza con un usuario administrador por defecto.
usuarios = {
    "admin": {"contraseña": "adminpass", "rol": "administrador"}
}


def obtener_input(mensaje):
    """Pide al usuario que escriba algo y lo devuelve limpio."""
    return input(mensaje).strip()


def pausar_pantalla():
    """Espera que el usuario presione Enter."""
    input("\nPresiona Enter para continuar...")


def registrar_usuario():  # Acciones del Sistema (Registrar e Iniciar Sesion)
    """Crea un nuevo usuario estandar."""
    print("\n--- REGISTRAR NUEVO USUARIO ---")
    nombre = obtener_input("Elige un nombre de usuario: ").lower()
    if nombre in usuarios:  # Si el usuario ya existe
        print("¡Ese usuario ya existe! Elegi otro.")
        pausar_pantalla()
        return  # Avisa y sale

    contraseña = obtener_input("Elige una contraseña: ")
    usuarios[nombre] = {"contraseña": contraseña,
                        "rol": "estandar"}  # Guarda el nuevo usuario
    print(f"¡Usuario '{nombre}' registrado con exito!")
    pausar_pantalla()


def iniciar_sesion():
    """Permite entrar al sistema. Devuelve usuario y rol si es correcto."""
    print("\n--- INICIAR SESIÓN ---")
    nombre = obtener_input("Usuario: ").lower()
    contra = obtener_input("Contraseña: ")

    if nombre in usuarios and usuarios[nombre]["contraseña"] == contra:
        print(f"¡Bienvenido, {nombre}!")
        return nombre, usuarios[nombre]["rol"]  # Devuelve datos si es correcto
    else:
        print("Usuario o contraseña incorrectos.")
        pausar_pantalla()
        return None, None  # Si falla, no devuelve nada


def menu_estandar(nombre_usuario):  # Menus para Usuarios
    """Muestra opciones para usuarios estandar."""
    while True:
        print(f"\n--- MENU ESTANDAR ({nombre_usuario}) ---")
        print("""
            1. Ver mis datos
            2. Activar/Ejecutar automatizacion
            3. Consultar dispositivos
            0. Cerrar sesion
            """)
        opcion = obtener_input("Elige una opción: ")

        if opcion == '1':
            print(
                f"\n--- TUS DATOS ---\nUsuario: {nombre_usuario}\nRol: {usuarios[nombre_usuario]['rol']}")
            pausar_pantalla()
        elif opcion == '2':
            print("\n--- AUTOMATIZACIÓN ---\n¡Automatizacion predefinida activada!")
            pausar_pantalla()
        elif opcion == '3':
            print("\n--- DISPOSITIVOS ---")
            if not dispositivos:
                print("No hay dispositivos conectados.")
            else:
                print("Dispositivos conectados:")
                for idx, dispositivo in enumerate(dispositivos, 1):
                    print(
                        f"{idx}. {dispositivo['tipo']} (ID: {dispositivo['id']}, Estado: {dispositivo['estado']})")
            pausar_pantalla()

        # Agregar la opcion dispositvos activos(enumerandolos) / no hay dispositivos activos
        elif opcion == '0':
            print(f"Cerrando sesion de {nombre_usuario}.")
            break  # Sale del menu
        else:
            print("Opcion no valida. Intentalo de nuevo.")


def menu_administrador(nombre_usuario):
    """Muestra opciones para usuarios administradores."""
    while True:
        print(f"\n--- MENU ADMINISTRADOR ({nombre_usuario}) ---")
        print("""
            1. Consultar automatizaciones activas
            2. Gestionar dispositivos
            3. Modificar rol de un usuario
            0. Cerrar sesion
            """)
        opcion = obtener_input("Elige una opcion: ")

        if opcion == '1':
            print(
                "\n--- AUTOMATIZACIONES ACTIVAS ---\nMostrando automatizaciones en curso.")
            pausar_pantalla()
        elif opcion == '2':
            # Acceso al menú de dispositivos desde administrador
            print(
                "\n--- GESTIONAR DISPOSITIVOS ---\nAqui puedes añadir, modificar o eliminar dispositivos.")
            mostrar_menu(dispositivos, volver_a=menu_administrador)
        elif opcion == '3':  # Cambiar rol de usuario
            print("\n--- CAMBIAR ROL DE USUARIO ---")
            usuario_a_modificar = obtener_input(
                "Nombre de usuario para cambiar su rol: ").lower()
            if usuario_a_modificar in usuarios and usuarios[usuario_a_modificar]["rol"] != "administrador":
                print(f"Rol actual: {usuarios[usuario_a_modificar]['rol']}")
                nuevo_rol = obtener_input(
                    "Nuevo rol (estandar/administrador): ").lower()
                if nuevo_rol in ["estandar", "administrador"]:
                    usuarios[usuario_a_modificar]["rol"] = nuevo_rol
                    print(
                        f"¡Rol de '{usuario_a_modificar}' cambiado a '{nuevo_rol}'!")
                    pausar_pantalla()
                else:
                    print("Rol no valido.")
                    pausar_pantalla()
            else:
                print("Usuario no encontrado o no puedes modificar su rol.")
                pausar_pantalla()
        elif opcion == '0':
            print(f"Cerrando sesión de {nombre_usuario}.")
            break  # Sale del menu
        else:
            print("Opción no valida. Intentalo de nuevo.")


def main_menu():
    """El menu principal que se muestra al inicio."""
    while True:
        print("""
            --- MENU PRINCIPAL ---
            1. Registrar nuevo usuario
            2. Iniciar sesion
            0. Salir
            """)
        opcion = obtener_input("Elige una opcion: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            usuario_actual, rol_actual = iniciar_sesion()
            if usuario_actual:  # Si el inicio de sesion fue exitoso
                if rol_actual == "estandar":
                    menu_estandar(usuario_actual)
                elif rol_actual == "administrador":
                    menu_administrador(usuario_actual)
        elif opcion == '0':
            print("Gracias por usar el programa ¡Hasta luego!")
            break  # Termina el programa
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")
