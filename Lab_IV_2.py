#----------------------------------------------------------------------------------
# Informática II - Laboratorio IV.2: Análisis de datos de telemetría de un nodo IoT
# Integrantes: 
#   - Velazquez Cruz, Joel
#
# URL del Repositorio de GitHub:
# 
#----------------------------------------------------------------------------------

import pandas as pd
import numpy as np

# 1. Cargar el archivo CSV
df = pd.read_csv('telemetria_nodo_iot.csv', parse_dates=['timestamp'], index_col='timestamp')

# 2. Calcular estadísticas descriptivas con NumPy y Pandas
numeric_cols = ['temperatura_C', 'humedad_pct', 'voltaje_bateria_V', 'rssi_dbm']

estadisticas = pd.DataFrame({
    'media': [np.mean(df[col]) for col in numeric_cols],
    'mínimo': [np.min(df[col]) for col in numeric_cols],
    'máximo': [np.max(df[col]) for col in numeric_cols],
    'desvío_estándar': [np.std(df[col], ddof=1) for col in numeric_cols]
}, index=numeric_cols)

print("=== PASO 2: Estadísticas Descriptivas ===")
print(estadisticas.round(2))