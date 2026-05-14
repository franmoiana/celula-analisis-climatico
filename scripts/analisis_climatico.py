import csv
import matplotlib.pyplot as plt

# Leer el dataset desde la carpeta /datos
fechas = []
temp_max = []
temp_min = []
precipitaciones = []

with open("datos/clima_2023.csv", "r") as f:
    reader = csv.DictReader(f)
    for fila in reader:
        fechas.append(fila["fecha"])
        temp_max.append(float(fila["temperatura_max"]))
        temp_min.append(float(fila["temperatura_min"]))
        precipitaciones.append(float(fila["precipitaciones"]))

# Calcular indicadores
temp_promedio = sum(temp_max) / len(temp_max)
temp_maxima = max(temp_max)
temp_minima = min(temp_min)
precip_promedio = sum(precipitaciones) / len(precipitaciones)

# Mostrar resultados
print("=== INDICADORES CLIMÁTICOS 2023 ===")
print(f"Temperatura promedio: {temp_promedio:.1f}°C")
print(f"Temperatura máxima registrada: {temp_maxima:.1f}°C")
print(f"Temperatura mínima registrada: {temp_minima:.1f}°C")
print(f"Precipitaciones promedio: {precip_promedio:.1f}mm")

# Generar gráfico
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

plt.figure(figsize=(10, 5))
plt.plot(meses, temp_max, marker="o", label="Temp. Máxima", color="red")
plt.plot(meses, temp_min, marker="o", label="Temp. Mínima", color="blue")
plt.title("Evolución de Temperaturas - 2023")
plt.xlabel("Mes")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("resultados/grafico_temperaturas.png")
plt.show()
print("Gráfico guardado en resultados/grafico_temperaturas.png")
