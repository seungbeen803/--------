# 문자열 관련 함수

#  문자 개수 세기(count)
a = "hobby"
print(a.count("b"))

# 위치 알려주기 1(find)
f = "Python is the best choice"
print(f.find('b'))

# 값이 없으면 -1을 반환함
print(f.find('k'))

# 위치 알려주기 2(index)
i = "Life is too short"
print(i.index('t'))

# 에러 발생
# print(i.index('k'))

# 문자열 삽입(join)
j = ",".join('abcd')
print(j)

print(",".join(['a', 'b', 'c', 'd']))

print(":".join('abcd'))

# 소문자를 대문자로 바꾸기(upper)
u = "hi"
print(u.upper())

# 대문자를 소문자로 바꾸기(lower)
l = "HI"
print(l.lower())

# 왼쪽 공백 지우기(lstrip)
left = " hi "
print(left.lstrip())

# 오른쪽 공백 지우기(rstrip)
right = " hi "
print(right.rstrip())

# 양쪽 공백 지우기(strip)
justyfiy = " hi "
print(justyfiy.strip())

# 문자열 바꾸기(replace)
replay = "Life is too short"
print(replay.replace("Life", "Your leg"))

# 문자열 나누기(split)
str = "Life is too short"
print(str.split())

str1 = "a:b:c:d"
print(str1.split(':'))