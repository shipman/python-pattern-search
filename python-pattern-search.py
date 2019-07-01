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

"""

import numpy as np
import math

def optimization_function(point): # Currently fixed at 2-D
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

# Rastrigin function
#	x = point[0]
#	y = point[1]
#	z = 20.0 + (x**2 - 10*math.cos(2*math.pi*x)) + (y**2 - 10*math.cos(2*math.pi*y))

# Easom function
	x = point[0]
	y = point[1]
	z = (-1)*math.cos(x)*math.cos(y)*math.exp((-1)*((x-math.pi)**2 + (y-math.pi)**2))

	return z

def bounds_check(point): # Assumes 2-D, though looks straightforward to generalize
	if bounds == True:
		if point[0] < x_min:
			point[0] = x_min
		if point[0] > x_max:
			point[0] = x_max
		if point[1] < y_min:
			point[1] = y_min
		if point[1] > y_max:
			point[1] = y_max

	return point

def generate_steps(num_dimensions,step_size,point):
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



# Hardcoded parameters section
num_dimensions = 2
initial_x = 4.3 # Need to be determined based on number of dimensions instead of hardcoded
initial_y = 4.7
step_size = 1.0 # Assumes uniform step sizes for all dimensions, I *think* this is fine given pattern search grid employed here
max_iterations = 1000
min_step_size = 1E-6
bounds = True # Says whether or not we want to check for bounds on the variables
x_min = -100 # These should be dynamically created depending on number of dimensions and whether or not bounds is true
x_max = 100
y_min = -100
y_max = 100
#

convergence_flag = 0
num_iterations = 0

initial_point = np.array([initial_x,initial_y])
if bounds == True: # Move initial point within boundaries if it's not already in
	initial_point = bounds_check(initial_point)

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

