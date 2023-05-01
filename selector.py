import random
print('원하는 뽑기횟수를 입력해주세요')
s = int(input())

for i in range(s):
    if i < s:
        numbers = random.sample(range(1, 46), 6)
        print(numbers)
