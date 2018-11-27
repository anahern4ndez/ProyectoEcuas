# Use ODEINT to solve the differential equations defined by the vector field
from scipy.integrate import odeint

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
         (-b2 * y2 - k2 * (x2 - x1 )) / m2,
         y3,
         (-b3 * y3 - k3 * (x3 - x2 -x1)) / m3,
         y4,
         (-b4 * y4 -k4 * (x4 - x3 -x2 -x1)) / m4]
    return f

