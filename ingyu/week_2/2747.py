# 피보나치수를 저장
fibo = [0,1]

# 문제에서 45번째까지 구한다고 함으로 45개를 모두 구해서 저장함
for i in range(44):
    fibo.append(fibo[i]+fibo[i+1])

# 몇 번째 인지 출력
print(fibo[int(input())])