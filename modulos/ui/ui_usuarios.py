# modulos/ui/ui_usuarios.py

from modulos.servicios import servicios_usuarios as su
from modulos.datos.datos_dispositivos import dispositivos
from modulos.ui.ui_dispositivos import menu_principal_dispositivos


def obtener_input(mensaje):
    """Pide al usuario que escriba algo y lo devuelve limpio."""
    return input(mensaje).strip()


def pausar_pantalla():
    """Espera que el usuario presione Enter."""
    input("\nPresiona Enter para continuar...")


def registrar_usuario():
    """Crea un nuevo usuario estandar."""
    print("\n--- Registrar Nuevo Usuario ---")
    nombre = obtener_input("Elige un nombre de usuario: ").lower()
    contraseña = obtener_input("Elige una contraseña: ")
    id_hogar = obtener_input("ID del hogar: ")
    edad = obtener_input("Edad: ")
    mail = obtener_input("Correo electrónico: ")
    telefono = obtener_input("Teléfono: ")

    if su.registrar_usuario(nombre, contraseña, id_hogar, edad, mail, telefono):
        print(f"¡Usuario '{nombre}' registrado con exito!")
    else:
        print("¡Ese usuario ya existe! Elija otro.")
    pausar_pantalla()


def iniciar_sesion():
    """Permite entrar al sistema. Devuelve usuario y rol si es correcto."""
    print("\n--- Iniciar Sesion ---")
    nombre = obtener_input("Usuario: ").lower()
    contra = obtener_input("Contraseña: ")
    usuario, rol = su.iniciar_sesion(nombre, contra)
    if usuario:
        print(f"¡Bienvenido, {nombre}!")
        return usuario, rol
    else:
        print("Usuario o contraseña incorrectos.")
        pausar_pantalla()
        return None, None


def menu_estandar(nombre_usuario):
    """Muestra opciones para usuarios estandar."""
    while True:
        print(f"\n--- Menu Estandar ({nombre_usuario}) ---")
        print("""
            1. Ver mis datos
            2. Activar/Ejecutar automatizacion
            3. Consultar dispositivos
            0. Cerrar sesion
            """)
        opcion = obtener_input("Elige una opcion: ")

        if opcion == '1':
            info = su.obtener_info_usuario(nombre_usuario)
            if info:
                print("\n--- Tus Datos ---")
                print(f"Usuario: {info['nombre']}")
                print(f"Rol: {info['rol']}")
                print(f"ID Hogar: {info.get('id_hogar')}")
                print(f"Edad: {info.get('edad')}")
                print(f"Correo: {info.get('mail')}")
                print(f"Teléfono: {info.get('telefono')}")
            else:
                print("No se encontro la informacion del usuario.")
            pausar_pantalla()
        elif opcion == '2':
            print("\n--- Automatizacion ---\n¡Automatizacion predefinida activada!")
            pausar_pantalla()
        elif opcion == '3':
            print("\n--- Dispositivos ---")
            if not dispositivos:
                print("No hay dispositivos conectados.")
            else:
                print("Dispositivos conectados:")
                for idx, dispositivo in enumerate(dispositivos, 1):
                    print(
                        f"{idx}. {dispositivo['tipo']} "
                        f"(ID: {dispositivo['id']}, Estado: {dispositivo['estado']}, "
                        f"Ubicación: {dispositivo.get('ubicacion','-')}, "
                        f"Marca: {dispositivo.get('marca_dispositivo','-')}, "
                        f"Consumo: {dispositivo.get('consumo_energetico','-')}W)"
                    )
            pausar_pantalla()
        elif opcion == '0':
            print(f"Cerrando sesion de {nombre_usuario}.")
            break
        else:
            print("Opcion no valida. Intentalo de nuevo.")


def menu_administrador(nombre_usuario):
    """Muestra opciones para usuarios administradores."""
    while True:
        print(f"\n--- Menu Administrador --- ({nombre_usuario}) ---")
        print("""
            1. Consultar automatizaciones activas
            2. Gestionar dispositivos
            3. Modificar rol de un usuario
            0. Cerrar sesion
            """)
        opcion = obtener_input("Elige una opcion: ")

        if opcion == '1':
            print(
                "\n--- Automatizaciones Activas ---\nMostrando automatizaciones en curso.")
            pausar_pantalla()
        elif opcion == '2':
            print("\n--- Gestionar Dispositivos ---")
            menu_principal_dispositivos(
                dispositivos, volver_a=menu_administrador)
        elif opcion == '3':
            print("\n--- Cambiar Rol de Usuario ---")
            usuario_a_modificar = obtener_input(
                "Nombre de usuario para cambiar su rol: ").lower()
            nuevo_rol = obtener_input(
                "Nuevo rol (estandar/administrador): ").lower()
            if su.cambiar_rol(usuario_a_modificar, nuevo_rol):
                print(
                    f"¡Rol de '{usuario_a_modificar}' cambiado a '{nuevo_rol}'!")
            else:
                print("Usuario no encontrado o rol invalido.")
            pausar_pantalla()
        elif opcion == '0':
            print(f"Cerrando sesion de {nombre_usuario}.")
            break
        else:
            print("Opcion no valida. Intentalo de nuevo.")


def menu_principal_usuarios():
    """El menu principal que se muestra al inicio."""
    while True:
        print("""
            --- Menu de Usuarios ---
            1. Registrar nuevo usuario
            2. Iniciar sesion
            0. Salir
            """)
        opcion = obtener_input("Elige una opcion: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            usuario_actual, rol_actual = iniciar_sesion()
            if usuario_actual:
                if rol_actual == "estandar":
                    menu_estandar(usuario_actual)
                elif rol_actual == "administrador":
                    menu_administrador(usuario_actual)
        elif opcion == '0':
            print("Gracias por usar el programa ¡Hasta luego!")
            break
        else:
            print("Opcion no valida. Por favor, elige 1, 2 o 0.")
