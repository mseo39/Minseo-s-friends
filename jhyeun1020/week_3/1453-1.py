n = int(input())
a = [int(x) for x in input().split()]
stack = 0
seat = 100*[0]
for i in a:
    if seat[i-1] == 0:
        seat[i-1] = 1
    else:
        stack += 1
print(stack)