import pandas as pd
print("========FILTRADO DE DATOS==============")
productos = pd.read_csv("SuperStoreOrders.csv")
# convertir la columna sales a número
productos["sales"] = pd.to_numeric(productos["sales"], errors="coerce")

#1.Mostrar solo las ventas realizadas en Florida
#Creamos un dataframe con las columnas de ventas y ciudad 
#filtramos a todas las ventas realizadas en Florida
df = productos[["sales","state"]]
ventas_florida= df[df["state"]=="Florida"]
print(" ====================================")
print(ventas_florida)
print(" ====================================")
#Exportamos el dataframe ventas_florida
ventas_florida.to_csv("ventas_florida.csv",index=False)

#2.Mostrar los productos cuyas ventas sean mayores a 300.
#Creamos un dataframe con las columnas de productos y ventas
#filtramos los productos cuyas ventas sean mayores a 300.
df = productos[["product_name","sales"]]
productos_mayores_a_300 = df[df["sales"] > 300]
print(" ====================================")
print(productos_mayores_a_300)
print(" ====================================")
#Exportamos el dataframe productos_mayores_a_300
productos_mayores_a_300.to_csv("productos_mayores_a_300.csv",index=False)

#3.Mostrar los productos cuya cantidad vendida sea mayor a 5.
#Creamos un dataframe con las columnas de productos y cantidad
#filtramos los productos cuya cantidad vendida sea mayor a 5.
df = productos[["product_name","quantity"]]
cantidad_mayor_a_5 = df[df["quantity"] > 5]
print(" ====================================")
print(cantidad_mayor_a_5)
print(" ====================================")
#Exportamos el dataframe productos_mayores_a_300
cantidad_mayor_a_5.to_csv("cantidad_mayor_a_5.csv",index=False)

