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




