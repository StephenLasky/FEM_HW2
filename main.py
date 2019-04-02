import math
import numpy as np

# This is the main file for the FEM HW # 2

# STEP # 1. INPUTS: f, omega, coefficients
N  = 16         # this code assumes that N is a real number with a root that is an integer

number_elements = N * 2
number_nodes = int( (math.sqrt(N) + 1) ** 2 )

print("N:{} Elements:{} Nodes:{}".format(N, number_elements, number_nodes))

# STEP # 2: Create Th?

# construct nodes_l2g
nodes_l2g = np.zeros((number_elements, 3), dtype=int) - 1

i = 0
e = 0
while i < number_nodes - int(math.sqrt(number_nodes)):      # skip 'last' node vertically
    if (i + 1) % int(math.sqrt(number_nodes)) == 0:         # skip 'last' node horizontally
        i += 1
        continue

    a = i
    b = int(math.sqrt(number_nodes)) + a

    # construct upper triangle
    nodes_l2g[e, 0] = a
    nodes_l2g[e, 1] = b+1
    nodes_l2g[e, 2] = b

    # construct lower triangle
    nodes_l2g[e + 1, 0] = 0
    nodes_l2g[e + 1, 1] = b+1
    nodes_l2g[e + 1, 2] = a+1

    # iteration here
    e += 2
    i += 1

# STEP 3. Compute a_K, b_K
# define function to compute a_k
def a_k(i,j):
    if i == 0 and j == 0: return -1
    if i == 0 and j == 1: return 2
    if i == 0 and j == 2: return 2

    if i == 1 and j == 0: return -2
    if i == 1 and j == 1: return 1
    if i == 1 and j == 2: return 1

    if i == 2 and j == 0: return -2
    if i == 2 and j == 1: return 1
    if i == 2 and j == 2: return 1

a = np.zeros((number_elements, number_elements))

for e in range(0, number_elements):
    for i in range(0,3):
        # compute b_k

        for j in range(0,3):
            a[nodes_l2g[e,i], nodes_l2g[e,j]] += a_k(i,j)
            # a[nodes_l2g[e, i], nodes_l2g[e, j]] += 1


for i in range(0,number_elements):
    print_str = ""
    for j in range(0,number_elements):
        x = str(a[i,j])
        if x == "0.0":
            x = " "
        else:
            # x = "*"
            pass
        print_str += x
    print(print_str)


