import math
import numpy as np
import functions

# ATTEMPT # 3: In this attempt, we try to make use of the interpolation stuff as seen in lecture notes #6.

# This is the main file for the FEM HW # 2

# STEP # 1. INPUTS: f, omega, coefficients
N  = 9         # this code assumes that N is a real number with a root that is an integer, N is the total number of squares!

number_elements = N * 2
number_nodes = int( (math.sqrt(N) + 1) ** 2 )

print("N:{} Elements:{} Nodes:{}".format(N, number_elements, number_nodes))

# STEP # 2: Create Th?

# construct nodes_l2g
nodes_l2g = functions.generate_nodes_l2g(N)

# STEP 3. Compute a_K, b_K  
# define a function to compute phi
def d_phi_hat(ijk, x1_hat, x2_hat):
    i,j,k = 0,1,2

    if ijk == i:
        return np.asarray([0, 1])
    elif ijk == j:
        return np.asarray([-1, -1])
    elif ijk == k:
        return np.asarray([1,0])
    else:
        print("warning: d_phi_hat error!")

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