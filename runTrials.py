# tester file for sim TSP

from travellingSalesman import runSim
import time

# 6pts takes ~36s, 7pts takes ~9m. 8 points would only be longer

print("Please enter minimum and maximum number of points to plot the "
      + "most efficient path between, as well as X and Y dimensions, "
      + "and the number of trials for every amount of points.\n")

minAmt = int(input("MIN: "))
maxAmt = int(input("MAX: "))
xDim = int(input("XDIM: "))
yDim = int(input("YDIM: "))
numTests = int(input("How many tests per point #?: "))

for val in range(minAmt, maxAmt+1):
    print("For " + str(val) + " points:")
    pathDists = []
    start = time.time()
    for trial in range(numTests):
        data = runSim(val, xDim, yDim)
        pathDists.append(data[1])
    end = time.time()
    print("Computation took " + '%.3f'%(end-start)
          + " seconds to complete. \nThe average answer was "
          + '%.3f'%(sum(pathDists)/len(pathDists)))
