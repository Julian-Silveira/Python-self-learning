# Variables
my_String_Variable = "My String Variable"
print (my_String_Variable) # Imprimimos invocando a la variable por su nombre

my_Int_Variable = 7
print(my_Int_Variable) # Imprimimos la variable (numero entero)

my_Int_To_Str_Variable = str(my_Int_Variable)
print(my_Int_To_Str_Variable)
print(type(my_Int_To_Str_Variable))   # Aca cambiamos el tipo de variable de entero a string, printea el tipo (Pero ya no se puede usar como numero, ahora es un string)

my_Bool_Variable = True 
print(my_Bool_Variable) # Imprimimos la variable (booleano)

# Concatenacion de Variables en un Print
# Print puede llevar diferentes argumentos, los argumentos se separan por comas dentro del print
print(my_String_Variable, my_Int_To_Str_Variable , my_Bool_Variable)
print("Este es el valor de: " , my_Bool_Variable) # Concatenar string y una variable

# Algunas funciones del sistema
print(len(my_String_Variable))  # Da el largo de un string o variable 

# Variables en una sola linea
name, surname, alias, age = "Julian" , "Silveira" , "Greedy", 23
print("Mi nombre es: ", name, surname, "Mi edad es", age, "Y mi alias es: ", alias ) 

# Inputs 

#name = input("Cual es tu nombre?")
#age = input ("Cual es tu edad?")
#print(name) 
#print(age)

# Aca arriba se esta dandole un nuevo valor a las variables mediante el input

# Cambiamos el tipo de Variable 
name = 23
age = "Julian"

print (name)
print (age) #   Esto puede generar problemas porque se pueden sobre-escribir variables existentes como en este caso.

#Quede en el minuto 1.28.00 del video de blais
