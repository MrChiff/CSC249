"""
File: shorttest.py
"""

from graph import LinkedDirectedGraph

g = LinkedDirectedGraph()

# Insert vertices
g.addVertex("1")
g.addVertex("2")
g.addVertex("3")
g.addVertex("4")
g.addVertex("5")

# Insert weighted edges
g.addEdge("1", "2", 1)
g.addEdge("1", "3", 1)
g.addEdge("2", "3", 1)
g.addEdge("2", "4", 1)
g.addEdge("3", "2", 1)
g.addEdge("3", "5", 1)
g.addEdge("4", "2", 1)
g.addEdge("4", "5", 1)
g.addEdge("5", "3", 1)
g.addEdge("5", "4", 1)
print(g)

print("Neighboring vertices of 2:")
for vertex in g.neighboringVertices("2"):
    print(vertex)

print("Incident edges of 2:")
for edge in g.incidentEdges("2"):
    print(edge)

print("Neighboring vertices of 5:")
for vertex in g.neighboringVertices("5"):
    print(vertex)

print("Incident edges of 5:")
for edge in g.incidentEdges("5"):
    print(edge)
