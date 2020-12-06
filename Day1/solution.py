import numpy as np

data_file = 'input.txt'


def parse_input(input_data_file):
    with open(input_data_file, 'r') as input_data_file:
        input_data = input_data_file.read()
        
    lines = input_data.split('\n')
    item_count = len(lines) - 1

    items = []

    for i in range(0, item_count):
        line = lines[i]
        items.append(int(line))
    
    return items


def solver1(items):
    for i in items:
        for j in items:
            if i + j == 2020:
                break
        if i + j == 2020:
            break
    return i*j


def solver2(items):
    for i in items:
        for j in items:
            for k in items:
                if i + j + k == 2020:
                    break
            if i + j + k == 2020:
                break
        if i + j + k == 2020:
            break
    return i*j*k


items = parse_input(data_file)
solution1 = solver1(items)
solution2 = solver2(items)

print(f'The 2 items that sum to 2020 multiplied together is equal to {solution1}.')
print(f'The 3 items that sum to 2020 multiplied together is equal to {solution2}.')