import time
import random
import matplotlib.pyplot as plt

def busqueda_lineal(arr, objetivo):
    for i, val in enumerate(arr):
        if val == objetivo:
            return i
    return "No encontrado"

def busqueda_binaria(arr, objetivo):
    inicio, fin = 0, len(arr) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return "No encontrado"

def medir_tiempo(funcion, arr, objetivo):
    inicio = time.time()
    resultado = funcion(arr, objetivo)
    fin = time.time()
    return resultado, fin - inicio

if __name__ == "__main__":
    tamanos = [10000, 50000, 100000, 250000, 500000, 750000, 1000000, 1500000, 2000000]
    tiempos_lineal = []
    tiempos_binaria = []

    for n in tamanos:
        lista = sorted(random.sample(range(n * 10), n))
        objetivo = lista[-1]  # elemento al final para peor caso en búsqueda lineal

        resultado_lineal, tiempo_lineal = medir_tiempo(busqueda_lineal, lista, objetivo)
        resultado_binario, tiempo_binaria = medir_tiempo(busqueda_binaria, lista, objetivo)

        tiempos_lineal.append(tiempo_lineal)
        tiempos_binaria.append(tiempo_binaria)

        print(f"n={n} | Lineal: {tiempo_lineal:.6f}s | Binaria: {tiempo_binaria:.6f}s")

    # Gráfico comparativo
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos_lineal, marker='o', label='Búsqueda Lineal')
    plt.plot(tamanos, tiempos_binaria, marker='s', label='Búsqueda Binaria')
    plt.title('Comparación de Tiempos de Búsqueda')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()