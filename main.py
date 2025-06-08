"""
Punto de Entrada Principal del Sistema SmartHome

Inicia la aplicacion cargando el menu de gestion de usuarios, que permite:
- Registrar nuevos usuarios
- Iniciar sesion con roles (administrador/estandar)
- Acceder a funcionalidades segun permisos.
"""

from modulos.gestion_usuarios import main_menu

if __name__ == "__main__":
    main_menu()  # Inicia con el sistema de usuarios
