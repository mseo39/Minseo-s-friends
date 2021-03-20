s= int(input())
for k in range(1,s+1):
    n=0
    total=0
    s1= input()
    for i in s1:
        if (i=="X"):
            n=0
        elif (i=="O"):
            n=n+1
            total=total+n
    print(total)
#5 OOXXOXXOOO OOXXOOXXOO OXOXOXOXOXOXOX OOOOOOOOOO OOOOXOOOOXOOOOX