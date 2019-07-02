"""

Python Pattern Search

This will be a version of pattern search in Python, based on the Matlab version.

can use fancier methods, this is a first pass for now

based on: https://www.mathworks.com/help/gads/how-pattern-search-polling-works.html

we'll start with test functions from here:
https://en.wikipedia.org/wiki/Test_functions_for_optimization

to-do:
may eventually want to add in constraints
will want to parallelize, but get single core version working first

basic outline:
need initial point in right number of dimensions (N)
need objective function
need initial step size

evaluate function at 2N+1 points (initial + steps of unit length (forward and backward) in each dimension)

if point is more optimal than initial point:
new initial point is the more optimal one (choice of whether to check all or to just move to the first one that's better)
double step size
evaluate function at all points
repeat

if no checkpoint is more optimal:
keep same initial point
half step size
evaluate function at all points
repeat

stopping criteria: (could add others, but these are fine)
mesh size less than minimum size (mesh tolerance from Matlab page)
reach max number of iterations

Version notes:

version 1 - can minimize on a spherical surface!
short term to-do: figure out how to implement constraints on coordinates, test on other optimization functions
longer term: generalize optimization function + number of dimensions, use multiprocessing

version 2 - works on other functions and can implement bounds!
short term to-do: generalize on number of dimensions
longer term: build GUI

version 3 - added interactivity and generalized the number of dimensions, mostly, though depends on user to make sure that optimization_function is consistent with number used
next steps: time to start thinking about turning the interactive parts into the GUI!

"""

import numpy as np
import math
import sys

def optimization_function(point): # Need to make sure that functions match with number of dimensions; not really an obvious way to do that, probably should just have that be a specification of each test function.
# Spherical function
	#x = point[0]
	#y = point[1]
	#z = x**2 + y**2

# Ackley function
	#x = point[0]
	#y = point[1]
	#z = -20.0*math.exp(-0.2*math.sqrt(0.5*(x**2 + y**2))) - math.exp(0.5*(math.cos(2*math.pi*x)+math.cos(2*math.pi*y))) + math.exp(1.0) + 20.0

# Beale function
#	x = point[0]
#	y = point[1]
#	z = (1.5-x+x*y)**2 + (2.25-x+x*y**2)**2 + (2.625-x+x*y**3)**2

# Rastrigin function - generalized to multi-dimensions, yay!

	z = 10*(len(point))
	for i in range(len(point)):
		x_i = point[i]
		z += (x_i**2 - 10*math.cos(2*math.pi*x_i))

# Easom function
#	x = point[0]
#	y = point[1]
#	z = (-1)*math.cos(x)*math.cos(y)*math.exp((-1)*((x-math.pi)**2 + (y-math.pi)**2))

	return z

def bounds_check(point):

	for i in range(len(point)):
		if point[i] < min_bounds[i]:
			point[i] = min_bounds[i]
		if point[i] > max_bounds[i]:
			point[i] = max_bounds[i]

	return point

def generate_steps(num_dimensions,step_size,point,bounds):
	output_list = [point] # Include starting point as a thing to be evaluated

	for i in range(num_dimensions):
		shift_vector = np.zeros(num_dimensions)
		shift_vector[i] = step_size
		newpoint_a = point + shift_vector
		newpoint_b = point - shift_vector

		if bounds == True:
			newpoint_a = bounds_check(newpoint_a)
			newpoint_b = bounds_check(newpoint_b)

		output_list.append(newpoint_a)
		output_list.append(newpoint_b)

	return output_list

def test_points(point_list):
	output_value_list = []

	for point in point_list:
		temp_output = optimization_function(point)
		output_value_list.append(temp_output)

	return output_value_list

def convergence_check(num_iterations,step_size):
	convergence_decision = 0

	if num_iterations > max_iterations:
		convergence_decision = 1

	if step_size < min_step_size:
		convergence_decision = 1

	return convergence_decision

def integer_check(user_input): # Adapted from stackoverflow: https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
	try:
		int(user_input)
		return True
	except ValueError:
		return False

