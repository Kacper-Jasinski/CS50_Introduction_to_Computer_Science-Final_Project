### Kacper Jasiński ###
### 02/23/2024 ###
### pimi function is implementation of performance index measured by independance of components ###
### Implementation of this index is based on notes from Big Data classes at Warsaw School of Economics ###

# Import libraries
import numpy as np

def pimi(w):

    # Assign absolute of w matrix to abs_w
    abs_w = np.abs(w)

    # Transpose abs_w matrix
    abs_w_t = abs_w.T

    # Fetch number of rows and cols from abs_w_t
    n_rows_t, n_cols_t = abs_w_t.shape
    n_rows, n_cols = abs_w.shape

    # Find max value for each column of abs_w_t
    max_t = np.max(abs_w_t, axis = 0)
    max = np.max(abs_w, axis = 0)

    # Create n_rows long vector of ones
    o_t = np.ones(n_rows_t)
    o = np.ones(n_rows)

    # Calculate Kronecker tensor
    kron_t = np.outer(o_t, max_t)
    kron = np.outer(o, max)

    # Divide abs_w_t by kron element-wise. Assign it to abs_w_t_kd
    abs_w_t_kd = abs_w_t / kron_t
    abs_w_kd = abs_w / kron

    # Calculate sum for abs_w_t_kd columns and subtract 1
    sum_t = np.sum(abs_w_t_kd, axis = 0) - 1
    sum = np.sum(abs_w_kd, axis= 0) - 1

    # Calculate total for sums
    p1 = np.sum(sum_t)
    p2 = np.sum(sum)

    p = p1 + p2
    p = p / (n_rows * (n_rows - 1))

    return p
