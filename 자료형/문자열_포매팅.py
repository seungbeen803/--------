# 문자열 포매팅
a = "I eat %d apples." % 3
print(a)

number = 10
day = "three"
b = "I ate %d apples. so I was sick for %s days" % (number, day)
print(b)

# 변수 이름 따라간다
c = "aasdf {age} asdfasd fasdf {name} asdfasdf".format(name="이시형", age=3)
print(c)

name = '홍길동'
age = 30
d = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
print(d)

