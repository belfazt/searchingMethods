import re

HMS = 40
HMRC = 0.8
PAR = 0.5

data = """
        8.. ... ...
        ..3 6.. ...
        .7. .9. 2..
        .5. ..7 ...
        ... .45 7..
        ... 1.. .3.
        ..1 ... .68
        ..8 5.. .1.
        .9. ... 4..
    """

sudoku = [[{'value': 0, 'final': True} for col in range(9)] for row in range(9)]

puzzle = re.sub(r'[^0-9\.]', '', data)
if len(puzzle) != 81:
    raise ValueError("Argument must contain 9*9 digits")

iterpuzzle = iter(puzzle)

for row in range(9):
    for col in range(9):
        val = iterpuzzle.next()
        if val != '.':
            sudoku[row][col]['value'] = int(val)
            sudoku[row][col]['final'] = False

def display(sudoku):
        row_values = ""

        for row in sudoku:
            for cell in row:
                row_values += str(cell['value']) + ", " 
        print row_values

def get_possible_values(x,y):
    values = [1,2,3,4,5,6,7,8,9]

    # Row
    for cell in sudoku[y]:
        if not cell['final']:
            continue

        current_value = cell['value']

        if current_value != 0 and current_value in values:
            print "index:" + str(values.index(current_value))
            values.remove(current_value)

    # Column
    for i in range(9):
        if not sudoku[i][x]['final']:
            continue

        current_value = sudoku[i][x]['value']

        if current_value != 0 and current_value in values:
            print "index:" + str(values.index(current_value))
            values.remove(current_value)
    
    # Sector
    sector_index_x = x / 3 * 3
    sector_index_y = y / 3 * 3

    for i in range(sector_index_x, sector_index_x + 3):
        for j in range(sector_index_y, sector_index_y + 3):
            if not sudoku[i][j]['final']:
                continue

            current_value = sudoku[i][j]['value']

            if current_value != 0 and current_value in values:
                values.remove(current_value)

    return values

def choose_cell_randomly():
    """ Get the first available cell """
    cell = {'x': 0, 'y': 0}
    for i in range(9):
        for j in range(9):
            if not sudoku[i][j]["final"]:
                return {'x': i, 'y': j}

    return cell

def calc_value(possible_values):
    if len(possible_values) == 1:
        return possible_values[0]
    else:
        return min(possible_values) + HMRC * (max(possible_values) - min(possible_values))

def fill_up():
    pass

def solve():
    pass


def main():
    display(sudoku)
    print possible_values(0,0)    


if __name__ == '__main__':
    main()
