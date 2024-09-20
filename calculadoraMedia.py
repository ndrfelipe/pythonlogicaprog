n1 = int(input("Nota 1: "))
n2 = int(input("Nota 2: "))
n3 = int(input("Nota 3: "))

media = (n1 + n2 + n3)/3
print("Média: ", media)
if(media <  6):
    print("Recuperação")
else:
    print('Aprovado')