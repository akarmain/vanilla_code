import numpy as np
import matplotlib.pyplot as plt

# Given lengths
AE_length = 91
EK_length = 60

# Let's set up the square with side length 'a'
# We'll adjust 'a' and 's' to satisfy the given lengths
# Define functions to compute AE and EK based on 'a' and 's'

def compute_AE(a, s):
    x_E = (2 * a**2 - s**2) / (2 * a)
    y_E = (2 * a**2 + s**2) / (2 * a)
    AE = np.sqrt(x_E**2 + y_E**2)
    return AE

def compute_EK(a, s):
    x_E = (2 * a**2 - s**2) / (2 * a)
    y_E = (2 * a**2 + s**2) / (2 * a)
    x_K = a - s
    y_K = a
    EK = np.sqrt((x_E - x_K)**2 + (y_E - y_K)**2)
    return EK

def compute_AK(a, s):
    x_A = 0
    y_A = 0
    x_K = a - s
    y_K = a
    AK = np.sqrt((x_K - x_A)**2 + (y_K - y_A)**2)
    return AK

# Let's try to find 'a' and 's' that satisfy AE = 91 and EK = 60
# We'll use numerical methods to approximate the values

from scipy.optimize import fsolve

def equations(vars):
    a, s = vars
    AE = compute_AE(a, s)
    EK = compute_EK(a, s)
    return [AE - AE_length, EK - EK_length]

# Initial guesses for 'a' and 's'
initial_guess = [100, 50]

solution = fsolve(equations, initial_guess)
a_solution, s_solution = solution

# Compute AK
AK_length = compute_AK(a_solution, s_solution)

print(f"Computed side length a = {a_solution}")
print(f"Computed s = {s_solution}")
print(f"The length of AK is approximately: {AK_length}")

# Now, let's draw the square and the points
plt.figure(figsize=(8,8))

# Square vertices
A = np.array([0, 0])
B = np.array([a_solution, 0])
C = np.array([a_solution, a_solution])
D = np.array([0, a_solution])

# Points K and L
K = np.array([a_solution - s_solution, a_solution])
L = np.array([a_solution, a_solution - s_solution])

# Line LD
LD_x = [L[0], D[0]]
LD_y = [L[1], D[1]]

# Point E (foot of the perpendicular from C to LD)
# Compute E coordinates
# Equation of line LD: y = m * x + b
m_LD = (D[1] - L[1]) / (D[0] - L[0])
b_LD = L[1] - m_LD * L[0]

# Equation of perpendicular line from C: y = m_perp * x + b_perp
m_perp = -1 / m_LD
b_perp = C[1] - m_perp * C[0]

# Intersection point E
x_E = (b_perp - b_LD) / (m_LD - m_perp)
y_E = m_LD * x_E + b_LD
E = np.array([x_E, y_E])

# Plot the square
square_x = [A[0], B[0], C[0], D[0], A[0]]
square_y = [A[1], B[1], C[1], D[1], A[1]]
plt.plot(square_x, square_y, 'k-')

# Plot the points
plt.plot([A[0], K[0]], [A[1], K[1]], 'ro', label='Points A and K')
plt.plot([C[0]], [C[1]], 'bo', label='Point C')
plt.plot([L[0]], [L[1]], 'go', label='Point L')
plt.plot([E[0]], [E[1]], 'mo', label='Point E')

# Plot lines
plt.plot(LD_x, LD_y, 'g--', label='Line LD')
plt.plot([C[0], E[0]], [C[1], E[1]], 'm--', label='Perpendicular from C to LD')

# Annotate points
plt.text(A[0], A[1], ' A', fontsize=12)
plt.text(B[0], B[1], ' B', fontsize=12)
plt.text(C[0], C[1], ' C', fontsize=12)
plt.text(D[0], D[1], ' D', fontsize=12)
plt.text(K[0], K[1], ' K', fontsize=12)
plt.text(L[0], L[1], ' L', fontsize=12)
plt.text(E[0], E[1], ' E', fontsize=12)

plt.title('Square ABCD with points K, L, and E')
plt.axis('equal')
plt.legend()
plt.grid(True)
plt.show()
