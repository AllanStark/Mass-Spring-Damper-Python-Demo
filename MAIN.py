import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# This code will solve for the example at
# https://www.crcpress.com/downloads/K11527/MATLAB%20Resources.pdf
# For a Driven Mass Spring Damper system, driven with a sine wave

# assume a free mass spring damper system m*a+b*v+k*x=0
# a=acceleration, v= velocity, x=displacement

# Second order response parameters are:

# omega_n=sqrt(k/m)     Natural Frequency
# zeta=b/(2*sqrt(k*m))  Damping ratio

# Define SI UNITS
meters = 1
seconds = 1
kg = 1
newtons = 1
centimeters = meters/100

# Define Model Parameters as per the PDF example
k = 100*newtons/meters
m = 1*kg
zeta = 0.1
omega_n = np.sqrt(k/m)
c = zeta*2*np.sqrt(m*k)


# Define input signal
omega = 2*omega_n
f_input = omega/(2*3.1415)
T_input = 1/f_input * seconds

fo = 100*newtons                # Input signal amplitude


# Print important variables to the command line
print("resonance frequency is ", omega_n )
print("input frequency is ", omega )


# Define State Sapce model
A = [[0, 1], [-k/m, -c/m]]
B = [[0], [1]]
C = [[1, 0]]
D = 0

sys1 = signal.StateSpace(A, B, C, D)

# Define input and time matrix
t_start = 0
t_end = 5*seconds
N_samples = 5*50
t = np.linspace(0,t_end,N_samples)

# DEFINE INPUT
u = np.sin(omega*t)
u = fo*u
initial_conditions=[0.02, 0 ]

response = signal.lsim(sys1, u, t, initial_conditions)  # Get response to time domain input u

t = response[0]
x = response[1]

# Plot the System response
plt.figure(1)
plt.plot(t, x)
plt.xlabel("time [s]")
plt.ylabel("x(t) [m]")

plt.show()

