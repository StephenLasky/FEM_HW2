import math

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

# takes the coordinates x1, x2 from a global node J, which is the j local node for some element e
# returns the global coordiantes x1, x2
def local_coor_to_global(x1_hat, x2_hat, e, J, N):
    L = 1 / math.sqrt(N)    # vertical/horizontal edge length

    # first assumption: element e is EVEN
    if e % 2 == 0:
        x1_base = J % (math.sqrt(N) + 1) * L

        R = (math.sqrt(N) + 1) ** 2 - (math.sqrt(N) + 1)
        J = J - J %(math.sqrt(N) + 1)

        R /= (math.sqrt(N) + 1)
        J /= (math.sqrt(N) + 1)

        x2_base = (R-J) * L

        x1 = x1_base + L * x1_hat
        x2 = x2_base + L * x2_hat

        return x1, x2



