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
  * Agregar y listar hogares

- Gestión de dispositivos de control:
  * Agregar y listar dispositivos de control

- Salir del sistema
"""

from modulos.ui.ui_usuarios import menu_principal_usuarios
from modulos.ui.ui_dispositivos import menu_principal_dispositivos
from modulos.ui.ui_hogares import menu_principal_hogares
from modulos.ui.ui_dispositivos_control import menu_principal_dispositivos_control
from modulos.datos.datos_dispositivos import dispositivos


def menu_global():
    while True:
        print("""
--- Menú Global ---
1. Gestión de usuarios
2. Gestión de dispositivos
3. Gestión de hogares
4. Gestión de dispositivos de control
0. Salir
""")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            menu_principal_usuarios()
        elif opcion == "2":
            menu_principal_dispositivos(dispositivos)
        elif opcion == "3":
            menu_principal_hogares()
        elif opcion == "4":
            menu_principal_dispositivos_control()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu_global()
