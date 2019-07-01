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
"""

import numpy as np

def optimization_function(point):
	x = point[0]
	y = point[1]
	z = x**2 + y**2
	return z

def generate_steps(num_dimensions,step_size,point):
	output_list = [point] # Include starting point as a thing to be evaluated

	for i in range(num_dimensions):
		shift_vector = np.zeros(num_dimensions)
		shift_vector[i] = step_size
		newpoint_a = point + shift_vector
		newpoint_b = point - shift_vector
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



# Hardcoded parameters section
num_dimensions = 2
initial_x = 1.3
initial_y = 1.7
step_size = 1.0
max_iterations = 1000
min_step_size = 1E-6
#

convergence_flag = 0
num_iterations = 0

initial_point = np.array([initial_x,initial_y])

while convergence_flag == 0:
	num_iterations += 1
	trial_points = generate_steps(num_dimensions,step_size,initial_point)
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

