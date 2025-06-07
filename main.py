# Importacion del modulo que contiene la logica del menu
from modulos.interfaz_menu import mostrar_menu


# Funcion principal que inicializa los datos esenciales y lanza la interfaz.
def inicializar_programa():
    dispositivos = []   # Lista que actuara como "base de datos" durante la ejecución
    mostrar_menu(dispositivos)   # Pasa el control a la interfaz del menú


if __name__ == "__main__":
    """
    Punto de entrada del programa. 

    Garantiza que el código solo se ejecute cuando este archivo es el programa principal,
    evitando ejecuciones accidentales si se importa como módulo.
    """
    inicializar_programa()   # Inicia la logica del programa
