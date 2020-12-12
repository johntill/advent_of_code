import math
from collections import Counter

input_file = 'input.txt'
with open(input_file) as f:
    data = f.read()

# data = """
# 16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4
# """

numbers = [int(line) for line in data.split('\n') if line]
numbers.extend((0, max(numbers)+3))
numbers = sorted(numbers)
differences = [numbers[i+1]-num for i, num in enumerate(numbers[:-1])]
diff = Counter(differences)
answer = diff[1] * diff[3]
print(f'Part 1 = {answer}')

choices = []
count = 0

translate = {2:2, 3:4, 4:7}

for num in differences:
    if num == 1:
        count += 1
    else:
        if count in translate:
            choices.append(translate[count])
        count = 0

print(f'Combinations = {math.prod(choices)}')
