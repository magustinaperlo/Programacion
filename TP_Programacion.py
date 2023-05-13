#TP_Programacion

import random

from math import pi

#Funciones sin parametros
def Hello_World():
    print("Hola Mundo")
Hello_World()

def Nombre():
    nombre = "Gonzalo"
    print(f"Hola mi nombre es {nombre}")
Nombre()

def Pares():
    pares = []
    Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for i in range(len(Lista)):
        if Lista[i] % 2 == 0:
            pares.append(Lista[i])
    print(pares)
Pares()

def Impares():
    impares = []
    Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for i in range(len(Lista)):
        if Lista[i] % 2 != 0:
            impares.append(Lista[i])
    print(impares)
Impares()

def Primos():
    primos = []
    Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for num in Lista:
        if num > 1:
            B = True
            for i in range(2,num):
                if num % i == 0:
                    B = False
                    break
            if B == True:
                primos.append(num)
    print(primos)
Primos()

def Dado():
    dado = random.randint(1, 6)
    print(dado)
Dado()

def Moneda():
    moneda = random.randint(1, 2)
    if moneda == 1:
        print("Cara")
    else:
        print("Cruz")
Moneda()

def MezclarVocales():
    Lista = ["a", "e", "i", "o", "u"]
    random.shuffle(Lista)
    print(Lista)
MezclarVocales()

def Mayus():
    Lista = ["goNzALo", "jUAn", "MAtias", "juLIAN"]
    mayus = [Nombre.upper() for Nombre in Lista]
    print(mayus)
Mayus()

def Minus():
    Lista = ["goNzALo", "jUAn", "MAtias", "juLIAN"]
    minus = [Nombre.lower() for Nombre in Lista]
    print(minus)
Minus()

def Usuarios():
    Users = {1 : "Gonzalo", 2 : "Juan", 3 : "Matias", 4: "Julian" }  
    print(Users.values())
Usuarios()

def Tipos():
    Numero = 0
    Cadena = ""
    Valor = True
    print(type(Numero))
    print(type(Cadena))
    print(type(Valor))
Tipos()

def Cambiar_2_Valores():
    A = 1
    B = 2
    A, B = B, A
    print(A, B)
Cambiar_2_Valores()

def Bola8():
    Num = random.randint(1, 3)
    if Num == 1:
        print("Si")
    elif Num == 2:
        print("No")
    else:
        print("Preguntame mas tarde")
Bola8()

def Loteria():
    Lista = []
    for i in range(5):
        Num = random.randint(0, 9)
        Lista.append(Num)
    print(Lista)
Loteria()

#Funciones con parametros
def Contador(C, Guardar):
    for i in range(0, 10):
        C += 1
        Guardar.append(C)
    print(Guardar)
Contador(C = 0, Guardar = [])

def Suma(A, B):
    return(A + B)
print(Suma(A = 5, B = 8))

def Area_Rectangulo(Base, Altura):
    return(Base * Altura)
print(Area_Rectangulo(Base = 15, Altura = 10))

def Multiplo_Num(Num):
    for i in range(0, 10):
        print(Num, "x", i, "=", Num * i)
Multiplo_Num(Num = 9)

def Celsius_Fahrenheit(Celsius):
    return((Celsius * 9 / 5) + 32)
print(Celsius_Fahrenheit(Celsius = 35))

def Fahrenheit_Celsius(Fahrenheit):
    return((Fahrenheit - 32) * 5 / 9)
print(Fahrenheit_Celsius(Fahrenheit = 95))

def Num_Pos_Neg(Num):
    #print(Num)
    if Num < 0:
        return("El numero es negativo")
    elif Num > 0:
        return("El numero es positivo")
    else:
        return("El numero es nulo (0)")
print(Num_Pos_Neg(Num = random.randint(-10, 10)))

def Num_Frecuente(Lista):
    return max(set(Lista), key = Lista.count)
print(Num_Frecuente(Lista = [1, 3, 4, 5, 6, 7, 8, 9, 3, 2, 6, 3, 7, 5, 2, 1, 5, 2, 5]))

def Orden_Men_May(Lista):
    return sorted(Lista)
print(Orden_Men_May(Lista = [2, 5, 1, 8, 4, 9, 3, 6, 7]))

def Area_Circulo(Radio):
    return(pi * Radio ** 2)
print(Area_Circulo(Radio = 6))



