import math
import numpy as np

input_data_file = 'input.txt'


def parse_input(input_data_file):
    with open(input_data_file, 'r') as input_data_file:
        input_data = input_data_file.read()
        
    return input_data.split('\n')[:-1]


def generate_map(lines, right_move_len, bottom_move_len=1):
    mapa = []
    total_moves = math.ceil(len(lines)/bottom_move_len)
    desired_line_size = total_moves * right_move_len
    line_multiplier = math.ceil(desired_line_size/len(lines[0]))
    for i, line in enumerate(lines):
        new_line = line * line_multiplier
        mapa.append(new_line)
    return mapa


def count_trees(map_, bottom_move_len, right_move_len, start_line=0, start_pos=0):
    current_line, current_pos = start_line, start_pos
    tree_count = 0

    for i in range(len(map_)//bottom_move_len + len(map_)%bottom_move_len):
        if map_[current_line][current_pos] == '#':
            tree_count+=1
        current_pos+=right_move_len
        current_line+=bottom_move_len

    return tree_count

lines = parse_input(input_data_file)

right_move_len = 3
bottom_move_len = 1

mapa = generate_map(lines, right_move_len, bottom_move_len)
solution1 = count_trees(mapa, bottom_move_len, right_move_len)


slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
count_arr = np.array([])

for slope in slopes:
    right_move_len = slope[0]
    bottom_move_len = slope[1]
    
    mapa = generate_map(lines, right_move_len, bottom_move_len)
    count = count_trees(mapa, bottom_move_len, right_move_len)
    count_arr = np.append(count_arr, count)
    
solution2 = int(np.product(count_arr))

print(f'With a slope of right 3 - down 1 we would encounter {solution1} trees.')
print(f'Multiplying together the number of trees encoutered with each slope, the result would be {solution2}.')