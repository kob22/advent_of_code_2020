with open('data_day_8.txt') as file:
    data = file.read()

instructions = []

for line in data.split('\n'):
    instruction = line.split()
    instructions.append((instruction[0], int(instruction[1])))

accumulator = 0
executed = set()
terminate = False
index = 0

while not terminate:

    if index not in executed:
        operation = instructions[index][0]
        value = instructions[index][1]
        executed.add(index)

        if operation == 'acc':
            accumulator += value
            index += 1
        elif operation == 'jmp':
            index += value
        elif operation == 'nop':
            index += 1

    else:
        terminate = True

print(accumulator)

# part two

not_working_swaps = set()
terminate = False
finished = len(instructions)

accumulator = 0
executed = set()
index = 0
swapped = False

while not terminate:
    if index not in executed:
        operation = instructions[index][0]
        value = instructions[index][1]
        executed.add(index)

        if operation == 'acc':
            accumulator += value
            index += 1

        elif operation == 'jmp':
            if not swapped and index not in not_working_swaps:
                swapped = True
                not_working_swaps.add(index)
                index += 1
            else:
                index += value

        elif operation == 'nop':
            if not swapped and index not in not_working_swaps:
                swapped = True
                not_working_swaps.add(index)
                index += value
            else:
                index += 1

    else:
        accumulator = 0
        executed = set()
        index = 0
        swapped = False

    if index >= finished:
        terminate = True

print(accumulator)
