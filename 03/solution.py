from helper import *


class Schematic:
    def __init__(self, filename):
        self.arr = []
        with open(filename) as file:
            for line in file:
                arr_line = [[char, False] for char in line.strip()]
                self.arr.append(arr_line)

    def print(self):
        for row in self.arr:
            row_str = ""
            for square in row:
                row_str += val(square)
            print(row_str)

    def is_valid(self, row, col):
        return 0 <= row < len(self.arr) \
            and 0 <= col < len(self.arr[0]) \
            and is_number(self.arr[row][col]) \
            and not is_marked(self.arr[row][col])

    def get_num(self, row, col):
        num_str = val(self.arr[row][col])
        mark(self.arr[row][col])
        left = col - 1
        right = col + 1

        while self.is_valid(row, left):
            num_str = val(self.arr[row][left]) + num_str
            mark(self.arr[row][left])
            left -= 1
        while self.is_valid(row, right):
            num_str = num_str + val(self.arr[row][right])
            mark(self.arr[row][right])
            right += 1

        return int(num_str)

    def get_adjacent_parts(self, row, col):
        adj_parts = []
        for adj_row in range(row - 1, row + 2):
            for adj_col in range(col - 1, col + 2):
                if self.is_valid(adj_row, adj_col):
                    adj_parts.append(self.get_num(adj_row, adj_col))
        return adj_parts

    def get_parts(self):
        part_nums = []
        for row_num, row in enumerate(self.arr):
            for col_num, square in enumerate(row):
                if is_symbol(square):
                    part_nums += self.get_adjacent_parts(row_num, col_num)
        return part_nums

    def clear_marks(self):
        for row in self.arr:
            for square in row:
                un_mark(square)

    def get_gear_ratios(self):
        ratios = []
        for row_num, row in enumerate(self.arr):
            for col_num, square in enumerate(row):
                if val(self.arr[row_num][col_num]) == "*":
                    self.clear_marks()
                    adj_parts = self.get_adjacent_parts(row_num, col_num)
                    if len(adj_parts) == 2:
                        ratios.append(adj_parts[0] * adj_parts[1])
        return ratios


engine_schematic = Schematic("input.txt")
print(f"Part 1: {sum(engine_schematic.get_parts())}")
print(f"Part 2: {sum(engine_schematic.get_gear_ratios())}")
