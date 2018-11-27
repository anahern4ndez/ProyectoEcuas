# Archivo py para la resolucion de una ODE para un edificio de dos pisos
# Maria Fernanda Lopez
# Ana Lucia Hernandez
# Gabriela Malouf
from scipy.integrate import odeint
from modulo import *
from numpy import loadtxt
from pylab import figure, plot, xlabel, grid, hold, legend, title, savefig
from matplotlib.font_manager import FontProperties

# Parameter values
# Masses:
m1 = 10000
m2 = 7500
m3 = 5000
m4 = 2500
# Spring constants
k1 = 10000
k2 = 10000
k3 = 10000
k4 = 10000
# Friction coefficients
b1 = 0.1
b2 = 0.1
b3 = 0.1
b4 = 0.1

# Initial conditions
# x1 and x2 are the initial displacements; y1 and y2 are the initial velocities
x1  = 0.1
y1 = 0.0
x2 = 0.1
y2 = 0.0
x3  = 0.1
y3  = 0.0
x4  = 0.1
y4 = 0.0

# ODE solver parameters
abserr = 1.0e-8
relerr = 1.0e-6
stoptime = 15 #tiempo (seg) en el que se detendra
numpoints = 306 #cantidad de datos (soluciones) a sacar

# Create the time samples for the output of the ODE solver.
# I use a large number of points, only because I want to make
# a plot of the solution that looks nice.
t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]

# Pack up the parameters and initial conditions:
p = [m1, m2, m3, m4, k1, k2, k3, k4, b1, b2, b3, b4]
w0 = [x1, y1, x2, y2, x3, y3, x4, y4]

# Call the ODE solver.
wsol = odeint(vectorfield4, w0, t, args=(p,),
              atol=abserr, rtol=relerr)

with open('four_floors.dat', 'w') as f:
    # Print & save the solution.
    for t1, w1 in zip(t, wsol):
        print >> f, t1, w1[0], w1[2], w1[4], w1[6]

t, x1, x2, x3, x4 = loadtxt('four_floors.dat', unpack=True)

figure(1, figsize=(6, 4.5))

xlabel('t')
grid(True)
hold(True)
lw = 1

plot(t, x1, 'b', linewidth=lw)
plot(t, x2, 'g', linewidth=lw)
plot(t, x3, 'r', linewidth=lw)
plot(t, x4, 'y', linewidth=lw)

legend((r'$m_1$', r'$m_2$', r'$m_3$', r'$m_4$'), prop=FontProperties(size=12))
title('Mass Displacements for the\n Four floors building')
savefig('four_floors.png', dpi=100)

