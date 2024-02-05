from math import sqrt, pi, exp

def Probability(PDF, args, c, GT=True):
    mu, sig = args
    if GT:
        lhl = c
        rhl = mu + 5 * sig  # Extending to the right for GT
    else:
        lhl = mu - 5 * sig  # Starting from far left for LT
        rhl = c

    # Correctly calling Simpson with a defined n
    p = Simpson(PDF, (mu, sig, lhl, rhl), n=20)  # n is the number of segments
    return p

def GPDF(args):
    x, mu, sig = args
    fx = (1 / (sig * sqrt(2 * pi))) * exp(-0.5 * ((x - mu) / sig) ** 2)
    return fx

def Simpson(fx, args, n=20):
    mu, sig, lhl, rhl = args
    if n % 2 == 1:
        n += 1  # Make sure n is even

    h = (rhl - lhl) / n
    x = [lhl + i * h for i in range(n + 1)]
    f = [fx((xi, mu, sig)) for xi in x]

    area = h / 3 * (f[0] + f[-1] + 4 * sum(f[i] for i in range(1, n, 2)) + 2 * sum(f[i] for i in range(2, n, 2)))
    return area

def main():
    # Example usage without user input for simplicity
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

