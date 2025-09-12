# ui_dispositivos.py

from modulos.servicios import servicios_dispositivos as sd
from modulos.ui.ui_utils import obtener_input, pausar_pantalla


def menu_principal_dispositivos(dispositivos, volver_a=None):
    """Menú principal para gestionar dispositivos."""
    while True:
        print("""
            --- Menú de Dispositivos ---
            1. Listar dispositivos
            2. Agregar dispositivo
            3. Eliminar dispositivo
            4. Buscar dispositivo
            5. Activar Modo Ahorro de Energía
            0. Volver al menú anterior
            """)
        opcion = obtener_input("Seleccione una opción: ")

        if opcion == "1":
            lista = sd.listar_dispositivos(dispositivos)
            if not lista:
                print("No hay dispositivos registrados.")
            else:
                for d in lista:
                    print(
                        f"ID: {d['id_dispositivo']}, Tipo: {d['tipo_dispositivo']}, Estado: {d['estado']}, "
                        f"Esencial: {'Sí' if d['es_esencial'] else 'No'}, "
                        f"Usuario Conectado: {d.get('id_usuario_conectado','-')}, "
                        f"Ubicación: {d.get('ubicacion','-')}, "
                        f"Marca: {d.get('marca_dispositivo','-')}, "
                        f"Consumo: {d.get('consumo_energetico','-')}W"
                    )
            pausar_pantalla()

        elif opcion == "2":
            print("\n--- Agregar Dispositivo ---")
            nuevo = {}
            nuevo['id_dispositivo'] = obtener_input("ID único: ")
            if not nuevo['id_dispositivo']:
                print("El ID no puede estar vacío.")
                pausar_pantalla()
                continue

            nuevo['tipo_dispositivo'] = obtener_input("Tipo: ")
            nuevo['estado'] = obtener_input("Estado (encendido/apagado): ").lower()
            if nuevo['estado'] not in ["encendido", "apagado"]:
                print("Estado inválido. Debe ser 'encendido' o 'apagado'.")
                pausar_pantalla()
                continue

            nuevo['es_esencial'] = obtener_input("¿Es esencial? (sí/no): ").lower() == "sí"
            nuevo['id_usuario_conectado'] = obtener_input("ID del usuario conectado: ")
            nuevo['ubicacion'] = obtener_input("Ubicación del dispositivo: ")
            nuevo['marca_dispositivo'] = obtener_input("Marca del dispositivo: ")

            try:
                nuevo['consumo_energetico'] = float(obtener_input("Consumo energético (W): "))
            except ValueError:
                print("Consumo inválido. Se asignará 0W.")
                nuevo['consumo_energetico'] = 0.0

            if sd.agregar_dispositivo(dispositivos, nuevo):
                print("Dispositivo agregado con éxito.")
            else:
                print("⚠ Error: ID ya existente.")
            pausar_pantalla()

        elif opcion == "3":
            dispositivo_id = obtener_input("ID a eliminar: ")
            if sd.eliminar_dispositivo(dispositivos, dispositivo_id):
                print("Dispositivo eliminado.")
            else:
                print("No se encontró el dispositivo.")
            pausar_pantalla()

        elif opcion == "4":
            dispositivo_id = obtener_input("ID a buscar: ")
            dispositivo = sd.buscar_dispositivo(dispositivos, dispositivo_id)
            if dispositivo:
                print(
                    f"ID: {dispositivo['id_dispositivo']}, Tipo: {dispositivo['tipo_dispositivo']}, Estado: {dispositivo['estado']}, "
                    f"Esencial: {'Sí' if dispositivo['es_esencial'] else 'No'}, "
                    f"Usuario Conectado: {dispositivo.get('id_usuario_conectado','-')}, "
                    f"Ubicación: {dispositivo.get('ubicacion','-')}, "
                    f"Marca: {dispositivo.get('marca_dispositivo','-')}, "
                    f"Consumo: {dispositivo.get('consumo_energetico','-')}W"
                )
            else:
                print("No se encontró el dispositivo.")
            pausar_pantalla()

        elif opcion == "5":
            apagados = sd.activar_modo_ahorro(dispositivos)
            if apagados == 0:
                print("Todos los dispositivos no esenciales ya estaban apagados.")
            else:
                print(f"{apagados} dispositivo(s) apagados para ahorrar energía.")
            pausar_pantalla()

        elif opcion == "0":
            if volver_a:
                return
            else:
                break

        else:
            print("Opción no válida. Inténtalo de nuevo.")
            pausar_pantalla()
