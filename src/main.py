# # 1. Leer el csv desde el main.py
# # 2. hacer la documentacion necesaria para el readme.md

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("data/data.csv")

# Mostrar las primeras filas
print(df.head())

