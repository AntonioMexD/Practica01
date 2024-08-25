def diferencia_unica(secuencia):
    """Determina si las diferencias entre números consecutivos son únicas."""
    diferencias = set()
    for i in range(1, len(secuencia)):
        diferencia = abs(secuencia[i] - secuencia[i-1])
        if diferencia in diferencias:
            return "NO"
        diferencias.add(diferencia)
    return "SI"

def longitud_subsecuencia_unica(secuencia):
    """Encuentra la longitud de la subsecuencia más larga de elementos únicos."""
    seen = set()
    max_len = 0
    start = 0
    
    for end in range(len(secuencia)):
        while secuencia[end] in seen:
            seen.remove(secuencia[start])
            start += 1
        seen.add(secuencia[end])
        max_len = max(max_len, end - start + 1)
    
    return max_len

def puede_reordenar_para_11(numero):
    digitos = list(map(int, str(numero)))
    
    # Diferencia entre suma de dígitos en posiciones pares e impares
    suma_par = 0
    suma_impar = 0
    
    # Recorremos los dígitos
    for i, digito in enumerate(digitos):
        if i % 2 == 0:
            suma_impar += digito
        else:
            suma_par += digito
    
    # Si la diferencia es múltiplo de 11, el número es divisible por 11
    if (suma_impar - suma_par) % 11 == 0:
        return "Si"
    else:
        return "No"
    
def determinar_cuadrante(X, Y, P, Q):
    """Determina el cuadrante o el eje en el sistema de coordenadas local."""
    # Transformar el punto (X, Y) al sistema de coordenadas local donde (P, Q) es el nuevo origen
    x_local = X - P
    y_local = Y - Q
    
    if x_local == 0 or y_local == 0:
        return "divisa"
    elif x_local > 0 and y_local > 0:
        return "NE"
    elif x_local > 0 and y_local < 0:
        return "SE"
    elif x_local < 0 and y_local > 0:
        return "NO"
    elif x_local < 0 and y_local < 0:
        return "SO"

def longitud_lcs(s1, s2):
    """Encuentra la longitud de la subsecuencia común más larga entre dos cadenas."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def suma_maxima_subsecuencia_contigua(secuencia):
    """Encuentra la suma máxima de una subsecuencia contigua no vacía de una secuencia de números enteros."""
    if not secuencia:
        return 0
    
    max_ending_here = max_so_far = secuencia[0]
    
    for num in secuencia[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max(max_so_far, 0)  # Retorna 0 si todas las entradas son negativas.

def contar_cuadrados_2x2(R, C):
    """Cuenta el número de cuadrados de 2x2 en un tablero de dimensiones R x C."""
    if R < 2 or C < 2:
        return 0
    return (R - 1) * (C - 1)
