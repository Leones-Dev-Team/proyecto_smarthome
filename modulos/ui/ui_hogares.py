# ui_hogares.py

hogares = []


def menu_principal_hogares():
    while True:
        print("""
        --- Menu Hogares ---
        1. Agregar hogar
        2. Listar hogares
        0. Volver
        """)
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            nuevo = {}
            nuevo["id"] = input("ID del hogar: ").strip()
            nuevo["direccion"] = input("Dirección: ").strip()
            nuevo["propietario"] = input("Nombre del propietario: ").strip()
            hogares.append(nuevo)
            print("Hogar agregado con éxito.")
        elif opcion == "2":
            if not hogares:
                print("No hay hogares registrados.")
            else:
                for h in hogares:
                    print(f"ID: {h['id']}, Dirección: {h['direccion']}, Propietario: {h['propietario']}")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
