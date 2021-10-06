import numpy as np

def getShipPoints():
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
