'''
    Greedy implementation 1
    Global data structure:
        slice: tuple ( (row1, column1), (row2, column2) )
        config: {
                row: pizza_row,
                column: pizza_column,
                L: minimum element on each slice,
                H: maximum cells
        }
        pizza[][]: 1== M, 2==T
'''

from random import randint

def load_in_data(filename):
    '''
        Load input data
        Data structure: array of columns of T's and M's
         T==>2 ; M==> 1
    '''
    # Array of input data
    pizza = open(filename).readlines();
    pizza_config = pizza[0].split();
    config = dict(row=pizza_config[0],column=pizza_config[1],L=pizza_config[2],H=pizza_config[3]);
    del pizza[0];
    for i in range(len(pizza)):
        # remove line breaks
        pizza[i] = pizza[i].replace("\n","");
        pizza[i] = pizza[i].replace("T","2"); #Tomato==2
        pizza[i] = pizza[i].replace("M","1");
        pizza[i] = [int(ch) for ch in pizza[i]];
    return config, pizza;

def check_overlap(slices, new_slice):
    '''
        check for overlaps returning true if overlap exists
        True: overlap exists
        takes arguments pizza, current slices and the new slice
        slice: tuple ( (row1, column1), (row2, column2) )
    '''
    if not slices:
        return False
    if slices[0] == None:
        return False;
    for s in slices:
        # condition for overlap: any corner falls in the area of an existing slice
        # check every corner
        for corner in new_slice:
            if (corner[0] >= s[0][0] and corner[0] <= s[1][0]) and (corner[1] >= s[0][1] and corner[1] <= s[1][1]):
                return True;
        # check the reverse
        for corner in s:
            if (corner[0] >= new_slice[0][0] and corner[0] <= new_slice[1][0]) and (corner[1] >= new_slice[0][1] and corner[1] <= new_slice[1][1]):
                return True;
    return False;

def check_slice_condition(pizza, config, new_slice):
    '''
        check that the slice meets the minimum TM condition and the maximum size condition
        False: condition not met
    '''
    row1 = new_slice[0][0];
    row2 = new_slice[1][0];
    column1 = new_slice[0][1];
    column2 = new_slice[1][1];

    # check that the slice matches the convention we are using: that row2 >= row1 and that column2 >= column1
    if row2 < row1 or column2 < column1:
        raise ValueError("Convention breached: for any slice, row2 >= row1 and column2 >= column1. This exception is raised to prevent unpredictable programme behaviour.");
        return False;

    # check that the total number of cells does not exceed H
    if (row2 - row1 + 1) * (column2 - column1 + 1) > int(config["H"]) :
        return False;

    # check that the slice contains at least L element of each
    MCount = 0;
    TCount = 0;
    for i in range(row1, row2 + 1):
        for j in range(column1 , column2 + 1):
            if pizza[i][j] == 2:
                TCount += 1;
            if pizza[i][j] == 1:
                MCount += 1;
    if MCount >= int(config["L"]) and TCount >= int(config["L"]):
        pass;
    else:
        return False;

    mRow = config["row"];
    mCol = config["column"];
    # check that the slice does not exceed any boundary condition
    if row1 < 0 or column1 < 0 or row2 < 0 or column2 < 0:
        if row1 > mRow or row2 > mRow or column1 > mCol or column2 > mCol:
            return False;

    return True;

if __name__ == "__main__":
    print(load_in_data("small.in"));
