input_data_file = 'input.txt'

def read_input_file(input_data_file):
    with open(input_data_file, 'r') as input_data_file:
        return input_data_file.read()


def make_passport_list(input_data):
    passports = input_data.split('\n\n')
    return [i.split() for i in passports]


def get_fields_list_from_item(passport_item):
    return [i.split(':')[0] for i in passport_item]


def get_values_from_item(passport_item):
    return [i.split(':')[1] for i in passport_item]


required_fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]

input_data = read_input_file(input_data_file)
passports = make_passport_list(input_data)
passports_fields = [get_fields_list_from_item(i) for i in passports]
passports_validity = [set(required_fields).issubset(set(i)) for i in passports_fields]
solution1 = sum(passports_validity)


def is_byr_valid(passport_item):
    if 'byr' in passport_item.keys():
        if (int(passport_item['byr']) >= 1920) & (int(passport_item['byr']) <= 2002):
            return True
    return False


def is_iyr_valid(passport_item):
    if 'iyr' in passport_item.keys():
        if (int(passport_item['iyr']) >= 2010) & (int(passport_item['iyr']) <= 2020):
            return True
    return False


def is_eyr_valid(passport_item):
    if 'eyr' in passport_item.keys():
        if (int(passport_item['eyr']) >= 2020) & (int(passport_item['eyr']) <= 2030):
            return True
    return False


def is_hgt_valid(passport_item):
    if 'hgt' in passport_item.keys():
        if passport_item['hgt'][-2:] == 'cm':
            if (int(passport_item['hgt'].split('c')[0]) >= 150) & \
                (int(passport_item['hgt'].split('c')[0]) <= 193):
                return True
        if passport_item['hgt'][-2:] == 'in':
            if (int(passport_item['hgt'].split('i')[0]) >= 59) & \
                (int(passport_item['hgt'].split('i')[0]) <= 76):
                return True
    return False


def is_hcl_valid(passport_item):
    if 'hcl' in passport_item.keys():
        if (len(passport_item['hcl']) == 7) & (passport_item['hcl'][0] == '#'):
            return True
    return False


def is_ecl_valid(passport_item):
    required_colors = [
        'amb',
        'blu',
        'brn',
        'gry',
        'grn',
        'hzl',
        'oth'
    ]
        
    if 'ecl' in passport_item.keys():
        if passport_item['ecl'] in required_colors:
            return True
    return False


def is_pid_valid(passport_item):
    if 'pid' in passport_item.keys():
        if len(passport_item['pid']) == 9:
            return True
    return False

def is_valid(passport_item):
    if (is_byr_valid(passport_item)) & \
        (is_iyr_valid(passport_item)) & \
        (is_eyr_valid(passport_item)) & \
        (is_hgt_valid(passport_item)) & \
        (is_hcl_valid(passport_item)) & \
        (is_ecl_valid(passport_item)) & \
        (is_pid_valid(passport_item)):
        return True
    return False


def make_passport_dict(passport_item):
    fields = get_fields_list_from_item(passport_item)
    values = get_values_from_item(passport_item)
    return dict(zip(fields, values))


passports = [make_passport_dict(i) for i in passports]
passports_validity2 = [is_valid(i) for i in passports]
solution2 = sum(passports_validity2)


print(f'{solution1} passports contain all the required fields.')
print(f'{solution2} passports are valid according to the field validity rules.')