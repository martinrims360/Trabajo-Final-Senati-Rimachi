import pandas as pd
print("========MANIPULACION DE DATOS ===========")
productos = pd.read_csv("SuperStoreOrders.csv")
#print(productos)

#1.Crear una nueva columna llamada Ventas, calculada como: Precio × Cantidad
productos["Ventas"] = productos["shipping_cost"]*productos["quantity"]
df = productos[["shipping_cost","quantity","Ventas"]]
print(df.head())

#2.Mostrar el DataFrame actualizado con la nueva columna.
#Exportamos el dataframe Ventas
df.to_csv("Resultado.csv",index=False)

#3.Calcular las siguientes estadísticas:

#Promedio de ventas
promedio_ventas = df["Ventas"].mean()
print("promedio de ventas :", promedio_ventas)
print(" ====================================")
#Venta máxima
venta_maxima = df["Ventas"].max()
print("Venta máxima :", venta_maxima)
print(" ====================================")
#Venta mínima
venta_minima =df["Ventas"].min()
print("Venta mínima:", venta_minima)
print(" ====================================")
#Suma total de ventas
venta_total = df["Ventas"].sum() 
print("Suma Total de Ventas :", venta_total)
print(" ====================================")

