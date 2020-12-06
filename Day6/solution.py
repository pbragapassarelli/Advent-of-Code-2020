input_data_file = 'input.txt'

def read_input_file(input_data_file):
    with open(input_data_file, 'r') as input_data_file:
        return input_data_file.read()[:-1]


def make_group_list(input_data):
    group_list = input_data.split('\n\n')
    unique_list = []
    for group in group_list:
        group_answers = group.split('\n')
        all_answers = ''.join(group_answers)
        unique_answers = list(set(all_answers))
        unique_list.append(unique_answers)
    return unique_list


def make_group_list(input_data):
    group_list = input_data.split('\n\n')
    for i, group in enumerate(group_list):
        group_list[i] = group.split('\n')
    return group_list


def get_unique_answers_per_group(group_answers):
    unique_list = []
    for group in group_answers:
        all_answers = ''.join(group)
        unique_answers = list(set(all_answers))
        unique_list.append(unique_answers)
    return unique_list


def count_answers_per_group(group_answers):
    return [len(answers) for answers in group_answers]


input_data = read_input_file(input_data_file)
group_answers = make_group_list(input_data)

unique_answers = get_unique_answers_per_group(group_answers)
answer_qty = count_answers_per_group(unique_answers)
solution1 = sum(answer_qty)


def get_common_answers(group_answers):
    common_answers = []
    for group in group_answers:
        current_common_answer = group[0]
        for answer in group:
            current_common_answer = list(set(current_common_answer) & set(answer))
        common_answers.append(current_common_answer)
    return common_answers


common_answers = get_common_answers(group_answers)
answer_qty2 = count_answers_per_group(common_answers)
solution2 = sum(answer_qty2)


print(f'The sum of unique answers between each group is {solution1}.')
print(f'The sum of common answers between each group is {solution2}.')

