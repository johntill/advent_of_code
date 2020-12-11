input_file = 'input.txt'
with open(input_file) as f:
    data = f.read()

answer1 = answer2 = 0

for line in data.split('\n\n'):
    line = [set(l) for l in line.split()]
    answer1 += len(set.union(*line))
    answer2 += len(set.intersection(*line))

print(answer1)
print(answer2)