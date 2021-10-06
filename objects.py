import numpy as np



def simpleTest():

    points =    [(1.0,1.0,1.0),
                (0.0,0.0,1.0),
                (2.0,2.0,1.0)]
    print(points)

    return points

def World():
    pass
    # points = 

def Sun():
    pass

def Moon():
    pass

def Ship():
    ship =  [
    (0.0, +0),
    (+0.05, 0.1),
    (0.05, 0.03),
    (0.1, 0),
    (0.04, 0.06),
    (0.06, 0.06),
    (0.05, 0.07)
    ]
    return np.array(ship)
