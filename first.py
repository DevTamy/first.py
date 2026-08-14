# Isso e um comentario
"""""
Isto é um comentario em uma linha e em varias linhas
"""""

# Como consultar o tipo de dado
print(type('sou um dado str'))  # Tipo 'str'
print(type(5)) #tipo int
print(type(5.5)) #tipo float
print(type(True)) #tipo bool
print(type(print('Minha cadeia de texto'))) #tipo 'NoneType'


# Variaveis
my_string_variavel = "My string variavel"
print(my_string_variavel)

my_int_variavel = 5
print(my_int_variavel)

my_bool_variavel = True
print(my_bool_variavel)

# Concatenacao de variavel em um print
print(type(print(my_string_variavel)))  # Tipo NoneType
print('Esse e o valor do:', my_bool_variavel)

# Algumas Funcoes do sistema
print(len(my_string_variavel)) 

# Variaveis em uma linha
name, surname, apelido, age = "Tannie", "Lima", "Tamy", 19
print("Meu nome é",name, surname, "Minha idade é:", age, "Meu apelido é:", apelido)

# Inputs
""""""""""
name = input("Qual seu nome? ")
age = input("Qual sua idade? ")
print("Meu nome é", name, "e minha idade é:", age)
"""""""""
# Forzamos o tipo?
address: str = 'Minha Direção'
address = 32
address = True
address = 3.14
print(type(address))
