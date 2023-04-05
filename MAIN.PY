speed (0)
red=12
green=0
blue=24

#i sets the new position down by 10(y axis) when it loops and without picking up the pen it fills the entire screen
def sky(r, g, b):
    penup()
    setposition(-200, 200)
    pendown()
    for i in range(42):#what number should be here to fill that gap
        pensize(10)
        setposition(-200, 200-i*10)

        print(i)

        color((r, g, b))
        forward(400)
        r=r+6
        g=g+2.4
        b=b-1.5
        
sky(red, green, blue)
speed (0)
red=12
green=0
blue=24

def river (r, g, b):
    penup()
    setposition(-100, 100)
    pendown()
    for i in range(21)
        pensize(10)
        setposition(-100, 100-i*10)

        print(i)

        color((r, g, b))
        forward(400)
        r=r+6
        g=g+2.4
        b=b-1.5
sky(red, green, blue)
speed (0)
red=0
green=1
blue=4
