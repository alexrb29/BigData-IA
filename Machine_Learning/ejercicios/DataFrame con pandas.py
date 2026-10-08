import pandas as pd

# Ejercicio 1: Estructura de datos
datos = {
    "nombre": ["Ana", "Paco", "Marta", "Luis", "Elena", "Carlos", "Sara", "Miguel", "Lucia", "Andres"],
    "edad": [23, 21, 19, 25, 22, 20, 18, 27, 21, 24],
    "puntos": [43, 38, 41, 35, 39, 36, 34, 45, 42, 37],
    "estudios_superiores": [True, False, True, False, True, True, False, False, True, False]
}

# Ejercicio 2: Crear un DataFrame
df = pd.DataFrame(datos)
print("--- Tabla completa ---")
print(df)

#Ejercicio 3: Explorar el DataFrame

print("\n--- Primeras filas ---")
print(df.head())

print("\n--- Tamaño del DataFrame ---")
print(df.shape)

print("\n--- Columnas ---")
print(df.columns)

print("\n--- Tipos de datos ---")
print(df.dtypes)

print("\n--- Información general ---")
df.info()

print("\n--- Estadísticas básicas ---")
print(df.describe())


#Ejercicio 4. Crear una regla de selección

# Lógica descrita: mayores de 22 con >=40 pts, o menores de 22 con estudios superiores y >=35 pts
condicion_mayores = (df["edad"] >= 22) & (df["puntos"] >= 40)
condicion_menores = (df["edad"] < 22) & (df["estudios_superiores"] == True) & (df["puntos"] >= 35)


#Ejercicio 5. Añadir una nueva columna

df["apto"] = condicion_mayores | condicion_menores
print(df)


#Ejercicio 6. Contar personas aptas y no aptas

print(df["apto"].value_counts())

#Ejercicio 7. Filtrar candidatos aptos

candidatos_aptos = df[df["apto"] == True]
print(candidatos_aptos)

#Ejercicio 8. Filtrar candidatos con estudios superiores

df_estudios = df[df["estudios_superiores"] == True]

print(f"Personas con estudios superiores: {len(df_estudios)}")
print(f"De ellas, son aptas: {df_estudios['apto'].sum()}")
print(f"¿Hay alguna con estudios que no sea apta?: {len(df_estudios[df_estudios['apto'] == False]) > 0}")

#Ejercicio 9. Ordenar los candidatos

# Menor a mayor
print(df.sort_values(by="puntos"))

# Mayor a menor
print(df.sort_values(by="puntos", ascending=False))

#Ejercicio 10. Calcular estadísticas

print(f"Edad media: {df['edad'].mean()}")
print(f"Puntuación media: {df['puntos'].mean()}")
print(f"Puntuación máxima: {df['puntos'].max()}")
print(f"Puntuación mínima: {df['puntos'].min()}")
print(f"Edad más joven: {df['edad'].min()}")
print(f"Edad más mayor: {df['edad'].max()}")

#Ejercicio 11. Crear una columna de nivel

def asignar_nivel(puntos):
    if puntos >= 40:
        return "alto"
    elif puntos >= 35:
        return "medio"
    else:
        return "bajo"

df["nivel"] = df["puntos"].apply(asignar_nivel)

#Ejercicio 12. Agrupar por nivel

agrupado = df.groupby("nivel").agg(
    cantidad=("nombre", "count"),
    media_edad=("edad", "mean"),
    media_puntos=("puntos", "mean")
)
print(agrupado)

#Ejercicio 13. Seleccionar columnas concretas

df_reducido = df[["nombre", "puntos", "apto"]]
print(df_reducido)

#Ejercicio 14. Renombrar columnas

df_final = df_reducido.rename(columns={
    "nombre": "Nombre del candidato",
    "puntos": "Puntuación"
})
print(df_final)

