import math
import numpy as np
import functions as f

# ATTEMPT # 3: In this attempt, we try to make use of the interpolation stuff as seen in lecture notes #6.

# This is the main file for the FEM HW # 2

# STEP # 1. INPUTS: f, omega, coefficients
N  = 400         # this code assumes that N is a real number with a root that is an integer, N is the total number of squares!

number_elements = N * 2
number_nodes = int( (math.sqrt(N) + 1) ** 2 )

print("N:{} Elements:{} Nodes:{}".format(N, number_elements, number_nodes))

# STEP # 2: Create Th?

# construct nodes_l2g
nodes_l2g = f.generate_nodes_l2g(N)

# STEP 3. Compute a_K, b_K  
# define a function to compute phi
def d_phi_hat(ijk, x1_hat, x2_hat):
    i,j,k = 0,1,2

    z = None
    if ijk == i:
        z = np.asarray([0, 1])
    elif ijk == j:
        z =  np.asarray([-1, -1])
    elif ijk == k:
        z =  np.asarray([1,0])
    else:
        print("warning: d_phi_hat error!")

    return z

# define function to compute a_k
# input : local node i, local node j, element e
def a_k(i,j,e):
    w_hat_g = 1 # weighting variable - we have no idea what this should be.

    # set up our local coordinates: we might need to change this later?
    x1_hat, x2_hat, x3_hat = 0, 1, 0
    y1_hat, y2_hat, y3_hat = 0, 0, 1

    # get global coordinates
    x1, y1 = f.local_coor_to_global(x1_hat, y1_hat, e, nodes_l2g, N)
    x2, y2 = f.local_coor_to_global(x2_hat, y2_hat, e, nodes_l2g, N)
    x3, y3 = f.local_coor_to_global(x3_hat, y3_hat, e, nodes_l2g, N)

    # compute our 'Z' array and B. B is Z^(-1).
    jacobian = np.abs(np.asarray([[x2-x1, x3-x1],[y2-y1, y3-y1]]))
    B = np.linalg.inv(np.abs(jacobian))     # take aboslute value of the jacobian

    x_g_hats = [1.0/6, 2.0/3, 1.0/6]
    y_g_hats = [1.0/6, 1.0/6, 2.0/3]
    w_g_hat = 1.0 / 6

    result = 0.0
    for g in range(0,3):
        x_g_hat = x_g_hats[g]
        y_g_hat = y_g_hats[g]
        z = d_phi_hat(j, x_g_hat, y_g_hat).reshape((1,2))
        z = np.matmul(z, np.matmul(B,B.T))
        z = np.matmul(z, d_phi_hat(i, x_g_hat, y_g_hat))
        z *= np.linalg.det(jacobian)
        result += z

    result *= w_g_hat

    return result



    # finally : compute the result!

    # side-attempt: nevermind the above, for now!
    d_phi_i = np.asarray([ d_phi_hat(i, x1_hat, x2_hat)[0] * B[0, 0] + d_phi_hat(i, x1_hat, x2_hat)[1] * B[1, 0],
                           d_phi_hat(i, x1_hat, x2_hat)[0] * B[0, 1] + d_phi_hat(i, x1_hat, x2_hat)[1] * B[1, 1] ])
    d_phi_j = np.asarray([d_phi_hat(j, x1_hat, x2_hat)[0] * B[0, 0] + d_phi_hat(j, x1_hat, x2_hat)[1] * B[1, 0],
                          d_phi_hat(j, x1_hat, x2_hat)[0] * B[0, 1] + d_phi_hat(j, x1_hat, x2_hat)[1] * B[1, 1]])

    result = np.dot(d_phi_i, d_phi_j)

    return result

a = np.zeros((number_nodes, number_nodes))
# create the HISTORY matrix. this is used to debug and figure out what exacty has happened at each spot
HISTORY = []
for i in range(0,number_nodes):
    new_r = []
    for j in range(0,number_nodes):
        new_r.append([])
    HISTORY.append(new_r)

n = int(math.sqrt(N))
for e in range(0, number_elements):
    for i in range(0,3):

        if not f.is_boundary(int(nodes_l2g[e, i]), n):
            # compute b_k

            for j in range(0,3):
                if not f.is_boundary(nodes_l2g[e, j], n):
                    a[nodes_l2g[e, i], nodes_l2g[e, j]] += a_k(i, j, e)
                    # a[nodes_l2g[e, j], nodes_l2g[e, i]] += a_k(i, j, e)
                    # a[nodes_l2g[e, i], nodes_l2g[e, j]] += a_k(j, i, e)
                    # a[nodes_l2g[e, j], nodes_l2g[e, i]] += a_k(j, i, e)

                    v1 = nodes_l2g[e, i]
                    v2 = nodes_l2g[e, j]
                    vr = a_k(i, j, e)
                    HISTORY[v1][v2].append(vr)

print("HIST:", HISTORY[1][1])



np.set_printoptions(linewidth=1e6, threshold=1e6)
print(a)



# for i in range(0,number_elements):
#     print_str = ""
#     for j in range(0,number_elements):
#         x = str(a[i,j])
#         if x == "0.0":
#             x = " "
#         else:
#             x = "*"
#             pass
#         print_str += x
#     print(print_str)
