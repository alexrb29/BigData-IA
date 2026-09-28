# Ejercicio 1. Listas: control de notas
# Crea una lista llamada notas con cinco calificaciones: 6, 8, 5, 9 y 7.Guarda en una variable primera_nota el primer elemento de la lista.Guarda en una variable ultima_nota el último elemento de la lista.Cambia la segunda nota de la lista por un 10.Añade una nueva nota, 8, al final de la lista.Guarda en una variable total_notas la cantidad de notas que hay en la lista.Muestra por consola la lista final, la primera nota, la última nota y el total de notas.


print("Solución del ejercicio 1 \n")

notas=[6,8,5,9,7]

primera_nota=notas[0]
ultima_nota=notas[-1]
notas[1]=10
notas.append(8)
total_notas=len(notas)

print("La lista final es:",notas)
print("La primera nota es:",primera_nota)
print("La última nota es:",ultima_nota)
print("La lista final es:",total_notas)




# Ejercicio 2. Tuplas: datos fijos de un producto
#Crea una tupla llamada producto con tres datos: nombre del producto, precio y unidades disponibles.Por ejemplo: ("teclado", 25.50, 12).Guarda cada dato de la tupla en una variable diferente: nombre, precio y unidades.Calcula el valor total del stock multiplicando precio por unidades.Muestra por consola el nombre del producto, el precio, las unidades y el valor total del stock.

print("\nSolución del ejercicio 2\n")

producto=("pelota", 15.50, 10)

nombre="Pelota"
precio=15.50
unidades=10
valor_total_stock=precio*unidades

print("El nombre del producto es:",nombre)
print("El precio es:",precio)
print("Las unidades son:",unidades)
print("El valor total de stock es:",valor_total_stock)






#Ejercicio 3. Diccionarios: ficha de alumno
# Crea un diccionario llamado alumno.El diccionario debe tener estas claves: nombre, edad, curso y nota.Usa valores concretos, por ejemplo: "Ana", 16, "IA" y 7.5.Muestra por consola el nombre del alumno usando la clave nombre.Muestra por consola la nota del alumno usando la clave nota.Cambia la nota del alumno por otro valor.Añade una nueva clave llamada aprobado. Su valor debe ser el resultado de comprobar si la nota es mayor o igual que 5.Muestra por consola el diccionario completo al final.

print("\nSolución del ejercicio 3\n")

alumno={"nombre":"Alex", "edad": 20, "curso": "IA", "nota": 6.5}

print("El nombre del alumno es: ",alumno["nombre"])
print("La nota del alumno es: ",alumno ["nota"])

alumno["nota"]=8
alumno["aprobado"]=alumno["nota"] >=5
print("El diccionario final es:",alumno)




#Ejercicio 4. Conjuntos: usuarios registrados
#Crea un conjunto llamado usuarios con estos nombres: Ana, Luis, Marta, Ana y Pedro.Crea una variable nuevo_usuario con el valor "Luis".Crea una variable usuario_existe que compruebe si nuevo_usuario está dentro del conjunto.Añade el usuario "Clara" al conjunto.Crea una variable total_usuarios con el número de usuarios únicos.Muestra por consola el conjunto final, usuario_existe y total_usuarios.

print("\nSolución del ejercicio 4\n")

usuarios={"Ana", "Luis", "Marta", "Ana", "Pedro"}
nuevo_usuario= "Luis"
usuario_existente= nuevo_usuario in usuarios
usuarios.add("Clara")
total_usuarios=len(usuarios)
print("El conjunto final es: ",usuarios)
print("Usuario existente: ",usuario_existente)
print("El total usuarios es: ",total_usuarios)




#Ejercicio 5. Condiciones con and, or y not
#Crea las variables edad, tiene_permiso, es_socio y sancionado.Asigna valores concretos a esas variables.Crea una variable acceso_por_edad que sea True si la persona tiene al menos 16 años y tiene permiso.Crea una variable acceso_por_socio que sea True si la persona es socio y no está sancionada.Crea una variable puede_acceder que sea True si se cumple acceso_por_edad o acceso_por_socio.Muestra por consola las tres variables: acceso_por_edad, acceso_por_socio y puede_acceder.
print("\nSolución del ejercicio 5\n")

edad=20
tiene_permiso=True
es_socio=False
sancionado=False

if edad>15 and tiene_permiso==True:
    acceso_por_edad=True
else:
    acceso_por_edad=False

if es_socio==True and sancionado==False:
    acceso_por_socio=True
else:
    acceso_por_socio=False

if acceso_por_socio==True or acceso_por_edad==True:
    puede_acceder=True
else:
    puede_acceder=False

print("Acceso por edad: ",acceso_por_edad)
print("Acceso por socio: ",acceso_por_socio)
print("Puede acceder: ",puede_acceder)
