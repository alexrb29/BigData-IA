#Ejercicios de estadística básica con CSV
#Cada cálculo se resuelve con tres métodos:
#  Metodo 1: Python elemental (for, if, acumuladores)
#  Metodo 2: Python funcional (map, filter, lambda, sorted, sum, min, max, set, count)
#  Metodo 3: pandas

import math
import pandas as pd


def comparar(nombre, bucle, funciones, pandas_):
    """Muestra los tres resultados y comprueba si coinciden.
    Se usa math.isclose porque los decimales pueden variar mínimamente."""
    print(f"{nombre}_bucle     =", bucle)
    print(f"{nombre}_funciones =", funciones)
    print(f"{nombre}_pandas    =", pandas_)

    if isinstance(bucle, list):
        iguales = len(bucle) == len(funciones) == len(pandas_)
        for a, b, c in zip(bucle, funciones, pandas_):
            if isinstance(a, str):
                iguales = iguales and a == b == c
            else:
                iguales = iguales and math.isclose(a, b) and math.isclose(a, c)
    else:
        iguales = math.isclose(bucle, funciones) and math.isclose(bucle, pandas_)

    print("¿Coinciden los tres métodos?", "Sí" if iguales else "No")
    return iguales


def redondear(lista, decimales=4):
    """Redondea una lista para que se lea mejor por consola."""
    return [round(x, decimales) for x in lista]




#Ejercicio 1. Carga y exploracion de datos

print("SOLUCIÓN DEL EJERCICIO 1\n")

df = pd.read_csv("datos_estadistica_alumnos.csv")
puntos = list(df["puntos_prueba"])
nombres = list(df["nombre"])

#Metodo 1: recorremos las 5 primeras posiciones con un contador
print("Primeras filas (bucle):")
contador = 0
for nombre, punto in zip(nombres, puntos):
    if contador == 5:
        break
    print(" ", nombre, "->", punto, "puntos")
    contador += 1

#Metodo 2: zip une nombres y puntos y el slicing se queda con 5
print("\nPrimeras filas (funciones):")
print(list(zip(nombres, puntos))[:5])

#Metodo 3: head() de pandas
print("\nPrimeras filas (pandas):")
print(df.head())

cantidad_datos = len(puntos)
print("\nCantidad de datos:", cantidad_datos)
print("Cada fila representa a un alumno: su id, su nombre, las horas que ha estudiado,")
print("los puntos que sacó en la prueba, los ejercicios entregados y los minutos en la plataforma.")




#Ejercicio 2. Media

print("\nSOLUCIÓN DEL EJERCICIO 2\n")

#Metodo 1: acumulador con for
suma = 0
for valor in puntos:
    suma += valor
media_bucle = suma / len(puntos)

#Metodo 2: sum + map con lambda
media_funciones = sum(map(lambda x: x, puntos)) / len(puntos)

#Metodo 3: pandas
media_pandas = df["puntos_prueba"].mean()

comparar("media", media_bucle, media_funciones, media_pandas)
print(f"De media, cada alumno ha sacado {media_bucle} puntos en la prueba.")

#A partir de aquí reutilizamos esta media en vez de volver a calcularla
media = media_bucle




#Ejercicio 3. Mediana

print("\nSOLUCIÓN DEL EJERCICIO 3\n")

#Metodo 1: ordenamos una copia con el método de la burbuja
lista_ordenada = puntos.copy()
n = len(lista_ordenada)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if lista_ordenada[j] > lista_ordenada[j + 1]:
            temporal = lista_ordenada[j]
            lista_ordenada[j] = lista_ordenada[j + 1]
            lista_ordenada[j + 1] = temporal

