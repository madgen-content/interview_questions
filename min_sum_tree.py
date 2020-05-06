def pprint(c):
    for x in c:
        print(x)
    return

example = [
    [4],
    [5,6],
    [1,2,4],
    [8,9,1,3],
    [7,6,1,3,2]
]

# explores all paths
def lchild_loc(i, j):
    return (i+1, j)

def rchild_loc(i, j):
    return (i+1, j+1)

def min_subtree_sum(T, i, j):

    if i == len(T) - 1:
        return T[i][j]

    lsum = min_subtree_sum(T, *lchild_loc(i,j))
    rsum = min_subtree_sum(T, *rchild_loc(i,j))
    m = min(lsum, rsum)

    return T[i][j] + m

print('simple best sum')
pprint(min_subtree_sum(example, 0, 0))
print()
# ================================

# eliminates possible paths from the bottom up

T = example

def lpar_loc(i,j):
    return (i-1, j-1)

def rpar_loc(i,j):
    return (i-1, j)

def lsib_loc(i,j):
    return (i, j-1)

def rsib_loc(i,j):
    return (i, j+1)

def optimize_T(T):
    for i in range(len(T)-1, -1, -1):
        row = T[i]
        for j in range(1, len(row)-1):
            val  = row[j]
            if val == None:
                continue
            else:
                m,n = lsib_loc(i,j)
                lsib = T[m][n]
                m,n = rsib_loc(i,j)
                rsib = T[m][n]
                if (lsib is None or val < lsib) and (rsib is None or val < rsib):
                    m,n = lpar_loc(i,j)
                    x,y = rpar_loc(i,j)
                    lpar = T[m][n]
                    rpar = T[x][y]
                    if lpar is not None and (rpar is None or lpar < rpar):
                        T[x][y] = None
                    elif rpar is not None and (lpar is None or rpar < lpar):
                        T[m][n] = None
                    else:
                        continue

pprint(T)
print('=============')
optimize_T(T)
pprint(T)

def better_min_subtree_sum(T, i, j):

    if i == len(T) - 1:
        return T[i][j]

    lsum = float('inf')
    rsum = float('inf')
    
    m,n = lchild_loc(i,j)
    if T[m][n] is not None:
        lsum = min_subtree_sum(T,m,n)

    m,n = rchild_loc(i,j)
    if T[m][n] is not None:
        rsum = min_subtree_sum(T,m,n)
    m = min(lsum, rsum)

    return T[i][j] + m