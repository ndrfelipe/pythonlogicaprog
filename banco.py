# Otimização de solicitações de empréstimo para a compra de uma casa.
import os



def recebimentoDados():
    global salario_comprador, pretacao_mensal, valor_casa
    os.system("cls")
    
    valor_casa = float(input("Digite o valor da casa desejada: "))
    salario_comprador = float(input("Digite o salário do comprador: "))
    prazo_anos = float(input("Digite o prazo de pagamentos em anos: "))
    pretacao_mensal = valor_casa/(prazo_anos*12)
    
continuar = 1
while continuar != 0:
    recebimentoDados()
    if pretacao_mensal > (salario_comprador*0.3):
        print(f"Empréstimo não aprovado, prestação mensal: {pretacao_mensal}")
    else:
        print("Empréstimo aprovado. ")
        print(f"Prestação mensal é de: {pretacao_mensal}")

    continuar = int(input("Deseja continuar? (1 - sim,  0 - não ): "))
    

print("\n Programa finalizado. ")
