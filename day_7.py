import re
from collections import defaultdict

with open('data_day_7.txt') as file:
    data = file.read().splitlines()

bags = defaultdict(list)
for line in data:
    type_of_bag = re.findall(r'^(\w+ \w+) bags contain', line)[0]
    contain = re.findall(r'\d (\w+ \w+)', line)

    for bag in contain:
        bags[bag].append(type_of_bag)

result = 0
finished = False
bags_to_check = ['shiny gold']
bags_checked = set()

while not finished:

    if bags_to_check:
        bag_to_check = bags_to_check.pop()
        bag_contain = bags.get(bag_to_check, None)
        if bag_contain is not None:
            bags_checked.update(bag_contain)
            bags_to_check.extend(bag_contain)

    else:
        finished = True

print(len(bags_checked))

## second part

bags = defaultdict(list)
for line in data:
    type_of_bag = re.findall(r'^(\w+ \w+) bags contain', line)[0]
    contain_str = re.findall(r'(\d) (\w+ \w+)', line)
    contain = []
    for qty, bag in contain_str:
        contain.append((int(qty), bag))
    bags[type_of_bag].extend(contain)

count_bags = 0
bags_to_check = bags['shiny gold']
finished = False

while not finished:
    if bags_to_check:

        bag_qty, bag_to_check = bags_to_check.pop()
        count_bags += bag_qty

        new_bags_to_check = [(bag_qty * qty, bag) for qty, bag in bags[bag_to_check]]
        bags_to_check.extend(new_bags_to_check)
    else:
        finished = True

print(count_bags)
