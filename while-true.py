acumulador = 0

while True:
    num = int(input("Infome um númerO (0 - sair): "))

    if num < 0:
        print("Não é permitido número negativo!")
        # continue #vai pular e não vai entrar numeros negativos no a
    elif num == 0:
        break
    acumulador = acumulador + num

print("Soma total: ", acumulador)