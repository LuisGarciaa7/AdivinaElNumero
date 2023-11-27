import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        try:
            guess = int(input("¿Cuál es tu suposición? "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        intentos += 1

        if guess == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        elif guess < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        else:
            print("Demasiado alto. Intenta de nuevo.")

if __name__ == "__main__":
    adivina_el_numero()
