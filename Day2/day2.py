input_file = 'input.txt'

info = []
with open(input_file) as f:
    for line in f:
        count, letter, password = line.split(' ')
        count_min, _, count_max = count.partition('-')
        count_min, count_max = int(count_min), int(count_max)
        letter = letter[0]
        password = password.strip()
        info.append((count_min, count_max, letter, password))

def count_letter(info):
    correct = 0
    for line in info:
        count_min, count_max, letter, password = line
        letter_count = password.count(letter)
        if count_min <= letter_count <= count_max:
            correct += 1
    return correct

def count_letter2(info):
    correct = 0
    for line in info:
        pos1, pos2, letter, password = line
        pos1 -= 1
        pos2 -= 1
        if (password[pos1] == letter) != (password[pos2] == letter):
            correct += 1
    return correct

answer = count_letter(info)
print(answer)

answer2 = count_letter2(info)
print(answer2)