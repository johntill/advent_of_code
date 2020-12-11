import re

input_file = 'input.txt'
with open(input_file) as f:
    data = f.read()

# data = """
# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm

# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929

# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm

# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in
# """

def clean_data(data):
    data = data.split('\n')
    new_data = []
    new_entry = []
    for line in data:
        if line != '':
            new_entry.append(line)
        else:
            if new_entry:
                new_data.append(new_entry)
                new_entry = []
    return new_data

def clean_data2(data):
    new_data = []
    for line in data:
        new_line = []
        line = ' '.join(line)
        line = line.split(' ')
        for item in line:
            if item.startswith('cid'):
                continue
            new_line.append(item)
        new_line = sorted(new_line)
        new_data.append(new_line)
    return new_data

def validate_data1(data):
    valid_count = 0
    for line in data:
        line = ' '.join(line)
        line = line.split(' ')
        line_cat = len(line)
        if line_cat == num_cat:
            valid_count += 1
        elif line_cat == num_cat - 1:
            present = set()
            for item in line:
                cat = item[:3]
                present.add(cat)
            missing = categories - present
            if missing == {'cid'}:
                valid_count += 1
    return valid_count

def validate_data2(data):
    eye_colours = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    valid_count = 0
    for line in data:
        line_cat = len(line)
        if line_cat < num_cat - 1:
            continue
        for item in line:
            cat = item[:3]
            value = item[4:]
            if cat in {'byr', 'iyr', 'eyr'}:
                task = re.compile(r'\d{4}')
                x = task.search(value)
                if not x:
                    break
                x = int(x.group())
                if cat == 'byr' and (x < 1920 or x > 2002):
                    break
                elif cat == 'iyr' and (x < 2010 or x > 2020):
                    break
                elif cat == 'eyr' and (x < 2020 or x > 2030):
                    break
            elif cat == 'hgt':
                x = value.endswith(('cm', 'in'))
                if not x:
                    break
                task = re.compile(r'\d+')
                x = task.search(value)
                if not x:
                    break
                x = int(x.group())
                if value.endswith('cm') and (x < 150 or x > 193):
                    break
                if value.endswith('in') and (x < 59 or x > 76):
                    break
            elif cat == 'hcl':
                x = re.findall(r'^#[a-f0-9]{6}', value)
                if not x:
                    break
            elif cat == 'ecl':
                if value not in eye_colours:
                    break
            elif cat == 'pid':
                x = re.findall(r'^\d{9}$', value)
                if not x:
                    break
        else:
            valid_count += 1
    return valid_count

categories = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
num_cat = len(categories)

data = clean_data(data)

valid1 = validate_data1(data)
print(f'Valid = {valid1} / {len(data)}')

data2 = clean_data2(data)

valid2 = validate_data2(data2)
print(f'Valid = {valid2} / {len(data2)}')