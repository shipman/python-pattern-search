# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\test scripts\pattern_search_first.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import numpy as np
import math
import sys

class Ui_Dialog_First_Window(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(275, 145)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.iter_label = QtWidgets.QLabel(Dialog)
        self.iter_label.setObjectName("iter_label")
        self.gridLayout.addWidget(self.iter_label, 0, 0, 1, 1)
        self.max_iter_input = QtWidgets.QLineEdit(Dialog)
        self.max_iter_input.setObjectName("max_iter_input")
        self.max_iter_input.setToolTip("This is the maximum number of iterations the search will run for.")
        self.max_iter_input.setText("1000") # Default value
        self.gridLayout.addWidget(self.max_iter_input, 0, 1, 1, 2)
        self.init_ss_label = QtWidgets.QLabel(Dialog)
        self.init_ss_label.setObjectName("init_ss_label")
        self.gridLayout.addWidget(self.init_ss_label, 1, 0, 1, 1)
        self.init_ss_input = QtWidgets.QLineEdit(Dialog)
        self.init_ss_input.setObjectName("init_ss_input")
        self.init_ss_input.setToolTip("This is the initial step size that the pattern search will take.")
        self.init_ss_input.setText("1.0") # Default value
        self.gridLayout.addWidget(self.init_ss_input, 1, 1, 1, 2)
        self.min_ss_label = QtWidgets.QLabel(Dialog)
        self.min_ss_label.setObjectName("min_ss_label")
        self.gridLayout.addWidget(self.min_ss_label, 2, 0, 1, 1)
        self.min_ss_input = QtWidgets.QLineEdit(Dialog)
        self.min_ss_input.setObjectName("min_ss_input")
        self.min_ss_input.setToolTip("The search will consider itself converged if the step size is smaller than this value.")
        self.min_ss_input.setText("1E-6") # Default value
        self.gridLayout.addWidget(self.min_ss_input, 2, 1, 1, 2)
        self.num_dim_label = QtWidgets.QLabel(Dialog)
        self.num_dim_label.setObjectName("num_dim_label")
        self.gridLayout.addWidget(self.num_dim_label, 3, 0, 1, 2)
        self.num_dim_input = QtWidgets.QSpinBox(Dialog)
        self.num_dim_input.setObjectName("num_dim_input")
        self.num_dim_input.setToolTip("This is the number of dimensions in the search space.")
        self.num_dim_input.setMinimum(1) #Need to be searching along at least one dimension!
        self.num_dim_input.setValue(2) # Default value
        self.gridLayout.addWidget(self.num_dim_input, 3, 2, 1, 1)
        self.bound_label = QtWidgets.QLabel(Dialog)
        self.bound_label.setObjectName("bound_label")
        self.gridLayout.addWidget(self.bound_label, 4, 0, 1, 2)
        self.bound_cb = QtWidgets.QCheckBox(Dialog)
        self.bound_cb.setObjectName("bound_cb")
        self.bound_cb.setToolTip("This indicates whether boundaries should be applied to coordinates.")
        self.gridLayout.addWidget(self.bound_cb, 4, 2, 1, 1)
        self.next_steps_button = QtWidgets.QPushButton(Dialog)
        self.next_steps_button.setObjectName("next_steps_button")
        self.next_steps_button.clicked.connect(self.proc_input)
        self.gridLayout.addWidget(self.next_steps_button, 5, 0, 1, 1)
        self.run_search_button = QtWidgets.QPushButton(Dialog)
        self.run_search_button.setObjectName("run_search_button")
        self.run_search_button.setEnabled(False)
        self.run_search_button.clicked.connect(self.run_search) # Change this to actually do the thing later
        self.gridLayout.addWidget(self.run_search_button, 5, 1, 1, 2)
        self.exit_button = QtWidgets.QPushButton(Dialog)
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(app.quit)
        self.gridLayout.addWidget(self.exit_button, 6, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Pattern Search"))
        self.iter_label.setText(_translate("Dialog", "Maximum # of Iterations"))
        self.init_ss_label.setText(_translate("Dialog", "Initial Step Size"))
        self.min_ss_label.setText(_translate("Dialog", "Minimum Step Size"))
        self.num_dim_label.setText(_translate("Dialog", "# of Dimensions in Search Space"))
        self.bound_label.setText(_translate("Dialog", "Add Constraints on Coordinates?"))
        self.next_steps_button.setText(_translate("Dialog", "Next Steps"))
        self.run_search_button.setText(_translate("Dialog", "Run Search!"))
        self.exit_button.setText(_translate("Dialog", "Exit"))

    def proc_input(self):
        process_input(self)

    def run_search(self):
        pattern_search(self)

class Ui_Dialog_Input_Error_Window(QtWidgets.QDialog):
    def setupUi(self, Dialog2, Error_String):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(275, 145)
        self.gridLayout = QtWidgets.QGridLayout(Dialog2)
        self.gridLayout.setObjectName("gridLayout")
        self.error_message = QtWidgets.QLabel(Dialog2)
        self.error_message.setObjectName("error_message")
        self.gridLayout.addWidget(self.error_message, 0, 0, 1, 1)
        self.error_message.setText(_translate("Dialog2", Error_String))
        self.updated_input = QtWidgets.QLineEdit(Dialog2)
        self.updated_input.setObjectName("updated_input")
        self.gridLayout.addWidget(self.updated_input, 1, 0, 1, 1)
        self.OK_button = QtWidgets.QPushButton(Dialog2)
        self.OK_button.setObjectName("OK_button")
        self.OK_button.clicked.connect(self.update_value)
        self.gridLayout.addWidget(self.OK_button, 2, 0, 1, 1)
        self.OK_button.setText(_translate("Dialog2", "Update Value"))
        self.exit_button = QtWidgets.QPushButton(Dialog2)
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(Dialog2.close)
        self.gridLayout.addWidget(self.exit_button, 3, 0, 1, 1)
        self.exit_button.setText(_translate("Dialog2", "Exit"))

        QtCore.QMetaObject.connectSlotsByName(Dialog2)
        Dialog2.setWindowTitle(_translate("Dialog2", "Input Validation"))


    def update_value(self):
        updated_value = self.updated_input.text()
        self.error_message.setText("The updated value is %s. If you're happy with this, press Exit."%updated_value)
        return updated_value

class Ui_Dialog_CoordInit_NoBounds(QtWidgets.QDialog):
    def setupUi(self, Dialog3a, num_dimensions):
        _translate = QtCore.QCoreApplication.translate
        Dialog3a.setObjectName("Dialog3a")
        Dialog3a.resize(100*num_dimensions,50)
        self.gridLayout = QtWidgets.QGridLayout(Dialog3a)
        self.gridLayout.setObjectName("gridLayout")
        self.num_dimensions = num_dimensions
        self.bounds_flag = False

        self.coords = []
        for i in range(num_dimensions):
            gen_label = QtWidgets.QLabel(self)
            gen_label.setText("Coordinate %s"%i)
            gen_input = QtWidgets.QLineEdit(self)
            gen_input.setText("0.0") # Default value

            self.coords.append({"coord_value":gen_input})

            self.gridLayout.addWidget(gen_label, 0, i)
            self.gridLayout.addWidget(gen_input, 1, i)

        self.OK_button = QtWidgets.QPushButton(Dialog3a)
        self.OK_button.setObjectName("OK_button")
        self.OK_button.clicked.connect(partial(report_init_coords,self))
        self.gridLayout.addWidget(self.OK_button, 2, 0, 1, (num_dimensions/2))
        self.OK_button.setText(_translate("Dialog3a", "OK"))

        self.exit_button = QtWidgets.QPushButton(Dialog3a)
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(Dialog3a.close)
        self.gridLayout.addWidget(self.exit_button, 2, (num_dimensions/2), 1, (num_dimensions/2))
        self.exit_button.setText(_translate("Dialog3a", "Exit"))

class Ui_Dialog_CoordInit_Bounds(QtWidgets.QDialog):
    def setupUi(self, Dialog3b, num_dimensions):
        _translate = QtCore.QCoreApplication.translate
        Dialog3b.setObjectName("Dialog3b")
        Dialog3b.resize(300,50*num_dimensions)
        self.gridLayout = QtWidgets.QGridLayout(Dialog3b)
        self.gridLayout.setObjectName("gridLayout")
        self.num_dimensions = num_dimensions
        self.bounds_flag = True

        self.coords = []
        self.min = []
        self.max = []

        self.init_label = QtWidgets.QLabel(Dialog3b)
        self.init_label.setObjectName("init_label")
        self.gridLayout.addWidget(self.init_label, 0, 1, 1, 1)
        self.init_label.setText(_translate("Dialog3b", "Initial Value"))

        self.min_label = QtWidgets.QLabel(Dialog3b)
        self.min_label.setObjectName("min_label")
        self.gridLayout.addWidget(self.min_label, 0, 2, 1, 1)
        self.min_label.setText(_translate("Dialog3b", "Minimum Value"))

        self.max_label = QtWidgets.QLabel(Dialog3b)
        self.max_label.setObjectName("max_label")
        self.gridLayout.addWidget(self.max_label, 0, 3, 1, 1)
        self.max_label.setText(_translate("Dialog3b", "Maximum Value"))

        for i in range(num_dimensions):
            gen_label = QtWidgets.QLabel(self)
            gen_label.setText("Coordinate %s"%i)
            gen_init_input = QtWidgets.QLineEdit(self)
            gen_init_input.setText("0.0") # Default value
            gen_min_input = QtWidgets.QLineEdit(self)
            gen_min_input.setText("-10.0") # Default value
            gen_max_input = QtWidgets.QLineEdit(self)
            gen_max_input.setText("10.0") # Default value

            self.coords.append({"coord_value":gen_init_input})
            self.min.append({"min_value":gen_min_input})
            self.max.append({"max_value":gen_max_input})

            self.gridLayout.addWidget(gen_label, 1+i, 0)
            self.gridLayout.addWidget(gen_init_input, 1+i, 1)
            self.gridLayout.addWidget(gen_min_input, 1+i, 2)
            self.gridLayout.addWidget(gen_max_input, 1+i, 3)

        self.OK_button = QtWidgets.QPushButton(Dialog3b)
        self.OK_button.setObjectName("OK_button")
        self.OK_button.clicked.connect(partial(report_init_coords,self))
        self.gridLayout.addWidget(self.OK_button, num_dimensions+1, 1, 1, 1) # fix positioning
        self.OK_button.setText(_translate("Dialog3b", "OK"))

        self.exit_button = QtWidgets.QPushButton(Dialog3b)
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(Dialog3b.close)
        self.gridLayout.addWidget(self.exit_button, num_dimensions+1, 2, 1, 1) # fix positioning
        self.exit_button.setText(_translate("Dialog3b", "Exit"))

class Ui_Dialog_Bounds_Error_Window(QtWidgets.QDialog):
    def setupUi(self, Dialog3c, Error_String):
        _translate = QtCore.QCoreApplication.translate
        Dialog3c.setObjectName("Dialog3c")
        Dialog3c.resize(275, 145)
        self.gridLayout = QtWidgets.QGridLayout(Dialog3c)
        self.gridLayout.setObjectName("gridLayout")
        self.error_message = QtWidgets.QLabel(Dialog3c)
        self.error_message.setObjectName("error_message")
        self.gridLayout.addWidget(self.error_message, 0, 0, 1, 2)
        self.error_message.setText(_translate("Dialog3c", Error_String))

        self.min_label = QtWidgets.QLabel(Dialog3c)
        self.min_label.setObjectName("min_label")
        self.gridLayout.addWidget(self.min_label, 1, 0, 1, 1)
        self.min_label.setText(_translate("Dialog3c", "Minimum Value"))

        self.max_label = QtWidgets.QLabel(Dialog3c)
        self.max_label.setObjectName("max_label")
        self.gridLayout.addWidget(self.max_label, 1, 1, 1, 1)
        self.max_label.setText(_translate("Dialog3c", "Maximum Value"))

        self.min_input = QtWidgets.QLineEdit(Dialog3c)
        self.min_input.setObjectName("min_ss_input")
        self.min_input.setText("-10.0") # Default value
        self.gridLayout.addWidget(self.min_input, 2, 0, 1, 1)

        self.max_input = QtWidgets.QLineEdit(Dialog3c)
        self.max_input.setObjectName("min_ss_input")
        self.max_input.setText("10.0") # Default value
        self.gridLayout.addWidget(self.max_input, 2, 1, 1, 1)

        self.OK_button = QtWidgets.QPushButton(Dialog3c)
        self.OK_button.setObjectName("OK_button")
        self.OK_button.clicked.connect(self.update_value)
        self.gridLayout.addWidget(self.OK_button, 3, 0, 1, 1)
        self.OK_button.setText(_translate("Dialog3c", "Update Value"))
        self.exit_button = QtWidgets.QPushButton(Dialog3c)
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(Dialog3c.close)
        self.gridLayout.addWidget(self.exit_button, 3, 1, 1, 1)
        self.exit_button.setText(_translate("Dialog3c", "Exit"))

        QtCore.QMetaObject.connectSlotsByName(Dialog3c)
        Dialog3c.setWindowTitle(_translate("Dialog3c", "Bounds Validation"))


    def update_value(self):
        updated_min = self.min_input.text()
        updated_max = self.max_input.text()

        min_OK_flag = float_check(updated_min)
        while min_OK_flag == False:
            error_message = "%s is not valid. It should be a float - please update this value."%updated_min
            Dialog2 = QtWidgets.QDialog()
            ui = Ui_Dialog_Input_Error_Window()
            ui.setupUi(Dialog2,error_message)
            Dialog2.exec_()
            updated_min = ui.update_value()
            min_OK_flag = float_check(updated_min)

        max_OK_flag = float_check(updated_max)
        while max_OK_flag == False:
            error_message = "%s is not valid. It should be a float - please update this value."%updated_max
            Dialog2 = QtWidgets.QDialog()
            ui = Ui_Dialog_Input_Error_Window()
            ui.setupUi(Dialog2,error_message)
            Dialog2.exec_()
            updated_max = ui.update_value()
            min_OK_flag = float_check(updated_max)

        self.min_input.setText(updated_min)
        self.max_input.setText(updated_max)

        self.error_message.setText("The updated values for min and max are %s and %s. If you're happy with this, press Exit."%(updated_min,updated_max))
        return (updated_min,updated_max)

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
#   x = point[0]
#   y = point[1]
#   z = (1.5-x+x*y)**2 + (2.25-x+x*y**2)**2 + (2.625-x+x*y**3)**2

# Rastrigin function - generalized to multi-dimensions, yay!

    z = 10*(len(point))
    for i in range(len(point)):
        x_i = point[i]
        z += (x_i**2 - 10*math.cos(2*math.pi*x_i))

# Easom function
#   x = point[0]
#   y = point[1]
#   z = (-1)*math.cos(x)*math.cos(y)*math.exp((-1)*((x-math.pi)**2 + (y-math.pi)**2))

    return z

def bounds_check(point,min_bounds,max_bounds):

    for i in range(len(point)):
        if point[i] < min_bounds[i]:
            point[i] = min_bounds[i]
        if point[i] > max_bounds[i]:
            point[i] = max_bounds[i]

    return point

def generate_steps(num_dimensions,step_size,point,min_bounds=[],max_bounds=[]):
    output_list = [point] # Include starting point as a thing to be evaluated

    for i in range(num_dimensions):
        shift_vector = np.zeros(num_dimensions)
        shift_vector[i] = step_size
        newpoint_a = point + shift_vector
        newpoint_b = point - shift_vector

        if min_bounds != []:
            newpoint_a = bounds_check(newpoint_a,min_bounds,max_bounds)
            newpoint_b = bounds_check(newpoint_b,min_bounds,max_bounds)

        output_list.append(newpoint_a)
        output_list.append(newpoint_b)

    return output_list

def test_points(point_list):
    output_value_list = []

    for point in point_list:
        temp_output = optimization_function(point)
        output_value_list.append(temp_output)

    return output_value_list

def convergence_check(num_iterations,max_iterations,step_size,min_step_size):
    convergence_decision = False

    if num_iterations > max_iterations:
        convergence_decision = True

    if step_size < min_step_size:
        convergence_decision = True

    return convergence_decision

def integer_check(user_input): # Adapted from stackoverflow: https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
    try:
        int(user_input)
        return True
    except ValueError:
        return False

def float_check(user_input):
    try:
        float(user_input)
        return True
    except ValueError:
        return False

def report_init_coords(data_object):
    init_coords = []
    num_dimensions = data_object.num_dimensions

    for i in range(num_dimensions):
        temp_coord = str(data_object.coords[i]["coord_value"].text())
        init_coords.append(temp_coord)

    if data_object.bounds_flag == True:
        min_coords = []
        max_coords = []
        for i in range(num_dimensions):
            temp_min_coord = str(data_object.min[i]["min_value"].text())
            min_coords.append(temp_min_coord)

            temp_max_coord = str(data_object.max[i]["max_value"].text())
            max_coords.append(temp_max_coord)

    for i in range(num_dimensions):
        coord_OK_flag = float_check(init_coords[i])
        while coord_OK_flag == False:
            error_message = "%s is not valid for coordinate %s. It should be a float - please update this value."%(init_coords[i],i)
            Dialog2 = QtWidgets.QDialog()
            ui = Ui_Dialog_Input_Error_Window()
            ui.setupUi(Dialog2,error_message)
            Dialog2.exec_()
            init_coords[i] = ui.update_value()
            coord_OK_flag = float_check(init_coords[i])

        data_object.coords[i]["coord_value"].setText(init_coords[i])
        init_coords[i] = float(init_coords[i])

        if data_object.bounds_flag == True:
            min_OK_flag = float_check(min_coords[i])
            while min_OK_flag == False:
                error_message = "%s is not valid for the minimum of coordinate %s. It should be a float - please update this value."%(min_coords[i],i)
                Dialog2 = QtWidgets.QDialog()
                ui = Ui_Dialog_Input_Error_Window()
                ui.setupUi(Dialog2,error_message)
                Dialog2.exec_()
                min_coords[i] = ui.update_value()
                min_OK_flag = float_check(min_coords[i])

            data_object.min[i]["min_value"].setText(min_coords[i])
            min_coords[i] = float(min_coords[i])

            max_OK_flag = float_check(max_coords[i])
            while max_OK_flag == False:
                error_message = "%s is not valid for the maximum of coordinate %s. It should be a float - please update this value."%(max_coords[i],i)
                Dialog2 = QtWidgets.QDialog()
                ui = Ui_Dialog_Input_Error_Window()
                ui.setupUi(Dialog2,error_message)
                Dialog2.exec_()
                max_coords[i] = ui.update_value()
                max_OK_flag = float_check(max_coords[i])

            data_object.max[i]["max_value"].setText(max_coords[i])
            max_coords[i] = float(max_coords[i])

            if min_coords[i] >= max_coords[i]:
                valid_bound_flag = False
            else:
                valid_bound_flag = True

            while valid_bound_flag == False:
                error_message = "Lower bound (%s) is greater than or equal to upper bound (%s) for coordinate %s. Please re-enter both bounds."%(min_coords[i],max_coords[i],i)
                Dialog3c = QtWidgets.QDialog()
                ui = Ui_Dialog_Bounds_Error_Window()
                ui.setupUi(Dialog3c,error_message)
                Dialog3c.exec_()
                (min_coords[i],max_coords[i]) = ui.update_value()
                if min_coords[i] < max_coords[i]:
                    valid_bound_flag = True

            data_object.min[i]["min_value"].setText(str(min_coords[i]))
            min_coords[i] = float(min_coords[i])
            data_object.max[i]["max_value"].setText(str(max_coords[i]))
            max_coords[i] = float(max_coords[i])
            valid_bound_flag = True

    if data_object.bounds_flag == True:
        return init_coords,min_coords,max_coords
    else:
        return init_coords

def process_input(data_object):
    num_iter_string = data_object.max_iter_input.text()
    init_ss_string = data_object.init_ss_input.text()
    conv_ss_string = data_object.min_ss_input.text()
    need_bounds = data_object.bound_cb.checkState()
    iter_OK_flag = integer_check(num_iter_string)
    init_OK_flag = float_check(init_ss_string)
    conv_OK_flag = float_check(conv_ss_string)

    while iter_OK_flag == False:
        error_message = "%s is not an integer. Please enter an integer."%num_iter_string
        Dialog2 = QtWidgets.QDialog()
        ui = Ui_Dialog_Input_Error_Window()
        ui.setupUi(Dialog2,error_message)
        Dialog2.exec_()
        num_iter_string = ui.update_value()
        iter_OK_flag = integer_check(num_iter_string)

    while init_OK_flag == False:
        error_message = "%s is not a valid initial step size. Please update this value."%init_ss_string
        Dialog2 = QtWidgets.QDialog()
        ui = Ui_Dialog_Input_Error_Window()
        ui.setupUi(Dialog2,error_message)
        Dialog2.exec_()
        init_ss_string = ui.update_value()
        init_OK_flag = float_check(init_ss_string)

    while conv_OK_flag == False:
        error_message = "%s is not a valid convergence step size. Please update this value."%conv_ss_string
        Dialog2 = QtWidgets.QDialog()
        ui = Ui_Dialog_Input_Error_Window()
        ui.setupUi(Dialog2,error_message)
        Dialog2.exec_()
        conv_ss_string = ui.update_value()
        conv_OK_flag = float_check(conv_ss_string)

    num_iterations = int(num_iter_string)
    data_object.max_iter_input.setText(str(num_iterations))

    init_ss = float(init_ss_string)
    data_object.init_ss_input.setText(str(init_ss))

    conv_ss = float(conv_ss_string)
    data_object.min_ss_input.setText(str(conv_ss))

    num_dimensions = data_object.num_dim_input.value()

    init_coords = []

    if need_bounds:
        #print "Boundaries are needed for coodinates!"
        Dialog3b = QtWidgets.QDialog()
        ui = Ui_Dialog_CoordInit_Bounds()
        ui.setupUi(Dialog3b,num_dimensions)
        Dialog3b.exec_()

        coord_bounds_min = []
        coord_bounds_max = []

        for i in range(num_dimensions):
            temp_coord = float(ui.coords[i]["coord_value"].text())
            temp_bound_min = float(ui.min[i]["min_value"].text())
            temp_bound_max = float(ui.max[i]["max_value"].text())
            init_coords.append(temp_coord)
            coord_bounds_min.append(temp_bound_min)
            coord_bounds_max.append(temp_bound_max)

    else:
        #print "Boundaries are not needed for coodinates!"
        Dialog3a = QtWidgets.QDialog()
        ui = Ui_Dialog_CoordInit_NoBounds()
        ui.setupUi(Dialog3a,num_dimensions)
        Dialog3a.exec_()

        for i in range(num_dimensions):
            temp_coord = float(ui.coords[i]["coord_value"].text())
            init_coords.append(temp_coord)

    #print "Number of iterations: %s"%num_iterations
    #print "Initial step size: %s"%init_ss
    #print "Convergence step size: %s"%conv_ss
    #print "Number of dimensions: %s"%num_dimensions
    #print "Initial coordinates: %s"%init_coords
    data_object.init_coords = init_coords

    if need_bounds:
        #print "Minimum boundaries: %s"%coord_bounds_min
        data_object.coord_bounds_min = coord_bounds_min
        #print "Maximum boundaries: %s\n"%coord_bounds_max
        data_object.coord_bounds_max = coord_bounds_max

    data_object.run_search_button.setEnabled(True)

    # At this point we then need to ungray the "Run Simulations" button and then actually do the thing!


def pattern_search(data_object):
    num_iter_string = data_object.max_iter_input.text()
    init_ss_string = data_object.init_ss_input.text()
    conv_ss_string = data_object.min_ss_input.text()
    need_bounds = data_object.bound_cb.checkState()

    max_iterations = int(num_iter_string)
    step_size = float(init_ss_string)
    conv_ss = float(conv_ss_string)
    num_dimensions = data_object.num_dim_input.value()

    init_coords = data_object.init_coords

    if need_bounds:
        coord_bounds_min = data_object.coord_bounds_min
        coord_bounds_max = data_object.coord_bounds_max

    print "Number of iterations: %s"%max_iterations
    print "Initial step size: %s"%step_size
    print "Convergence step size: %s"%conv_ss
    print "Number of dimensions: %s"%num_dimensions

    initial_point = np.zeros(num_dimensions)

    if need_bounds:
        min_bounds = np.zeros(num_dimensions)
        max_bounds = np.zeros(num_dimensions)

    for i in range(num_dimensions):
        initial_point[i] = float(init_coords[i])

        if need_bounds:
            min_bounds[i] = float(coord_bounds_min[i])
            max_bounds[i] = float(coord_bounds_max[i])

    convergence_flag = False
    num_iterations = 0

    if need_bounds:
        initial_point = bounds_check(initial_point,min_bounds,max_bounds)

    if need_bounds:
        print "Minimum boundaries: %s"%coord_bounds_min
        print "Maximum boundaries: %s"%coord_bounds_max

    for i in range(num_dimensions):
        if i == 0:
            init_coord_string = "[%s"%str(initial_point[i])
        else:
            init_coord_string += ", %s"%str(initial_point[i])

    init_coord_string += "]"

    print "Initial coordinates: %s\n"%init_coord_string

    while convergence_flag == False:
        num_iterations += 1

        if need_bounds:
            trial_points = generate_steps(num_dimensions,step_size,initial_point,min_bounds,max_bounds)
        else:
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

        convergence_flag = convergence_check(num_iterations,max_iterations,step_size,conv_ss)

    print "Finished!\n"


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_First_Window()
    ui.setupUi(Dialog)
    #ui = Ui_Dialog_Input_Error_Window()
    #test_string = "This is a test"
    #ui.setupUi(Dialog, test_string)
    Dialog.show()
    sys.exit(app.exec_())

