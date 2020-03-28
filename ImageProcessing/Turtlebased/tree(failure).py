import turtle

def tree(length,n):
    """ paints a branch of a tree with 2 smaller branches, like an Y"""
    if length < (length/n):
           return       # escape the function
    alex.forward(length)        # paint the thik branch of the tree
    alex.left(45)          # rotate left for smaller "fork" branch
    tree(length * 0.5,length/n)      # create a smaller branch with 1/2 the lenght of the parent branch
    alex.right(90)         # rotoate right for smaller "fork" branch
    tree(length * 0.5,n-1)      # create second smaller branch
    alex.left(45)          # rotate back to original heading
    alex.backward(length)       # move back to original position
    return None           # leave the function, continue with calling program

length = int(input("Length: "))
n = int(input("n: "))
scrr= turtle.Screen()
alex = turtle.Turtle()
alex.speed(10)
tree(length,n)
