import numpy as np

# Leer los puntos desde el archivo de texto
puntos = np.loadtxt("puntos.txt", delimiter=",")

# Calcular la distancia euclidiana entre los puntos
num_puntos = len(puntos)
distancia_matriz = np.zeros((num_puntos, num_puntos))

for i in range(num_puntos):
    for j in range(num_puntos):
        distancia = np.linalg.norm(puntos[i] - puntos[j])
        distancia_matriz[i][j] = round(distancia, 3)  # Redondear a 3 decimales

# Imprimir la matriz de distancias con formato
print("Matriz de Distancias Euclidianas:")
for fila in distancia_matriz:
    print(" ".join(map(lambda x: f"{x:.3f}", fila)))
