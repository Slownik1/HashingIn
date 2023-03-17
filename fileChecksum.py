import hashlib
import time

def fileChecksum(file):
    with open(file, "rb") as f:
        bytes = f.read()
        return hashlib.sha256(bytes).hexdigest()
