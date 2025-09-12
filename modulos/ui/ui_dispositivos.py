# ui_dispositivos.py

from modulos.servicios import servicios_dispositivos as sd


def menu_principal_dispositivos(dispositivos, volver_a=None):
    while True:
        print("""
            --- Menu Dispositivos ---
            1. Listar dispositivos
            2. Agregar dispositivo
            3. Eliminar dispositivo
            4. Buscar dispositivo
            5. Activar Modo Ahorro de Energia
            0. Volver
            """)
        opcion = input("Seleccione una Opcion: ").strip()

        if opcion == "1":
            lista = sd.listar_dispositivos(dispositivos)
            if not lista:
                print("No hay dispositivos registrados.")
            else:
                for d in lista:
                    print(
                        f"ID: {d['id']}, Tipo: {d['tipo']}, Estado: {d['estado']}, Esencial: {'Si' if d['es_esencial'] else 'No'}")

        elif opcion == "2":
            nuevo = {}
            nuevo['id'] = input("ID unico: ").strip()
            nuevo['tipo'] = input("Tipo: ").strip()
            nuevo['estado'] = input(
                "Estado (encendido/apagado): ").strip().lower()
            nuevo['es_esencial'] = input(
                "¿Es esencial? (si/no): ").strip().lower() == "si"
            if sd.agregar_dispositivo(dispositivos, nuevo):
                print("Dispositivo agregado con exito.")
            else:
                print("Error: ID ya existente.")

        elif opcion == "3":
            dispositivo_id = input("ID a eliminar: ").strip()
            if sd.eliminar_dispositivo(dispositivos, dispositivo_id):
                print("Dispositivo eliminado.")
            else:
                print("No se encontro el dispositivo.")

        elif opcion == "4":
            dispositivo_id = input("ID a buscar: ").strip()
            dispositivo = sd.buscar_dispositivo(dispositivos, dispositivo_id)
            if dispositivo:
                print(
                    f"ID: {dispositivo['id']}, Tipo: {dispositivo['tipo']}, Estado: {dispositivo['estado']}, Esencial: {'Si' if dispositivo['es_esencial'] else 'No'}")
            else:
                print("No se encontro el dispositivo.")

        elif opcion == "5":
            apagados = sd.activar_modo_ahorro(dispositivos)
            if apagados == 0:
                print("Todos los dispositivos no esenciales ya estaban apagados.")
            else:
                print(f"{apagados} dispositivo(s) apagados para ahorrar Energia.")

        elif opcion == "0":
            if volver_a:
                return
            else:
                break
        else:
            print("Opcion incorrecta.")
