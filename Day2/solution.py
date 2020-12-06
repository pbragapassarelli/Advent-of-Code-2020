import pandas as pd

input_data_file = 'input.txt'

def parse_input(input_data_file):
    with open(input_data_file, 'r') as input_data_file:
        input_data = input_data_file.read()
            
    lines = input_data.split('\n')[:-1]

    return lines


def get_password_df(input_data_file):
    passwords = pd.DataFrame()
    lines = parse_input(input_data_file)

    for password_rule in lines:
        qty_rule = password_rule.split()[0]
        minim = int(qty_rule.split('-')[0])
        maxim = int(qty_rule.split('-')[1])
        character = password_rule.split()[1][0]
        password = password_rule.split()[2]
        passwords = passwords.append({'min': minim,
                                    'max': maxim,
                                    'character': character,
                                    'password': password
                                    },
                                    ignore_index = True)
    return passwords


def count_letters_in_string(row):
    count = 0
    for i in row['password']:
        if i == row['character']:
            count+=1
    return count


passwords = get_password_df(input_data_file)
passwords['count'] = passwords.apply(count_letters_in_string, axis=1)
passwords['is_ok'] = (passwords['min'] <= passwords['count']) & (passwords['count'] <= passwords['max'])
solution1 = passwords[passwords['is_ok'] == True].count()[0]


def get_letter_min(row):
    position = int(row['min']-1)
    return row['password'][position]


def get_letter_max(row):
    position = int(row['max']-1)
    return row['password'][position]


passwords['letter_in_min_position'] = passwords.apply(get_letter_min, axis=1)
passwords['letter_in_max_position'] = passwords.apply(get_letter_max, axis=1)
passwords['is_ok2'] = (passwords['letter_in_min_position'] != passwords['letter_in_max_position']) & \
                        ((passwords['letter_in_min_position'] == passwords['character']) | \
                         (passwords['letter_in_max_position'] == passwords['character']))
solution2 = passwords[passwords['is_ok2'] == True].count()[0]

print(f'There are {solution1} valid passwords according to the first given policies.')
print(f'There are {solution2} valid passwords according to the corrected policies.')
