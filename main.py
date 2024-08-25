from menu import mostrar_menu, obtener_opcion, ejecutar_opcion

def main():
    """Función principal que controla el flujo del programa."""
    while True:
        mostrar_menu()
        opcion = obtener_opcion()
        if not ejecutar_opcion(opcion):
            break

if __name__ == "__main__":
    main()
