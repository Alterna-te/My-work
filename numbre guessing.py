import random

n = random.randint(1,10)
attempts = 0
#numero de intentos

print("adivina el numero entre 1 y 10")

while True:
    ug = int(input("adivina:"))
    attempts += 1

    if ug == n:
        print("adivinaste!")
        break
    elif n < ug:
        print("es menor")
    else:
        print("es mayor")
