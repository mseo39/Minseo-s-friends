import sys # sys.stdin.readline() 메소드를 사용하기 위해서 sys 모듈을 임포트
sys.stdin.readline() # input() 함수와 같은 기능을 함, input() 함수보다 빠르다고 생각하면 됨
sum = 0 # 각 자리 수의 합을 저장할 변수

#   ----sys.stdin.readline() 메소드로 문자열(숫자)을 입력 받고 문자열에 대해 for 문 실행
#  |    문자열에 대해 for 문을 실행하면 한 개의 문자가 for 문의 루프마다 변수 i에 저장됨
#  |    ex) for i in 'abcd': print(i,end=' ') -> a b c d
#  |    여기서 .strip()를 붙여준 이유? -> sys.stdin.readline() 메소드는 input() 함수와 다르게 입력 받은 문자 뒤에 개행문자('\n')를 더함
#  v    개행문자를 int() 함수를 사용하여 형 변환 하면 에러가 발생하므로 strip() 메소드를 사용하여 개행문자를 제거
for i in sys.stdin.readline().strip():
    sum += int(i) # 각 자리의 수를 나타내는 문자 i를 int() 함수를 사용하여 정수형으로 변환한 뒤 변수 sum에 더함
print(sum) # 출력