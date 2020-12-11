import re

# input_file = 'input.txt'
# with open(input_file) as f:
#     data = f.read()

# Test data

data = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

data = re.sub('[^a-z0-9,\n]','', data.replace('bags', '').replace('bag', ''))
data = data.replace('noother', '0none')

bags = []
contents = []
simple_rules = {}

for line in data.split('\n'):
    if line:
        bag, content = line.split('contain')
        bags.append(bag)
        items = content.split(',')
        colours = [re.search(r'[a-z]\w+', item).group() for item in items]
        amounts = [int(re.search(r'\d+', item).group()) for item in items]
        simple_rules[bag] = set(colours)
        bag_dict = dict(zip(colours, amounts))
        contents.append(bag_dict)

complex_rules = dict(zip(bags, contents))

def search_inner_bags(target, found=None):
    if not found: found = []
    for key, value in complex_rules[target].items():
        if value != 0:
            for _ in range(value):
                found.append(key)
                search_inner_bags(key, found)
    return len(found)

target = 'shinygold'

found = search_inner_bags(target)
print(found)