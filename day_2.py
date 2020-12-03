import re
from collections import Counter, namedtuple

PasswordData = namedtuple('Password_data', ['x', 'y', 'letter', 'password'])

valid_password = 0

with open('data_day_2.txt', 'r') as data:
    pass_iterator = re.finditer(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", data.read())
    passwords = [PasswordData(int(x.group(1)), int(x.group(2)), x.group(3), x.group(4)) for x in pass_iterator]

for password in passwords:
    counted_letters = Counter(password[3])
    if password.x <= counted_letters[password.letter] <= password.y:
        valid_password += 1

print(valid_password)

print('second part')
valid_password = 0

for item in passwords:
    letters_to_check = {item.password[item.x - 1], item.password[item.y - 1]}
    if len(letters_to_check) == 2 and item.letter in letters_to_check:
        valid_password += 1

print(valid_password)
