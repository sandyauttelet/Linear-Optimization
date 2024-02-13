import numpy as np
import scipy.optimize as opt

deltas = np.linspace(0,60,13)
for delta in deltas:
    c=np.array([35,26,21,15,4])

    A = np.array([[6,5,7,4,8],\
    [35,26,21,15,4],\
        [-35,-26,-21,-15,-4]] )

    b = np.array([57,235+delta,-235+delta])

    bounds=((1,np.inf),(1,np.inf),(1,np.inf),(1,np.inf),(1,np.inf))

    isint=[1,1,1,1,1]

    res=opt.linprog(c,A,b,A_eq=None,b_eq=None,bounds=bounds,integrality=isint)

    print("Delta: ", delta)
    print("zstar: ",res['fun'])
    print("xstar: ",res['x'],"\n")
