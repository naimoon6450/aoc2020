import csv
import sys
import re

# OOP ish...

class Passport(object):
    def __init__(self, birth_yr=None, issue_yr=None, exp_yr=None, height=None, hair_color=None, eye_color=None, pid=None, cid=None):
        self.birth_yr = int(birth_yr)
        self.issue_yr = int(issue_yr)
        self.exp_yr = int(exp_yr)
        self.height = height
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.pid = pid
        self.cid = cid
    
    def is_valid_passport(self):
        return self.verify_byr() and self.verify_iyr() and self.verify_eyr() and self.verify_hgt() and self.verify_hcl() and self.verify_ecl() and self.verify_pid()

    def verify_byr(self):
        return self.birth_yr >= 1920 and self.birth_yr <= 2002

    def verify_iyr(self):
        return self.issue_yr >= 2010 and self.issue_yr <= 2020
        
    def verify_eyr(self):
        return self.exp_yr >= 2020 and self.exp_yr <= 2030
        
    def verify_hgt(self):
        if 'cm' in self.height:
            parsed_height = int(self.height.replace('cm', ''))
            return parsed_height >= 150 and parsed_height <= 193
        if 'in' in self.height:
            parsed_height = int(self.height.replace('in', ''))
            return parsed_height >= 59 and parsed_height <= 76
        return False

    def verify_hcl(self):
        search = re.search('^#[0-9a-f]{6,}$', self.hair_color)
        return bool(search)

    def verify_ecl(self):
        return self.eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def verify_pid(self):
        # search = re.search('[0-9]{9,}$', pid)
        return len(self.pid) == 9


with open(sys.argv[1]) as input_file:
    csv_file = csv.reader(input_file)

    valid_p = 0
    parsed_passports = {}
    valid_part_1 = {}
    temp = {}
    # for passport keys
    p = 1

    for row in csv_file:
        if row:
            fields = row[0].split(' ')
            for field in fields:
                actual_field = field.split(':')[0]
                temp[actual_field] = field.split(':')[1]
        else:
            parsed_passports['p' + str(p)] = dict(temp)
            temp = {}
            p += 1
        
        # put last passport in dict
        parsed_passports['p' + str(p)] = dict(temp)

    # PART 1
    for key in parsed_passports:
        p_keys = parsed_passports[key].keys()
        if len(p_keys) == 8:
            valid_p += 1
            valid_part_1[key] = parsed_passports[key]
        
        if len(p_keys) == 7 and not parsed_passports[key].get('cid'):
            valid_p += 1
            valid_part_1[key] = parsed_passports[key]
    
    # PART 2
    valid_p2 = 0
    # print(valid_part_1)
    for key in valid_part_1:
        truth_counter = 0
        pass_obj = valid_part_1[key]
        # build passport object
        passport = Passport(birth_yr=pass_obj['byr'], issue_yr= pass_obj['iyr'],exp_yr= pass_obj['eyr'],height= pass_obj['hgt'],hair_color= pass_obj['hcl'],eye_color= pass_obj['ecl'],pid= pass_obj['pid'])


        if passport.is_valid_passport():
            valid_p2 += 1
        
    
    print(valid_p2)