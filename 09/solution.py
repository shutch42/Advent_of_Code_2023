def are_zeroes(arr):
    for val in arr:
        if val != 0:
            return False
    return True


def extrapolate(numbers):
    extrapolation_table = [numbers]

    while True:
        differences = []
        for i in range(len(numbers) - 1):
            curr_num = numbers[i]
            next_num = numbers[i+1]
            differences.append(next_num - curr_num)

        if are_zeroes(differences):
            break

        numbers = differences
        extrapolation_table.append(differences)

    extrapolation_table.reverse()
    for i in range(len(extrapolation_table) - 1):
        extrapolation_table[i+1].append(extrapolation_table[i+1][-1] + extrapolation_table[i][-1])

    return extrapolation_table[-1][-1]


with open("input.txt") as file:
    sum_extrapolate_forward = 0
    sum_extrapolate_backward = 0
    for line in file:
        nums = [int(num) for num in line.split()]
        sum_extrapolate_forward += extrapolate(nums)
        nums.reverse()
        sum_extrapolate_backward += extrapolate(nums)

    # Part 1
    print(sum_extrapolate_forward)

    # Part 2
    print(sum_extrapolate_backward)
