import matplotlib.pyplot as plt


def plotPts(ptDict, xLen, yLen, path):
    xs = []
    ys = []
    xBound = xLen/2
    yBound = yLen/2
    for pt in ptDict:
        xs.append(ptDict[pt][0])
        ys.append(ptDict[pt][1])

    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')

    plt.plot(xs, ys, 'ro')
    plt.axis([-xBound, xBound, -yBound, yBound])

    # Drawing blue lines
    #plt.plot([0, ptDict[path[0]][0]], [0, ptDict[path[0]][1]], 'b-')
    for p in range(len(path)-1):
        plt.plot([ptDict[path[p]][0], ptDict[path[p+1]][0]],
                 [ptDict[path[p]][1], ptDict[path[p+1]][1]],
                 'b-')
    #plt.plot([ptDict[path[-1]][0], 0], [ptDict[path[-1]][1], 0], 'b-')
    #trying to fix:
    plt.plot([ptDict[path[-1]][0], ptDict[path[0]][0]],
             [ptDict[path[-1]][1], ptDict[path[0]][1]], 'b-')
        

    # plt.savefig('name')
    plt.show()
