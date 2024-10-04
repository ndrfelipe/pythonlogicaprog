banho = tosa = banho_tosa = outros = 0

def menu():
    print(" 1 - banho")
    print(" 2 - tosa")
    print(" 3 - banho e tosa")
    print(" 4 - outros")
    global opcao #transformando a variável opção em global, para que ela possa ir para o escopo do match

    opcao = int(input("Informe o serviço desejado: "))

for i in range(5):
    menu()
    match(opcao):
        case 1:
            banho +=1
        case 2:
            tosa +=1
        case 3:
            banho_tosa +=1
        case 4: 
            outros +=1
    

print(" -- Quantidade --")
print("Banho: ", banho)
print("Tosa: ", tosa)
print("Banho e tosa: ", banho_tosa)
print("Outros serviços: ", outros)