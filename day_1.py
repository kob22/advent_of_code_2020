with open('data_day_1.txt', 'r') as data:
    numbers = [int(x) for x in data.readlines()]

solution = set([x * y for x in numbers for y in numbers if x + y == 2020])
print(solution)

solution_part_two = set([x * y * z for x in numbers for y in numbers for z in numbers if x + y + z== 2020])
print(solution_part_two)