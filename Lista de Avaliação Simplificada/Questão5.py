pa = 5000000
pb = 7000000
c=0
while pa < pb:
    pa = pa + pa*0.03
    pb = pb + pb*0.02
    c+=1
print("A população A ultrapassará a população B em: ", c, "anos")