x = int(input("Enter a number: "))
sum = 0
i = x
while i > 0:
    x = i
    while x > 0:
        sum = sum + x
        x = x-1
    print(sum)
    i = i - 1
    sum =0
