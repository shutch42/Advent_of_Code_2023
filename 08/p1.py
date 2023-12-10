graph = {}


def find_z(instructions):
    curr = 'AAA'
    steps = 0

    while True:
        # Loop until 'ZZZ' is found
        for instruction in instructions:
            steps += 1
            if instruction == 'L':
                curr = graph[curr][0]
            else:
                curr = graph[curr][1]
            if curr == 'ZZZ':
                return steps


with open("input.txt") as file:
    lines = file.readlines()
    instructions = lines[0].strip()

    # Create graph
    for line in lines[2:]:
        [node, paths] = line.split(' = ')
        [left, right] = paths[1:-2].split(', ')
        graph[node] = (left, right)

    print(find_z(instructions))
