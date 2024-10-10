valor_total = float(input("Digite o valor total da compra: (0 - sair)"))

while valor_total > 0:
  if valor_total > 100:
    valor_total = valor_total - (valor_total*0.1)
   
    print(f"O valor total com desconto é: {valor_total}")
  else:
    print(f"O valor final é: {valor_total}")
  valor_total = float(input("Digite o valor total da compra: (0 - sair)"))
