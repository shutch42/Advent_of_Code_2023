num_cubes = {'red': 12,
             'green': 13,
             'blue': 14}
sum_ids = 0


def pairs_impossible(color_pairs):
    for pair in color_pairs:
        if int(pair[0]) > num_cubes[pair[1]]:
            return True
    return False


def game_impossible(cube_sets):
    for cube_set in cube_sets:
        cubes_per_color = cube_set.split(", ")
        num_color_pairs = [num_color_str.split(" ") for num_color_str in cubes_per_color]
        if pairs_impossible(num_color_pairs):
            return True
    return False


with open("input.txt") as file:
    for game_id, line in enumerate(file, 1):
        sets = line.strip().split(": ")[1].split("; ")
        if not game_impossible(sets):
            sum_ids += game_id

print(sum_ids)
