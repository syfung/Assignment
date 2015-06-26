""" CSC148 Assigment 1 Part 1, UnitTest

Joshua Fung
June 24th, 2015

Block box tesing for a1
"""


import a1_design

# Tests on Matrix
print("Tesing Matrix()")

try:
    matrix_a = a1_design.Matrix(2, 3)
    matrix_b = a1_design.Matrix(2, 3)
except:
    print("Failed Matrix init")
else:
    print("Passed Matrix init")

try:
    large_matrix = a1_design.Matrix(100, 200)
except:
    print("Failed Large Matrix init")
else:
    print("Passed Large Matrix init")

try:
    temp = str(matrix_a)
except:
    print("Failed str test")
else:
    if(temp == "0,0,0\n0,0,0"):
        print("Passed str test")
    else:
        print("Failed str test")

try:
    matrix_a.set(1,1,2)
    matrix_b.set(1,1,2)
except:
    print("Failed set and get test")
else:
    try:
        temp = matrix_a.get(1,1)
    except:
        print("Failed set and get test")
    else:
        if(temp == 2):
            print("Passed set and get test")

# Will only work if init, set and get works
try:
    matrix_c = matrix_a + matirx_b
except:
    print("Failed (+) test")
else:
    if(matrix_c.get(1, 1) == 4):
        print("Passed (+) test")
    else:
        print("Failed (+) test")

try:
    matrix_a.add(matrix_b)
except:
    print("Failed add test")
else:
    if(matrix_a.get(1, 1) == 4):
        print("Passed add test")
    else:
        print("Failed add test")

try:
    matrix_a.get_c(1)

try:
    matrix_a.get_r(1)

try:
    matrix_a.set_c(1, 2, 2)

try:
    matrix_a.set_r(1, 2, 2, 2)

try:
    matrix_a.swap_c(0, 1)
except:
    print("Failed swap_c test")

try:
    matric_b.swap_r(0,1)

try:
    matric_a.tran()


# Tests on NumMatrix
try:
    number_matrix_a = NumMatrix(2, 2)
    number_matrix_b = NumMatrix(2, 2)
    number_matrix_c = NumMAtrix(100,200)

# Tests on OneDMatrix


# Tests on SquareMatrix
try:
    square_matrix_a = SquareMatrix(2)

# Tests on SymmetricMatrix
try:
    symmetric_matrix_a = SymmetricMatrix(5)

try:
    symmetric_matrix_a.set(1, 1, 5)
    a = symmetric_matrix_a.get(1, 1)
    b = symmetric_matrix_b.get(4, 4)
except:
    print("Failed symmetric matrix test")
else:
    if(a == 5 and b == 5):
        print("Passed symmetric matrix test")
    else:
        print("Failed symmetric matrix test")


# Tests on identity matrix
try:
    square_matrix_a.ident(7)

try:
    square_matirx_a.ident()

# Tests on determinate
try:
    temp = square_matrix_a.det()
except:
    print("Failed det test")
else:
    if(temp == 1):
        print("Passed det test")
    else:
        print("Failed det test")
        
try:
    square_matrix_b.det()
except IncorrectDimensionError:
    print("Passed det onlt work on 2x2")
else:
    print("Failed det only work on 2x2")


# Tests on WordMatrix
