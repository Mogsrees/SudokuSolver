import sys

with open(sys.argv[1], 'r') as f:
    contents = f.read().splitlines()
arr = []
for line in contents:
    arr.append(line.split(';'))

def findcell(arr, row, col):
    cellrow = 3*(row/3)
    cellcol = 3*(col/3)
    vals = []
    for rs in range (3):
	for cs in range(3):
	    vals.append(arr[cellrow +rs][cellcol +cs]) 
    return vals

def findvals(arr, row, col):
    posvals = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for nums in xrange(9):
	rowval = arr[row][nums]
	colval = arr[nums][col]
	if rowval in posvals:
	    posvals.remove(rowval)
	if colval in posvals:
	    posvals.remove(colval)
    vals = findcell(arr, row, col)
    for val in vals:
	if val in posvals:
	    posvals.remove(val)
    return posvals

#Problem: this solves sudoku by backtracking but does not believe the last value is correct, and will therefore keep iterating again, and ends up finding 'no solution'; however, looking at logs it is obvious the solution is there just the last value is missing, which could be an oversight with the checking method... The work-around is when the number of empty values = 1, stop the algorithm and declare this the solution by manually inputting the correct solution. 

#Several solutions which function in python can be found on stack overflow, most notably the solution by Tristan Reid found here https://codereview.stackexchange.com/questions/96792/sudoku-puzzle-solver. In any other case, I would cite and use this source code, if permitted.  

def solve_sudoku(arr):
    for m, lines in enumerate(arr):
        for x, vals in enumerate(lines):
            if vals == '':
	        posvals = findvals(arr, m, x) 
        	for val in posvals:
                    arr[m][x] = val
                    posnewarr = solve_sudoku(arr)
                    if(posnewarr != None):
                        return posnewarr
                    else:
                        arr[m][x] = ''
                return None



#code function below found from https://stackoverflow.com/questions/22389128/python-sudoku-solver-nice-lay-out, credit to ALink 

def print_sudoku(board):
    y = 0
    for n in board:
        x = 0
        while x != 3:
            print n[x],
            x += 1
        print "|",
        while x != 6:
            print n[x],
            x += 1
        print "|",
        while x != 9:
            print n[x],
            x += 1
        print ""
        y = y + 1
        if y == 3 or y == 6:
            print "------|-------|------"


if (solve_sudoku(arr) != None):
    print_sudoku(arr)
else:
    print 'No solution found'

 


