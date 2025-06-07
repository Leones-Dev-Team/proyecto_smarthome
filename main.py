# Importacion del modulo que contiene la logica del menu
from modulos.interfaz_menu import mostrar_menu
from modulos.dispositivos_listados import dispositivos

# Funcion principal que inicializa los datos esenciales y lanza la interfaz.
def inicializar_programa():
    mostrar_menu(dispositivos)   # Pasa el control a la interfaz del menu


if __name__ == "__main__":
    """
    Punto de entrada del programa. 

    Garantiza que el codigo solo se ejecute cuando este archivo es el programa principal,
    evitando ejecuciones accidentales si se importa como módulo.
    """
    inicializar_programa()   # Inicia la logica del programa