"""
Created on Thu Jan 18 11:40:38 2024

@author: sandy
"""

import numpy as np
import scipy.optimize as opt

#deltas = np.linspace(0.5,1.2,8)
deltas = [0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2]
for delta in deltas:
    c=np.array([delta, delta, 1.0, 1.0])

    A = np.array([[ 1.0, 2.0, 1.0, 2.0],\
    [ 2.0, 1.0, 2.0, 1.0],\
    [ 1.0, 1.0, 1.0, 3.0]])

    b = np.array([70.0,50.0, 62.0])

    bounds=((0,np.inf),(0,np.inf),(0,np.inf),(0,np.inf))

    #isint=[0,0,0,0] #For all x's to be real numbers
    isint=[1,1,1,1] #For all x's to be integers

    res=opt.linprog(-c,A,b,bounds=bounds,integrality=isint)

    print("Delta = ",delta)
    print("x: ",res['fun'])
    print("x-vector: ",res['x'])
    print("Norm of x-vector =", np.round(np.linalg.norm(res['x']),2), "\n")
