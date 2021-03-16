fib = [0,1]
for i in range(int(input())-1):
    fib[1],fib[0] = fib[1] + fib[0],fib[1]
print(fib[1])