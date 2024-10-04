
homens_cadastrados = 0
mulheres_mais_vinte = 0
idade_total = 0
mulher_velha = 0

def pesquisaIdadeSexo():
    global idade, sexo
    
    sexo = input(f"Digite o sexo da pessoa {i+1}: ( M / F ) ")
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    
for i in range(5):
    pesquisaIdadeSexo()
    if sexo == "M" or sexo == "m":
        homens_cadastrados += 1
    else:
        if idade > mulher_velha:
            mulher_velha = idade
        if idade > 20:
            mulheres_mais_vinte += 1
            
    idade_total = idade_total + idade
     
     
    
    
    
print(f"Quantos homens foram cadastrados: {homens_cadastrados}")
print(f"Idade da mulher mais velha: {mulher_velha}")
print(f"Média da idade do grupo: {(idade_total/5)}")
print(f"Quantidade de mulheres com mais de 20 anos: {mulheres_mais_vinte}")
            
