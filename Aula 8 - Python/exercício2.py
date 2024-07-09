list = [6,3,11,9,7,15,20,4,18]
max = list[0]
min = list[0]
for i in list[1:]:
    if i>max:
        max = i
    else:
        if i<min: 
            min = i
print(max)
print(min)