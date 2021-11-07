
import random
def decorforlist(func):
    def inner():
        s = set(func())
        return list(s)
    return inner

@decorforlist
def listcreator():
    somelist = [random.randint(10,50) for x in range(100)]
    return somelist
print(listcreator())