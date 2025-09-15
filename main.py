# main.py
from modulos.ui.ui_usuarios_estandar import iniciar_sesion as iniciar_sesion_estandar, menu_estandar
from modulos.ui.ui_usuarios_administrador import iniciar_sesion_admin, menu_administrador
from modulos.ui.ui_dispositivos import menu_principal_dispositivos
from modulos.ui.ui_hogares import menu_principal_hogares
from modulos.ui.ui_dispositivos_control import menu_principal_dispositivos_control

"""
Punto de entrada principal del sistema SmartHome
"""


def menu_global():
    print("\n--- Inicio de Sesion ---")
    tipo_usuario = (input(
        "Iniciar sesion como administrador (a) o estandar (e)? ") or "").strip().lower()

    if tipo_usuario == "a":
        usuario_actual = iniciar_sesion_admin()
    else:
        usuario_actual = iniciar_sesion_estandar()

    if not usuario_actual or not usuario_actual.get("usuario"):
        print("No se pudo iniciar sesion. Cerrando sistema...")
        return

    nombre_usuario = usuario_actual["usuario"]
    rol = usuario_actual.get("rol", "estandar")

    while True:
        print("\n--- Menu Global ---")
        print("1. Gestion de usuarios")
        print("2. Gestion de dispositivos")
        if rol == "administrador":
            print("3. Gestion de hogares")
            print("4. Gestion de dispositivos de control")
        print("0. Salir")

        opcion = (input("Elige una opcion: ") or "").strip()

        if opcion == "1":
            if rol == "administrador":
                menu_administrador(nombre_usuario)
            else:
                menu_estandar(nombre_usuario)

        elif opcion == "2":
            menu_principal_dispositivos()

        elif opcion == "3" and rol == "administrador":
            menu_principal_hogares()

        elif opcion == "4" and rol == "administrador":
            menu_principal_dispositivos_control()

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opcion no valida o sin permisos.")


if __name__ == "__main__":
    menu_global()
