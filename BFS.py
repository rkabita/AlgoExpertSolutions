class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
		queue = [self]
		while queue:
			s = queue.pop(0)
			array.append(s.name)
			
			for neighbour in s.children:
				queue.append(neighbour)
		return array
