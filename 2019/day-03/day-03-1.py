import re

# Opening the file and getting two line paths
fo = open("input.txt", "r")
path_a = fo.readline().strip().split(",")
path_b = fo.readline().strip().split(",")
fo.close()

# This function returns a list of tuple objects for each
# segment of the line path
# Each object has the structure: ((x1,y1),(x2,y2))
def create_line_list(path: list):
    prev = (0,0)
    output = []
    for point in path:
        num = int(re.findall(r"\d+", point)[0])
        if "R" in point:
            temp = (prev,(prev[0]+num, prev[1]))
            output.append(temp)
            prev = temp[1]
        elif "L" in point:
            temp = (prev,(prev[0]-num, prev[1]))
            output.append(temp)
            prev = temp[1]
        elif "U" in point:
            temp = (prev,(prev[0], prev[1]+num))
            output.append(temp)
            prev = temp[1]
        elif "D" in point:
            temp = (prev,(prev[0], prev[1]-num))
            output.append(temp)
            prev = temp[1]

    return output

# Takes two line segments defined by p1,p2 and p3,p4 and
# returns the x,y coordinates if they intersect or False
# if they do not
# Using formula from Simon Walton, Dept of Computer Science, Swansea
# http://www.cs.swan.ac.uk/~cssimon/line_intersection.html
def find_intersection(p1, p2, p3, p4):
    # Unpacking for readability
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    x4,y4 = p4

    d_a = ((x4-x3)*(y1-y2))-((x1-x2)*(y4-y3))
    d_b = ((x4-x3)*(y1-y2))-((x1-x2)*(y4-y3))
    if d_a == 0 or d_b == 0:
        # If we reach this point, it means the lines are colinear
        # or parallel. If they're colinear, all x-coords or y-coords
        # will be the same depending on if the lines are vertical or
        # horizontal and intersect at every point where the lines overlap
        # We're dealing with a discrete system because we're using
        # Manhattan distance, so we can just return a list of all
        # integer values where the lines overlap.
        # If the x-coords or y-coords aren't all the same, then the lines
        # are just parallel and we can return False for no intersect

        # Vertical line
        if x1 == x2 and x1 == x3 and x1 == x4:
            y_list = [y1,y2,y3,y4]
            y_list.remove(min(y_list))
            y_list.remove(max(y_list))
            yi_1 = min(y_list)
            yi_2 = max(y_list)
            output = [(x1,y) for y in range(yi_1,yi_2)]
            return output
        # Horizontal line
        elif y1 == y2 and y1 == y3 and y1 == y4:
            x_list = [x1,x2,x3,x4]
            x_list.remove(min(x_list))
            x_list.remove(max(x_list))
            xi_1 = min(x_list)
            xi_2 = max(x_list)
            output = [(x,y1) for x in range(xi_1,xi_2)]
            return output
        # Parallel lines
        else:
            return False
    else:
        t_a = (((y3-y4)*(x1-x3))+((x4-x3)*(y1-y3)))/d_a
        t_b = (((y1-y2)*(x1-x3))+((x2-x1)*(y1-y3)))/d_b

    if ((0 <= t_a <= 1) and (0 <= t_b <= 1)):
        # It doesn't matter which line equation we use
        # We just need t_a and t_b to verify they do intersect
        x = int(x1 + t_a*(x2-x1))
        y = int(y1 + t_a*(y2-y1))
        return (x,y)
    else:
        return False
    
# Finally, some easy math - https://i.imgur.com/FrVGO1F.png
# Just calculating the Manhattan distance of each intersection
# from the origin and returning the shortest distance
# Removes the origin from the list of intersections because duh
def shortest_distance(points):
    if (0,0) in points:
        points.remove((0,0))
    distances = [(abs(x)+abs(y)) for (x,y) in points]
    return min(distances)

a_lines = create_line_list(path_a)
b_lines = create_line_list(path_b)

intersections = []
for line_a in a_lines:
    for line_b in b_lines:
        intersect = find_intersection(line_a[0], line_a[1], line_b[0], line_b[1])
        # Can receive either a single point or a list of points back
        if isinstance(intersect, tuple):
            intersections.append(intersect)
        elif isinstance(intersect, list):
            intersections.extend(intersect)

print(shortest_distance(intersections))
