def alg(x1, y1, x2, y2):
    print("Method: linear1")
    print("f(x)=m*x+c")
    print("calculating...")

    m = (x2 - x1) / (y2 - y1)
    c = y1 * m + x1

    print("done")
    print("f(x)=" + str(round(m)) + "*x+" + str(c))
