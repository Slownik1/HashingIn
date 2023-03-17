import hashlib
import time

def allHash(text):

    for algorithm in hashlib.algorithms_available:
        if((algorithm == "shake_128") or (algorithm == "shake_256")):
            continue
        hash = hashlib.new(algorithm)
        startTime = time.time()
        hash.update(text.encode())
        print(f"{algorithm}:")
        hash_result = hash.hexdigest()
        endTime = time.time()
        print(f"{hash_result} ({endTime - startTime:.5f} s)")