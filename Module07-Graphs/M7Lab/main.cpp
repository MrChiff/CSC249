// Map for Zelda (Lesser Hyrule)

#include "StringGraph.h"
#include <iostream>
#include <queue>
// if your edge connections are strings use
// #include "StringGraph.h" instead

using namespace std;

// Breadth First Search
// BFS
vector<Vertex *>
BreadthFirstSearch(Graph &graph, Vertex *startVertex,
                   unordered_map<Vertex *, double> &distances) {
  unordered_set<Vertex *> discoveredSet;
  queue<Vertex *> frontierQueue;
  vector<Vertex *> visitedList;

  // startVertex has a distance of 0 from itself
  distances[startVertex] = 0.0;

  frontierQueue.push(startVertex);   // Enqueue startVertex in frontierQueue
  discoveredSet.insert(startVertex); // Add startVertex to discoveredSet

  while (frontierQueue.size() > 0) {
    Vertex *currentVertex = frontierQueue.front();
    frontierQueue.pop();
    visitedList.push_back(currentVertex);
    for (Edge *edge : *graph.GetEdgesFrom(currentVertex)) {
      Vertex *adjacentVertex = edge->toVertex;
      if (0 == discoveredSet.count(adjacentVertex)) {
        frontierQueue.push(adjacentVertex);
        discoveredSet.insert(adjacentVertex);

        // Distance of adjacentVertex is 1 more than currentVertex
        distances[adjacentVertex] = distances[currentVertex] + 1;
      }
    }
  }
  return visitedList;
}

int main() {
  // Create a new Graph object
  Graph graph1;

  // Add vertices and edges representing plane flights
  Vertex *castle = graph1.AddVertex("Hyrule Castle");
  Vertex *swamp = graph1.AddVertex("The Swamp");
  Vertex *coast = graph1.AddVertex("The Coast");
  Vertex *maiden = graph1.AddVertex("Village of the Blue Maiden");
  Vertex *etemp = graph1.AddVertex("Eastern Temple");
  Vertex *lake = graph1.AddVertex("Lake Hylia");
  Vertex *cave = graph1.AddVertex("Cave of No Return");
  Vertex *tower = graph1.AddVertex("Tower of Flames");
  Vertex *mountain = graph1.AddVertex("Mountain Path");
  Vertex *foothills = graph1.AddVertex("DM Foothills");
  Vertex *darkness = graph1.AddVertex("Temple of Darkness");
  Vertex *woods = graph1.AddVertex("Lost Woods");
  Vertex *kakariko = graph1.AddVertex("Kakariko Village");
  graph1.AddUndirectedEdge(castle, swamp, "se");
  graph1.AddUndirectedEdge(swamp, castle, "nw");

  graph1.AddUndirectedEdge(coast, swamp, "n");
  graph1.AddUndirectedEdge(swamp, coast, "s");

  graph1.AddUndirectedEdge(etemp, swamp, "e");
  graph1.AddUndirectedEdge(swamp, etemp, "w");

  graph1.AddUndirectedEdge(etemp, maiden, "e");
  graph1.AddUndirectedEdge(maiden, etemp, "w");

  graph1.AddUndirectedEdge(etemp, lake, "nw");
  graph1.AddUndirectedEdge(lake, etemp, "se");

  graph1.AddUndirectedEdge(lake, cave, "w");
  graph1.AddUndirectedEdge(cave, lake, "e");

  graph1.AddUndirectedEdge(cave, castle, "sw");
  graph1.AddUndirectedEdge(castle, cave, "ne");

  graph1.AddUndirectedEdge(cave, tower, "n");
  graph1.AddUndirectedEdge(tower, cave, "s");

  graph1.AddUndirectedEdge(cave, mountain, "w");
  graph1.AddUndirectedEdge(mountain, cave, "e");

  graph1.AddUndirectedEdge(mountain, castle, "se");
  graph1.AddUndirectedEdge(castle, mountain, "nw");

  graph1.AddUndirectedEdge(mountain, foothills, "sw");
  graph1.AddUndirectedEdge(foothills, mountain, "ne");

  graph1.AddUndirectedEdge(foothills, castle, "w");
  graph1.AddUndirectedEdge(castle, foothills, "e");

  graph1.AddUndirectedEdge(foothills, darkness, "w");
  graph1.AddUndirectedEdge(darkness, foothills, "e");

  graph1.AddUndirectedEdge(woods, darkness, "n");
  graph1.AddUndirectedEdge(darkness, woods, "s");

  graph1.AddUndirectedEdge(woods, foothills, "e");
  graph1.AddUndirectedEdge(foothills, woods, "w");

  graph1.AddUndirectedEdge(kakariko, darkness, "se");
  graph1.AddUndirectedEdge(darkness, kakariko, "nw");

  graph1.AddUndirectedEdge(kakariko, woods, "s");
  graph1.AddUndirectedEdge(woods, kakariko, "e");

  // Show the graph's vertices and edges
  for (Vertex *vertex : graph1.GetVertices()) {
    cout << "Location: " << vertex->label << endl;

    // Show outgoing edges (flights from location)
    cout << "  Connections from " << vertex->label << ":" << endl;
    for (Edge *outgoingEdge : *graph1.GetEdgesFrom(vertex)) {
      cout << "   - " << vertex->label << " to ";
      cout << outgoingEdge->toVertex->label << ", ";
      cout << outgoingEdge->weight << " " << endl;
    }

    // Show incoming edges (flights to location)
    /*  cout << "  Connections to " << vertex->label << ":" << endl;
      for (Edge *incomingEdge : *graph1.GetEdgesTo(vertex)) {
        cout << "   - " << incomingEdge->fromVertex->label << " to ";
        cout << vertex->label << ", ";
        cout << incomingEdge->weight << " " << endl;
      }*/
    cout << endl;
  }

  cout << "BFS Demo" << endl;
  // Ask the user for the starting person's name
  cout << "Enter the starting node name: ";
  string startName;
  getline(cin, startName);
  cout << endl;

  // Get the start vertex
  Vertex *startVertex = graph1.GetVertex(startName);
  cout << "You selected: " << startVertex->label << endl;
  // the actual search itself
  if (startVertex) {
    unordered_map<Vertex *, double> vertexDistances;
    vector<Vertex *> visitedList =
        BreadthFirstSearch(graph1, startVertex, vertexDistances);

    // Output the result
    cout << "Breadth-first search traversal" << endl;
    cout << "Start vertex: " << startVertex->label << endl;
    for (Vertex *vertex : visitedList) {
      cout << vertex->label << ": " << vertexDistances[vertex] << endl;
    }
  } else {
    cout << "Start vertex \"" << startName << "\" not found" << endl;
  }

  return 0;
}
