
analisePh = int(input("Digite o valor da substância: ( -1 | sair ): "))
while analisePh != -1:
  if analisePh < 7:
    print("Substância ácida. ")
  elif analisePh > 7:
    print("Substância básica. ")
  else:
    print("Substância neutra. ")
  analisePh = int(input("Digite o valor da substância: ( -1 | sair ): "))