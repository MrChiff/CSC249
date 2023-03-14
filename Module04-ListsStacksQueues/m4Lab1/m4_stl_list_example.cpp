#include <iostream>
#include <list> 
using namespace std;

/*
You don't have to write your own linked list --
you can use the STL (Standard template library) version.
This code is from Gaddis C++ ch18 (18-6)
see also: https://www.geeksforgeeks.org/list-cpp-stl/
which is a decent example, done differently.
*/

int main() {
  // define an empty list
  list<int> myList;

  // add some values
  // push_back = append, push_front = prepend
  for (int x = 0; x < 100; x+= 5) {
    myList.push_back(x);
  }

  // use an iterator to display the values
  // (this is a handy thing to functionize)
  // it is an "iterator"
  for (auto it = myList.begin(); it != myList.end(); it++ ) {
    cout << *it << " ";
  }
  cout << endl;

  // reverse the list elements order
  myList.reverse();

  // display the values again, this time using 
  // a range-based loop (this is Pythonic)
  for (auto element : myList) {
    cout << element << " ";
  }
  cout << endl;

  cout << "Done" << endl;
  return 0;
}