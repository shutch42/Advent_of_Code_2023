import re

numbers = []
number_strings = {'zero': '0',
                  'one': '1',
                  'two': '2',
                  'three': '3',
                  'four': '4',
                  'five': '5',
                  'six': '6',
                  'seven': '7',
                  'eight': '8',
                  'nine': '9'}

regex = "(?=([0-9]"
for word in number_strings.keys():
    regex += f"|{word}"
regex += "))"

with open("input.txt") as file:
    for line in file:
        digits = re.findall(regex, line.strip())
        clean_digits = [digit if digit.isdigit() else number_strings[digit] for digit in digits]
        numbers.append(int(clean_digits[0]+clean_digits[-1]))

print(sum(numbers))
