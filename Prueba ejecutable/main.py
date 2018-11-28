# -*- coding: cp1252 -*-
# Proyecto Ecuaciones Diferenciales
# Maria Fernanda Lopez
# Ana Lucia Hernandez
# Ana Gabriela

from scipy.integrate import odeint
from numpy import loadtxt
from pylab import figure, plot, xlabel, grid, hold, legend, title, savefig
from matplotlib.font_manager import FontProperties

# funcion para edificio de tres pisos
def vectorfield3(w, t, p):
    """
    Defines the differential equations for the coupled spring-mass system.

    Arguments:
        w :  vector of the state variables:
                  w = [x1,y1,x2,y2,x3,y3]
        t :  time
        p :  vector of the parameters:
                  p = [m1,m2,m3,k1,k2,k3,b1,b2,b3]
    """
    x1, y1, x2, y2, x3, y3 = w
    m1, m2, m3, k1, k2, k3, b1, b2, b3 = p

    # Create f = (x1',y1',x2',y2',x3',y3'):
    f = [y1,
         (-b1 * y1 - k1 * (x1) + k2 * (x2 - x1)) / m1,
         y2,
         (-b2 * y2 - k2 * (x2 - x1) + k3 * (x3 - x2)) / m2,
         y3,
         (-b3 * y3 - k3 * (x3 - x2)) / m3]
    return f

#funcion para edificio de dos pisos
def vectorfield2(w, t, p):
    """
    Defines the differential equations for the coupled spring-mass system.

    Arguments:
        w :  vector of the state variables:
                  w = [x1,y1,x2,y2]
        t :  time
        p :  vector of the parameters:
                  p = [m1,m2,k1,k2,L1,L2,b1,b2]
    """
    x1, y1, x2, y2 = w
    m1, m2, k1, k2, b1, b2 = p

    # Create f = (x1',y1',x2',y2'):
    f = [y1,
         (-b1 * y1 - k1 * (x1) + k2 * (x2 - x1)) / m1,
         y2,
         (-b2 * y2 - k2 * (x2 - x1)) / m2]
    return f


#funcion para edificio de cuatro pisos
def vectorfield4(w, t, p):
    """
    Defines the differential equations for the coupled spring-mass system.

    Arguments:
        w :  vector of the state variables:
                  w = [x1,y1,x2,y2]
        t :  time
        p :  vector of the parameters:
                  p = [m1,m2,k1,k2,L1,L2,b1,b2]
    """
    x1, y1, x2, y2, x3, y3, x4, y4 = w
    m1, m2, m3, m4, k1, k2, k3, k4, b1, b2, b3, b4 = p

    # Create f = (x1',y1',x2',y2', x3', y3', x4', y4'):
    #traduccion de variables a una funcion que python puede procesar
    f = [y1,
         (-b1 * y1 - k1 * (x1) + k2 * (x2 - x1)) / m1,
         y2,
         (-b2 * y2 - k2 * (x2 - x1 ) + k3 * (x3 - x2)) / m2,
         y3,
         (-b3 * y3 - k3 * (x3 - x2) + k4 * (x4 - x3)) / m3,
         y4,
         (-b4 * y4 -k4 * (x4 - x3)) / m4]
    return f

def dosPisos(masa, k):
    m1 = masa
    m2 = masa * 2
    # Spring constants
    k1 = k
    k2 = k
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
    stoptime = 15 #tiempo (seg) en el que se detendra
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
            print >> f, t1, w1[2], w1[0]
            
    t, x1, x2 = loadtxt('two_floors.dat', unpack=True)

    figure(1, figsize=(6, 4.5))

    xlabel('t')
    grid(True)
    hold(True)
    lw = 1

    plot(t, x1, 'b', linewidth=lw)
    plot(t, x2, 'g', linewidth=lw)

    legend((r'$m_1$', r'$m_2$'), prop=FontProperties(size=16))
    title('Mass Displacements for the\n Two floors building')
    savefig('two_floors.png', dpi=100)

def tresPisos(masa, k):
    # Parameter values
    # Masses:
    m1 = masa
    m2 = masa * 2
    m3 = masa * 3
    # Spring constants
    k1 = k
    k2 = k
    k3 = k
    # Friction coefficients
    b1 = 0.05
    b2 = 0.05
    b3 = 0.05

    # Initial conditions
    # x1 and x2 are the initial displacements; y1 and y2 are the initial velocities
    x1  = 0.1
    y1 = 0.0
    x2 = 0.1
    y2 = 0.0
    x3  = 0.1
    y3  = 0.0

    # ODE solver parameters
    abserr = 1.0e-8
    relerr = 1.0e-6
    stoptime = 15 #tiempo (seg) en el que se detendra
    numpoints = 240 #cantidad de datos (soluciones) a sacar, para que regrese a 0 aqui son 268

    # Create the time samples for the output of the ODE solver.
    # I use a large number of points, only because I want to make
    # a plot of the solution that looks nice.
    t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]

    # Pack up the parameters and initial conditions:
    p = [m1, m2, m3, k1, k2, k3, b1, b2, b3]
    w0 = [x1, y1, x2, y2, x3, y3]

    # Call the ODE solver.
    wsol = odeint(vectorfield3, w0, t, args=(p,),
                  atol=abserr, rtol=relerr)

    with open('three_floors.dat', 'w') as f:
        # Print & save the solution.
        for t1, w1 in zip(t, wsol):
            print >> f, t1, w1[4], w1[2], w1[0]

    t, x1, x2, x3 = loadtxt('three_floors.dat', unpack=True)

    figure(1, figsize=(6, 4.5))

    xlabel('t')
    grid(True)
    hold(True)
    lw = 1

    plot(t, x3, 'r', linewidth=lw)

    legend((r'$m_1$', r'$m_2$', r'$m_3$'), prop=FontProperties(size=12))
    title('Mass Displacements for the\n Three floors building')
    savefig('three_floors.png', dpi=100)

def cuatroPisos(masa, k):
    # Parameter values
    # Masses:
    m1 = masa
    m2 = masa * 2
    m3 = masa * 3
    m4 = masa * 4
    # Spring constants
    k1 = k
    k2 = k
    k3 = k
    k4 = k
    # Friction coefficients
    b1 = 0.05
    b2 = 0.05
    b3 = 0.05
    b4 = 0.05

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

def grafica4():
            
    t, x1, x2, x3, x4 = loadtxt('four_floors.dat', unpack=True)

    figure(1, figsize=(6, 4.5))

    xlabel('t')
    grid(True)
    hold(True)
    lw = 1

    plot(t, x4, 'y', linewidth=lw)

    legend((r'$m_1$', r'$m_2$', r'$m_3$', r'$m_4$'), prop=FontProperties(size=12))
    title('Mass Displacements for the\n Four floors building')
    savefig('four_floors.png', dpi=100)


masa, k  = loadtxt('Parametros.dat', unpack=True)
dosPisos(masa,k)
tresPisos(masa,k)
cuatroPisos(masa,k)
grafica4()
