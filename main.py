import numpy as np

# Load input file into Numpy array
sweeps = np.loadtxt("input.txt", dtype=int)

# Loop through array and if current is greater than previous, update count
count = 0
for i,sample in enumerate(sweeps):
    if sample > sweeps[i-1]:
        count = count + 1

print("Amount of sweeps greater than previous: ", count)


