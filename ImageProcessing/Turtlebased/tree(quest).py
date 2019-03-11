import turtle

def tree(size):
    if size<5:
        alex.forward(size)
        alex.backward(size)
    elif size == 0:
        return
    alex.forward(size/3)
    
    alex.left(30)
    tree(size*(2/3))
    alex.right(30)
    
    alex.forward(size/6)
    
    alex.right(25)
    tree(size/2)
    alex.left(25)
    
    alex.forward(size/3)

    right(25)
    tree(size/2)
    left(25)

    forward(size/6)
    return size

size = int(input())
window = turtle.Screen()
alex = turtle.Turtle()
alex.speed(12)
tree(size)
