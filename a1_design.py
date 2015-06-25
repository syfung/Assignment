""" CSC148 Assignment 1 Part 1

Joshua Fung
June 24th, 2015

The following is the ADT design of class hierarchy for a Matrix
class.
Includes classes:
Matrix
NumMatrix
WorldMatrix
OneDMatrix
SquareMatrix
SymmetricMatrix.

It also include 4 exceptions that will be raised, detail of when these
will be raised ais include later:
NonNumError
NonWordError
IndexOutOfBoundError
IncorrectDimensionError


For now all of the Matrix (and children) will be inited to certain
dimension but with 0 for NumMatrix or Matrix, "" for
WordMatrix. Then you can set any value you want.

If you want to create a square matrix, use the identity method for
SquareMatrix. There is no separate class for identity matrix since you
might want to use it as a normal matrix afterwords.  


I am still debating should I include a IdentityMatrix, since it can be
inited then modified after I don't want to constrain it only as a
IdentityMatrix.
"""


class Matrix(object):
    """ This is the Matrix class
    It is the general matrix or the mixed matrix.  
    
    Children classes:
    NumMatrix
    WordMatrix
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

        
class OneDMatrix(NumMatrix):
    """ This is the OneDMatrix class"""
    def __init__(self, length):
        """(int) -> NoType

        Override the Matrix __init__
        Asking for only the length, assuming it is a row matrix
        It might be a problem if the user try to use OneDMatrix with
        Matrix multiplication 
        """

    def set(self, index, value):
        """(int, float) -> NoType

        Overrideing NumMatrix set
        Set the value in the 1D matrix
        """
        
    def get(self, index):
        """(int) -> float

        Overriding NumMatrix get
        Return the value of the 1D matrix
        """
           
class SquareMatrix(NumMatrix):
    """ This is the SquareMatrix class"""
    def __init__(self, size):
        """(int) -> NoType
        
        Override the init from Matrix
        Only need one dimension
        Init with zeros
        """
        
    def get_diag(self):
        """(NoType) -> list

        Return a list of values from the diagonal (forward only)
        """

    def set_diag(self, *values):
        """(...) -> Notype

        Set a list of floats as the diagonal (forward only)
        If worng length raise IncorrectDimensionError
        """
        
    def ident(self, value=1):
        """(int) -> NoType
        
        Make the matrix as a identity matrix with given values
        if not given it is assume to be 1
        """
        
    def det(self):
        """(NoType) -> int
        
        Return the determinant of a 2x2 matrix
        If not a 2x2 matrix raise IncorrectDimensionError
        """
        
class SymmetricMatrix(SquareMatrix):
    """ This is the SymmetricMatrix class"""
    def set(self, row, column, value):
        """(int, int, float) -> NoType
        
        Override the NumMatrix set. Will change both the given index
        and the minor of the matrix
        """
        
    def set_c(self, column, *values):
        """(int, ...) -> NoType
        
        Overide the NumMatrix set_c. Will change both the given column
        and the minor column
        """
        
    def set_r(self, row, *values):
        """(int, ...) -> NoType
        
        Overide the NumMatrix set_r. Will change both the given row
        and the minor row
        """
        
    
class WordMatrix(Matrix):
    """ This is the WordMatrix class"""
    def __str__

    
    def __add__(self, matrix):
        """(WordMatrix) -> WordMatrix
        
        Return a new WorldMatrix with self + matrix using operator (+)
        """
        
    def add(self, matrix):
        """(WordMatric) -> WordMatrix
        
        Add the word from matrix to self
        Also return self
        """
        
# Exception, I almost want to keep it in a different file

        
class NonNumError(Exception):
    """ This is the NonNumError exception"""


class NonWordError(Exception):
    """ This is the NonWordError exception"""

    
class IndexOutOfBound(Exception):
    """ This is the IndexOutOfBound exception"""


class IncorrectDimensionError(Exception):
    """ This is the IncorrectDimensionError exception"""
