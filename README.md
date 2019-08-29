# travellingsalesman
A travelling salesman simulator in Python. Uses numpy and matplotlib to plot the shortest distance between n randomly chosen points by testing all (necessary) possibilities.
- travellingSalesman.py plots the path in matplotlib, and prints data of path (length, point-letter identifiers).
- plotter.py just contains the plotting function (and so matplotlib import).
- runTrials.py is included to analyze the algorithm, printing number of seconds to run n trials on m points in a range.

Some issues:
- clunky. still not sure if it's entirely necessary to juggle the points as strings of characters.
- lots of outsourced work. permutations of strings, finding minimum value in a dictionary.
- slow. yes, it's n! and will always be slow for any n over ~8, but I feel like this script is especially so.
