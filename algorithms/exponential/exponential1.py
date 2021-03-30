import math


def alg(y0, x1, y1):
    print("Method: linear1")
    print("f(x)=f(0)*e^(k*x)")
    print("calculating...")

    k = (math.log(y1 / y0))/x1

    print("done")
    print("f(x)=" + str(y0) + "*e^(" + str(k) + "*x)")
