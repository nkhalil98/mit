# Given two lists of numbers, write a procedure that returns a list of the element-wise sum of the number in those two lists. In the following, no imports should be used.


def add_two_lists(a, b):

    sum_list = []

    for i in range(len(a)):

        sum_list.append(a[i] + b[i])

    return sum_list

# Given two column vectors (each represented as a list of numbers), write a procedure dot that returns the (scalar) dot product of two input vectors, each represented as a list of numbers.

def dot(v1, v2):
    dot = 0
    for i in range(len(v1)):
        dot += v1[i] * v2[i]
    return dot

# Write a function add_n that takes a single numeric argument n, and returns a function. The returned function should take a vector v as an argument and return a new vector with the value for n added to each element of vector v. For example, add_n(10)([1, 5, 3]) should return [11, 15, 13].

def add_n(n):
    def new_vector(v):
        return [e + n for e in v]
    return new_vector

# Write a function array_mult that takes two two-dimensional arrays and performs a matrix multiplication, return a new two-dimensional array. Each array should be represented as a list of lists, i.e., as a list of rows, as discussed earlier. For example,

# >>> M1 = [[1, 2, 3], [-2, 3, 7]]
# >>> M2 = [[1,0,0],[0,1,0],[0,0,1]]
# >>> array_mult(M1, M2)
# [[1, 2, 3], [-2, 3, 7]]

# >>> M3 = [[1], [0], [-1]]
# >>> array_mult(M1, M3)
# [[-2], [-9]]

def array_mult(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    print(m,n,p)
    
    for row in range(m):
        ([]).append([])
    print([])
    
    for i in range(m):
        for j in range(p):
            mult = 0
            for k in range(n):
                mult += A[i][k]*B[k][j]
                if k == (n-1):
                    ([])[i].append(mult)
    
    return []
# Given two column vectors (each represented as a list of numbers), write a procedure dot that returns the (scalar) dot product of two input vectors, each represented as a list of numbers.

def dot(v1, v2):
    dot = 0
    for i in range(len(v1)):
        dot += v1[i] * v2[i]
    return dot

# Write a function add_n that takes a single numeric argument n, and returns a function. The returned function should take a vector v as an argument and return a new vector with the value for n added to each element of vector v. For example, add_n(10)([1, 5, 3]) should return [11, 15, 13].

def add_n(n):
    def new_vector(v):
        return [e + n for e in v]
    return new_vector

# Write a function array_mult that takes two two-dimensional arrays and performs a matrix multiplication, return a new two-dimensional array. Each array should be represented as a list of lists, i.e., as a list of rows, as discussed earlier. For example,

# >>> M1 = [[1, 2, 3], [-2, 3, 7]]
# >>> M2 = [[1,0,0],[0,1,0],[0,0,1]]
# >>> array_mult(M1, M2)
# [[1, 2, 3], [-2, 3, 7]]

# >>> M3 = [[1], [0], [-1]]
# >>> array_mult(M1, M3)
# [[-2], [-9]]

def array_mult(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    
    mat = []
    for row in range(m):
        mat.append([])
    
    for i in range(m):
        for j in range(p):
            mult = 0
            for k in range(n):
                mult += A[i][k]*B[k][j]
                if k == (n-1):
                    mat[i].append(mult)
    
    return mat