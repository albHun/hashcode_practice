from g1 import *
from random import randint
from visualisation import plot_out_data
import pprint

input_file = "big.in"
random_limit = 20000
random_limit_step = 20000
partitions_init = 10
partitions_step = 2
partitions_delta = 4
iteration_limit = 5

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

configuration, pizza = load_in_data(input_file)
row = int(configuration["row"])
column = int(configuration["column"])
slicing_methods = list()

while True:
	# reset large variables and increment random_limit
	print("Finished iteration block. Incrementing random_limit. Current random_limit count: " + str(random_limit));
	random_limit += random_limit_step
	partitions = 8;
	del slicing_methods[1:-1];

	for partitions in range(partitions_init - partitions_delta, partitions_init + partitions_delta, partitions_step):
		print("incrementing partition, partition = " + str(partitions))
		for iter in range(0, iteration_limit):
			slices = list()
			for time in range(0, random_limit):

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
					update_filled_pizza(new_slice);
					slices.append(new_slice)

			slicing_methods.append((check_final_points(slices), output_slices(slices)))
			slicing_methods.sort(reverse=True)

		print("Finished iteration step. Current optimal count: ")
		print(slicing_methods[0][0])
		print("saving optimal output data")
		with open("output.txt", "w") as text_file:
			#save optimal solution at the end of every partition change
		    text_file.write(slicing_methods[0][1])

plot_out_data(input_file, "output.txt")
