from itertools import combinations

with open('data_day_9.txt') as file:
    data = file.read()

numbers = [int(x) for x in data.split('\n')]

first_number = None

for i, num in enumerate(numbers[25:]):
    number_combi = combinations(numbers[i:i + 25], 2)
    if not any(sum(x) == num for x in number_combi):
        print(num)
        first_number = num
        break

index_invalid_num = numbers.index(first_number)

working = True
sum = numbers[0] + numbers[1]
i, j = 0, 1

while (sum != first_number):
    while (sum < first_number):
        j += 1
        sum += numbers[j]
    while (sum > first_number):
        sum -= numbers[i]
        i += 1

print(min(numbers[i:j]) + max(numbers[i:j]))
