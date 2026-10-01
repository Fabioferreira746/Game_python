import random
VERDE = "\033[32m"
VERMELHO = "\033[31m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m"  

numero_secreto = random.randint(1, 10)
acertou = False

print(f"{AZUL}=== JOGO DO NÚMERO SECRETO ==={RESET}")

while not acertou:
    try:
        tentativa = int(input(f"{AZUL}Digite um número de 1 a 10: {RESET}"))

        if tentativa < 1 or tentativa > 10:
            print(f"{AMARELO}Digite um número inteiro de 1 a 10.{RESET}")
            continue

        if tentativa == numero_secreto:
            print(f"{VERDE}Parabéns! Você acertou!{RESET}")
            acertou = True
        elif tentativa < numero_secreto:
            print(f"{VERMELHO}Seu chute foi menor.{RESET}")
        else:
            print(f"{VERMELHO}Seu chute foi maior.{RESET}")
    except ValueError:
        print(f"{AMARELO}Erro: Digite apenas números inteiros!{RESET}")