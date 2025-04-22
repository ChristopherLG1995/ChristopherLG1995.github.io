import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('sales_data.csv')

# Agregar columna de ingreso total (Price * Quantity)
df['Revenue'] = df['Price'] * df['Quantity']

# Mostrar el DataFrame
print("Datos con columna de ingresos:\n", df)

# Calcular el ingreso total
total_revenue = df['Revenue'].sum()
print("\n💰 Ingreso total:", total_revenue)

# Producto más vendido por cantidad
best_selling = df.loc[df['Quantity'].idxmax(), 'Product']
print("📦 Producto más vendido (por cantidad):", best_selling)

# Día con mayores ventas (suma de Revenue por día)
top_day = df.groupby('Date')['Revenue'].sum().idxmax()
print("📅 Día con mayores ventas:", top_day)

# Ordenar productos por ingresos generados
sorted_by_revenue = df.sort_values(by='Revenue', ascending=False)
print("\n🔝 Productos ordenados por ingresos:\n", sorted_by_revenue[['Product', 'Revenue']])

# (Opcional) Gráfico simple
plt.bar(df['Product'], df['Revenue'])
plt.title('Ingresos por producto')
plt.ylabel('Revenue')
plt.xlabel('Producto')
plt.tight_layout()
plt.show()
