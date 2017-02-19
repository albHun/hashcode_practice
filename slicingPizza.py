from g1 import *
from random import randint


def check_final_points(slices):
	count = 0
	for slice in slices:
		count += (slice[1][0] - slice[0][0] + 1) + (slice[1][1] - slice[0][1] + 1)
	return count

iteration_limit = 1000
configuration, pizza = load_in_data("small.in")
row = int(configuration["row"])
column = int(configuration["column"])

slices = list()
for time in range(0, iteration_limit):
	row1 = randint(0, row-1)
	row2 = randint(row1, row-1)
	col1 = randint(0, column-1)
	col2 = randint(col1, column-1)
	if row1 == row2 and col1 == col2:
		break
	new_slice = ((row1, col1), (row2, col2))
	if (not check_overlap(slices, new_slice)) and check_slice_condition(pizza, configuration, new_slice):
		slices.append(new_slice)
print(check_final_points(slices))
