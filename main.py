import math
import numpy as np
import functions

# ATTEMPT # 3: In this attempt, we try to make use of the interpolation stuff as seen in lecture notes #6.

# This is the main file for the FEM HW # 2

# STEP # 1. INPUTS: f, omega, coefficients
N  = 9         # this code assumes that N is a real number with a root that is an integer

number_elements = N * 2
number_nodes = int( (math.sqrt(N) + 1) ** 2 )

print("N:{} Elements:{} Nodes:{}".format(N, number_elements, number_nodes))

# STEP # 2: Create Th?

# construct nodes_l2g
nodes_l2g = np.zeros((number_elements, 3), dtype=int) - 1

i = 0
e = 0
while i < number_nodes:
    n = int( math.sqrt(N) )
    e = functions.get_associated_element(i,n)

    # figure out segments to skip here as we run the hexagonal figure over the grid
    top, right, bot, left = functions.is_edge(i, n)
    skip = [False, False, False, False, False, False]

    if top:
        skip[2] = True
        skip[3] = True
        skip[4] = True
    if right:
        skip[0] = True
        skip[4] = True
        skip[5] = True
    if bot:
        skip[0] = True
        skip[1] = True
        skip[5] = True
    if left:
        skip[1] = True
        skip[2] = True
        skip[3] = True

    assignments = [0,1,2,0,1,2]
    es = [e, e-1, e-2-2*n, e-1-2*n, e-2*n, e+1]

    for j in range(0,6):
        e = es[j]
        assign = assignments[j]

        # print("Trying to set e:{} assign:{} -> i:{}".format(e, assign, i))
        if skip[j] == False:
            # print("\tSET e:{} assign:{} -> i:{}".format(e,assign,i))
            nodes_l2g[e, assign] = i


    i += 1

print(nodes_l2g)

# run some tests here
# for n = 4
if N/4 == 4:
    assert nodes_l2g[0,0] == 0
    assert nodes_l2g[0,1] == 5
    assert nodes_l2g[8,0] == 5
    assert nodes_l2g[20,0] == 12
    assert nodes_l2g[20,1] == 17
    assert nodes_l2g[20,2] == 18

# STEP 3. Compute a_K, b_K
# define function to compute a_k
def a_k(i,j):
    d = [[0,1], [-1,-1], [1,0]]     # derivatives of phi stored as [i,j,k][x1,x2]
    to_integrate = d[i][0] * d[j][0] + d[i][1] * d[j][1]

    return to_integrate


a = np.zeros((number_elements, number_elements))

for e in range(0, number_elements):
    for i in range(0,3):
        # compute b_k

        for j in range(0,3):
            a[nodes_l2g[e,i], nodes_l2g[e,j]] += a_k(i,j)




# for i in range(0,number_elements):
#     print_str = ""
#     for j in range(0,number_elements):
#         x = str(a[i,j])
#         if x == "0.0":
#             x = " "
#         else:
#             # x = "*"
#             pass
#         print_str += x
#     print(print_str)
#