if n % 2 == 0:
    centro_izq = lista_ordenada[n // 2 - 1]
    centro_der = lista_ordenada[n // 2]
    mediana_bucle = (centro_izq + centro_der) / 2
else:
    mediana_bucle = lista_ordenada[n // 2]

#Metodo 2: sorted, len y acceso por índice
ordenada = sorted(puntos)
mitad = len(ordenada) // 2
if len(ordenada) % 2 == 0:
    mediana_funciones = sum(ordenada[mitad - 1:mitad + 1]) / 2
else:
    mediana_funciones = ordenada[mitad]

#Metodo 3: pandas
mediana_pandas = df["puntos_prueba"].median()

comparar("mediana", mediana_bucle, mediana_funciones, mediana_pandas)
print("Lista ordenada:", lista_ordenada)
print("Como hay 10 datos (par), la mediana es la media de los dos centrales (70 y 80).")
print("Representa el centro porque deja la mitad de los alumnos por debajo y la otra mitad por encima.")




#Ejercicio 4. Moda

print("\nSOLUCIÓN DEL EJERCICIO 4\n")

#Metodo 1: diccionario de frecuencias con un bucle
frecuencias = {}
for valor in puntos:
    if valor in frecuencias:
        frecuencias[valor] += 1
    else:
        frecuencias[valor] = 1

max_frecuencia = 0
moda_bucle = None
for valor in frecuencias:
    if frecuencias[valor] > max_frecuencia:
        max_frecuencia = frecuencias[valor]
        moda_bucle = valor

#Metodo 2: set quita repetidos, count cuenta y max se queda con el más repetido
moda_funciones = max(set(puntos), key=lambda v: puntos.count(v))

#Metodo 3: pandas (mode devuelve una Series, cogemos el primer valor)
moda_pandas = df["puntos_prueba"].mode()[0]

comparar("moda", moda_bucle, moda_funciones, moda_pandas)
print("Frecuencias:", frecuencias)
print(f"La moda es {moda_bucle}: es la puntuación más repetida ({max_frecuencia} alumnos la sacaron).")




#Ejercicio 5. Desviación de cada dato respecto a la media

print("\nSOLUCIÓN DEL EJERCICIO 5\n")

print("Media:", media)

#Metodo 1: for + append
desviaciones_bucle = []
for valor in puntos:
    desviaciones_bucle.append(valor - media)

#Metodo 2: map + lambda
desviaciones_funciones = list(map(lambda x: x - media, puntos))

#Metodo 3: pandas, nueva columna desviacion
df["desviacion"] = df["puntos_prueba"] - df["puntos_prueba"].mean()
desviaciones_pandas = list(df["desviacion"])

comparar("desviaciones", desviaciones_bucle, desviaciones_funciones, desviaciones_pandas)
print("Suma de las desviaciones:", sum(desviaciones_bucle), "(siempre da 0)")
print("Positiva: el alumno está por encima de la media. Negativa: por debajo. Cero: justo en la media.")




#Ejercicio 6. Varianza (poblacional, dividimos entre n)

print("\nSOLUCIÓN DEL EJERCICIO 6\n")

#Metodo 1: desviación -> cuadrado -> acumulamos -> promedio
suma_desv_cuadrado = 0
for valor in puntos:
    desviacion = valor - media
    suma_desv_cuadrado += desviacion ** 2
varianza_bucle = suma_desv_cuadrado / len(puntos)

#Metodo 2: map con lambda para los cuadrados, sum y len
cuadrados = list(map(lambda x: (x - media) ** 2, puntos))
varianza_funciones = sum(cuadrados) / len(cuadrados)

#Metodo 3: pandas con ddof=0 (si no, divide entre n-1)
varianza_pandas = df["puntos_prueba"].var(ddof=0)

comparar("varianza", varianza_bucle, varianza_funciones, varianza_pandas)
print("La varianza mide cuánto se separan los datos de la media (en puntos al cuadrado).")
print("Cuanto mayor es, más diferentes son las notas de los alumnos entre sí.")




#Ejercicio 7. Desviación estándar

print("\nSOLUCIÓN DEL EJERCICIO 7\n")

#Metodo 1: raíz cuadrada de la varianza calculada con bucles
desviacion_estandar_bucle = varianza_bucle ** 0.5

#Metodo 2: map, lambda, sum, len y math.sqrt
desviacion_estandar_funciones = math.sqrt(
    sum(map(lambda x: (x - media) ** 2, puntos)) / len(puntos)
)

#Metodo 3: pandas con ddof=0
desviacion_estandar_pandas = df["puntos_prueba"].std(ddof=0)

comparar("desviacion_estandar", desviacion_estandar_bucle,
         desviacion_estandar_funciones, desviacion_estandar_pandas)
print(f"Las notas se separan de la media unos {desviacion_estandar_bucle:.2f} puntos.")
print("Es más fácil de interpretar que la varianza porque está en puntos, no en puntos al cuadrado.")




#Ejercicio 8. Normalización min-max

print("\nSOLUCIÓN DEL EJERCICIO 8\n")

#Metodo 1: buscamos mínimo y máximo con un bucle
#(no llamamos a las variables min y max para no tapar las funciones de Python)
minimo = puntos[0]
maximo = puntos[0]
for valor in puntos:
    if valor < minimo:
        minimo = valor
    if valor > maximo:
        maximo = valor

normalizados_bucle = []
for valor in puntos:
    normalizados_bucle.append((valor - minimo) / (maximo - minimo))

#Metodo 2: min, max, map y lambda
rango = max(puntos) - min(puntos)
normalizados_funciones = list(map(lambda x: (x - min(puntos)) / rango, puntos))

#Metodo 3: pandas, nueva columna puntos_normalizados
columna = df["puntos_prueba"]
df["puntos_normalizados"] = (columna - columna.min()) / (columna.max() - columna.min())
normalizados_pandas = list(df["puntos_normalizados"])

print("Mínimo:", minimo, "| Máximo:", maximo)
comparar("normalizados", normalizados_bucle, normalizados_funciones, normalizados_pandas)
print("0 es la nota más baja (50), 1 la más alta (100) y 0.5 quedaría justo en medio (75).")




#Ejercicio 9. Estandarización z-score

print("\nSOLUCIÓN DEL EJERCICIO 9\n")

desviacion_est = desviacion_estandar_bucle
print("Media:", media, "| Desviación estándar:", round(desviacion_est, 4))

#Metodo 1: for + append
z_bucle = []
for valor in puntos:
    z_bucle.append((valor - media) / desviacion_est)

#Metodo 2: map + lambda con las variables ya calculadas
z_funciones = list(map(lambda x: (x - media) / desviacion_est, puntos))

#Metodo 3: pandas, nueva columna puntos_estandarizados
df["puntos_estandarizados"] = (columna - columna.mean()) / columna.std(ddof=0)
z_pandas = list(df["puntos_estandarizados"])

comparar("estandarizados", redondear(z_bucle), redondear(z_funciones), redondear(z_pandas))
print("z positivo: por encima de la media. z negativo: por debajo.")
print("z cercano a 0: el alumno está muy cerca de la media.")




#Ejercicio 10. Interpretación final

print("\nSOLUCIÓN DEL EJERCICIO 10\n")

#--- Por encima de la media ---
#Metodo 1
por_encima_bucle = []
for i in range(len(puntos)):
    if puntos[i] > media:
        por_encima_bucle.append(nombres[i])

#Metodo 2: filter sobre parejas (nombre, puntos) y map para quedarnos con el nombre
por_encima_funciones = list(map(lambda p: p[0], filter(lambda p: p[1] > media, zip(nombres, puntos))))

#Metodo 3: filtrado con condición sobre la columna
por_encima_pandas = list(df[df["puntos_prueba"] > media]["nombre"])

print("Por encima de la media:")
comparar("por_encima", por_encima_bucle, por_encima_funciones, por_encima_pandas)

#--- Por debajo de la media ---
#Metodo 1
por_debajo_bucle = []
for i in range(len(puntos)):
    if puntos[i] < media:
        por_debajo_bucle.append(nombres[i])

#Metodo 2
por_debajo_funciones = list(map(lambda p: p[0], filter(lambda p: p[1] < media, zip(nombres, puntos))))

#Metodo 3
por_debajo_pandas = list(df[df["puntos_prueba"] < media]["nombre"])

print("\nPor debajo de la media:")
comparar("por_debajo", por_debajo_bucle, por_debajo_funciones, por_debajo_pandas)

#--- Valor normalizado más alto y más bajo ---
norm_max = df["puntos_normalizados"].max()
norm_min = df["puntos_normalizados"].min()
mejores = list(df[df["puntos_normalizados"] == norm_max]["nombre"])
peores = list(df[df["puntos_normalizados"] == norm_min]["nombre"])
print("\nValor normalizado más alto (", norm_max, "):", mejores)
print("Valor normalizado más bajo (", norm_min, "):", peores)

#--- ¿Algún valor alejado? Usamos el criterio |z| > 2 ---
alejados = [nombres[i] for i in range(len(z_bucle)) if abs(z_bucle[i]) > 2]
z_max = max(z_bucle, key=abs)
print("\nMayor |z|:", round(abs(z_max), 2), "->", nombres[z_bucle.index(z_max)])
if alejados:
    print("Valores especialmente alejados (|z| > 2):", alejados)
else:
    print("Ningún alumno tiene |z| > 2, así que no hay valores atípicos claros.")
    print("Lo más alejado son los extremos: Lucía (100) por arriba y Ana (50) por abajo.")

#--- Conclusión ---
print("\nConclusión:")
print(f"El grupo tiene una media de {media} puntos, una mediana de {mediana_bucle} y una moda de {moda_bucle}.")
print(f"La desviación estándar es de unos {desviacion_est:.2f} puntos, una dispersión moderada.")
print("Media y mediana están muy próximas, por lo que los datos están bastante equilibrados.")
print(f"{len(por_encima_bucle)} alumnos superan la media y {len(por_debajo_bucle)} quedan por debajo;")
print("en general el rendimiento del grupo es aceptable, con la mayoría entre 60 y 80 puntos.")
