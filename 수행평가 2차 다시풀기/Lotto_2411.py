# 2411 최승빈
import random

def func_lotto(num):
    for r in range(1, 11):
        for i in range(7):
            n = random.randint(1, 45)
        print("당첨번호 : ", n)
func_lotto(6)