### Kacper Jasiński ###
### 02/21/2024 ###
### This script allows to output signals, noises and mix matrices to csv files ###
### Usage: python mixsignals.py <max> <step> ###

# Import libraries
import sys
import numpy as np

def mixsignals():
    # Define interval for testing
    min = 0

    try:
        max = float(sys.argv[1])
        step = float(sys.argv[2])
    except:
        print("Usage: python mixsignals.py <observations> <step>")
        print("For visualization step of 0.0001 is recommended. e.g. python mixsignals.py 0.3 0.0001")
        
        return 1

    # Create number of observations variable
    observations = int(max / step) + 1

    # Define signal functions
    def f1(x):
        return np.sin((300 * x) + 30 * np.cos(60 * x))

    def f2(x):
        return np.sin(350 * x)

    def f3(x):
        return np.cos(3000 * x) * np.sin(60 * x) / np.pi

    def f4(x):
        return np.sign(np.sin(700 * x))

    # Define source signals arrays
    s1 = [f1(i) for i in np.arange(min, max, step)]
    s2 = [f2(i) for i in np.arange(min, max, step)]
    s3 = [f3(i) for i in np.arange(min, max, step)]
    s4 = [f4(i) for i in np.arange(min, max, step)]
    s5 = np.random.normal(0, 1, observations)

    # Create signals matrix
    s_matrix = np.vstack((s1, s2, s3, s4, s5))

    # Fetch number of signals
    n_signals = s_matrix.shape[0]

    # Create mixing matrix
    m_matrix = np.random.normal(0, 1, (n_signals, n_signals))

    # Apply noises to signals matrix
    x_matrix = np.dot(m_matrix, s_matrix)

    # Export matrices to csv filesl s - signals, a - mixing matrix (noises), x - data
    np.savetxt("s.csv", s_matrix, delimiter=',', fmt='%.6f')
    np.savetxt("a.csv", m_matrix, delimiter=',', fmt='%.6f')
    np.savetxt("x.csv", x_matrix, delimiter=',', fmt='%.6f')

    # Print matrix conditioning for noises
    print(f"Matrix conditioning: {np.linalg.cond(m_matrix)}")

mixsignals()
