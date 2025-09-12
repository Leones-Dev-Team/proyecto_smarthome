# ui_dispositivos_control.py

dispositivos_control = []


def menu_principal_dispositivos_control():
    while True:
        print("""
        --- Menu Dispositivos de Control ---
        1. Agregar dispositivo de control
        2. Listar dispositivos de control
        0. Volver
        """)
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            nuevo = {}
            nuevo["id"] = input("ID del dispositivo de control: ").strip()
            nuevo["tipo"] = input("Tipo (ej: sensor, termostato, hub): ").strip()
            nuevo["ubicacion"] = input("Ubicación: ").strip()
            dispositivos_control.append(nuevo)
            print("Dispositivo de control agregado con éxito.")
        elif opcion == "2":
            if not dispositivos_control:
                print("No hay dispositivos de control registrados.")
            else:
                for d in dispositivos_control:
                    print(f"ID: {d['id']}, Tipo: {d['tipo']}, Ubicación: {d['ubicacion']}")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
