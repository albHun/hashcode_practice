from g1 import *
from random import randint
import pprint


def check_final_points(slices):
	count = 0
	for sl in slices:
		count += (sl[1][0] - sl[0][0] + 1) * (sl[1][1] - sl[0][1] + 1)
	return count


def output_slices(slices):
	final_slices = ""
	for sl in slices:
		final_slices += str(sl[0][0]) +" " +str(sl[0][1]) +" " + str(sl[1][0]) +" " + str(sl[1][1]) + '\n'
	return final_slices

random_limit = 100
iteration_limit = 100

configuration, pizza = load_in_data("small.in")
row = int(configuration["row"])
column = int(configuration["column"])
slicing_methods = list()

for iter in range(0, iteration_limit):
	slices = list()
	for time in range(0, random_limit):
		row1 = randint(0, row-1)
		row2 = randint(row1, row-1)
		col1 = randint(0, column-1)
		col2 = randint(col1, column-1)
		if row1 == row2 and col1 == col2:
			continue
		new_slice = ((row1, col1), (row2, col2))
		if (not check_overlap(slices, new_slice)) and check_slice_condition(pizza, configuration, new_slice):
			slices.append(new_slice)

	slicing_methods.append((check_final_points(slices), output_slices(slices)))
	slicing_methods.sort(reverse=True)
	pprint.pprint(slicing_methods[0])