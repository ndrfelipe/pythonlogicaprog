# salario = salarioFixo + comissaoFixa + (vendas * 5/100)
nome = input("Digite o nome do funcionário: ")
vendasCarro = int(input("Digite o total de carros vendidos: "))
vendasTotal = int(input("Digite o total de vendas por mês: "))
salarioFixo = int(input("Digite o salário fixo: "))
comissao = int(input("Comissão por carro vendido: "))

comissaoFixa = comissao * vendasCarro

salarioFinal = salarioFixo + comissaoFixa + ( vendasTotal* 0.05)

print("O salário final de", nome, " é R$",salarioFinal)
