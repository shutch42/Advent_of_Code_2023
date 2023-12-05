with open("input.txt") as file:
    points = 0
    for line in file:
        card = line.strip().split(": ")[1]
        [winning_number_str, my_number_str] = card.split(" | ")
        winning_numbers = winning_number_str.split()
        my_numbers = my_number_str.split()

        my_winning_numbers = []
        for number in my_numbers:
            if number in winning_numbers:
                my_winning_numbers.append(number)

        power = len(my_winning_numbers) - 1
        if power >= 0:
            points += 2**power

    print(points)
