# Aula de estrutura de repetição.
# contador em python:
# cont += 1

# estrutura do for
# for i in range(0, 5, 1): ou for i in range(5):
# for i in range(1, 5, 2): pulando em de 2 em 2 casas

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in num:
#     if(i == num):
#         break
#     else:
#         print(i)

num = int(input("Infome um número positivo (0 - sair): "))
acumulador = 0 #acumulador precisa ser iniciado com 0

while (num != 0):
    if num < 0:
        print(f" {num} não é válido pois é negativo \n")
    else:
        acumulador = acumulador + num
    
    num = int(input("Infome um número positivo (0 - sair): "))
print("A soma dos números informados pelo usuário: ", acumulador)