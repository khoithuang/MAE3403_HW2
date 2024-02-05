from math import cos

def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    This funciton implements th Secant method to find the root of an equation.  You should write your equation in a form
    fcn = 0 such that when the correct value of x is selected, the fcn actually equals zero (or very close to it).
    :param fcn: the function for which we want to find the root
    :param x0: x value in neighborhood of root (or guess 1)
    :param x1: another x value in neighborhood of root (or guess x0+1)
    :param maxiter: exit if the number of iterations (new x values) equals this number
    :param xtol:  exit if the |xnewest - xprevious| < xtol
    :return: tuple with: (the final estimate of the root (most recent value of x), number of iterations)
    """
    for i in range(maxiter):
        fx0 = fcn(x0)
        fx1 = fcn(x1)
        if fx1 - fx0 == 0:
            return x1, i  # Avoid division by zero
        xnew = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        if abs(xnew - x1) < xtol:
            return xnew, i + 1  # Converged
        x0, x1 = x1, xnew  # Prepare for next iteration
    return x1, maxiter  # Max iterations reached

def fn1(x):
    return x - 3 * cos(x)

def fn2(x):
    return cos(2 * x) * x ** 3 - 1.57

def main():
    """
       fn1:  x-3cos(x)=0; with x0=1, x1= 2, maxiter = 5 and xtol = 1e-4
       fn2:  cos(2x)*x**3; with x0=1, x1= 2, maxiter = 15 and xtol = 1e-8
       fn2:   with x0=1, x1= 2, maxiter = 3 and xtol = 1e-8

       I observe that for functions 2 and 3, the answer should be pi/2 or about 1.57
    :return: nothing, just print results
    """
    r1 = Secant(fn1, 1, 2, 5,1e-4)
    r2 = Secant(fn2, 1,2,15, 1e-8)
    r3 = Secant(fn2,1,2,3,1e-8)
    print(f"root of fn1 = {r1[0]:0.4f}, after {r1[1]} iterations")
    print(f"root of fn2 (15 iterations) = {r2[0]:0.4f}, after {r2[1]} iterations")
    print(f"root of fn2 (3 iterations) = {r3[0]:0.4f}, after {r3[1]} iterations")
if __name__=="__main__":
    main()