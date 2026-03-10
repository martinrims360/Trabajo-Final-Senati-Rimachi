import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
productos = pd.read_csv("SuperStoreOrders.csv")

# convertir ventas a numero 
# convertir quantity a numero
# eliminar valores vacíos
productos = productos.dropna(subset=["sales"])
productos["sales"] = pd.to_numeric(productos["sales"], errors="coerce")
productos["quantity"] = pd.to_numeric(productos["quantity"], errors="coerce")

#a.Convertir la columna Ventas del DataFrame en un array de NumPy.
ventas = productos["sales"]
array_numpy = ventas.to_numpy()

#b.Convertir la columna producto del DataFrame en un array de NumPy.
producto = productos["product_name"]
array_numpy = producto.to_numpy()

#c.Convertir la columna cantidad del DataFrame en un array de NumPy.
cantidad = productos["quantity"]
array_numpy = cantidad.to_numpy()

#d.Convertir la columna sub_category del DataFrame en un array de NumPy.
cantidad = productos["sub_category"]
array_numpy = cantidad.to_numpy()

#e.Convertir la columna state del DataFrame en un array de NumPy.
ciudad = productos["state"]
array_numpy = cantidad.to_numpy()

#==============================================================================================
#1. Gráfico de Barras- Mostrar las ventas por producto.
#==============================================================================================
# agrupar ventas por producto
ventas_producto = productos.groupby("product_name")["sales"].sum()

# obtener los 10 productos con más ventas
top10 = ventas_producto.nlargest(10)

# crear grafico el grafico de barras
plt.figure(figsize=(10,6))
plt.bar(top10.index, top10.values , color= ["blue","orange","green","red","pink"])

#agregamos titulos y etiquetas
plt.title("Top 10 productos con más ventas")
plt.xlabel("Producto")
plt.ylabel("Ventas")

plt.xticks(rotation=45)
plt.tight_layout()

#mostrar el grafico
plt.savefig("grafico de barras.png")
plt.show()

#==============================================================================================
#2. Gráfico de linea - Mostrar la cantidad vendida de los productos.
#==============================================================================================
# agrupar cantidad por producto
cantidad_producto = productos.groupby("sub_category")["quantity"].sum()

# obtener top 10 productos con mayor cantidad
top10 = cantidad_producto.nlargest(10)

# creando el grafico de linea
plt.figure(figsize=(10,6))
plt.plot(top10.index, top10.values, marker="o", linestyle="--", color="orange")

#agregamos titulos y etiquetas

plt.title("Cantidad vendida de productos (Top 10)")
plt.xlabel("Producto")
plt.ylabel("Cantidad")

#mostrar el grafico
plt.savefig("grafico de linea.png")
plt.show()

#==============================================================================================
#3. Gráfico de Pastel - Mostrar la distribución de ventas por ciudad.
#==============================================================================================
# agrupar ventas por ciudad
ventas_ciudad = productos.groupby("state")["sales"].sum()

# ordenar de mayor a menor
ventas_ciudad = ventas_ciudad.sort_values(ascending=False)

# tomar las primeras 10
top10 = ventas_ciudad.head(10)

# creando el grafico de pastel
plt.figure(figsize=(8,8))
plt.pie(top10.values, labels=top10.index, autopct="%1.1f%%")
plt.title("Distribución de ventas por ciudad (Top 10)")
plt.savefig("grafico pastel.png")
plt.show()

#==============================================================================================
#4. Histograma de ventas 
#==============================================================================================

sns.histplot(data=productos, x="sales", bins=20, kde=True ,color="green")

# titulos y etiquetas
plt.title("Distribución de ventas")
plt.xlabel("Ventas")
plt.ylabel("Frecuencia")
plt.savefig("Histograma de ventas.png")
plt.show()

#==============================================================================================
#5. Grafico de dispersion
#==============================================================================================

# gráfico de dispersión
sns.scatterplot(data=productos.sample(100), x="sales", y="quantity")

# titulos y etiquetas
plt.title("Relación entre Precio y Cantidad")
plt.xlabel("Precio (sales)")
plt.ylabel("Cantidad (quantity)")
plt.savefig("Grafico de dispersion.png")
plt.show()