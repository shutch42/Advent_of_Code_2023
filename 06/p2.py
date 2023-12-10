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

with open("input.txt") as file:
    file_content = file.readlines()
    time = int(file_content[0].split(': ')[1].strip().replace(' ', ''))
    distance = int(file_content[1].split(': ')[1].strip().replace(' ', ''))

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
    print(num_solutions)
