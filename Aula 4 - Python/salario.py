s = float(input("Digite seu salário:"))
if s<500:
    s=s*1.15 
else:
  if s>=500 and s<=1000: s=s*1.10
  else: s=s*1.05
print("O salário é:", s)