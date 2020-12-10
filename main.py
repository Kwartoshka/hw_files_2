import os

file_list = ['1.txt', '2.txt', '3.txt']
list = []

for file in file_list:
    with open(file, encoding='utf-8') as current_file:
        current_list = current_file.read().splitlines()
        current_list.insert(0, len(current_list))
        current_list.insert(0, file)
        list.append(current_list)

list.sort(key = lambda file: file[1])
with open('file.txt', 'w', encoding='utf-8') as current_file:
    for file in list:
        for line in file:
            if isinstance(line, int):
                line = str(line)
            line += '\n'
            current_file.write(line)

