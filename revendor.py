# salario = salarioFixo + comissaoFixa + (vendas * 5/100)
nome = input("Digite o nome do funcionário: ")
vendas_carro = float(input("Digite o total de carros vendidos: "))
vendas_total = float(input("Digite o total de vendas por mês: "))
salario_fixo = float(input("Digite o salário fixo: "))
comissao = int(input("Comissão por carro vendido: "))

comissao_fixa = comissao * vendas_carro

salario_final = salario_fixo + comissao_fixa + ( vendas_total* 0.05)

print("O salário final de", nome, " é R$",salario_final)
