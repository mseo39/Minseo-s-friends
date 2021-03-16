for i in range(int(input())):
    n = input()
    check = 0
    sum = 0
    for j in n:
        if j == 'O':
            check += 1
            sum += check
        else:
            check = 0
    print(sum)