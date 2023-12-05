numbers = []

with open("input.txt") as file:
    for line in file:
        digits = [letter for letter in line.strip() if letter.isdigit()]
        numbers.append(int(digits[0]+digits[-1]))

print(sum(numbers))
