pergunta = "s"

while pergunta != "n":
    total_Compra = float(input("Insira o valor total da compra: "))
    desconto = total_Compra * (10/100)
    if total_Compra > 100:
        valor_final = total_Compra - desconto
    else:
        valor_final = total_Compra

    print("Valor final: ", valor_final)
    pergunta = input("Você deseja repetir? (s / n)")

