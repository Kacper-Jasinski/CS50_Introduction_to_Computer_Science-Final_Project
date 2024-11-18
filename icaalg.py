### Kacper Jasiński ###
### 02/23/2024 ###
### This script is implementation of Independent Component Analysis in Python ###
### It takes matrix with data formatted as a csv file, learning parameters and number of iterations to maximize performance index ###

# Import libraries
import sys
import numpy as np
from itertools import product
import warnings
from pimi import pimi

# Catch all runtime warnings
warnings.filterwarnings("error", category=RuntimeWarning)

def icaalg():

    # Manage step constants for optimizing pimi by changing l1-l2 params
    step_l1 = 1
    step_l2 = 0.0001
    best_pimi = 1

    # Ensure proper usage
    if len(sys.argv) != 6:
        print("Usage: python icaalg.py <file_name>.csv l_param1 l_param2 l_param3 radius")
        print("Make sure to include all 5 arguments")
        return 1

    # Load matrix from file
    try:
        x = np.loadtxt(sys.argv[1], delimiter = ",")
    except:
        print("Usage: python icaalg.py <file_name>.csv l_param1 l_param2 l_param3 radius")
        print("Where <file_name>.csv is a csv formatted file containing matrix to visualize")
        return 2

    # Find number of rows and cols of the matrix
    n_rows, n_cols = x.shape

    # Define weights matrix
    w = np.eye(n_rows)

    # Define empty matrix of inverted signals
    y = np.zeros_like(x)

    # Assign learning parameters from CLI to variables
    try:
        l_param1 = int(sys.argv[2])
        l_param2 = float(sys.argv[3])
        l_param3 = float(sys.argv[4])
        radius = int(sys.argv[5])

    except:
        print("Usage: python icaalg.py <file_name>.csv l_param1 l_param2 l_param3 radius")
        print("l_params are learning paramaters that affect changing learning rate")
        print("radius is an integer used to calculate optimization area")
        return 3

    # Define radius for l1 and l2 params
    r_l1 = radius * step_l1
    r_l2 = radius * step_l2

    # Create ranges for learning param optimization
    range_l1 = [i for i in np.arange(l_param1 - r_l1, l_param1 + r_l1, step_l1)]
    range_l2 = [i for i in np.arange(l_param2 - r_l2, l_param2 + r_l2, step_l2)]

    # Initiate best learning parameters to be CLA
    best_l1 = l_param1
    best_l2 = l_param2

    # Find the best fit in given diameter using itertools product
    for l1, l2 in product(range_l1, range_l2):

        # Iterate through every observation
        # ei variable is used to adjust learning rate
        for i in range(n_cols):

            if i < l1:
                ei = l2
            else:
                ei = l2 * np.exp(l_param3 * (i - l1))

            # Calculate y's , f's and g's ith column values
            # f and g are arbitrarily chosen functions to represent y. Both are chosen to be non-linear
            # f and g can be adjusted. In default configuration I decided one will be exponential and the second one will be tangent
            y[:, i] = np.dot(w, x[:, i])
            f = y[:, i] ** 3
            g = np.tanh(y[:, i]) / 2

            # Update weight matrix accordingly to difference between identity matrix and outer product of f and g
            w += ei * np.dot((np.eye(n_rows) - np.outer(f, g)), w)


        # Check if pimi for current learning parameters is lower than last best value
        if pimi(w) < best_pimi:
            best_pimi = pimi(w)
            best_l1 = l1
            best_l2 = l2

    # Print pimi value and best parameters
    print(f"best result for l1 = {best_l1} and l2 = {best_l2}")
    print(f"PIMI for these parameters: {best_pimi}")

    # Save separated signals and weights to csv file
    np.savetxt("y.csv", y, delimiter=',', fmt='%.6f')
    np.savetxt("w.csv", w, delimiter=',', fmt='%.6f')

    # Finish function with 0 exit code
    return 0

icaalg()
