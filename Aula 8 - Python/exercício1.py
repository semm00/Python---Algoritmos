list = [6,3,11,9,7,15,20,4,18]
for i in range(len(list)-1):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print(list[::-1])