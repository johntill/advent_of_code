input_file = 'input.txt'

with open(input_file) as f:
    numbers = [int(line) for line in f]

def find_number(numbers):
    numbers = set(numbers)
    for number in numbers:
        target = 2020 - number
        if target in numbers:
            return number * target

def find_three_numbers(numbers):
    for index, num1 in enumerate(numbers):
        numbers2 = set(numbers[index+1:])
        for num2 in numbers2:
            target = 2020 - num1 - num2
            if target in numbers2:
                return num1 * num2 * target

answer = find_number(numbers)
answer2 = find_three_numbers(numbers)

print(answer)
print(answer2)
