import math

cipher_file = 'input.txt'
with open(cipher_file) as f:
    data = f.read()

data = data.split('\n')
data = data[:-1]

#data = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

#line = data[0]

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
    seat = row * 8 + column
    seats.append(seat)

seats = sorted(seats)
highest = seats[-1]
print(highest)

for index, number in enumerate(seats[:-1]):
    if number+1 != seats[index+1]:
        print(number+1)