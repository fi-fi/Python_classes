# ---------------------- PYTHON-----------------------
# Set 3
# Author: Filip Kowalski
#
# Problem 10

# Initiating lists for roman numbers dictionary
l = ["I", "V", "X", "L", "C", "D", "M"]
l0 = [1, 5, 10, 50, 100, 500, 1000]

# Three ways of forming a dictionary
d1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
d2 = dict(zip(l, l0))
d3 = {}
for k, v in zip(l, l0):
    d3[k] = v
