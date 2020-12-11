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

def run_numbers(numbers, preamble):
    for index, number in enumerate(numbers):
        if index >= preamble:
            pool = set(numbers[index-preamble:index])
            valid = any(number-item in pool for item in pool)
            if not valid:
                return number
    return 'All numbers are valid'

numbers = [int(line) for line in data.split('\n') if line]
answer = run_numbers(numbers, preamble)
print(answer)

