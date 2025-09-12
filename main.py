# main.py
"""
Punto de Entrada Principal del Sistema SmartHome

Inicia la aplicación mostrando el menu global, que permite:
- Acceder a la gestión de usuarios:
    * Registrar nuevos usuarios
    * Iniciar sesion con roles (administrador/estandar)
    * Acceder a funcionalidades segun permisos
- Acceder a la gestión de dispositivos:
    * Listar, agregar, eliminar y buscar dispositivos
    * Activar el modo ahorro de energía
- Salir del sistema
"""


from modulos.ui.ui_usuarios import menu_principal_usuarios
from modulos.ui.ui_dispositivos import menu_principal_dispositivos
from modulos.datos.datos_dispositivos import dispositivos


def menu_global():
    while True:
        print("""
--- Menu Global ---
1. Gestion de usuarios
2. Gestion de dispositivos
0. Salir
""")
        opcion = input("Elige una opcion: ").strip()
        if opcion == "1":
            menu_principal_usuarios()
        elif opcion == "2":
            menu_principal_dispositivos(dispositivos)
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu_global()
