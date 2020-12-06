import csv
import sys
import re


# helpers
def verify_byr(year):
    return year >= 1920 and year <= 2002

def verify_iyr(year):
    return year >= 2010 and year <= 2020
    
def verify_eyr(year):
    return year >= 2020 and year <= 2030
    
def verify_hgt(height):
    if 'cm' in height:
        parsed_height = int(height.replace('cm', ''))
        return parsed_height >= 150 and parsed_height <= 193
    if 'in' in height:
        parsed_height = int(height.replace('in', ''))
        return parsed_height >= 59 and parsed_height <= 76
    return False

def verify_hcl(hcl):
    search = re.search('^#[0-9a-f]{6,}$', hcl)
    return bool(search)

def verify_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def verify_pid(pid):
    # search = re.search('[0-9]{9,}$', pid)
    return len(pid) == 9


    

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
        passport = valid_part_1[key]
        for new_key in passport:
            if new_key == 'byr' and verify_byr(int(passport[new_key])):
                truth_counter += 1
            elif new_key == 'iyr' and verify_iyr(int(passport[new_key])):
                truth_counter += 1
            elif new_key == 'eyr' and verify_eyr(int(passport[new_key])):
                truth_counter += 1
            elif new_key == 'hgt' and verify_hgt(passport[new_key]):
                truth_counter += 1
            elif new_key == 'hcl' and verify_hcl(passport[new_key]):
                truth_counter += 1
            elif new_key == 'ecl' and verify_ecl(passport[new_key]):
                truth_counter += 1
            elif new_key == 'pid' and verify_pid(passport[new_key]):
                truth_counter += 1
            
        if truth_counter == 7:
            valid_p2 += 1
        
    
    print(valid_p2)