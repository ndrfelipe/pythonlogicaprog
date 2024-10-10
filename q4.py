continuar = 1
while continuar != 0:
  valor_casa = float(input("Digite o valor da casa: "))
  salario = float(input("Digite o salário: "))
  prazo = float(input("Digite o prazo em anos: "))

  prestacao_mensal = valor_casa/(prazo*12)
  excendente = salario*0.3

  if prestacao_mensal > excendente:
    print("Empréstimo negado. ")
  else:
    print("Empréstimo aceito: ")

  continuar = int(input("Deseja fazer outro empréstimo? ( 1 = S / 0 = N)"))