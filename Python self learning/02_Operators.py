### Operadores ### 

print( 3 + 4) ## igual 7 
print( 3 - 4) ## igual -1
print( 3 * 4) ## igual 12
print( 3 / 4) ## 0.75 
print(10 % 3) ## es el modulo
print(10 // 3) ## Float division, siempre da un numero entero aproximado.
print(2 ** 3) ## Calcular el exponente ( Dos elevado a tres )

print("Hola " + "Python" + ", Que tal?") ## Los operadores pueden tambien funcionar con variables aunque de manera limitad (no se pueden restar strings)
print("Hola " + str(5)) ## Definir varial numerica como tipo string, el dato se transforma
print("Hola " * 5) # Multiplicar strings
print("Hola " * (2 * 3)) # Operar con operadores 

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

print("aaaa" > "bbbb") ## Ordenacion alfabetica (POR ASCII), no esta contando caracteres
print(len("Hola") < len("Python")) ### Cuenta caracteres
print("Hola" >= "Python") 
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

### Operadores Logicos ###

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")

print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(not(3 > 4)) ## El not esta negando la condicion, en este caso > no falso es verdadero o "Contrario de falso es verdadero"

