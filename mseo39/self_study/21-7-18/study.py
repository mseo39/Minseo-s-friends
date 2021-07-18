#용감하게 시작하는 코딩테스트 2편
#https://covenant.tistory.com/142?category=874690

#배열 초기화
N, M=map(int, input().split())
arr=[[0]*N for _ in range(M)]

#배열의 원소로 거꾸로(문제_2588)
arr.reverse()

#배열 원소 갯수(문제_2490)
list.count() #배열에 값이 몇개가 있는 지 찾을 수 있음
str.count() #배열뿐만 아니라 문자열도 가능함