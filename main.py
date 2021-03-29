from algorithms import linear1

algorithmsDict = {
    'linear1': linear1,
}


def runAlgorithm(algorithm, arg0, arg1, x0, y0, x1, y1, x2, y2, x3, y3):
    return algorithmsDict[algorithm](arg0, arg1, x0, y0, x1, y1, x2, y2, x3, y3)


runAlgorithm("linear1", 0, 0, 1, 5, 2, 7, 0, 0, 0, 0)
