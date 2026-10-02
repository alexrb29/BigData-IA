#Ejercicio 1. Control de notas
#Crea una lista llamada notas con al menos 10 calificaciones numéricas.El programa debe:Mostrar todas las notas.Calcular cuántas notas están aprobadas y cuántas suspendidas.Calcular la nota media.Mostrar la nota más alta y la nota más baja.Indicar si la media final está aprobada o suspendida.Condición: Debe utilizar listas, bucle for, operadores de comparación y condicionales.
print("Solucion ejercicio 1:\n")
notas=[2,4,7,8,5,4,3,2,9,10]
print("Las notas son:",notas)
aprobado=0
suspendido=0
suma=0
for nota in notas:
    suma=suma+nota
    if nota>=5:
        aprobado=aprobado+1
    else:
        suspendido=suspendido+1

media=suma/len(notas)
        

print("La nota mas alta es:", max(notas))
print("La nota mas baja es:",min(notas))

if media>=5:
    print("La media esta aprobada")
else:
    print("La media esta suspendida")


print("Las notas aprobadas son:",aprobado)
print("Las notas suspendidas son:",suspendido)




#Ejercicio 2. Carrito de la compra
#Mostrar cada producto con su precio.Calcular el precio total de la compra.Aplicar un descuento del 10% si el total supera 20 euros.Mostrar el total final que debe pagarse.

print("\nSolucion ejercicio 2:\n")

productos=["pan", "leche", "arroz", "jamon"]
precios=[1.20, 0.95,2.10, 50]
total=0

for producto,precio in zip(productos,precios):
    print(producto,precio)
    total+=precio

if total>20:
    descuento=total*0.1
    total=total-descuento

print(total)


#Ejercicio 3. Registro de alumno
#Mostrar todos los datos del alumno.Indicar si el alumno aprueba. Aprueba si su nota_media es mayor o igual que 5.Indicar si debe recibir un aviso. Recibe aviso si tiene más de 10 faltas.Mostrar un mensaje final combinando el resultado académico y el aviso por faltas.

print("\nSolucion ejercicio 3:\n")

alumno={"nombre":"Alex", "edad":20, "curso":"IA", "nota_media":4.5, "faltas":13}
print(alumno)

if alumno["nota_media"]>=5:
    print("Aprueba")
elif alumno["faltas"]>10:
    print("Recibe aviso")
else:
    print("Suspende")



#Ejercicio 4. Números pares, impares y múltiplos
#Contar cuántos números son pares.Contar cuántos números son impares.Contar cuántos números son múltiplos de 5.Mostrar los tres resultados finales

print("\nSolucion ejercicio 4:\n")

pares=0
impares=0
multiplos_de_5=0

for numero in range(1,51):
    if numero%2==0:
        pares+=1
    else:
        impares+=1
    if numero%5==0:
        multiplos_de_5+=1

print("Los numeros pares son: ",pares)
print("Los numeros impares son: ",impares)
print("Los multiplos de 5 son: ",multiplos_de_5)



#Ejercicio 5. Validación de contraseña
#Comprobar si la contraseña tiene al menos 8 caracteres.Comprobar si contiene el símbolo @.Comprobar que no sea igual a 12345678.Si cumple todas las condiciones, mostrar Contraseña válida.En caso contrario, mostrar Contraseña no válida.

print("\nSolucion ejercicio 5:\n")

password="F35h7k9@"

if len(password)>7 and "@" in password and password!=12345678:
    print("Contraseña válida")
else:
    print("Contraseña no válida")




#Ejercicio 6. Inventario de productos
#Mostrar todos los productos y sus unidades.Mostrar qué productos están agotados.Calcular cuántas unidades hay en total.Mostrar cuántos productos tienen menos de 10 unidades.

print("\nSolucion ejercicio 6:\n")

total_unidades=0

inventario={ "ratón":12, "teclado":5, "monitor":0, "cable":25}

