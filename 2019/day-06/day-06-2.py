# Take the input and split into a list of (parent, child) orbit tuples
fo = open("input.txt", "r")
orbit_data = [tuple(line.strip().split(")")) for line in fo]
fo.close()

# Create empty dict
orbit_table = dict()

# Parent entry will hold list of orbiting children. setdefault adds an
# empty array if the dict entry doesn't exist, which we then append to
for (parent, child) in orbit_data:
    orbit_table.setdefault(parent, []).append(child)

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

orbit_count_checksum = count_orbits("COM", 0)
print(orbit_count_checksum)
