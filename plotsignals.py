### Kacper Jasiński ###
### 02/23/2024 ###
### This script allows to investigate signals visually by displaying graph ###
### It is additional script - no need to execute, unless user wants to assess signals solely ###
### Usage: python plotsignals.py <file_name>.csv <out_file>.png ###

# Import libraries
import sys
import numpy as np
import matplotlib.pyplot as plt

def plotsignals():
    # Ensure proper usage
    if len(sys.argv) != 3:
        print("Usage: python plotsignals.py <file_name>.csv <out_file>.png")
        print("Where <file_name>.csv is a csv formatted file containing matrix to visualize")
        return 1

    # Load matrix from file
    try:
        matrix = np.loadtxt(sys.argv[1], delimiter = ",")
    except Exception as e:
        print("Usage: python plotsignals.py <file_name>.csv <out_file>.png")
        print("Where <file_name>.csv is a csv formatted file containing matrix to visualize")
        return 2

    # Find number of rows of the matrix
    n_rows = matrix.shape[0]

    # Create subplots for each row
    fig, axs = plt.subplots(n_rows, 1, figsize=(8, 2*n_rows))

    # Plot each row as a separate subplot
    for i in range(n_rows):
        axs[i].plot(matrix[i])

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Save the plots as images
    try:
        fig.savefig(sys.argv[2])
    except:
        print("Usage: python plotsignals.py <file_name>.csv <out_file>.png")
        print("Where <file_name>.csv is a csv formatted file containing matrix to visualize")
        return 3

plotsignals()
