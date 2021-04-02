import numpy as np


def alg(x1, y1, x2, y2, x3, y3):
    print("Method: 2nd degree 1")
    print("f(x)=ax²+bx+c")
    print("calculating...")

    # this is a linear matrix equation, or system of linear scalar equations.
    # we will fill this with a 2-dimensional array, with what we use to solve this.
    matrix = np.array(
        [
            [x1 ** 2, x1, 1],
            [x2 ** 2, x2, 1],
            [x3 ** 2, x3, 1]
        ])
    y = np.array([y1, y2, y3])

    # this numpy function solves this systems and we get an array
    solved = np.linalg.solve(matrix, y)

    # now we will set the values to the associated letter in the function
    a = solved[0]
    b = solved[1]
    c = solved[2]

    if np.allclose(np.dot(matrix, solved), y):
        # printing the solution
        print("done")
        print("f(x)=" + str(round(a, 3)) + "x²+" + str(round(b, 3)) + "x+" + str(round(c, 3)))
    else:
        print("Something went wrong.")
        print("This solution might be a bit inaccurate.")
        print("This is what we found:")
        print("f(x)=" + str(round(a, 3)) + "x²+" + str(round(b, 3)) + "x+" + str(round(c, 3)))
