def alg(x1, y1, x2, y2):
    print("Method: linear1")
    print("f(x)=m*(x-d)+c")
    print("calculating...")

    m = (x2 - x1) / (y2 - y1)
    d = y1
    c = y1 * m + x1

    print("done")
    print("f(x)=" + str(m) + "*(x-(" + str(d) + "))+" + str(c))
