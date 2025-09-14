# ui_utils.py

"""
Funciones de utilidad para las interfaces de usuario (UI).
Se usan para evitar duplicación de código en los distintos menús.
"""


def obtener_input(mensaje: str, tipo: type = str, obligatorio: bool = True):
    """
    Pide un input al usuario con validación de tipo y obligatoriedad.
    - mensaje: texto a mostrar al pedir el input
    - tipo: tipo de dato esperado (str, int, float, etc.)
    - obligatorio: si es True, obliga a ingresar un valor
    """
    while True:
        valor = input(mensaje).strip()
        if not valor and obligatorio:
            print("Este campo es obligatorio. Inténtalo de nuevo.")
            continue
        if not valor and not obligatorio:
            return None
        try:
            return tipo(valor)
        except ValueError:
            print(f"Ingresa un valor válido ({tipo.__name__}).")


def pausar_pantalla():
    """
    Pausa la pantalla hasta que el usuario presione Enter.
    """
    input("\nPresiona Enter para continuar...")
