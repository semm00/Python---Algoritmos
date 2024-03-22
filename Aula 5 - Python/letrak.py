#PG (1,2,4,8,16,32...)
q = 1
g=0
while q <= 64:
    g=(2**q)-1
    q+=1
print("O somatório é {} grão(s)".format(g))
