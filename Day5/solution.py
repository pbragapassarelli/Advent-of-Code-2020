input_data_file = 'input.txt'

def read_input_file(input_data_file):
    with open(input_data_file, 'r') as input_data_file:
        input_data = input_data_file.read()
    return input_data.split('\n')[:-1]


available_rows = 128
available_columns = 8

row_list = [i for i in range(available_rows)]
column_list = [i for i in range(available_columns)]


def get_remaining_list(character, available_list):
    half = len(available_list) // 2
    if (character == 'F') | (character == 'L'):
        return available_list[:half]
    if (character == 'B') | (character == 'R'):
        return available_list[half:]
    return None


def find_seat_row(seat):
    remaining_rows = row_list
    for character in seat[:7]:
        remaining_rows = get_remaining_list(character, remaining_rows)
    return remaining_rows[0]


def find_seat_column(seat):
    remaining_columns = column_list
    for character in seat[-3:]:
        remaining_columns = get_remaining_list(character, remaining_columns)
    return remaining_columns[0]


def get_seat_id(seat):
    return find_seat_row(seat) * 8 + find_seat_column(seat)

seats = read_input_file(input_data_file)
seat_ids = [get_seat_id(seat) for seat in seats]
solution1 = max(seat_ids)


def find_my_seat(remaining_seats):
    for i, seat in enumerate(remaining_seats):
        if i == 0 or i == len(remaining_seats)-1:
            continue
        if remaining_seats[i-1] == seat - 1 or remaining_seats[i+1] == seat + 1:
            continue
        return seat


available_seats = [i for i in range(available_rows * available_columns)]
remaining_seats = list(set(available_seats) - set(seat_ids))
solution2 = find_my_seat(remaining_seats)

print(f'The highest seat ID is {solution1}.')
print(f'My seat is {solution2}.')