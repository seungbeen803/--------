# 리스트 관련 함수

# 리스트에 요소 추가(append)
a = [1, 2, 3]
a.append(4) # 리스트의 맨 마지막에 값 추가
print(a)
a.append([5, 6])
print(a)

# 리스트 정렬(sort)
a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.sort()
print(a)

# 리스트 뒤집기(reverse)
a = ['a', 'c', 'b']
a.reverse()
print(a)

# 위치 반환(index)
a = [1, 2, 3, 'home']
print(a.index(3))
print(a.index('home'))

# 값이 없기 때문에 에러가 발생한다.
# print(a.index(0)) 

# 리스트에 요소 삽입(insert)
a = [1, 2, 3]
a.insert(0, 4)
print(a)
a.insert(3, 5)
print(a)

# 리스트 요소 제거(remove)
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
a.remove(3)
print(a)

# (*) 리스트 요소 끄집어내기(pop)
a = [1, 2, 3] # 맨 마지막에 있는 요소를 꺼냄
a.pop()
print(a)

# 괄호 안에 값이 있을 경우
b = [1, 2, 5, 6]
print(b.pop(2))

# 리스트에 포함된 요소 x의 개수 세기(count)
a = [1, 2, 3, 1, 4, 1]
print(a.count(1))

# 리스트 확장(extend)
a = [1, 2, 3]
a.extend([4, 5]) # 괄호 안에는 리스트만 올 수 있다
print(a)
b = [6, 7]
a.extend(b)
print(a)