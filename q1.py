mulher_mais_que_dois = 0
mulher_menos_que_Dois = 0

for i in range(10):
  print(f"Digite a quantidade de filhos da mulher {i+1}")
  filho = int(input("Digite: "))
  if filho > 2:
    mulher_mais_que_dois +=1
  else:
    mulher_menos_que_Dois +=1

print(f"Mulheres com mais de dois filhos: {mulher_mais_que_dois}")
print(f"Mulheres com maisd de dois filhos: {mulher_menos_que_Dois}")