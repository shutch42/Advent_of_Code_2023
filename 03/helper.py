def val(square):
    return square[0]


def is_symbol(square):
    return not val(square).isdigit() and val(square) != '.'


def is_number(square):
    return val(square).isdigit()


def is_marked(square):
    return square[1]


def mark(square):
    square[1] = True


def un_mark(square):
    square[1] = False
