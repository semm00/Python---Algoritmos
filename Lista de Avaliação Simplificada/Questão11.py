i = (int(input("Digite sua nota do 1° exame: ")))
ii = (int(input("Digite sua nota do 2° exame: ")))
iii = (int(input("Digite sua nota do 3° exame: ")))
iv = (int(input("Digite sua nota do 4° exame: ")))
v = (int(input("Digite sua nota do 5° exame: ")))
if i > 6.9 and ii > 6.9 and iii > 6.9 and iv > 6.9 and v > 6.9:
    print("A - passou em todos os exames")
elif i > 6.9 and ii > 6.9 and iv > 6.9 and (iii < 6.9 or v < 6.9):
    print("B - passou em i, ii e iv mas não em iii ou v")
elif i > 6.9 and ii > 6.9 and (iii > 6.9 or iv > 6.9) and v < 6.9:
    print("C - passou em i e ii, iii ou iv, mas não em v")
else:
    print("Reprovado")