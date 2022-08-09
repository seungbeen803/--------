# 2411 최승빈
# 5. 학생들의 점수를 입력받고, 점수대별로 해당 학생 수 만큼 '*'가 표시되는 프로그램을 작성하시오.
# (단, 점수는 0~100 사이의 값들만 들어온다고 가정한다.)

scores = input("점수 입력 : ")
score = scores.split(' ')
count = [0,0,0,0,0]

# 점수 비교한 후 카운트해주기
for i in score:
    if int(i) >= 90:
        count[0] += 1
    elif int(i) >= 80:
        count[1] += 2
    elif int(i) >= 70:
        count[2] += 1
    elif int(i) >= 60:
        count[3] += 1
    else:
        count[4] += 1

# 출력
print("90점 이상        : ", "*"*count[0])
print("80점 대          : ", "*"*count[1])
print("70점 대          : ", "*"*count[2])
print("60점 대          : ", "*"*count[3])
print("60점 미만        : ", "*"*count[4])

# 최대, 최소 구하기(함수 이용)
max_value = max(score)
min_value = min(score)

# 출력
print("최고점수 : ", max_value)
print("최저점수 : ", min_value)