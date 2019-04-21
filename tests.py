import functions
import random
import math

# local_coor_to_global(x1_hat, x2_hat, e, J, N):
def local_coor_to_global_test():
    N = 16

    tcs = []    # e, J, N, x1_base, x2_base
    nodes_l2g = functions.generate_nodes_l2g(N)
    tcs.append([0,nodes_l2g,N,0,0.75])
    tcs.append([2,nodes_l2g,N,0.25,0.75])
    tcs.append([12,nodes_l2g,N,0.5,0.5])
    tcs.append([18,nodes_l2g,N,0.25,0.25])

    # test for N = 9
    N = 9
    nodes_l2g = functions.generate_nodes_l2g(N)
    tcs.append([0,nodes_l2g,N,0,2.0/3])
    tcs.append([12,nodes_l2g,N,0,0])
    tcs.append([10,nodes_l2g,N,2.0/3, 1.0/3])

    for tc in tcs:
        rx1 = random.uniform(0,1)
        rx2 = random.uniform(0,1)

        N = tc[2]
        L = 1 / math.sqrt(N)

        x1, x2 = functions.local_coor_to_global(rx1, rx2, tc[0], tc[1], tc[2])

        # print("About to test x1:{} x2:{}".format(x1,x2))
        # print("{}=={}, {}=={}".format(x1, tc[3] + rx1 * L, x2, tc[4] + rx2 * L))

        assert x1 == tc[3] + rx1 * L
        assert x2 == tc[4] + rx2 * L

def generate_nodes_l2g_test():
    # comprehensive test for N = 9
    N9_table = [
        [0, 4, 5],
        [5, 1, 0],
        [1, 5, 6],
        [6, 2, 1],

        [2, 6, 7],
        [7, 3, 2],
        [4, 8, 9],
        [9, 5, 4],

        [5, 9, 10],
        [10, 6, 5],
        [6, 10, 11],
        [11, 7, 6],

        [8, 12, 13],
        [13, 9, 8],
        [9, 13, 14],
        [14, 10, 9],

        [10, 14, 15],
        [15, 11, 10]
    ]
    N = 9
    nodes_l2g = functions.generate_nodes_l2g(N)

    for e in range(0,18):
        for i in range(0,3):
            assert nodes_l2g[e,i] == N9_table[e][i]

    # comprehensive test for N = 16
    N = 16
    nodes_l2g = functions.generate_nodes_l2g(N)
    N16_table = [
        [0, 5, 6],
        [6, 1, 0],
        [1, 6, 7],
        [7, 2, 1],

        [2, 7, 8],
        [8, 3, 2],
        [3, 8, 9],
        [9, 4, 3],

        [5, 10, 11],
        [11, 6, 5],
        [6, 11, 12],
        [12, 7, 6],

        [7, 12, 13],
        [13, 8, 7],
        [8, 13, 14],
        [14, 9, 8],

        [10, 15, 16],
        [16, 11, 10],
        [11, 16, 17],
        [17, 12, 11],

        [12, 17, 18],
        [18, 13, 12],
        [13, 18, 19],
        [19, 14, 13],

        [15, 20, 21],
        [21, 16, 15],
        [16, 21, 22],
        [22, 17, 16],

        [17, 22, 23],
        [23, 18, 17],
        [18, 23, 24],
        [24, 19, 18]
    ]
    for e in range(0,N*2):
        for i in range(0,3):
            assert nodes_l2g[e,i] == N16_table[e][i]
# tests run here
local_coor_to_global_test()
generate_nodes_l2g_test()