def YN_check(user_input):
	if (user_input == "Y") or (user_input == "y") or (user_input == "N") or (user_input == "n"):
		return True
	else:
		return False

def float_check(user_input):
	try:
		float(user_input)
		return True
	except ValueError:
		return False


# Hardcoded parameters section
step_size = 1.0 # Assumes uniform step sizes for all dimensions, I *think* this is fine given pattern search grid employed here
max_iterations = 1000
min_step_size = 1E-6
#

num_dimensions_user = raw_input("How many dimensions are in the search space? ") # Need raw_input, not input
int_flag = integer_check(num_dimensions_user)

while int_flag == False:
	print("Your input wasn't an integer.\n")
	num_dimensions_user = raw_input("How many dimensions are in the search space? ")
	int_flag = integer_check(num_dimensions_user)

num_dimensions = int(num_dimensions_user)

initial_point = np.zeros(num_dimensions)

for i in range(num_dimensions):
	initial_point_user = raw_input("What is the initial coordinate for dimension %s? "%i)
	valid_point_flag = float_check(initial_point_user)

	while valid_point_flag == False:
		print("Your input wasn't a valid number.\n")
		initial_point_user = raw_input("What is the initial coordinate for dimension %s? "%i)
		valid_point_flag = float_check(initial_point_user)

	initial_point[i] = initial_point_user

bounds_input = str.strip(raw_input("Do you want to put boundaries on the search range? (Y/N) "))
bounds_input_flag = YN_check(bounds_input)

while bounds_input_flag == False:
	print("Your input wasn't either Y or N (or y or n).\n")
	bounds_input = str.strip((raw_input("Do you want to put boundaries on the search range? (Y/N) ")))
	bounds_input_flag = YN_check(bounds_input)

if bounds_input == "Y" or bounds_input == "y":	# Loop above should guarantee that this is fine.
	bounds = True
	min_bounds = np.zeros(num_dimensions)
	max_bounds = np.zeros(num_dimensions)
else:
	bounds = False


if bounds == True:
	for i in range(num_dimensions):
		valid_range_flag = False

		while (valid_range_flag == False):
			bound_user_lower = raw_input("What is the lower bound for dimension %s? "%i)
			valid_bound_flag = float_check(bound_user_lower)

			while valid_bound_flag == False:
				print("Your input wasn't a valid number.\n")
				bound_user_lower = raw_input("What is the lower bound for dimension %s? "%i)
				valid_bound_flag = float_check(bound_user_lower)

			min_bounds[i] = float(bound_user_lower)

			bound_user_upper = raw_input("What is the upper bound for dimension %s? "%i)
			valid_bound_flag = float_check(bound_user_upper)

			while valid_bound_flag == False:
				print("Your input wasn't a valid number.\n")
				bound_user_upper = raw_input("What is the upper bound for dimension %s? "%i)
				valid_bound_flag = float_check(bound_user_upper)

			max_bounds[i] = float(bound_user_upper)

			if (min_bounds[i] >= max_bounds[i]):
				print("Lower bound is greater than or equal to upper bound. Please re-enter both bounds.")
			else:
				valid_range_flag = True

convergence_flag = 0
num_iterations = 0

if bounds == True: # Move initial point within boundaries if it's not already in
	initial_point = bounds_check(initial_point)

while convergence_flag == 0:
	num_iterations += 1
	trial_points = generate_steps(num_dimensions,step_size,initial_point,bounds)
	output_values = test_points(trial_points)
	min_value = min(output_values) # Hard-coded optimizing for minimum...
	min_pos = output_values.index(min_value)
	best_point = trial_points[min_pos]

	print "Iteration #: %s, Best point: %s, Best value: %s, Step size: %s"%(num_iterations,best_point,min_value,step_size)

	if min_pos == 0:
		step_size = step_size*0.5

	else:
		initial_point = best_point
		step_size = step_size*2

	convergence_flag = convergence_check(num_iterations,step_size)

print "Finished!"
