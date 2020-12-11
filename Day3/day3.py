import math

input_file = 'input.txt'
with open(input_file) as f:
    terrain = [line.strip() for line in f]

# terrain = (['..##.......', '#...#...#..', '.#....#..#.', '..#.#...#.#',
#             '.#...##..#.', '..#.##.....', '.#.#.#....#', '.#........#',
#             '#.##...#...', '#...##....#', '.#..#...#.#'])

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def traverse_slope(terrain, slope):
    line_len = len(terrain[0])
    pos = trees = 0
    for line in terrain[1:]:
        pos = (pos + slope) % line_len
        trees += line[pos] == '#'
    return trees

answers = [traverse_slope(terrain[::slope[1]], slope[0]) for slope in slopes]

answer = math.prod(answers)
print(answer, answers)