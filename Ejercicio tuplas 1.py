#Ejercicio tuplas

Tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

while True:
    try:
        Numero = int(input("Ingrese un numero entre 1 y 12 o digite 0 para salir: "))
        if Numero > 0 and Numero < 13:
            print(Tupla[Numero - 1])
        else:
            print("Numero fuera de rango")

        if Numero == 0:
            break
    except ValueError:
        print("Valor erroneo")
