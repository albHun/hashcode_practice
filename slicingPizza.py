from g1 import *
from random import randint
from visualisation import plot_out_data
import pprint

input_file = "big.in"


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


random_limit = 50000
partitions = 10
partitions_step = 3
partitions_delta = 8
iteration_limit = 10

configuration, pizza = load_in_data(input_file)
row = int(configuration["row"])
column = int(configuration["column"])
slicing_methods = list()

# for iter in range(0, iteration_limit):
for partitions in range(partitions - partitions_delta, partitions + partitions_delta, partitions_step):
	print("Entering iteration with partitions as " + str(partitions));
	slices = list()
	for time in range(0, random_limit):
		# row1 = randint(row / partitions * part, row * (part + 1)/partitions - 1)
		# row2 = randint(row1, row * (part + 1)/partitions - 1)
		# col1 = randint(column / partitions * part, column * (part + 1)/partitions - 1)
		# col2 = randint(col1, column * (part + 1)/partitions - 1)

		# row1 = randint(0, row-1)
		# row2 = randint(row1, row-1)
		# col1 = randint(0, column-1)
		# col2 = randint(col1, column-1)

		row1 = randint(0, row - 1)
		if row1 + partitions > row - 1:
			temp = row - 1
		else:
			temp = row1 + partitions
		row2 = randint(row1, temp)
		col1 = randint(0, column - 1)
		if col1 + partitions > row - 1:
			temp = column - 1
		else:
			temp = col1 + partitions
		col2 = randint(col1, temp)

		if row1 == row2 and col1 == col2:
			continue
		new_slice = ((row1, col1), (row2, col2))
		if (not check_overlap(slices, new_slice)) and check_slice_condition(pizza, configuration, new_slice):
			slices.append(new_slice)

	slicing_methods.append((check_final_points(slices), output_slices(slices)))
	slicing_methods.sort(reverse=True)
	print("Finished iteration step. Current optimal count: ")
	print(slicing_methods[0][0])

# print(slicing_methods[0])
with open("output.txt", "w") as text_file:
    text_file.write(slicing_methods[0][1])
plot_out_data(input_file, "output.txt")
