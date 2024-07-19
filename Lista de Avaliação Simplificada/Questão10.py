p = (float(input("Insira seu peso: ")))
a = (float(input("Insira sua altura: ")))
if p%(a**2) < 18.5:
    print("Você está abaixo do peso!")
elif 18.6 < p%(a**2) < 24.9:
    print("Peso ideal, parabéns!")
elif 25 < p%(a**2) < 29.9:
    print("Levemente acima do peso!")
elif 30 < p%(a**2) < 34.9:
    print("Você está com obesidade grau I!")
elif 35 < p%(a**2) < 39.9:
    print("Você está com obesidade grau II (severa)!")
else:
    p%(a**2) > 39.9
    print("Você está com obesidade grau III (mórbida)!")