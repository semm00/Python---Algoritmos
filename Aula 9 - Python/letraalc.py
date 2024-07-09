import random
a = [[ random.randint(0,10) for i in range(3)] for j in range(5)]
b = [[ random.randint(0, 10) for i in range(3)] for j in range(5)]
c = [[a[i][j] + b[i][j] for j in range(3)] for i in range(5)]
print (a)
print (b)
print (c)