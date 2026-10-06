bateria = float(input("Bateria atual: "))
tempo = float(input("Duracao da missao: "))
consumo = float(input("Consumo por minuto: "))

if bateria < 0 or bateria > 100:
    print("Valor invalido")

elif tempo <= 0 or consumo <= 0:
    print("Valor invalido")

else:
    gasto = tempo * consumo

    if gasto <= bateria:
        restante = bateria - gasto
        print("A missao pode ser concluida")
        print("Bateria restante:", restante, "%")

    else:
        falta = gasto - bateria
        print("A missao nao pode ser concluida")
        print("Faltam", falta, "pontos percentuais de bateria")
