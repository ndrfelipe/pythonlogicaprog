def calcularFatorial(numero):
    fatorial = 1
    i = 1
    
    while i <= numero:
        fatorial*=i
        i+=1
    return fatorial
    
pergunta = input("Deseja fazer uma operação? (S / N): ")

while pergunta != "n" and pergunta != "N":
    numero = int(input("Digite um número inteiro positivo: "))
    print(f"O fatorial de {numero} é {calcularFatorial(numero)}")

    pergunta = input("Deseja fazer outra operação? (S / N): ")

