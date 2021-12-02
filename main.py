import numpy as np

##### Part 1

# Load input file into Numpy array
sweeps = np.loadtxt("input.txt", dtype=int)

# Loop through array and if current is greater than previous, update count
count = 0
for i,sample in enumerate(sweeps):
    if sample > sweeps[i-1]:
        count = count + 1

print("Amount of sweeps greater than previous: ", count)

    
##### Part 2
count = 0
for i,sample in enumerate(sweeps):
    if (i+3) >= np.size(sweeps):
        break
    group1 = sample + sweeps[i+1] + sweeps[i+2]
    group2 = sweeps[i+1] + sweeps[i+2] + sweeps[i+3]

    if group2 > group1:
        count = count + 1
        print(count)
    
print("Amount of sweep groups greater than previous groups: ", count)