# Importación de los modulos que contienen la lógica de los administradores de dispositivos y modo ahorro
import uuid
from modulos.administrador_dispositivos import listar_dispositivos, agregar_dispositivo, eliminar_dispositivo, buscar_dispositivo
from modulos.administrador_automatizacion import activar_modo_ahorro


def mostrar_menu(dispositivos):   # Funcion menu que gestiona el programa SmartHome
    # Bucle while para mantener el menu activo hasta que el usuario seleccione "0. Salir"
    while True:
        # Opciones del menu
        print("\n--- Menu Principal ---")
        print("1. Listar dispositivos")
        print("2. Agregar dispositivo")
        print("3. Eliminar dispositivo")
        print("4. Buscar dispositivo")
        print("5. Activar Modo Ahorro de Energia")
        print("0. Salir")
        opcion = input("Seleccione una opcion: ")

        if not opcion.isdigit():   # Verifica si la opción no es un número
            print("¡Ingrese un número válido!")
            continue   # Vuelve al inicio del bucle (muestra el menú otra vez)

        # Estructura if-elif-else que ejecuta la acción seleccionada en el menú
        if opcion == "1":
            # Recibe la lista Dispositivos como parametro
            listar_dispositivos(dispositivos)
        elif opcion == "2":
            # Solicita los datos del nuevo dispositivo al usuario y genera un diccionario
            nuevo_dispositivo = {
                # Genera automáticamente un ID único y corto
                "id": str(uuid.uuid4())[:4],
                "tipo": input("Tipo (luz, camara, etc.): "),
                # Convierte el str ingresado en booleano
                "es_esencial": input("¿Es esencial? (s/n): ").lower() == "s"
            }
            # Bucle while para validar el estado
            estado = input("Estado (encendido/apagado): ").lower()
            while estado not in ["encendido", "apagado"]:
                print("Error: El estado debe ser 'encendido' o 'apagado'.")
                estado = input("Estado (encendido/apagado): ").lower()
            # Asigna el estado validado al diccionario
            nuevo_dispositivo["estado"] = estado
            agregar_dispositivo(dispositivos, nuevo_dispositivo)
        elif opcion == "3":
            eliminar_dispositivo(dispositivos, input(
                "Ingrese ID del dispositivo a eliminar: "))
        elif opcion == "4":
            dispositivo = buscar_dispositivo(
                dispositivos, input("ID del dispositivo a buscar: "))
            print(dispositivo if dispositivo else "Dispositivo no encontrado.")
        elif opcion == "5":
            activar_modo_ahorro(dispositivos)
        elif opcion == "0":   # Opción "0" para salir (cierra el bucle while)
            print("Saliendo...")
            break
        else:
            print("Opcion incorrecta.")