print(inventario)

for producto,unidades in inventario.items():
    total_unidades=total_unidades+unidades
    if unidades==0:
        print("El producto:",producto, "esta agotado")
    if unidades<10:
        print("El producto:",producto, "tiene menos de 10 unidades")

print("Unidades totales: ",total_unidades)





#Ejercicio 7. Búsqueda en una lista
#Recorrer la lista buscando ese nombre.Si encuentra el nombre, mostrar en qué posición está.Cuando lo encuentre, detener la búsqueda.Si no lo encuentra, mostrar Alumno no encontrado.

print("\nSolucion ejercicio 7:\n")

alumnos=["Juan","Pepe", "Luis", "Marina", "Laura"]
nombre_alumno="Marina"
encontrado=False

for posicion, nombre in enumerate(alumnos):
    if nombre==nombre_alumno:
        print("El nombre se ha encontrado en la posición: ",posicion)
        encontrado=True
        break

if encontrado==False:
    print("Alumno no encontrado")





#Ejercicio 8. Limpieza de datos
#Recorrer la lista completa.Ignorar los números negativos usando continue.Sumar solo los números positivos.Contar cuántos ceros hay.Mostrar la suma final y la cantidad de ceros.

print("\nSolucion ejercicio 8:\n")

numeros=[2,-5,4.2,0,-7.8,-6,0,0.1]
num_ceros=0
suma=0
for numero in numeros:
    if numero<0:
        continue
    
    if numero>0:
        suma=suma+numero
    elif numero==0:
        num_ceros=num_ceros+1


print(suma)
print(num_ceros)


#Ejercicio 9. Clasificación de usuarios
#Clasificar como Premium a los usuarios activos con 100 puntos o más.Clasificar como Estándar a los usuarios activos con menos de 100 puntos.Clasificar como Inactivo a los usuarios que no estén activos.Además, si el usuario es menor de 18 años, debe indicarse como usuario menor de edad.Mostrar el nombre de cada usuario y su clasificación.

print("\nSolucion ejercicio 9:\n")
estandar=[]
premium=[]
inactivo=[]
menor=[]
usuarios=[
    {"nombre":"Alex", "edad":20, "activo":True,"puntos":250},
    {"nombre":"Raúl", "edad":13, "activo":False,"puntos":100},
    {"nombre":"Diego", "edad":30, "activo":False,"puntos":100},
    {"nombre":"Paula", "edad":17, "activo":True,"puntos":70}
]


for usuario in usuarios:
    if usuario["puntos"]>=100 and usuario["activo"]==True:
        premium.append(usuario["nombre"])
    elif usuario["activo"]==True and usuario["puntos"]<100:
        estandar.append(usuario["nombre"])
    elif usuario["activo"]==False:
        inactivo.append(usuario["nombre"])

    if usuario["edad"]<18:
        menor.append(usuario["nombre"])

for nombre in premium:
    print(nombre, "- Premium")

for nombre in estandar:
    print(nombre, "- Estándar")

for nombre in inactivo:
    print(nombre, "- Inactivo")

for nombre in menor:
    print(nombre, "- Menor de edad")



#Ejercicio 10. Sistema de intentos
#Recorrer todos los intentos.Mostrar cada intento realizado.Si un intento está vacío, debe entrar en una condición donde se use pass como marcador.Si un intento coincide con el código correcto, mostrar Acceso concedido y terminar el bucle.Si después de todos los intentos no se encuentra el código correcto, mostrar Acceso denegado.

print("\nSolucion ejercicio 10:\n")

codigo_correcto="567"
intentos=["154","","567", "888"]
acceso=False

for codigo in intentos:
    print(codigo)
    if codigo=="":
        pass
    elif codigo==codigo_correcto:
        print("Acceso concedido")
        acceso=True
        break
    else:
        print("Código incorrecto")

if acceso == False:
    print("Acceso denegado")
