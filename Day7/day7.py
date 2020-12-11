import re

# input_file = 'input.txt'
# with open(input_file) as f:
#     data = f.read()

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

data = re.sub('[^a-z,\n]','', data.replace('bags', '').replace('bag', '').replace('noother', ''))

rules = {}
for line in data.split('\n'):
    if line:
        bag, content = line.split('contain')
        rules[bag] = set(content.split(','))

print(rules)
target = ['shinygold']
found = set()

def search_outer_bags(targets, found):
    if not targets:
        return found
    new_targets = set()
    for target in targets:
        for bag, contents in rules.items():
            if target in contents:
                found.add(bag)
                new_targets.add(bag)
    return search_outer_bags(new_targets, found)
    
found = search_outer_bags(target, found)
print(f'{len(found)} / {len(rules)}')