def fib1(n):
    if n == 1 or n == 2:
        return(1)
    else:
        return(fib1(n-1) + fib1(n-2))

def fib2(n):
    i = 1
    while i <= n:
        print(fib1(i))
        i += 1


print(fib1(7))
fib2(7)
    