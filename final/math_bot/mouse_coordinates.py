from ctypes import windll, Structure, c_long, byref


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


 
def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return [pt.x, pt.y]



def take_corners():
    
    foo = input("point to the left upper corner and  press enter  -- ")
    left_up = queryMousePosition()

    print ("")
    doo = input("point to the right lower corner and  press enter  -- ")
    right_down = queryMousePosition()

    vertices = []

##    print (left_up)
##    print (right_down)


    ##    WIDTH, HEIGHT 

    
    for n in left_up:
        vertices.append(n)

    width = abs(left_up[0] - right_down[0])

    height = abs(left_up[1] - right_down[1])

    vertices.append(width)
    vertices.append(height)
    

##    print ("vertices are   - ", vertices)
    return vertices


