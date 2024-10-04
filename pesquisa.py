mulheres_mais_dois = 0
mulheres_ate_dois = 0

for i in range(10):
    print(f"Digite a quantidade de filhos da mulher {i+1}:")
    qtd_Filhos = int(input("digite: "))

    if qtd_Filhos <= 2:
        mulheres_ate_dois += 1
    elif qtd_Filhos > 2:
        mulheres_mais_dois +=1

print("\nTotal de mulheres com até 2 filhos: ", mulheres_ate_dois)
print("Total de mulheres com mais de 2 filhos: ", mulheres_mais_dois)
