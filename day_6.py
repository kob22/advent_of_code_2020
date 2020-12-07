with open('data_day_6.txt') as file:
    data = file.read().split("\n\n")

total_sum = 0
total_sum_yes = 0

for group in data:
    answers_set = set(group)
    answers_set.discard('\n')
    total_sum += len(answers_set)
    answers = group.splitlines()
    answers_intersection = set(answers[0])

    for answer in answers[1:]:
        answers_intersection &= set(answer)

    total_sum_yes += len(answers_intersection)

print(total_sum)
print(total_sum_yes)
