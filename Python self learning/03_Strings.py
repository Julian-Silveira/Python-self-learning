### Strings ### 

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string) # Esto suma un espacio la concatenacion de strings

my_new_line_string = "Este es un string\ncon salto de linea" #Salto de linea o linebreak
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un string \\nescapado"
print(my_scape_string)

### Formateo ###

name, surname, age = "Julian", "Silveira", 23
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))