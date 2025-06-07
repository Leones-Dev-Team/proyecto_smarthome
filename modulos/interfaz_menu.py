# Importación de los modulos que contienen la logica de los administradores de dispositivos y modo ahorro
import uuid
from modulos.administrador_dispositivos import listar_dispositivos, agregar_dispositivo, eliminar_dispositivo, buscar_dispositivo
from modulos.administrador_automatizacion import activar_modo_ahorro


def mostrar_menu(dispositivos):   # Funcion menu que gestiona el programa SmartHome
    # Bucle while para mantener el menu activo hasta que el usuario seleccione "0. Salir"
    while True:
        # Opciones del menu
        print("""
            --- Menu Principal ---"
            1. Listar dispositivos
            2. Agregar dispositivo
            3. Eliminar dispositivo
            4. Buscar dispositivo
            5. Activar Modo Ahorro de Energia
            0. Salir
            """)
        opcion = input("Seleccione una opcion: ").strip()

        if not opcion.isdigit():   # Verifica si la opcion no es un numero
            print("¡Ingrese un numero valido!")
            continue   # Vuelve al inicio del bucle (muestra el menu otra vez)

        # Estructura if-elif-else que ejecuta la accion seleccionada en el menu
        if opcion == "1":
            # Recibe la lista Dispositivos como parametro
            listar_dispositivos(dispositivos)
        elif opcion == "2":
            # Solicita los datos del nuevo dispositivo al usuario y genera un diccionario
            agregar_dispositivo(dispositivos)
        elif opcion == "3":
            dispositivo_id = input(
                "Ingrese ID del dispositivo a eliminar: ").strip()
            if not dispositivo_id:
                print("Error: el ID no puede estar vacio.")
            else:
                eliminar_dispositivo(dispositivos, dispositivo_id)
        elif opcion == "4":
            dispositivo_id = input(
                "Ingrese el ID del dispositivo a buscar: ").strip()
            if not dispositivo_id:
                print("Error: el ID no puede estar vacio.")
            else:
                dispositivo = buscar_dispositivo(dispositivos, dispositivo_id)
                print(dispositivo if dispositivo else "Dispositivo no encontrado.")
        elif opcion == "5":
            activar_modo_ahorro(dispositivos)
        elif opcion == "0":   # Opcion "0" para salir (cierra el bucle while)
            print("Saliendo...")
            break
        else:
            print("Opcion incorrecta.")
