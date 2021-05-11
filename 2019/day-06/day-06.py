### Common Code ###
#######################################################################
# Take the input and split into a list of (parent, child) orbit tuples
year = "2019"
day = "day-06"
sample = False

if sample:
    fo = open(year+"/"+day+"/sample.txt", "r")
else:
    fo = open(year+"/"+day+"/input.txt", "r")
orbit_data = [tuple(line.strip().split(")")) for line in fo]
fo.close()

# Create empty dict
orbit_table = dict()

# Parent entry will hold list of orbiting children. setdefault adds an
# empty array if the dict entry doesn't exist, which we then append to
for (parent, child) in orbit_data:
    orbit_table.setdefault(parent, []).append(child)

### Part 1 Code ###
#######################################################################
# Depth first search of each orbit with its children. The weight is how
# many ancestor orbits the parent has + 1 for the relationship between
# parent and child + the weight of all its children's orbits
def count_orbits(key, weight):
    # There are no children weights to count
    if orbit_table.get(key) is None:
        return 0
    # If it exists, it has children, so count the total children weight
    # before adding to the parent's weights
    children_weight = 0
    for child in orbit_table[key]:
        children_weight += weight + 1 + count_orbits(child, weight + 1)
    return children_weight

# Part 1 Output
orbit_count_checksum = count_orbits("COM", 0)
print("Part 1: ", orbit_count_checksum)

### Part 2 Code ###
#######################################################################
# Another depth first search, but this one is building an unordered
# list of visited nodes from COM to the search term (YOU/SAN)
def find_path(key, search, travel_path):
    # Not found in dead ends
    if orbit_table.get(key) is None:
        return ([], False)
    
    # Search term was found among the orbiting children
    # Nothing to do with the other siblings, so just ignore them
    if search in orbit_table[key]:
        # Don't append the search term to the path
        return (travel_path, True)
    else:
        # Search value is not in the children
        for orbit in orbit_table[key]:
            (_, found) = find_path(orbit, search, travel_path)
            # If the search term was found in the children's children,
            # add this object to the travel_path
            if found is True:
                travel_path.append(orbit)
                return (travel_path, True)
    # Search value not found
    return (travel_path, False)

# Build paths from "COM" to You and Santa
(you_path, _) = find_path("COM", "YOU", ["COM"])
(santa_path, _) = find_path("COM", "SAN", ["COM"])

# Build a list of unique objects in both paths
transfer_path = [x for x in you_path + santa_path if not (x in you_path and x in santa_path)]

# Part 2 Output
print("Part 2: ", len(transfer_path))