// Map for Zelda (Lesser Hyrule)

#include "StringGraph.h"
#include <iostream>
// if your edge connections are strings use
// #include "StringGraph.h" instead

using namespace std;

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
  //Vertex *woods = graph1.AddVertex("Lost Woods");
  graph1.AddUndirectedEdge(castle, swamp, "se");
  graph1.AddUndirectedEdge(swamp, castle, "nw");
  graph1.AddUndirectedEdge(coast, swamp, "n");
  graph1.AddUndirectedEdge(swamp, coast, "s");
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

  return 0;
}
