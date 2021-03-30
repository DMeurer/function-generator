# Please read the readme for a detailed documentation

def alg(x1, y1, x2, y2):
    print("Method: linear1")
    print("f(x)=m*x+c")
    print("calculating...")

    m = (y2 - y1) / (x2 - x1)
    z1 = x1 * m
    c = ((-1 * x1) * m) + y1

    print("done")
    print("f(x)=" + str(round(m, 3)) + "*x+" + str(round(c, 3)))
