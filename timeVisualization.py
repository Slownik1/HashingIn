import timeit
from fileChecksum import *
import numpy as np
import matplotlib.pyplot as plt

def timeVisualization(text):

    timeMeasure = []

    for i in range(20):
        time = timeit.timeit(lambda: hashlib.sha256(text.encode()), number=100)
        timeMeasure.append(time)
        text+=text

    xPoints = range(0, 20)
    plt.plot(xPoints, timeMeasure)
    plt.show()
