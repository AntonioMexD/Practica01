def obtener_secuencia():
    """Solicita una secuencia de números al usuario y la devuelve como una lista de enteros."""
    return list(map(int, input("Ingresa la secuencia de números (separados por espacios): ").split()))

def get_numero():
    return int(input("Ingrese un numero: "))

def get_coordenadas():
    X, Y, P, Q = map(int, input("Ingresa las coordenadas (X Y P Q): ").split())
    return X, Y, P, Q

