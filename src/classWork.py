def myHash0(value):
    return len(value)


bobAddress = myHash0('bob')
dadAddress = myHash0('dad')
ahmedAddress = myHash0('ahmed')

print(bobAddress)

# -------------------------------

# solution 1
myArray = [None] * 8

myArray[bobAddress] = 'bob'
myArray[ahmedAddress] = 'ahmed'

print(myArray[bobAddress])

print(myArray[myHash0('bob')])

# this is fast but not unique at all NAME COLLISION
# dad and bob both has 3 letters so location both would be 3 so bad bad bad
# this is non-invertable it can't go backwards and it's pretty secure

# --------------------------------

# solution 2
def myHash1(key):
    stringIndex = 0
    for char in key:
        if char == 'a':
            stringIndex += 1

        if char == 'b':
            stringIndex += 2

    return stringIndex

# this is also a better but slower way
# no name collision dad and bob give different numbers
# dad then goes to index of 9 but it is now kind of invertable it lowers the list of potential words to reverse engineer 

def myHash3(key,scrambleNumber):
    stringIndex = 0
    scrambleNumber = 17
    for char in key:
        if char == 'a':
            stringIndex += 1
            stringIndex *= scrambleNumber

        if char == 'b':
            stringIndex += 2
            stringIndex *= scrambleNumber

    return stringIndex