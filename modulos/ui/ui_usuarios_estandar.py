# ui_usuarios_estandar.py
from modulos.servicios import servicios_usuarios_estandar as su
from modulos.servicios import servicios_dispositivos as sd
from modulos.ui.ui_utils import obtener_input, pausar_pantalla


def registrar_usuario():
    """Crea un nuevo usuario estándar."""
    print("\n--- Registrar Nuevo Usuario ---")

    nombre_raw = obtener_input("Elige un nombre de usuario: ")
    contraseña_raw = obtener_input("Elige una contraseña: ")
    id_hogar_raw = obtener_input("ID del hogar: ")

    nombre = (nombre_raw or "").strip().lower()
    contraseña = (contraseña_raw or "").strip()
    id_hogar = (id_hogar_raw or "").strip()

    if not nombre:
        print("El nombre de usuario no puede estar vacío.")
        pausar_pantalla()
        return
    if not contraseña:
        print("La contraseña no puede estar vacía.")
        pausar_pantalla()
        return
    if not id_hogar:
        print("El ID del hogar no puede estar vacío.")
        pausar_pantalla()
        return

    try:
        edad_val = obtener_input("Edad: ", int)
        # asegurar int “real”
        edad: int = int(edad_val)  # type: ignore[arg-type]
        if edad < 0:
            raise ValueError
    except Exception:
        print("Edad inválida.")
        pausar_pantalla()
        return

    mail_in = obtener_input("Correo electrónico: ") or ""
    telefono_in = obtener_input("Teléfono: ") or ""

    mail = mail_in.strip() or None
    telefono = telefono_in.strip() or None

    ok = su.registrar_usuario(
        nombre=nombre,
        contraseña=contraseña,
        id_hogar=id_hogar,
        edad=edad,
        mail=mail,
        telefono=telefono
    )
    if ok:
        print(f"Usuario '{nombre}' registrado con éxito.")
    else:
        print("Ese usuario ya existe o el hogar no existe.")
    pausar_pantalla()


def iniciar_sesion():
    """Permite entrar al sistema. Devuelve un dict con usuario y rol si es correcto."""
    print("\n--- Iniciar Sesión ---")
    nombre = (obtener_input("Usuario: ") or "").strip().lower()
    contraseña = (obtener_input("Contraseña: ") or "").strip()

    usuario, rol = su.iniciar_sesion(nombre, contraseña)
    if usuario:
        print(f"Bienvenido/a, {nombre}! (Rol: {rol})")
        return {"usuario": nombre, "rol": rol}
    else:
        print("Usuario o contraseña incorrectos.")
        pausar_pantalla()
        return {"usuario": None, "rol": None}


def menu_estandar(nombre_usuario):
    """Muestra opciones para usuarios estándar."""
    while True:
        print(f"\n--- Menú Estándar ({nombre_usuario}) ---")
        print("""
        1. Ver mis datos
        2. Activar/Ejecutar automatización
        3. Consultar dispositivos
        0. Cerrar sesión
        """)
        opcion = (obtener_input("Elige una opción: ") or "").strip()

        if opcion == '1':
            info = su.obtener_info_usuario(nombre_usuario)
            if info:
                print("\n--- Tus Datos ---")
                print(f"Usuario: {info.get('nombre', '-')}")
                print(f"Rol: {info.get('rol', '-')}")
                print(f"ID Hogar: {info.get('id_hogar', '-')}")
                print(f"Edad: {info.get('edad', '-')}")
                print(f"Correo electrónico: {info.get('mail', '-')}")
                print(f"Teléfono: {info.get('telefono', '-')}")
            else:
                print("No se encontró la información del usuario.")
            pausar_pantalla()

        elif opcion == '2':
            print("\n--- Automatización ---\nAutomatización predefinida activada.")
            pausar_pantalla()

        elif opcion == '3':
            print("\n--- Dispositivos ---")
            lista = sd.listar_dispositivos()
            if not lista:
                print("No hay dispositivos conectados.")
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

        elif opcion == '0':
            print(f"Cerrando sesión de {nombre_usuario}.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


def menu_principal_usuarios_estandar():
    """Menú principal de gestión de usuarios estándar."""
    while True:
        print("""
        --- Menú de Usuarios Estándar ---
        1. Registrar nuevo usuario
        2. Iniciar sesión
        0. Volver al menú global
        """)
        opcion = (obtener_input("Elige una opción: ") or "").strip()

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            return iniciar_sesion()
        elif opcion == '0':
            print("Saliendo del menú de usuarios estándar.")
            break
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 0.")
