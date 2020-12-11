input_file = 'input.txt'
with open(input_file) as f:
    data = f.read()

# data = """
# 35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576
# """

numbers = [int(line) for line in data.split('\n') if line]
preamble = 25

def run_numbers(numbers, preamble):
    for index, number in enumerate(numbers):
        if index >= preamble:
            pool = set(numbers[index-preamble:index])
            valid = any(number-item in pool for item in pool)
            if not valid:
                return number
    return 'All numbers are valid'

def find_range(numbers, target):
    for n in range(3, 30):
        for i in range(len(numbers)-n):
            pool = numbers[i:i+n]
            if sum(pool) == target:
                return min(pool) + max(pool)

answer1 = run_numbers(numbers, preamble)
print(f'Invalid number = {answer1}')

numbers = numbers[:numbers.index(answer1)]

answer2 = find_range(numbers, answer1)
print(f'Part 2 answer = {answer2}')
