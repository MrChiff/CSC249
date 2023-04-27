#include "StringGraph.h"
#include <iostream>
// if your edge connections are strings use
// #include "StringGraph.h" instead

using namespace std;

int main() {
  // Create a new Graph object
  Graph graph1;

  // Add vertices and edges representing plane flights
  Vertex *hc = graph1.AddVertex("Hyrule Castle");
  Vertex *swamp = graph1.AddVertex("The Swamp");
  Vertex *coast = graph1.AddVertex("The Coast");
  Vertex *maiden = graph1.AddVertex("Village of the Blue Maiden");
  Vertex *etemp = graph1.AddVertex("Eastern Temple");
  graph1.AddUndirectedEdge(hc, swamp, "se");
  graph1.AddUndirectedEdge(swamp, hc, "nw");
  graph1.AddUndirectedEdge(coast, swamp, "n");
  graph1.AddUndirectedEdge(swamp, coast, "s");
  graph1.AddUndirectedEdge(maiden, swamp, "w");
  graph1.AddUndirectedEdge(swamp, maiden, "e");

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
