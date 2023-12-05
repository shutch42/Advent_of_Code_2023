sum_power = 0

with open("input.txt") as file:
    for line in file:
        color_maxima = {}
        sets = line.strip().split(": ")[1].split("; ")

        for cube_set in sets:
            cubes_per_color = cube_set.split(", ")
            num_color_pairs = [num_color_str.split(" ") for num_color_str in cubes_per_color]

            for pair in num_color_pairs:
                [count, color] = pair
                if color not in color_maxima or int(count) > color_maxima[color]:
                    color_maxima[color] = int(count)

        power = 1
        for color in color_maxima:
            power *= color_maxima[color]

        sum_power += power

print(sum_power)
