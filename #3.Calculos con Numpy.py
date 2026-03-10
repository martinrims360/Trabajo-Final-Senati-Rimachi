#libreria SCIPY
import numpy as np
from scipy import stats
import pandas as pd
productos = pd.read_csv("SuperStoreOrders.csv")

# convertir la columna sales a número
productos["sales"] = pd.to_numeric(productos["sales"], errors="coerce")

# eliminar NaN
productos = productos.dropna(subset=["sales"])

#====================================
#CONVERSION A NUMPY
#====================================
#1.Convertir la columna Ventas del DataFrame en un array de NumPy.
df = productos[["sales"]]
array_numpy = df.to_numpy()
print(array_numpy)

#2.Usar NumPy para calcular:
#Media
media =stats.tmean(df)
print("La Media es :",media)

#Desviación estándar
desviacion=stats.tstd(df)
print("La Desviacion es :",desviacion)

#Valor máximo
maximo = np.max(df)
print("Valor máximo:", maximo)

#Valor mínimo
minimo = np.min(df)
print("Valor mínimo:", minimo)