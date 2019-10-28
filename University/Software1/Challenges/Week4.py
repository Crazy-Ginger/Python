#!/usr/bin/env python3
from random import randint as Rint
from random import randrange as Rrang
from math import log, hypot

#for making the diagram look better
from PIL import Image
def node_gen(width, height):
    nodes= []
    for i in range(4, round((log(height*width)))):
        nodes.append([Rint(6, width-7), Rint(6, height-7)])
    colours = []
    for i in range(len(nodes)):
        colours.append([Rrang(255), Rrang(255), Rrang(255)])
    return nodes, colours

def set_Voroni_text(plane, nodes):
    width = len(plane[0])
    height = len(plane)
    chars = ["X", "O", "I", "H", "Z", "S"]
    for y in range(height):
        for x in range(width):
            nearest_node =  -1
            nearest_dist = width*height
            for node in nodes:
                dist =  hypot(node[0]-x, node[1]-y)
                if dist == nearest_dist:
                    nearest_node = -1
                    break
                elif dist < nearest_dist:
                    nearest_node = nodes.index(node)
                    nearest_dist = dist

            if nearest_node == -1:
                plane[y][x] = "|"
            else:
                to_add = chars[nearest_node]
                plane[y][x] = to_add
    for i in nodes:
        x = i[0]
        y = i[1]
        plane[y][x] = "+"
    return plane

def set_voroni_eucl(image, nodes, colours):
    img = image.load()
    width = image.size[0]
    height = image.size[1]
    for y in range(height):
        for x in range(width):
            nearest_node =  -1
            nearest_dist = width*height
            for node in nodes:
                dist =  hypot(node[0]-x, node[1]-y)
                if dist == nearest_dist:
                    nearest_node = -2
                    nearest_dist = dist
                elif dist < nearest_dist:
                    nearest_node = nodes.index(node)
                    nearest_dist = dist

            if nearest_node == -2:
                img[x, y] = (0, 0, 0)
            else:
                img[x, y] = (colours[nearest_node][0], colours[nearest_node][1],colours[nearest_node][2])
    for node in nodes:
        x = node[0]
        y = node[1]
        for i in range(-5, 5):
            for j in range(-5, 5):
                img[x+i, y+j] = (255, 255, 255)
    return img

def set_voroni_man(image, nodes, colours):
    img = image.load()
    width = image.size[0]
    height = image.size[1]
    for y in range(height):
        for x in range(width):
            nearest_node =  -1
            nearest_dist = width*height
            for node in nodes:
                dist =abs(x-node[0]) + abs(y-node[1])
                if dist == nearest_dist:
                    nearest_node = -2
                    nearest_dist = dist
                elif dist < nearest_dist:
                    nearest_node = nodes.index(node)
                    nearest_dist = dist

            if nearest_node == -2:
                img[x, y] = (0, 0, 0)
            else:
                img[x, y] = (colours[nearest_node][0], colours[nearest_node][1],colours[nearest_node][2])
    for node in nodes:
        x = node[0]
        y = node[1]
        for i in range(-5, 5):
            for j in range(-5, 5):
                img[x+i, y+j] = (255, 255, 255)
    return img

#####Main Code Block######
height = int(input("Height: "))
width = int(input("Width; "))
nodes, colours = node_gen(width, height)
print (nodes)
plane = [[None]*width for _ in range(height)]
print ("number of nodes:", len(nodes))

# text based output
# new_plane  = set_Voroni_text(plane, nodes)
# for row in new_plane:
    # newrow = ""
    # for item in row:
        # newrow += item
    # print (newrow)


# image output
image = Image.new('RGB', (width, height),"black")
set_voroni_eucl(image, nodes, colours)
image.show()
set_voroni_man(image, nodes, colours)
image.show()



#https://en.wikipedia.org/wiki/Fortune%27s_algorithm
