import matplotlib.pyplot as plt
import numpy as np

t, y = consumo_proteina.simular(dosis=30, tiempo_total=24, k=0.1)
plt.plot(t, y, color='green')
plt.title("Consumo de Proteína (mg) vs Tiempo (h)")
plt.xlabel("Tiempo (h)")
plt.ylabel("Concentración de Proteína (mg)")
plt.grid(True)
plt.show()
