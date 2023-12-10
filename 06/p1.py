# boat rules:
# for each 1 second of delay, acceleration increases by 1 mm/s^2
# initial speed is 0 mm/s
# vo = t_del
# x = vo*t
# x = (t_del)*(t_total - t_del)
# x = t_total*t_del - t_del^2
# solving for t_del:
# t_del^2 - t_total*t_del + x = 0
# use quadratic:
# t_del = (-t_total +/- sqrt(t_total^2 - 4*x))/2

import math

margin_of_error = 1

with open("input.txt") as file:
    file_content = file.readlines()
    time_str = file_content[0].split(': ')[1].strip()
    times = [int(time) for time in time_str.split()]
    distance_str = file_content[1].split(': ')[1].strip()
    distances = [int(distance) for distance in distance_str.split()]

    for i, time in enumerate(times):
        distance = distances[i]

        # quadratic formula time!
        t_hold_min = (time - math.sqrt(time**2 - 4*distance))/2
        t_hold_max = (time + math.sqrt(time**2 - 4*distance))/2

        # make sure minimum time > solution val
        if t_hold_min.is_integer():
            t_hold_min = int(t_hold_min) + 1
        else:
            t_hold_min = math.ceil(t_hold_min)

        # max sure maximum time < solution val
        if t_hold_max.is_integer():
            t_hold_max = int(t_hold_max) - 1
        else:
            t_hold_max = math.floor(t_hold_max)

        num_solutions = t_hold_max - t_hold_min + 1
        margin_of_error *= num_solutions

print(margin_of_error)
