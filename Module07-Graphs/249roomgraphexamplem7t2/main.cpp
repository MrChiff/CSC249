/*
      map from zork 1

*/

#include <iostream>
#include <queue>
#include "StringGraph.h"
// if your edge connections are strings use 
// #include "StringGraph.h" instead

using namespace std;

// BFS 
vector<Vertex*> BreadthFirstSearch(Graph& graph, Vertex* startVertex, unordered_map<Vertex*, double>& distances) {
   unordered_set<Vertex*> discoveredSet;
   queue<Vertex*> frontierQueue;
   vector<Vertex*> visitedList;
    
   // startVertex has a distance of 0 from itself
   distances[startVertex] = 0.0;

   frontierQueue.push(startVertex);   // Enqueue startVertex in frontierQueue
   discoveredSet.insert(startVertex); // Add startVertex to discoveredSet

   while (frontierQueue.size() > 0) {
      Vertex* currentVertex = frontierQueue.front();
      frontierQueue.pop();
      visitedList.push_back(currentVertex);
      for (Edge* edge : *graph.GetEdgesFrom(currentVertex)) {
         Vertex* adjacentVertex = edge->toVertex;
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
    
   // Add vertices and edges representing rooms
  
   Vertex* lr = graph1.AddVertex("Living Room");
   Vertex* k = graph1.AddVertex("Kitchen");
  Vertex* attic = graph1.AddVertex("Attic");
  Vertex* cellar = graph1.AddVertex("Cellar");
  Vertex* beh_house = graph1.AddVertex("Behind House");
  Vertex* n_house = graph1.AddVertex("North of House");
  Vertex* s_house = graph1.AddVertex("South of House");
  Vertex* w_house = graph1.AddVertex("West of House");
   //Vertex* b1 = graph1.AddVertex("Bedroom 1");
   //Vertex* b2 = graph1.AddVertex("Bedroom 2");
  // The Living Room is west of the kitchen.
   graph1.AddDirectedEdge(lr, k, "e");
   graph1.AddDirectedEdge(k, lr, "w");
  // kitchen goes up to attic
  graph1.AddDirectedEdge(k, attic, "u");
  graph1.AddDirectedEdge(attic, k, "d");
  // living room goes down to cellar
  graph1.AddDirectedEdge(lr, cellar, "d");
  graph1.AddDirectedEdge(cellar, lr, "u");

  // connect rooms around house 
  graph1.AddDirectedEdge(w_house, n_house, "ne");
  graph1.AddDirectedEdge(n_house, w_house, "sw");
  graph1.AddDirectedEdge(w_house, s_house, "se");
  graph1.AddDirectedEdge(s_house, w_house, "nw");
  graph1.AddDirectedEdge(n_house, beh_house, "se");
  graph1.AddDirectedEdge(beh_house, n_house, "nw");
  graph1.AddDirectedEdge(s_house, beh_house, "ne");
  graph1.AddDirectedEdge(beh_house, s_house, "sw");
  // entry into house
  graph1.AddDirectedEdge(k, beh_house, "e");
  graph1.AddDirectedEdge(beh_house, k, "w");
  
  /*graph1.AddDirectedEdge(k, b2, "se");
  graph1.AddDirectedEdge(b2, k, "nw");
  graph1.AddDirectedEdge(b2, b1, "ne");
  graph1.AddDirectedEdge(b1, b2, "sw");
  graph1.AddDirectedEdge(b1, lr, "nw");
  graph1.AddDirectedEdge(lr, b1, "se");*/
    
   // Show the graph's vertices and edges
   for (Vertex* vertex : graph1.GetVertices()) {
      cout << "Location: " << vertex->label << endl;
        
      // Show outgoing edges ( from location)
      cout << "  Connections from " << vertex->label << ":" << endl;
      for (Edge* outgoingEdge : *graph1.GetEdgesFrom(vertex)) {
         cout << "   - " << vertex->label << " to ";
         cout << outgoingEdge->toVertex->label << ", ";
         cout << outgoingEdge->weight << " " << endl;
      }
    /*
      // Show incoming edges ( to location)
      cout << "  Connections to " << vertex->label << ":" << endl;
      for (Edge* incomingEdge : *graph1.GetEdgesTo(vertex)) {
         cout << "   - " << incomingEdge->fromVertex->label << " to ";
         cout << vertex->label << ", ";
         cout << incomingEdge->weight << " " << endl;
      }
     */
     cout << endl;
   }
  
    cout << "BFS Demo" << endl;
    // Ask the user for the starting person's name
   cout << "Enter the starting node name: ";
   string startName;
   getline(cin, startName);
   cout << endl;
      
   // Get the start vertex
   Vertex* startVertex = graph1.GetVertex(startName);
     cout << "You selected: " << startVertex->label << endl;
  // the actual search itself
  if (startVertex) {
      unordered_map<Vertex*, double> vertexDistances;
      vector<Vertex*> visitedList =
         BreadthFirstSearch(graph1, startVertex, vertexDistances);
         
      // Output the result
      cout << "Breadth-first search traversal" << endl;
      cout << "Start vertex: " << startVertex->label << endl;
      for (Vertex* vertex : visitedList) {
         cout << vertex->label << ": " << vertexDistances[vertex] << endl;
      }
   }
   else {
      cout << "Start vertex \"" << startName << "\" not found" << endl;
   }
     

          
   return 0;
}
