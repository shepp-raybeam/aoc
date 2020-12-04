import re

from aoc import AocDay

class day4(AocDay):
    pattern = r'(byr|iyr|eyr|hgt|hcl|ecl|pid|cid):(\S+)'
    passports = []
    
    def __init__(self, day):
        AocDay.__init__(self, day)
        self.process_passports()    
    
    def process_passports(self):
        """idk why this misses last passport unless i add extra newline"""
        passport = {}
        for input in [line.strip() for line in self.input]:
            if input == '':
                self.passports.append(passport)
                passport = {}
                continue
            for token in input.split(' '):
                parsed = re.match(self.pattern, token)
                key = parsed.groups()[0]
                value = parsed.groups()[1]
                if key in passport:
                    print('dupe key')
                passport[key] = value


    challenge1 = "how many passports are valid"
    def solve1(self):
        count = 0
        for passport in self.passports:
            if self.valid1(passport):
                count = count + 1
        return count

    challenge2 = "how many passports are valid with rules"
    def solve2(self):
        count = 0
        for passport in self.passports:
            if self.valid2(passport):
                count = count + 1
        return count

    def valid1(self, passport):
        keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
        passport['cid'] = False
        return set(keys) == set(passport.keys())

    def check_byr(self, str):
        return re.match(r'[0-9]{4}', str) and (1920 <= int(str) <= 2002)

    def check_iyr(self, str):
        return re.match(r'[0-9]{4}', str) and (2010 <= int(str) <= 2020)

    def check_eyr(self, str):
        return re.match(r'[0-9]{4}', str) and (2020 <= int(str) <= 2030)

    def check_hcl(self, str):
        return re.match(r'^#[0-9a-f]{6}$', str)
    
    def check_ecl(self, str):
        return re.match(r'^amb|blu|brn|gry|grn|hzl|oth$', str)
        
    def check_pid(self, str):
        return re.match(r'^[0-9]{9}$', str)
    
    def check_hgt(self, str):
        if not(re.match(r'^[0-9]+(in|cm)$', str)):
            return False
        if str.endswith('cm'):
            if not(150 <= int(str[:-2]) <= 193):
                return False
        if str.endswith('in'):
            if not(59 <= int(str[:-2]) <= 76):
                return False
        return True

    def valid2(self, passport):
        return self.valid1(passport) and self.check_byr(passport['byr']) and self.check_iyr(passport['iyr']) and self.check_eyr(passport['eyr']) and self.check_hgt(passport['hgt']) and self.check_hcl(passport['hcl']) and self.check_ecl(passport['ecl']) and self.check_pid(passport['pid'])
        

 
day = day4(4)
day.solve()
"""
for passport in day.passports:
    repr = ''
    for k,v in sorted(passport.items(), key=lambda x: x[0]):
        repr = repr + "{} : {} ".format(k,v)
    print(repr)
"""