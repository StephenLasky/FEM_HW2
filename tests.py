import functions
import random
import math

# local_coor_to_global(x1_hat, x2_hat, e, J, N):
def local_coor_to_global_test():
    N = 16

    tcs = []    # e, J, N, x1_base, x2_base
    tcs.append([0,5,N,0,0.75])
    tcs.append([2,6,N,0.25,0.75])
    tcs.append([12,12,N,0.5,0.5])
    tcs.append([18,16,N,0.25,0.25])

    # test for N = 9
    N = 9

    tcs.append([0,4,N,0,2.0/3])
    tcs.append([12,12,N,0,0])
    tcs.append([10,10,N,2.0/3, 1.0/3])

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



# tests run here
local_coor_to_global_test()