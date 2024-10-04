

valorPh = float(input("Digite o valor da substância (-1 - sair): "))
while valorPh != -1:
    if valorPh >= 0 and valorPh < 7:
        print("A substância é ácida")
    elif valorPh > 7:
        print("A substância é básica")
    else:
        print("A substância é neutra")
        
    valorPh = float(input("Digite o valor da substância (-1 - sair): "))
    
print("Programa finalizado. ")