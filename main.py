import random

numero_secreto = random.randint(1, 10)
acertou = False

while not acertou:
    try:
        tentativa = int(input("Digite um número de 1 a 10: "))

        if tentativa < 1 or tentativa > 10:
            print("Digite um número inteiro de 1 a 10.")
            continue

        if tentativa == numero_secreto:
            print("Acertou!")
            acertou = True
        elif tentativa < numero_secreto:
            print("Seu chute foi menor")
        else:
            print("Seu chute foi maior")
    except ValueError:
        print("Digite apenas números inteiros!")