import numpy as np
from scipy.integrate import odeint

# ======================
# 1. Consumo de proteína
# ======================
class ConsumoProteina:
    @staticmethod
    def simular(dosis, tiempo_total, k):
        t = np.linspace(0, tiempo_total, 100)
        y = dosis * np.exp(-k * t)
        return t, y

consumo_proteina = ConsumoProteina()

# ======================
# 2. Inventario
# ======================
class Inventario:
    @staticmethod
    def simular(inventario_inicial, demanda, dias):
        t = np.arange(0, dias + 1)
        stock = inventario_inicial - demanda * t
        stock = np.clip(stock, 0, None)
        return t, stock

inventario = Inventario()

# ======================
# 3. Consumo no lineal
# ======================
class ConsumoNoLineal:
    @staticmethod
    def simular(dosis, tiempo_total, k):
        t = np.linspace(0, tiempo_total, 100)
        y = dosis / (1 + k * t)
        return t, y

consumo_nolineal = ConsumoNoLineal()

# ======================
# 4. Electrolitos
# ======================
class Electrolitos:
    @staticmethod
    def simular(concentracion_inicial, k, tiempo_total):
        t = np.linspace(0, tiempo_total, 100)
        y = concentracion_inicial * np.exp(-k * t)
        return t, y

electrolitos = Electrolitos()

# ======================
# 5. Suplementos acoplados simples
# ======================
class SuplementosAcoplados:
    @staticmethod
    def simular(dosis1, dosis2, tiempo_total, k_a, k_b=0.05):
        t = np.linspace(0, tiempo_total, 100)
        y_a = dosis1 * np.exp(-k_a * t)
        y_b = dosis2 * np.exp(-k_b * t)
        return t, y_a, y_b

suplementos_acoplados = SuplementosAcoplados()

