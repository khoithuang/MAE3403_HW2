from math import sqrt, pi, exp
def Probability(PDF, args, c, GT=True):
    """
    This is the function to calculate the probability that x is >c or <c depending
    on the GT boolean.
    Step 1:  unpack args into mu and stDev
    Step 2:  compute lhl and rhl for Simpson
    Step 3:  package new tuple args1=(mu, stDev, lhl, rhl) to be passed to Simpson
    Step 4:  call Simpson with GNPDF and args1
    Step 5:  return probability
    :param PDF: the probability density function to be integrated
    :param args: a tuple with (mean, standard deviation)
    :param c: value for which we ask the probability question
    :param GT: boolean deciding if we want probability x>c (True) or x<c (False)
    :return: probability value
    """

    mu,sig, = args
    if GT:
        lhl = c
        rhl = mu + 5 * sig  # Adjust as needed for a more accurate result
    else:
        lhl = mu - 5 * sig
        rhl = c

    p= Simpson(PDF, (mu, sig, lhl, rhl))
    return p

def GPDF(args):
    """
    Here is where I will define the Gaussian probability density function.
    This requires knowing the population mean and standard deviation.
    To compute the GPDF at any value of x, I just need to compute as stated
    in the homework assignment.
    Step 1:  unpack the args tuple into variables called: x, mu, stDev
    Step 2:  compute GPDF value at x
    Step 3:  return value
    :param args: (x, mean, standard deviation)  tuple in that order
    :return: value of GPDF at the desired x
    """
    #Step 1: unpack args
    x, mu, sig=args
    #step 2: compute GPDF at x
    fx=(1/(sig*sqrt(2*pi)))*exp(-0.5*((x-mu)/sig)**2)
    #step 3: return value
    return fx

def Simpson(fx,  args, n=100):
    """
    This executes the Simpson 1/3 rule for numerical integration (see page 832, Table 19.4).
    As I recall:
    1. divide the range from x=lhl to x=rhl into an even number of parts. Perhaps 20?
    2. compute fx at each x value between lhl and rhl
    3. sum the even and odd values of fx as prescribed
    4. return the area beneath the function fx
    :param fx: some function of x to integrate
    :param args: a tuple containing (mean, stDev, lhl, rhl)
    :return: the area beneath the function between lhl and rhl
    """
    mu, sig, lhl, rhl=args
    if n % 2 != 1:
        n += 1

    h = (rhl - lhl) / n
    x = [lhl + i * h for i in range(n + 1)]
    f = [fx((xi, mu, sig)) for xi in x]  # Get help form ChatGPT

    # Apply Simpson's 1/3 formula
    area = h / 3 * (
                f[0] + f[-1] + 4 * sum(f[i] for i in range(1, n, 2)) + 2 * sum(f[i] for i in range(2, n - 1, 2)))
    return area


def main():
    """
    I want to integrate the Gaussian probability density function between
    a left hand limit = (mean - 5*stDev) to a right hand limit = (c).  Here
    is my step-by-step plan:
    1. Decide mean, stDev, and c and if I want P(x>c) or P(x<c).
    2. Define args tuple and c to be passed to Probability
    3. Pass args, and a callback function (GPDF) to Probability
    4. In probability, pass along GPDF to Simpson along with the appropriate args tuple
    5. Return the required probability from Probability and print to screen.
    :return: Nothing to return, just print results to screen.
    """

    p1 = Probability(GPDF, (0, 1), 0, True)
    print(f"P(x>0|N(0,1))={p1:.5f}")

        # Example with user input
    mean = float(input("Population mean? "))
    stDev = float(input("Standard deviation? "))
    c = float(input("c value? "))
    GT = input("Probability greater than c? (y/n): ").lower() in ["y", "yes", "true"]
    p_user = Probability(GPDF, (mean, stDev), c, GT)
    print(f"P(x{'>=' if GT else '<='}{c}|N({mean},{stDev}))={p_user:.5f}")

if __name__ == "__main__":
        main()