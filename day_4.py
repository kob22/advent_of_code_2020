import re
from dataclasses import dataclass


@dataclass
class Passport:
    byr: int
    iyr: int
    eyr: int
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: str = None

    def valid_byr(self):
        return 1920 <= self.byr <= 2002

    def valid_iyr(self):
        return 2010 <= self.iyr <= 2020

    def valid_eyr(self):
        return 2020 <= self.eyr <= 2030

    def valid_hgt(self):
        if len(self.hgt) == 5 and self.hgt[-2:] == 'cm' and (150 <= int(self.hgt[:3]) <= 193):
            return True
        if len(self.hgt) == 4 and self.hgt[-2:] == 'in' and (59 <= int(self.hgt[:2]) <= 76):
            return True
        return False

    def valid_hcl(self):
        return re.match(r'^#[a-f0-9]{6}$', self.hcl)

    def valid_ecl(self):
        eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        return self.ecl in eye_colors

    def valid_pid(self):

        return re.match(r'^[\d]{9}$', self.pid)

    def valid_passport(self):
        return self.valid_byr() and self.valid_iyr() and self.valid_eyr() and self.valid_hgt() and self.valid_hcl() and self.valid_ecl() and self.valid_pid()


with open('data_day_4.txt') as file:
    data = file.read().split("\n\n")
required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

valid_passports = 0
valid_all_passport_fields = 0
for line in data:
    passport_fields = re.findall(r'([a-z]{3}):([\w#]*)', line)
    passport_data = {k: v for (k, v) in passport_fields}
    set_passport_fields = set(passport_data.keys())
    if required_fields.issubset(set_passport_fields):
        passport_data['byr'] = int(passport_data['byr'])
        passport_data['iyr'] = int(passport_data['iyr'])
        passport_data['eyr'] = int(passport_data['eyr'])
        valid_passports += 1
        passport = Passport(**passport_data)
        if passport.valid_passport():
            valid_all_passport_fields += 1
print(valid_passports)
print(valid_all_passport_fields)
