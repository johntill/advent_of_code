import re

input_file = 'input.txt'
with open(input_file) as f:
    data = f.read()

# Test data
# data = """
# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# """

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

def search_outer_bags(targets, found):
    if not targets:
        return found
    new_targets = set()
    for target in targets:
        for bag, contents in simple_rules.items():
            if target in contents:
                found.add(bag)
                new_targets.add(bag)
    return search_outer_bags(new_targets, found)

def search_inner_bags(target, total):
    for bag, amount in complex_rules[target].items():
        for _ in range(amount):
            total.append(iter(search_inner_bags(bag, total)))
    return total

target = 'shinygold'

found = set()
found = search_outer_bags([target], found)
print(f'Outer bags = {len(found)}')

total = []
total = search_inner_bags(target, total)
print(f'Inner bags = {len(total)}')