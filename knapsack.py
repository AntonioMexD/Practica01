def knapsack(weights, values, capacity):
    """Resuelve el problema de la mochila 0/1 para una capacidad dada."""
    dp = [0] * (capacity + 1)
    
    for weight, value in zip(weights, values):
        for cap in range(capacity, weight - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - weight] + value)
    
    return dp[capacity]

def process_case(weights, values, capacities):
    """Procesa un caso de prueba y devuelve los resultados para cada capacidad."""
    results = []
    for capacity in capacities:
        results.append(knapsack(weights, values, capacity))
    return results

def interactive_knapsack():
    """Ejecuta el problema de la mochila de manera interactiva."""
    
    while True:
        N = int(input("Introduce el número de artículos (o 0 para terminar): "))
        
        if N == 0:
            break
        
        weights = []
        values = []
        
        print(f"Introduce los pesos y valores para los {N} artículos:")
        for _ in range(N):
            weight, value = map(int, input().split())
            weights.append(weight)
            values.append(value)
        
        G = int(input("Introduce el número de grupos: "))
        capacities = []
        
        print(f"Introduce las capacidades máximas de las mochilas para los {G} grupos:")
        for _ in range(G):
            capacities.append(int(input()))
        
        # Procesar y mostrar los resultados del caso actual
        results = process_case(weights, values, capacities)
        print("Resultados para las capacidades dadas:")
        for result in results:
            print(result)
