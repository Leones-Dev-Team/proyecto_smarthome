# main.py

"""
Punto de Entrada Principal del Sistema SmartHome

Inicia la aplicación mostrando el menú global, que permite:

- Gestión de usuarios:
  * Registrar nuevos usuarios
  * Iniciar sesión con roles (administrador/estándar)
  * Acceder a funcionalidades según permisos

- Gestión de dispositivos:
  * Listar, agregar, eliminar y buscar dispositivos
  * Activar el modo ahorro de energía

- Gestión de hogares:
  * Agregar y listar hogares (solo administrador)

- Gestión de dispositivos de control:
  * Agregar y listar dispositivos de control (solo administrador)

- Salir del sistema
"""
from modulos.ui.ui_usuarios_estandar import iniciar_sesion
from modulos.ui.ui_usuarios_estandar import menu_estandar
from modulos.ui.ui_usuarios_administrador import menu_administrador
from modulos.ui.ui_dispositivos import menu_principal_dispositivos
from modulos.ui.ui_hogares import menu_principal_hogares
from modulos.ui.ui_dispositivos_control import menu_principal_dispositivos_control
from modulos.datos.datos_dispositivos import dispositivos


def menu_global():
    # Login inicial
    usuario_actual = iniciar_sesion()
    if usuario_actual["usuario"] is None:
        print("No se pudo iniciar sesión. Cerrando sistema...")
        return

    nombre_usuario = usuario_actual["usuario"]
    rol = usuario_actual.get("rol", "estandar")

    while True:
        print("\n--- Menú Global ---")
        print("1. Gestión de usuarios")
        print("2. Gestión de dispositivos")

        if rol == "administrador":
            print("3. Gestión de hogares")
            print("4. Gestión de dispositivos de control")

        print("0. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            if rol == "administrador":
                menu_administrador(nombre_usuario)
            else:
                menu_estandar(nombre_usuario)

        elif opcion == "2":
            menu_principal_dispositivos(dispositivos)

        elif opcion == "3" and rol == "administrador":
            menu_principal_hogares()

        elif opcion == "4" and rol == "administrador":
            menu_principal_dispositivos_control()

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida o sin permisos.")


if __name__ == "__main__":
    menu_global()
