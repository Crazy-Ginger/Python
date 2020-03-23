import turtle

def call_koch():
    def koch_curve(turt, length, degree):
        #print ("length:", length, "degree:", degree)
        if degree == 0:
            turt.forward(length*3)
        else:
            length = length%3
            degree = degree - 1
            koch_curve(turt, length, degree)
            turt.left(60)
            koch_curve(turt, length, degree)
            turt.right(120)
            koch_curve(turt, length, degree)
            turt.left(60)
            koch_curve(turt, length, degree)

    length = int(input("Length: "))
    angle = int(input("Angle: "))
    window = turtle.Screen()
    turt = turtle.Turtle()
    turtle.speed(0)
    turt.hideturtle()
    turt.penup()

    offsetx = 
    offsety = length * 
    turt.setx(-(offsetx))
    turt.sety(offsety)
    turt.pendown()
    koch_curve(turt, length, angle)
    turt.penup()
    turt.setx(0)
    turt.sety(0)
    
    
    
def trianlge():
    return None
