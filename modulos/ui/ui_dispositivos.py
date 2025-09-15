# ui_dispositivos.py
from modulos.servicios import servicios_dispositivos as sd
from modulos.automatizaciones.modo_ahorro_energia import activar_modo_ahorro as ma
from modulos.ui.ui_utils import obtener_input, pausar_pantalla


def menu_principal_dispositivos(volver_a=None, rol=None):
    while True:
        encabezado = "--- Menú de Dispositivos ---"
        if rol == "administrador":
            encabezado = "--- Menú de Dispositivos (Administrador) ---"
        print(f"\n{encabezado}")
        print("1. Listar dispositivos")
        print("2. Agregar dispositivo")
        print("3. Eliminar dispositivo")
        print("4. Buscar dispositivo")
        print("5. Activar Modo Ahorro de Energía")
        print("0. Volver al menú anterior")

        opcion = (obtener_input("Seleccione una opción: ") or "").strip()

        if opcion == '1':
            lista = sd.listar_dispositivos()
            if not lista:
                print("No hay dispositivos registrados.")
            else:
                for d in lista.values():
                    print(
                        f"ID: {d.get('id_dispositivo', '-')}, "
                        f"Tipo: {d.get('tipo_dispositivo', '-')}, "
                        f"Estado: {d.get('estado', '-')}, "
                        f"Esencial: {'Sí' if d.get('es_esencial') else 'No'}, "
                        f"Usuario Conectado: {d.get('id_usuario_conectado', '-')}, "
                        f"Ubicación: {d.get('ubicacion', '-')}, "
                        f"Marca: {d.get('marca_dispositivo', '-')}, "
                        f"Consumo: {d.get('consumo_energetico', '-')}W"
                    )
            pausar_pantalla()

        elif opcion == '2':
            print("\n--- Agregar Dispositivo ---")
            id_disp = (obtener_input("ID único: ") or "").strip()
            if not id_disp:
                print("El ID no puede estar vacío.")
                pausar_pantalla()
                continue

            tipo = (obtener_input("Tipo: ") or "").strip()
            estado = (obtener_input("Estado (encendido/apagado): ")
                      or "").lower().strip()
            if estado not in ["encendido", "apagado"]:
                print("Estado inválido. Debe ser 'encendido' o 'apagado'.")
                pausar_pantalla()
                continue

            es_esencial = (obtener_input("¿Es esencial? (sí/no): ")
                           or "").lower().strip() == "sí"
            id_usuario = (obtener_input(
                "ID del usuario conectado: ") or "").strip()
            ubicacion = (obtener_input(
                "Ubicación del dispositivo: ") or "").strip()
            marca = (obtener_input("Marca del dispositivo: ") or "").strip()

            try:
                consumo = obtener_input(
                    "Consumo energético (W): ", tipo=float, obligatorio=False)
            except ValueError:
                print("Consumo inválido. Se asignará 0W.")
                consumo = 0.0

            if sd.agregar_dispositivo(
                id_dispositivo=id_disp,
                id_usuario_conectado=id_usuario if id_usuario else None,
                ubicacion=ubicacion if ubicacion else None,
                nombre_dispositivo=None,
                tipo_dispositivo=tipo if tipo else None,
                marca_dispositivo=marca if marca else None,
                consumo_energetico=consumo if consumo is not None else 0.0,
                estado=estado,
                es_esencial=es_esencial
            ):
                print("Dispositivo agregado con éxito.")
            else:
                print("Error: ID ya existente o datos inválidos.")
            pausar_pantalla()

        elif opcion == '3':
            dispositivo_id = (obtener_input("ID a eliminar: ") or "").strip()
            if not dispositivo_id:
                print("El ID no puede estar vacío.")
                pausar_pantalla()
                continue
            if sd.eliminar_dispositivo(dispositivo_id):
                print("Dispositivo eliminado.")
            else:
                print("No se encontró el dispositivo.")
            pausar_pantalla()

        elif opcion == '4':
            dispositivo_id = (obtener_input("ID a buscar: ") or "").strip()
            if not dispositivo_id:
                print("El ID no puede estar vacío.")
                pausar_pantalla()
                continue
            dispositivo = sd.buscar_dispositivo(dispositivo_id)
            if dispositivo:
                print(
                    f"ID: {dispositivo.get('id_dispositivo', '-')}, "
                    f"Tipo: {dispositivo.get('tipo_dispositivo', '-')}, "
                    f"Estado: {dispositivo.get('estado', '-')}, "
                    f"Esencial: {'Sí' if dispositivo.get('es_esencial') else 'No'}, "
                    f"Usuario Conectado: {dispositivo.get('id_usuario_conectado', '-')}, "
                    f"Ubicación: {dispositivo.get('ubicacion', '-')}, "
                    f"Marca: {dispositivo.get('marca_dispositivo', '-')}, "
                    f"Consumo: {dispositivo.get('consumo_energetico', '-')}W"
                )
            else:
                print("No se encontró el dispositivo.")
            pausar_pantalla()

        elif opcion == '5':
            apagados = ma()
            if apagados == 0:
                print("Todos los dispositivos no esenciales ya estaban apagados.")
            else:
                print(f"{apagados} dispositivo(s) apagados para ahorrar energía.")
            pausar_pantalla()

        elif opcion == '0':
            if volver_a:
                return volver_a(nombre_usuario=None, rol=rol) if callable(volver_a) else None
            else:
                break

        else:
            print("Opción no válida. Inténtalo de nuevo.")
            pausar_pantalla()
