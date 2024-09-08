import cmath

# -------------------------------------------------------------------------
# FFT
# -------------------------------------------------------------------------
def fft(x): # modified from base code by perplexity.ai
    """
    A recursive implementation of the 1D Cooley-Tukey FFT algorithm.
    
    :param x: input signal
    :return: A list of complex numbers representing the frequency domain
    """
    N = len(x)
    
    # Base case: if the input has only one element, return it
    if N <= 1:
        return x
    
    # Recursive case
    # Split the input into even and odd indices
    even = fft(x[0::2]) # for Pe(x^2)
    odd = fft(x[1::2])  # for Po(x^2)
    
    # Combine the results
    w = cmath.exp(2j * cmath.pi / N) # w ** k: evaluation pts
    wkodd = [ w ** k  * odd[k] for k in range(N // 2)]
    PePo = [even[k] + wkodd[k] for k in range(N // 2)]
    Pe_Po = [even[k] - wkodd[k] for k in range(N // 2)]
    return PePo + Pe_Po

print(fft([1, 5, 7, 1])) # [(14+0j), (-6+4j), (2+0j), (-6-4j)]
# x coordinates are:       1, i, -1 -i


# -------------------------------------------------------------------------
# IFFT (We should scale after calling the function
# -------------------------------------------------------------------------

def ifft(x): # modified from base code by perplexity.ai
    N = len(x)

    # Base case: if the input has only one element, return it
    if N <= 1:
        return x

    # Recursive case
    # Split the input into even and odd indices
    even = ifft(x[0::2]) # for Pe(x^2)
    odd = ifft(x[1::2])  # for Po(x^2)

    # Combine the results
    w = cmath.exp(-2j * cmath.pi / N )  # w ** k: evaluation pts
    wkodd = [ w ** k  * odd[k] for k in range(N // 2)]
    PePo = [even[k] + wkodd[k] for k in range(N // 2)]
    Pe_Po = [even[k] - wkodd[k] for k in range(N // 2)]
    return PePo+Pe_Po

x = [1, 5, 7, 1]
X = fft(x)
x_recon = [element / len(X) for element in ifft(X)]

print(x_recon)

# -------------------------------------------------------------------------
# Multiplication of polynomials
# $A(x) = 1 + 5x + 7x^2 + x^3$ and $B(x) = 1 + 2x^3$,
# $A(x)B(x) = 1 + 5x + 7x² + 3x³ + 10x⁴ + 14x⁵ + 2x⁶$
# -------------------------------------------------------------------------

n = 16
p1 = [1, 5, 7, 1]
p2 = [1, 0, 0, 2]

deg = 6

p1_padded = p1 + [0] * (n - len(p1))
p2_padded = p2 + [0] * (n - len(p2))

X1 = fft(p1_padded)
X2 = fft(p2_padded)
X1X2 = [X1[k]*X2[k] for k in range(len(X1))]
x1x2 = [x / len(X1) for x in ifft(X1X2)]

print([x.real for x in x1x2[:deg+1]])
# [1.0, 5.0, 7.00000, 3.00000, 10.0, 13.9999999, 1.9999999]
