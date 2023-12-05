num_card_queue = [1]
total = 0

with open("input.txt") as file:
    for num, line in enumerate(file):
        card_str = line.strip().split(": ")[1]
        [winning_number_str, my_number_str] = card_str.split(" | ")
        winning_numbers = winning_number_str.split()
        my_numbers = my_number_str.split()

        my_winning_numbers = []
        for number in my_numbers:
            if number in winning_numbers:
                my_winning_numbers.append(number)

        num_matches = len(my_winning_numbers)
        num_cards = num_card_queue.pop(0)

        # Always make sure that the first card is accounted for
        if len(num_card_queue) == 0:
            num_card_queue.append(1)
        else:
            num_card_queue[0] += 1

        # Add a card for each match
        for i in range(num_matches):
            if i < len(num_card_queue):
                num_card_queue[i] += num_cards
            else:
                num_card_queue.append(num_cards)

        total += num_cards

print(total)
