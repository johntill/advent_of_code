from collections import Counter

# input_file = 'input.txt'
# with open(input_file) as f:
#     data = f.read()

data = """
16
10
15
5
1
11
7
19
6
12
4
"""

numbers = [int(line) for line in data.split('\n') if line]
numbers.extend((0, max(numbers)+3))
numbers = sorted(numbers)
diff = Counter([numbers[i+1]-num for i, num in enumerate(numbers[:-1])])
answer = diff[1] * diff[3]
print(answer)

