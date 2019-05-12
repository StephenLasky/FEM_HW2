import math
import numpy as np
import functions

# returns the element number e as such:
# i---
# | \
# | E \
# |     \
# Inputs: i: node, n: grid size
def get_associated_element(i,n):
    r = int(i/(n+1))
    e = 2*(i-r)

    return e

# input i: node, n: edge length
def is_edge(i,n):
    left = False
    right = False
    top = False
    bot = False

    if i % (n+1) == 0: left = True          # LEFT
    if (i+1) % (n+1) == 0: right = True     # RIGHT
    if i <= n    : top = True               # TOP
    if i >= n * (n+1): bot = True           # BOT

    return top, right, bot, left

# input: global node i, n: edge length (typically sqrt(N))
def is_boundary(i,n):
    top, right, bot, left = is_edge(i,n)

    res = top or right or bot or left
    return res

# takes the coordinates x1, x2 from a global node J, which is the j local node for some element e
# returns the global coordiantes x1, x2
def local_coor_to_global(x1_hat, x2_hat, e, nodes_l2g, N):
    L = 1 / math.sqrt(N)    # vertical/horizontal edge length
    J = nodes_l2g[e,1]

    if e % 2 == 0: # e is EVEN
        pass
    else:          # e is odd, triangle is inverted!!!
        x1_hat = 1 - x1_hat
        x2_hat = 1 - x2_hat

    x1_base = J % (math.sqrt(N) + 1) * L

    R = (math.sqrt(N) + 1) ** 2 - (math.sqrt(N) + 1)
    J = J - J %(math.sqrt(N) + 1)

    R /= (math.sqrt(N) + 1)
    J /= (math.sqrt(N) + 1)

    x2_base = (R-J) * L

    x1 = x1_base + L * x1_hat
    x2 = x2_base + L * x2_hat

    return x1, x2

# generate the local to global nodes matrix using a mesh with N squares (side length sqrt(N))
def generate_nodes_l2g(N):
    number_elements = N * 2
    number_nodes = int((math.sqrt(N) + 1) ** 2)

    nodes_l2g = np.zeros((number_elements, 3), dtype=int) - 1

    i = 0
    e = 0
    while i < number_nodes:
        n = int(math.sqrt(N))
        e = functions.get_associated_element(i, n)

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

        assignments = [0, 1, 2, 0, 1, 2]
        es = [e, e - 1, e - 2 - 2 * n, e - 1 - 2 * n, e - 2 * n, e + 1]

        for j in range(0, 6):
            e = es[j]
            assign = assignments[j]

            # print("Trying to set e:{} assign:{} -> i:{}".format(e, assign, i))
            if skip[j] == False:
                # print("\tSET e:{} assign:{} -> i:{}".format(e,assign,i))
                nodes_l2g[e, assign] = i

        i += 1

    return nodes_l2g


