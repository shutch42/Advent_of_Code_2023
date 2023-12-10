# Brute force isn't gonna work on this one
# I think one way to get around this is to find the path length to each node, and then find the LCM of the path lengths
import math

graph = {}


def find_z(instructions, start_node):
    curr_node = start_node
    steps = 0

    while True:
        # Loop until 'xxZ' is found on all nodes
        for instruction in instructions:
            steps += 1
            if instruction == 'L':
                curr_node = graph[curr_node][0]
            else:
                curr_node = graph[curr_node][1]

            if curr_node[-1] == 'Z':
                return steps


with open("input.txt") as file:
    lines = file.readlines()
    instructions = lines[0].strip()

    start_nodes = []
    # Create graph
    for line in lines[2:]:
        [node, paths] = line.split(' = ')
        [left, right] = paths[1:-2].split(', ')
        graph[node] = (left, right)

        if node[-1] == 'A':
            start_nodes.append(node)

    distances = []
    for node in start_nodes:
        distances.append(find_z(instructions, node))

    lcm = 1
    for distance in distances:
        lcm = math.lcm(lcm, distance)
    print(lcm)
