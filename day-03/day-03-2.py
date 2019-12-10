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

# All lines are either horizontal or vertical, so you can
# check to see if a point is in a path segment by checking
# if one of the coords equals the corresponding coordinate
# and then testing if the opposite one falls within the
# given range of the two line ends
def within(point, line) -> bool:
    x1,y1 = line[0]
    x2,y2 = line[1]
    px,py = point
    # Vertical line
    if x1 == x2 and x1 == px and py in range(min(y1,y2),max(y1,y2)):
        return True
    # Horizontal line
    elif y1 == y2 and y1 == py and px in range(min(x1,x2),max(x1,x2)):
        return True
    # Not in line segment
    else:
        return False

# Iterates through each line in a given path until a point
# lies along the line. Add the total distance of the line
# if the point isn't found and goes to the next segment or
# returns the distance from the origin side of line to the
# intersection point.
# Returns the total distance of a path to given intersection
def get_path_distance(point, path) -> int:
    px,py = point
    path_distance = 0
    for line in path:
        x1,y1 = line[0]
        x2,y2 = line[1]
        if within(point, line):
            path_distance += abs(x1-px) + abs(y1-py)
            break
        else:
            path_distance += abs(x1-x2) + abs(y1-y2)
    return path_distance

# This function iterates through the intersection points and
# builds the path length list of path A + path B for each
# Returns the smallest total path distance
def shortest_path(intersect_points, a_lines, b_lines) -> int:
    if (0,0) in intersect_points:
        intersect_points.remove((0,0))

    distances = []
    for point in intersect_points:
        distance = get_path_distance(point, a_lines) + get_path_distance(point, b_lines)
        distances.append(distance)
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

print(shortest_path(intersections, a_lines, b_lines))
