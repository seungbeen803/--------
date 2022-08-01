# 리스트의 인덱싱과 슬라이싱

# 인덱싱
from re import L


a = [1, 2, 3]
print(a)
print(a[0])
print(a[0] + a[2])
print(a[-1])

b = [1, 2, 3, ['a', 'b', 'c']]
print(b)
print(b[0])
print(b[-1])
print(b[3])

# 이중 리스트 인덱싱
print(b[-1][0])
print(b[-1][1])
print(b[-1][2])

# 삼중 리스트 인덱싱
c = [1, 2, ['a', 'b', ['Life', 'is']]]
print(c[2][2][0])

# 슬라이싱
d = [1, 2, 3, 4, 5]
print(d[0:2])

e = "12345"
print(e[0:2])

l = [1, 2, 3, 4, 5]
i = l[:2]
s = l[2:]
t = l[::-1]
print(i)
print(s)
print(t)

# 중첩된 리스트에서 슬라이싱하기
list = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(list[2:5])
print(list[3][:2])