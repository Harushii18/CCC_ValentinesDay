import math
#get number of pics to be laid out
numPics=int(input())
while numPics!=0:
    if numPics == 0:
        break
    else:
        l = math.floor(math.sqrt(numPics))
        while (numPics % l != 0):
            l -= 1
        w = numPics / l
        print('Minimum perimiter is %.0f with dimensions %.0f x %.0f' % (2 * l + 2 * w, l, w))
        numPics = int(input())
    

