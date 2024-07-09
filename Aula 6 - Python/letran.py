a = []
for i in range(10):
    a.append(float(input(f"Digite o {i+1}° numero: ")))
a.sort()
print("A menor temperatura foi: ",a[0])
print("A maior temperatura foi: ",a[9])
print("A media das temperaturas foi: ",sum(a)/10)