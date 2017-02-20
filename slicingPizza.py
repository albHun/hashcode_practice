from g1 import *
from random import randint
from visualisation import plot_out_data
import pprint

input_file = "big.in"
iterationLimit = 100000000
reportingInterval = 100000
partitions = 6
# partitions_step = 2
# partitions_delta = 1
# iteration_limit = 10


configuration, pizza = load_in_data(input_file)
row = int(configuration["row"])
column = int(configuration["column"])
slicing_methods = list()

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

def status_update(slices, iterationCount): 
	slicing_methods.append((check_final_points(slices), output_slices(slices)))
	slicing_methods.sort(reverse=True)
	print("Status Reporting. Current optimal count: ")
	print(slicing_methods[0][0])
	print("Current iterationCount: ")
	print(iterationCount)
	print("saving optimal output data")
	with open("output.txt", "w") as text_file:
		#save optimal solution at the end of every partition change
	    text_file.write(slicing_methods[0][1])

while True:
	slices = list()
	for iterationCount in range(0, iterationLimit):

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

		# if row1 == row2 and col1 == col2:
		# 	continue
		new_slice = ((row1, col1), (row2, col2))
		if (not check_overlap(slices, new_slice)) and check_slice_condition(pizza, configuration, new_slice):
			update_filled_pizza(new_slice);
			slices.append(new_slice)
		if iterationCount % reportingInterval == 0:
			status_update(slices, iterationCount);

	print("Iterated till limit, restarting iteration, but keeping optimal value.")
	del slicing_methods[2:-1];

	

plot_out_data(input_file, "output.txt")
