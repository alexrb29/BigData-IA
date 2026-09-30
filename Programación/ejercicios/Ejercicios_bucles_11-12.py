#Ejercicio 11
#Diferencia entre i++ e ++i y i+=1 y lo mismo en negativos.

i=0
while i<=5 :
    print(i)
    i=i+1

print("\n")
y=0
while y<=5 :
    print(y)
    y+=1

# "i=i+1" es igual que "i+=1" hace lo mismo, solo que se puede expresar de forma diferente. Lo que si que me he dado cuenta es que cambia el resultado si pones primero el "i=i+1" antes que el print.


#Ejercicio 12
#Como se utiliza el enumerate y el zip

frutas = ["Uva", "Pera", "Mandarina"]

for i, frutas in enumerate(frutas):
    print(i, frutas)


#El enumerate sirve cuando quieres recorrer una lista y además saber la posición

nombres = ["Ana", "Luis", "Pedro"]
edades = [20, 25, 30]

for nombre, edad in zip(nombres, edades):
    print(nombre, edad)


#zip junta los elementos que están en la misma posición


