import timeit
from allHash import *
from timeVisualization import *
from fileChecksum import *

print(hashlib.algorithms_available)
dataFromConsole = input()

#b98dac940a82b110e6265ca78d1320f1f7103861e922aa1a54e4202686e9bbd3 - ubuntu check sum

#allHash(dataFromConsole)

# I have used this to 2 and 3 step
#print(fileChecksum("test.txt"))

timeVisualization(dataFromConsole)