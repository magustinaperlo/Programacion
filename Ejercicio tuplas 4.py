#Ejercicio tuplas 4

Tuplas = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
while True:
    try:

        Numero = int(input("Ingrese un numero como indice: "))

        if Numero < len(Tuplas) + 1 and Numero >= 0:
            print(Tuplas[Numero - 1])
        else:
            print("Numero fuera de rango")

    except ValueError:
        print("Valor erroneo")