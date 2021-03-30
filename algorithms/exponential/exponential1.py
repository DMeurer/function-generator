import math

# Please read the readme for a detailed documentation

def alg(y0, x1, y1):
    print("Method: exponential 1")
    print("f(x)=f(0)*e^(k*x)")
    print("calculating...")

    k = (math.log(y1 / y0))/x1

    print("done")
    print("f(x)=" + str(round(y0, 3)) + "*e^(" + str(round(k, 3)) + "*x)")
