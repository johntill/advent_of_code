from time import perf_counter_ns

# input_file = 'input.txt'
# with open(input_file) as f:
#     data = f.read()

data = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

seats = [line for line in data.split('\n') if line]
rows = len(seats)
columns = len(seats[0])

seats = list(''.join(seats))
max_seat = len(seats) - 1

def get_surrounding_seats(seat, template, columns, max_seat):
    seat_column = seat % columns
    surrounding_seats = []
    for n in template:
        surrounding_seat = seat + n
        if (0 <= surrounding_seat <= max_seat) and abs(seat_column - surrounding_seat % columns) <= 1:
            surrounding_seats.append(surrounding_seat)
    return surrounding_seats

def evaluate_seat(seats, surrounding_seats):
    return [seats[seat] for seat in surrounding_seats].count('#')


seat_template = [-columns-1, -columns, -columns+1, -1, 1, columns-1, columns, columns+1]
old_seats = []

t1_start = perf_counter_ns()
while old_seats != seats:
    old_seats = [*seats]
    seats = []
    for index, seat in enumerate(old_seats):
        if seat != ".":
            surrounding_seats = get_surrounding_seats(index, seat_template, columns, max_seat)
            occupied = evaluate_seat(old_seats, surrounding_seats) 
            if seat == 'L' and occupied == 0:
                new_seat = '#'
            elif seat == 'L' or seat == '#' and occupied < 4:
                new_seat = seat
            elif seat == '#':
                new_seat = 'L'
        else:
            new_seat = '.'
        seats.append(new_seat)

    # show_key = ''.join(seats)
    # for i in range(0, len(seats), rows):
    #     print(show_key[i:i+rows])
    # print()

t1_stop = perf_counter_ns()
print(f"Occupied seats = {seats.count('#')}")
print((t1_stop - t1_start) / 1_000_000_000)
