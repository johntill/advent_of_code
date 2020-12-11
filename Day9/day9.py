input_file = 'input.txt'
with open(input_file) as f:
    data = f.read()

preamble = 25

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

def check_number(number, pool):
    pool = set(pool)
    for item in pool:
        target = number - item
        if target in pool and target != item:
            return True

def run_numbers(numbers, preamble):
    for index, number in enumerate(numbers):
        if index >= preamble:
            pool = numbers[index-preamble:index]
            # print(index, number, pool)
            valid = check_number(number, pool)
            if not valid:
                #print(f'{number} is not valid!')
                return number
    return 'All numbers are valid'

answer = run_numbers(numbers, preamble)
print(answer)
