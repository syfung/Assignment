""" CSC148 Assignment 1 Part 1

Joshua Fung
June 24th, 2015

The following is the ADT design of class hierarchy for a Matrix
class.

Includes classes:
Matrix
NumMatrix
MixedMatrix
WorldMatrix
OneDMatrix
SquareMatrix
SymmetricMatrix.

I am still debating should I include a IdentityMatrix, since it can be
inited then modified after I don't want to constrain it only as a
IdentityMatrix.

It also include 4 exceptions that will be raised, detail of when these
will be raised ais include later:
NonNumError
NonWordError
IndexOutOfBoundError
IncorrectDimensionError

For now all of the Matrix (and children) will be inited to certain
dimension but with 0 for NumMatrix or MixedMatrix, "" for
WordMatrix. Then you can set any value you want.

If you want to create a square matrix, use the identity method for
SquareMatrix. There is no separate class for identity matrix since you
might want to use it as a normal matrix afterwords.  

"""


class Matrix(object):
    """ This is the Matrix class
    It is the general matrix. It is not meant to use, rather it is
    just the parent of all other Matrix. 
    
    **If you want a matrix for mixed values use the MixedMatrix

    Children classes:
    NumMatrix
    WordMatrix
    MixedMatrix
    OneDMatrix
    """
    def __init__(self, rows, columns):
        """(int, int) -> NoType

        Init the empty matrix  with rows and columns then filled with
        zeros
        """

    def __str__(self):
        """(Notype) -> str
        
        Print the matrix

        >>>print(matrix)
        0,0,0
        0,0,0
        0,0,0
        >>>
        """

    def __add__(self, matrix):
        """(Matrix) -> Matrix
        
        Return a new Matrix with self + matrix with operator (+)
        **might cause problem to child class
        
        >>>print(b)
        1,0,0
        0,1,0
        0,0,1
        >>>print(a)
        1,0,0
        0,1,0
        0,0,1
        >>>c = a + b
        >>>print(c)
        2,0,0
        0,2,0
        0,0,2
        >>>
        """

    def add(self, matrix):
        """(Matrix) -> Matrix
        
        Add the values of the matrix to self
        Also retrun self

        >>>print(b)
        1,0,0
        0,1,0
        0,0,1
        >>>print(a)
        1,0,0
        0,1,0
        0,0,1
        >>>a.add(b)
        >>>print(a)
        2,0,0
        0,2,0
        0,0,2
        >>>
        """

    def get(self, row, column):
        """(int, int) -> float

        Return the value at a specific index

        >>>matrix.get(1, 1)
        1
        >>>
        """

    def set(self, row, column, value):
        """(int, int, object) -> NoType

        Set a value (or object) at specfic location

        >>>matrix.set(1, 2, 1)
        >>>matrix.get(1, 2)
        1
        >>>
        """

    def get_c(self, column):
        """(int) -> list
        
        Return a list containing the whole column
        
        >>>matrix.get_c(2)
        [0,0,0]
        >>>
        """
        
    def set_c(self, column, *values):
        """(int, ...) -> NoType
        
        Set mutiple values for a columne
        If the dimension and the length of the values don't match
        rasie a IncorrectDimensionError

        >>>matrix.set_c(2, 1, 1, 1)
        >>>print(matrix)
        0,0,1
        0,0,1
        0,0,1
        >>>
        """
        
    def get_r(self, row):
        """(int) -> list
        
        Return a list containing the whole row
        
        >>>matrix.get_r(2)
        [0,0,0]
        >>>
        """
        
    def set_r(self, row, *values):
        """(int, ...) -> NoType
        
        Set mutiple values for a row
        If the dimension and the length of the values don't match
        rasie a IncorrectDimensionError

        >>>matrix.set_r(2, 1, 1, 1)
        >>>print(matrix)
        0,0,0
        0,0,0
        1,1,1
        >>>
        """
        
    def swap_c(self, column1, column2):
        """(int, int) -> NoType
        
        Swap two columns
        Raise IndexOutOfBound if index is outside of dimension 

        >>>print(matrix)
        0,0,0
        0,0,0
        1,2,3
        >>>matrix.swap_c(1, 2)
        >>>print(matrix)
        0,0,0
        0,0,0
        1,3,2
        >>>
        """
        
    def swap_r(self, row1, row2):
        """(int, int) -> NoType
        
        Swap two rows
        Raise IndexOutOfBound if index is outside of dimension 

        >>>print(matrix)
        0,0,0
        0,0,0
        1,2,3
        >>>matrix.swap_c(1, 2)
        >>>print(matrix)
        0,0,0
        1,2,3
        0,0,0
        >>>
        """
        
    def tran(self):
        """(NoType) -> NoType
        
        Tranpose self and return self

        >>>print(matrix)
        2,2
        2,2
        2,2
        >>>print(matrix.tran())
        2,2,2
        2,2,2
        >>>
        """
        
class NumMatrix(Matrix):
    """ This is the NumMatrix class"""
    def __mul__(self, matrix):
        """(NumMatrix) -> NumMatrix
        
        Return a new Matrix of self * matirx (matirx multiplcation)
        with operator (*)        
        If worng dimension raise IncorrectDimesionError
        If matrix is not all numbers raise NonNumError
        """
        
    def mul(self, matrix):
        """(NumMatrix) -> NumMatrix
        
        Matrix multiplation of self with matrix
        Also return self
        If worng dimension raise IncorrectDimesionError
        If matrix is not all numbers raise NonNumError
        """
                
    def element_mul(self, matrix):
        """(NumMatrix) -> NumMatrix
        
        Element by element multiplation of self with matirx
        Also return self
        If not the same dimension raise IncorrectDimesionError
        If matrix is not all numbers raise NonNumError
        """
           
    def __sub__(self, matrix):
        """(NumMatrix) -> NumMatrix
        
        Return a new Matrix of self - matirx (element wise)
        with operator (-)
        If worng dimension raise IncorrectDimesionError
        If matrix is not all numbers raise NonNumError
        """
        
    def sub(self, matirix):
        """(NumMatrix) -> NumMatrix
        
        Element by element subtraction of self with matirx
        Also return self
        If not the same dimension raise IncorrectDimesionError
        If matrix is not all numbers raise NonNumError
        """
           
class SquareMatrix(NumMatrix):
    """ This is the SquareMatrix class"""
    def __init__(self, size):
        """(int) -> NoType
        
        Override the init from Matrix
        Only need one dimension
        Init with zeros
        """
        
    def get_diag(self, *values):

    def set_diag(self, *values):

    def ident(self, value=1):

    def det(self):

class SymmetricMatrix(SquareMatrix):
    """ This is the SymmetricMatrix class"""
    def set():

    def set_c():

    def set_r():

    
class WordMatrix(Matrix):
    """ This is the WordMatrix class"""
    def __add__(self, matrix):
        
    def add(self, matrix):

        
class MixedMatrix(Matrix):
    """ This is the MixedMatrix class"""
    def __str__(self):
       

class OneDMatrix(Matrix):
    """ This is the OneDMatrix class"""
    def __init__(self, length):


# Exception, I almost want to keep it in a different file
class NonNumError(Exception):
    """ This is the NonNumError exception"""


class NonWordError(Exception):
    """ This is the NonWordError exception"""

    
class IndexOutOfBound(Exception):
    """ This is the IndexOutOfBound exception"""


class IncorrectDimensionError(Exception):
    """ This is the IncorrectDimensionError exception"""
