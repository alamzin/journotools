# -*- coding: utf-8 -*-

def get_size (x_aspect, y_aspect, x_size, y_size):
    # takes x-aspect, y-aspect of a picture and the size of the origin
    # gives two varieties of the destination picture 
    # rounds results

    print ("x-aspect", x_aspect)
    print ("y-aspect", y_aspect)
    print ("x-size", x_size)
    print ("y-size", y_size)
    x_unit = x_size/x_aspect

    print ("Variety 1: x as base", round(x_unit*x_aspect),"x",round(x_unit*y_aspect))

    y_unit = y_size/y_aspect

    print ("Variety 2: y as base", round(y_unit*x_aspect), "x", round(y_unit*y_aspect))


get_size(9,16,564,797)

