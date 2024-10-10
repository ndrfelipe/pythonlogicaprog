quantia_horas = int(input("Insira quantas horas de atividade física você fez esse mês: "))
if quantia_horas < 10: pontos = quantia_horas*2
elif quantia_horas < 20: pontos = quantia_horas*5
else: pontos = quantia_horas*10

print("Total de pontos: ", pontos)