import re

HMS = 40
HMRC = 0.8
PAR = 0.5

data = """
        .5. 3.6 ..7
        ... .85 .24
        .98 42. 6.3
        9.1 ..3 2.6
        .3. ... .1.
        5.7 26. 9.8
        4.5 .9. 38.
        .1. 57. ..2
        8.. 1.4 .7.
    """

sudoku = [[{'value': 0, 'final': False, 'possible_values': []} for col in range(9)] for row in range(9)]

puzzle = re.sub(r'[^0-9\.]', '', data)
if len(puzzle) != 81:
    raise ValueError("Argument must contain 9*9 digits")

iterpuzzle = iter(puzzle)

for row in range(9):
    for col in range(9):
        val = iterpuzzle.next()
        if val != '.':
            sudoku[row][col]['value'] = float(val)
            sudoku[row][col]['final'] = True

def display():
        row_values = ""
        print ""

        for row in sudoku:
            for cell in row:
                row_values += '%.2f  ' % cell['value']
            print row_values
            row_values = ""

        print ""

def get_possible_values(x,y):
    values = [1,2,3,4,5,6,7,8,9]

    #print values
    # Row
    for cell in sudoku[x]:
        
        if not cell['final']:
            continue

        current_value = cell['value']
        
        if current_value != 0 and current_value in values:
            ##print "index:" + str(values.index(current_value))
            values.remove(current_value)

    #print values

    # Column
    for i in range(9):

        if not sudoku[i][y]['final']:
            continue

        current_value = sudoku[i][y]['value']
        
        if current_value != 0 and current_value in values:
            ##print "index:" + str(values.index(current_value))
            values.remove(current_value)
    
    # Sector
    sector_index_x = x / 3 * 3
    sector_index_y = y / 3 * 3

    #print values

    for i in range(sector_index_x, sector_index_x + 3):
        for j in range(sector_index_y, sector_index_y + 3):
            
            if not sudoku[i][j]['final']:
                continue

            current_value = sudoku[i][j]['value']

            if current_value != 0 and current_value in values:
                values.remove(current_value)

    #print values

    return values

def choose_cell_randomly():
    """ Get the first available cell """
    cell = {'x': 0, 'y': 0}
    for i in range(9):
        for j in range(9):
            if not sudoku[i][j]["final"]:
                return {'x': i, 'y': j}

    return cell

# Value for first iteration
def calc_value(cell):
    if len(cell['possible_values']) == 1:
        cell['value'] = cell['possible_values'][0]
        cell['final'] = True
        cell['possible_values'] = []
        return cell
    else:

        cell['value'] = min(cell['possible_values']) + HMRC * (max(cell['possible_values']) - min(cell['possible_values']))
        #cell['final'] = False
        #cell['possible_values'] = 
        return cell

def fill_up():
    possible_values = []
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if not sudoku[i][j]['final']:
                sudoku[i][j]['possible_values'] = get_possible_values(i, j)
                #print "{0} {1}".format(i, j)
                #print possible_values
                sudoku[i][j] = calc_value(sudoku[i][j])

def new_value(cell, iterations):
    values = [cell['value'], cell['value']]
    values[0] += HMRC * PAR * 0.5 * iterations
    values[1] -= HMRC * PAR * 0.5 * iterations
    if int(values[0]) in cell['possible_values']:
        cell['value'] = values[0]
        return cell
    elif int(values[1]) in cell['possible_values']:
        cell['value'] = values[1]
        return cell
    return cell

# number of iteration over a cell value
def num_iterations(cell):
    return (cell['value'] - cell['possible_values'][0]) / ( HMRC * PAR * .5 )
# Get next value for all cells
def iterate():
    possible_values = []
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if not sudoku[i][j]['final']:
                #possible_values = get_possible_values(i, j)
                iterations = num_iterations(sudoku[i][j])
                print sudoku[i][j]['value']
                print iterations
                sudoku[i][j] = new_value(sudoku[i][j], iterations)
                #sudoku[i][j]['possible_values'] = get_possible_values(i, j)

    # Mark new final values
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            sudoku[i][j]['possible_values'] = get_possible_values(i, j)

def solve():
    display()
    fill_up()
    display()
    iterate()
    display()



def main():
    #display(sudoku)
    ##print get_possible_values(7,0)    
    solve()


if __name__ == '__main__':
    main()
