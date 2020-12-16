import math

cipher_file = 'input.txt'
with open(cipher_file) as f:
    data = f.read()

data = data.splitlines()

#data = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

def binary_search(line, lower, upper):
    for letter in line:
        boundary = math.ceil((upper-lower) / 2)
        if letter in {'F', 'L'}:
            upper -= boundary
        else:
            lower += boundary
        if upper == lower:
            return upper

seats = []
for line in data:
    row = binary_search(line[:7], 0, 127)
    column = binary_search(line[7:], 0, 7)
    seats.append(row * 8 + column)

seats = sorted(seats)
highest = seats[-1]
print(f'Highest seat number = {highest}')

for index, number in enumerate(seats[:-1]):
    if number+1 != seats[index+1]:
        print(f'My seat number = {number+1}')