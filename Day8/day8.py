input_file = 'input.txt'
with open(input_file) as f:
    data = f.read()

data = [line for line in data.splitlines()]
instructions = {index+1: line.split(' ') for index, line in enumerate(data)}
max_pos = len(instructions) + 1

def run_program(instructions, commands, pos=1, acc=0):
    completed = set()
    while pos not in completed:
        completed.add(pos)
        command, step = instructions[pos]
        pos, acc = commands[command](step, pos, acc)
    return acc

def fix_flaw(instructions, commands):
    for index, instruction in instructions.items():
        if instruction[0].startswith('acc'):
            continue
        pos, acc = 1, 0
        completed = set()
        while pos not in completed:
            completed.add(pos)
            command, step = instructions[pos]
            if pos == index:
                command = 'jmp' if command == 'nop' else 'nop'
            pos, acc = commands[command](step, pos, acc)
            if pos == max_pos:
                return acc

commands = {'acc': lambda x, pos, acc: (pos+1, acc+int(x)),
            'nop': lambda x, pos, acc: (pos+1, acc),
            'jmp': lambda x, pos, acc: (pos+int(x), acc)}

answer1 = run_program(instructions, commands)
print(f'Part 1 = {answer1}')
answer2 = fix_flaw(instructions, commands)
print(f'Part 2 = {answer2}')
