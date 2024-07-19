sm = int(input("Informe seu saldo médio: "))
if sm < 201:
    print("Saldo médio de", sm, "reais. Nenhum crédito.")
elif 200 < sm < 401:
    print(f"Saldo médio de {sm} reais. Crédito de R${sm*0.20}")
elif 400 < sm < 601:
    print(f"Saldo médio de {sm} reais. Crédito de R${sm*0.30}")
else:
    print(f"Saldo médio de {sm} reais. Crédito de R${sm*0.40}")