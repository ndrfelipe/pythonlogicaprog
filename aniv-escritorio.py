valor_bolo = float(input("Escreva o valor do bolo: "))
salgado1 = float(input("Escreva o valor do salgado 1: "))
qt1 = float(input("A quantidade do salgado 1: "))

salgado2 = float(input("Escreva o valor do salgado 2: "))
qt2 = float(input("A quantidade do valor 2: "))

salgado3 = float(input("Digite o valor do salgado 3: "))
qt3 = float(input("Quantidade do salgado 3: "))

valor_total = (valor_bolo + (qt1*salgado1) + (qt2*salgado2) + (qt3*salgado3)) / 11

print(f"O valor total pago por cada membro da festa é {valor_total:f.2}")