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
                        f"ID: {d['id']}, Tipo: {d['tipo']}, Estado: {d['estado']}, "
                        f"Esencial: {'Si' if d['es_esencial'] else 'No'}, "
                        f"Usuario Conectado: {d.get('id_usuario_conectado','-')}, "
                        f"Ubicación: {d.get('ubicacion','-')}, "
                        f"Marca: {d.get('marca_dispositivo','-')}, "
                        f"Consumo: {d.get('consumo_energetico','-')}W"
                    )

        elif opcion == "2":
            nuevo = {}
            nuevo['id'] = input("ID unico: ").strip()
            nuevo['tipo'] = input("Tipo: ").strip()
            nuevo['estado'] = input("Estado (encendido/apagado): ").strip().lower()
            nuevo['es_esencial'] = input("¿Es esencial? (si/no): ").strip().lower() == "si"
            nuevo['id_usuario_conectado'] = input("ID del usuario conectado: ").strip()
            nuevo['ubicacion'] = input("Ubicación del dispositivo: ").strip()
            nuevo['marca_dispositivo'] = input("Marca del dispositivo: ").strip()
            try:
                nuevo['consumo_energetico'] = float(input("Consumo energético (W): ").strip())
            except:
                nuevo['consumo_energetico'] = 0.0

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
                    f"ID: {dispositivo['id']}, Tipo: {dispositivo['tipo']}, Estado: {dispositivo['estado']}, "
                    f"Esencial: {'Si' if dispositivo['es_esencial'] else 'No'}, "
                    f"Usuario Conectado: {dispositivo.get('id_usuario_conectado','-')}, "
                    f"Ubicación: {dispositivo.get('ubicacion','-')}, "
                    f"Marca: {dispositivo.get('marca_dispositivo','-')}, "
                    f"Consumo: {dispositivo.get('consumo_energetico','-')}W"
                )
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
