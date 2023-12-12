input_filename = 'input.txt'
with open(input_filename, 'r') as file:
    lines = file.readlines()

new_lines = [line.strip() + ' Бум-бум-кабум!\n' for line in lines]

output_filename = 'output.txt'
with open(output_filename, 'w') as file:
    file.writelines(new_lines)
