##    667b6c7d63677f3c733c7f323c3c7b333e7b3c3c7f3e7b333e3232393c3d3268

## UN - XOR

## input = string


def rox(foo):
    arr = []
    for phi in range(len(foo)):
        poop = chr(ord(foo[phi])^10)
        
        arr.append(poop)
    return arr


