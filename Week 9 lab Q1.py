a = [10,20,30,40,50]
b = [0,0,0,0,0]
for i in range(len(a)):
    if i == 0:
        b[i] = a[i] + a[i+1]
    elif i == len(a) - 1:
        b[i] = a[i] + a[i-1]
    else:
        b[i] = a[i] + a[i+1] +a[i-1]

print(b)

