fo = open("input.txt", "r")
orbit_data = [line.strip() for line in fo]
fo.close()

print(*orbit_data, sep="\n")

class Node:
    __name = ""
    __parent_node_id = -1
    __child_node_ids = []

    def __init__(self, name, parent_node_id):
        # Leave the parent's id as negative to show it has
        # no parents for the top level. Used for traversal
        self.__name = name
        if parent_node_id < 0:
            self.__parent_node_id = -1
        else:
            self.__parent_node_id = parent_node_id
    
    def add_child(self, child_node_id):
        self.__child_node_ids.append(child_node_id)

    def find_child(self, child_node_id):
        self.__child_node_ids.append(child_node_id)

    def get_id(self) -> int:
        return id(self)

for orbit in orbit_data:
    parent, child = [planet for planet in orbit.split(")")]
    # Instantiate the top level node
    print(parent,"has child planet",child)
    #if OrbitChart is None:
    #    OrbitChart = Node(-1)
