import random
print('원하는 뽑기횟수를 입력해주세요')
num = int(input())

for i in range(num):
    if i < num:
        result = random.sample(range(1, 46), 6)
        print(result)
