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
nodes_l2g = np.zeros((number_elements, 3)) - 1

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
