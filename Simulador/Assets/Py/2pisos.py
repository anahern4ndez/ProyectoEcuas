# Archivo py para la resolucion de una ODE para un edificio de dos pisos
# Maria Fernanda Lopez
# Ana Lucia Hernandez
# Gabriela Malouf
from scipy.integrate import odeint
from modulo import *

# Parameter values
# Masses:
m1 = 2500
m2 = 5000
# Spring constants
k1 = 10000
k2 = 10000
# Friction coefficients
b1 = 0.05
b2 = 0.05

# Initial conditions
# x1 and x2 are the initial displacements; y1 and y2 are the initial velocities
x1  = 0.1
y1 = 0.0
x2 = 0.1
y2 = 0.0

# ODE solver parameters
abserr = 1.0e-8
relerr = 1.0e-6
stoptime = 10 #tiempo (seg) en el que se detendra
numpoints = 252 #cantidad de datos (soluciones) a sacar

# Create the time samples for the output of the ODE solver.
# I use a large number of points, only because I want to make
# a plot of the solution that looks nice.
t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]

# Pack up the parameters and initial conditions:
p = [m1, m2, k1, k2, b1, b2]
w0 = [x1, y1, x2, y2]

# Call the ODE solver.
wsol = odeint(vectorfield2, w0, t, args=(p,),
              atol=abserr, rtol=relerr)

with open('two_floors.dat', 'w') as f:
    # Print & save the solution.
    for t1, w1 in zip(t, wsol):
        print >> f, w1[0], w1[2]
