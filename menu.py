from secuencia import diferencia_unica, longitud_subsecuencia_unica, puede_reordenar_para_11, determinar_cuadrante, longitud_lcs, suma_maxima_subsecuencia_contigua, contar_cuadrados_2x2
from utils import obtener_secuencia, get_numero, get_coordenadas
from knapsack import interactive_knapsack
from operations import determine_data_structure
from social_network import handle_social_network

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("Menú de Opciones")
    print("1. Verificar diferencias unicas")
    print("2. Encontrar la longitud de la subsecuencia mas larga de elementos unicos")
    print("3. Verificar digitos divisibles por 11")
    print("4. Sistema de coordenadas local")
    print("5. Encontrar longitud de la subsecuencia comun mas larga")
    print("6. Suma maxima de subsecuencia contigua")
    print("7. Contar cuadrados 2x2")
    print("8. Problema de la mochila Knapsack")
    print("9. Verificar tipo de estructura")
    print("10. Red Social")
    print("0. Salir")

def obtener_opcion():
    """Obtiene y devuelve la opción seleccionada por el usuario."""
    return input("Selecciona una opción: ")

def ejecutar_opcion(opcion):
    """Ejecuta la acción correspondiente a la opción seleccionada por el usuario."""
    if opcion == '1':
        secuencia = obtener_secuencia()
        resultado = diferencia_unica(secuencia)
        print(f"Resultado: {resultado}\n")
        
    elif opcion == '2':
        secuencia = obtener_secuencia()
        resultado = longitud_subsecuencia_unica(secuencia)
        print(f"Longitud de la subsecuencia más larga de elementos únicos: {resultado}\n")
    elif opcion == '3':
        secuencia = get_numero()
        resultado = puede_reordenar_para_11(secuencia)
        print(f"Resultado: {resultado}\n") 
    elif opcion == '4':
        K = int(input("Ingresa numero de casos de prueba:"))
        results = []
        for _ in range(K):
            X, Y, P, Q = get_coordenadas()
            resultado = determinar_cuadrante(X, Y, P, Q)
            results.append(resultado)
        for result in results:
            print(result)
    elif opcion == '5':
        print("Para encontrar la longitud de la subsecuencia común más larga, ingresa dos cadenas de caracteres.")
        while True:
            s1 = input("Ingresa la primera cadena: ").strip()
            s2 = input("Ingresa la segunda cadena: ").strip()
            if s1 and s2:
                resultado = longitud_lcs(s1, s2)
                print(f"Longitud de la subsecuencia común más larga: {resultado}\n")
                break
            else:
                print("Ambas cadenas deben ser no vacías. Inténtalo de nuevo.")
    elif opcion == '6':
        secuencia = obtener_secuencia()
        print("Suma máxima de una subsecuencia contigua:", suma_maxima_subsecuencia_contigua(secuencia))
    elif opcion == '7':
        R, C = obtener_secuencia()
        resultado = contar_cuadrados_2x2(R, C)
        print("Número de cuadrados de 2x2:", resultado)
    elif opcion == '8':
        print("Ejercicio de la Mochila seleccionado.")
        interactive_knapsack()
    elif opcion == '9':
        print("Ejercicio de la estructura de datos seleccionado.")
        while True:
            try:
                n = int(input("Introduce el número de operaciones (o 0 para terminar): "))
                if n == 0:
                    break
                operations = []
                for _ in range(n):
                    op, x = input().split()
                    operations.append((op, int(x)))
                result = determine_data_structure(operations)
                print(result)
            except Exception as e:
                print(f"Error: {e}")
    elif opcion == '10':
        print("Ejercicio de la red social seleccionado.")
        handle_social_network()
    elif opcion == '0':
        print("Saliendo del programa...")
        return False
        
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.\n")
    
    return True
