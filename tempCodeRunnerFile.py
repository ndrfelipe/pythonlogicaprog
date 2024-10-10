analisePh = 0

while analisePh != -1:
  analisePh = int(input("Digite o valor da substância: ( -1 | sair )"))
  if analisePh < 7:
    print("Substância ácida. ")
  elif analisePh > 7:
    print("Substância básica. ")
  else:
    print("Substância netura. ")
  analisePh = int(input("Digite o valor da substância: ( -1 | sair )"))