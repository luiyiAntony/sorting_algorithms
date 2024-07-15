import matplotlib.pyplot as plt
import numpy as np
import json

def line_plot(data):
    """
    data example = {
        'Bubble Sort': [(100, 0.01, 4950), (1000, 0.12, 499500), (5000, 3.00, 12497500)],
        'Merge Sort': [(100, 0.001, 200), (1000, 0.01, 4000), (5000, 0.05, 10000)],
        'Quick Sort': [(100, 0.002, 150), (1000, 0.015, 3000), (5000, 0.06, 7500)]
    }
    """
    # Extraer datos para los gráficos
    bubble_times = [x[1] for x in results['Bubble Sort']]
    merge_times = [x[1] for x in results['Merge Sort']]
    quick_times = [x[1] for x in results['Quick Sort']]

    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, bubble_times, label='Bubble Sort', marker='o')
    plt.plot(sizes, merge_times, label='Merge Sort', marker='o')
    plt.plot(sizes, quick_times, label='Quick Sort', marker='o')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de tiempos de ejecución')
    plt.legend()
    plt.grid(True)
    plt.show()

def bar_plot(data):
    # Datos de ejemplo
    bar_width = 0.25
    bar_positions = np.arange(len(sizes))

    # Graficar tiempos de ejecución
    plt.figure(figsize=(10, 6))
    plt.bar(bar_positions, bubble_times, width=bar_width, label='Bubble Sort')
    plt.bar(bar_positions + bar_width, merge_times, width=bar_width, label='Merge Sort')
    plt.bar(bar_positions + 2*bar_width, quick_times, width=bar_width, label='Quick Sort')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de tiempos de ejecución')
    plt.xticks(bar_positions + bar_width, sizes)
    plt.legend()
    plt.show()

def scatter_plot(data):
    # Graficar dispersión de tiempos de ejecución
    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, bubble_times, label='Bubble Sort', marker='o')
    plt.scatter(sizes, merge_times, label='Merge Sort', marker='x')
    plt.scatter(sizes, quick_times, label='Quick Sort', marker='^')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de tiempos de ejecución')
    plt.legend()
    plt.grid(True)
    plt.show()

def box_plot(data):
    # Datos para Box Plot
    data = [bubble_times, merge_times, quick_times]

    # Graficar Box Plot
    plt.figure(figsize=(10, 6))
    plt.boxplot(data, labels=['Bubble Sort', 'Merge Sort', 'Quick Sort'])
    plt.xlabel('Algoritmos')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Distribución de tiempos de ejecución')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":

    with open("results.json", "r") as f:
        results = json.load(f)

    # Extraer datos para los gráficos
    sizes = [100, 1000, 5000, 10000]
    bubble_times = [x[1] for x in results['Bubble Sort']]
    merge_times = [x[1] for x in results['Merge Sort']]
    quick_times = [x[1] for x in results['Quick Sort']]

    line_plot(results)
    bar_plot(results)
    scatter_plot(results)
    box_plot(results)
