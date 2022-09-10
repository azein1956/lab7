#Function Global Variables
maxVal = 100
minVal = -100

# val is a function parameter
def inBounds(val):
    # Local variables bigEnough and smallEnough
    bigEnough = minVal <= val
    smallEnough = val <= maxVal
    return bigEnough and smallEnough

print(inBounds(55))
print(inBounds(502))
print(minVal, maxVal)  # This is okay, global variables are in scope
# print(val)  # This generates an error
# print(bigEnough)  # This generates an error