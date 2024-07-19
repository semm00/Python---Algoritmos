while True:
    sb = (int(input("Digite seu salário bruto: ")))
    if sb < 1501:
        sl = sb*0.95
        im = sb*0.05
    elif sb > 1500 and sb < 3001:
        sl = sb*0.92
        im = sb*0.08
    elif sb > 3000 and sb < 10001:
        sl = sb*0.85
        im = sb*0.15
    else:
        sl = sb*0.73
        im = sb*0.27   
    print("Seu salário bruto é: {}; Seu salário líquido é: {} e o imposto é: {}".format(sb, sl, im))
    continuar = input("Deseja continuar? (SIM/NÃO) ")
    if continuar == "NÃO":
        break
