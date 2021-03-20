# 입력된 횟수에 따라 반복
for _ in range(int(input())):
    # 리스트에 저장
    lst = [x for x in input()]

    cnt = 1; sum = 0

    # 만약 O이 연속으로 나오면 cnt도 증가시킨다.
    for i in lst:
        if i == 'O':
            sum += cnt
            cnt += 1
        # 연속이 깨지면, cnt = 1으로 초기화
        else:
            cnt = 1

    # 점수 출력
    print(sum)