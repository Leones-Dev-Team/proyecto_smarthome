# ui_usuarios_administrador.py
from modulos.servicios import servicios_usuario_administrador as sa
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
        opcion = (obtener_input("Elige una opción: ") or "").strip()

        if opcion == '1':
            print(
                "\n--- Automatizaciones Activas ---\nMostrando automatizaciones en curso...")
            pausar_pantalla()

        elif opcion == '2':
            # Se pasa el mismo menú admin como "volver_a" para regresar luego
            menu_principal_dispositivos(volver_a=menu_administrador)

        elif opcion == '3':
            usuario_a_modificar = (obtener_input(
                "Usuario para cambiar su rol: ") or "").strip().lower()
            nuevo_rol = (obtener_input(
                "Nuevo rol (estandar/administrador): ") or "").strip().lower()

            if not usuario_a_modificar or not nuevo_rol:
                print("Usuario y rol no pueden estar vacíos.")
            elif nuevo_rol not in ("estandar", "administrador"):
                print("Rol inválido. Debe ser 'estandar' o 'administrador'.")
            elif sa.cambiar_rol(usuario_a_modificar, nuevo_rol):
                print(
                    f"Rol de '{usuario_a_modificar}' cambiado a '{nuevo_rol}'.")
            else:
                print("Usuario no encontrado o rol inválido.")
            pausar_pantalla()

        elif opcion == '4':
            print("\n--- Lista de Usuarios ---")
            usuarios = sa.listar_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                for datos in usuarios.values():
                    print(
                        f"Usuario: {datos.get('nombre', '-')}, "
                        f"Rol: {datos.get('rol', '-')}, "
                        f"Hogar: {datos.get('id_hogar', '-')}"
                    )
            pausar_pantalla()

        elif opcion == '0':
            print(f"Cerrando sesión de {nombre_usuario}.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            pausar_pantalla()


def menu_principal_usuarios_administrador():
    """Menú principal de gestión de usuarios administradores."""
    nombre_admin = (obtener_input(
        "Ingresa tu nombre de usuario administrador: ") or "").strip().lower()
    if nombre_admin:
        menu_administrador(nombre_admin)


def iniciar_sesion_admin():
    """Permite entrar como administrador. Devuelve un dict con usuario y rol si es correcto."""
    print("\n--- Iniciar Sesión Administrador ---")
    nombre = (obtener_input("Usuario: ") or "").strip().lower()
    contra = (obtener_input("Contraseña: ") or "").strip()

    usuario, rol = sa.iniciar_sesion(nombre, contra)
    if usuario:
        print(f"Bienvenido/a, {nombre}! (Rol: {rol})")
        return {"usuario": nombre, "rol": rol}
    else:
        print("Usuario o contraseña incorrectos.")
        pausar_pantalla()
        return {"usuario": None, "rol": None}
