temperatura = int(input("Temperatura em celsius: "))

if temperatura >= 25 and temperatura <= 30:
    print("Temperatura agradável. ")
elif temperatura < 36:
    print("Clima está quente e é recomendável hidratação adequada. ")
else:
    print("Calor intenso, busque ambientes refrigerados. ")