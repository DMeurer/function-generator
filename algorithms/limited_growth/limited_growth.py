import math

# Please read the readme for a detailed documentation

def alg(s, y0, x1, y1):
    print("Method: limited growth 1")
    print("f(x)=s-c*e^(-k*x)")
    print("calculating...")

    c = (s - y0)
    k = (math.log((y1 + s) / (s - y0)) / x1)

    print("done")
    print("f(x)=" + str(s) + "-" + str(c) + "*e^(-" + str(round(k, 3)) + "*x)")
