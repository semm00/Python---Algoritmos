'''fib = [1, 1]
for i in range (2,15):
    proxterm = fib[i-1] + fib[i-2]
    fib += [proxterm]
print(fib)'''
p = 1
s = 1
print(p)
print(s)
for i in range(1,14):
    prox = p + s
    print(prox)
    p = s
    s = prox
print("FIM!")
    