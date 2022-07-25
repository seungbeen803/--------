# 3. 홍길동 씨의 주민등록번호는 881120-1068234이다. 
# 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD)부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
pin = "881120-10682340"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)