for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())

    distance = (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5
    gravity = r1 + r2

    if distance > gravity:
        print(0)
    elif distance == gravity:
        print(1)
    elif distance < gravity:
        print(2)
    elif distance == 0 and r1 == r2:
        print(-1)
    elif distance == 0:
        print(0)