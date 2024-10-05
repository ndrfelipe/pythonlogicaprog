
pergunta = "S"

while pergunta != "n" and pergunta != "N":
    valor_inicial_investimento = float(input("Digite o valor inicial do investimento: "))
    taxa_juros_anual = float(input("Digite a taxa de juros anual: "))
    numero_de_anos = int(input("Digite o número de anos para o investimento: "))

    for i in range(numero_de_anos):
        valor_inicial_investimento = valor_inicial_investimento * ( 1 + (taxa_juros_anual)/100)
        print(f"O investimento no ano {i+1} foi de {valor_inicial_investimento}")
        
    pergunta = input("Deseja realizar outra operação? ( S / N )")

