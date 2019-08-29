# Simple TSP

import numpy as np
import time
from itertools import permutations
from string import ascii_lowercase
from plotter import plotPts


def genPoints(numPts, xLen, yLen):
    # for example: 5, 100, 100 gives 5 random points on 100x100 board
    points = {}
    for i in range(numPts):
        letter = ascii_lowercase[i]
        points.update({letter: (np.random.randint(-xLen/2, xLen/2),
                                np.random.randint(-yLen/2, yLen/2))})
    return points


def genPaths(pts):
    # returns permutations of string of points, i.e. 'abcd'
    perms = [''.join(p) for p in permutations(pts)]

    # remove duplicates (same path going backwards)
    uniquePerms = list()
    [x for x in perms if str(x[::-1]) not in uniquePerms
        and not uniquePerms.append(str(x))]
    ptdict = dict.fromkeys(uniquePerms, 0)

    return ptdict


def calcDistance(s1, s2):
    # s1, s2 are tuples; (x pos, y pos)
    return np.sqrt(np.square(s2[1] - s1[1]) + np.square(s2[0] - s1[0]))


def calcLenPath(path, locs):
    # path is string of order of points; locs is dict of their chosen positions
    # returns float, path length moving through all points
    startpt = locs[path[0]]
    dist = 0

    for choice in path[1:]:
        endpt = locs[choice]
        dist += calcDistance(startpt, endpt)
        startpt = endpt

    return dist


def findShortestPath(dictPaths, ptLocs):
    # calculate the answer!
    # can return dictPaths to see all answers
    for path in dictPaths:
        dictPaths[path] = calcLenPath(path, ptLocs)

    minPath = min(dictPaths, key=dictPaths.get)
    minVal = dictPaths[minPath]

    # return minPath, minVal, dictPaths
    return minPath, minVal


def runSim(numPts, xLen, yLen):
    # basially a main() function that puts it all together
    ptLocs = genPoints(numPts, xLen, yLen)
    paths = genPaths(ascii_lowercase[0:numPts])
    shortestPath, shortestDistance = findShortestPath(paths, ptLocs)
    plotPts(ptLocs, xLen, yLen, shortestPath)
    
    return [shortestPath, shortestDistance]

def main():
    # beginning with dimensions
    print("Please enter values for the lengths of the X and Y dimensions.\n")
    lenX = int(input("X dimension: "))
    lenY = int(input("Y dimension: "))
    
    while lenX <= 0 or lenY <= 0:
        print("Error: please enter nonzero values for X and Y.")
        lenX = int(input("X dimension: "))
        lenY = int(input("Y dimension: "))

    # determine whether to show a range of number of points or just one
    print("Would you like to see a range of points, or just one?")
    response = input("Enter 'range' or 'one' >> ").lower()

    while response != "range" and response != "one":
        print("Error: please enter either \"range\" or \"one\".")
        response = input(">> ").lower()
    
    if response == "range":
        maxPts = int(input("Enter the MINIMUM amount of points to plot: "))
        minPts = int(input("Enter the MAXIMUM amount of points: "))
        if minPts > maxPts: # make sure we go from largest to smallest
            temp = maxPts
            maxPts = minPts
            minPts = temp
        # plotting and returning values
        for i in range(minPts, maxPts):
            print(str(i) + " points returns a path of length "
                  + runSim(i, lenX, lenY) + " and took x seconds")
            input("Press Enter to continue...")
            
    elif response == "one":
        pts = int(input("Enter the amount of points to plot: "))
        while pts <= 1:
            print("Error: please enter an amount >= 2.")
            pts = int(input("Amount of points to plot: "))
        #plot and return
        print(str(pts) + " points returns a path of length ",
                  runSim(pts, lenX, lenY), " and took x seconds")
        input("Press Enter to continue...")
    
        


main()
