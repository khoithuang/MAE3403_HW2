from copy import deepcopy
def GaussSeidel(Aaug, x, Niter = 15):
    """
    This should implement the Gauss-Seidel method (see page 860, Tabl 20.2) for solving a system of equations.
    :param Aaug: The augmented matrix from Ax=b -> [A|b]
    :param x:  An initial guess for the x vector. if A is nxn, x is nx1
    :param Niter:  Number of iterations to run the GS method
    :return: the solution vector x
    """
    pass

def MakeDiagDom(A):
    """
    This function reorders the rows of matrix A to put the larges absolute values along the diagonal.

    :param A: The matrix to sort
    :return: The sorted matrix
    """
    pass

def main():
    pass

if __name__=="__main":
    main()