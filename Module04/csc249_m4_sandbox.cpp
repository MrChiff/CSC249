#include <iostream>
#include <vector>
using namespace std;

/*
Some "warmup" example code for Module 4 - Lists
We've used arrays as a basic linear ADT, but they
lack some basic functionality such as add and remove.

The vector class in C++ handles some of this for us.
It can be thought of as an "array-list" structure.

We'll then look at singly linked lists using a basic
node and pointer structure.

*/
// forward declarations (method signatures)
void do_array_example();
void do_vector_example();
void do_singly_linked_list_example();

int main() {
  cout << "Various linear ADTs demonstrated" << endl;

  do_array_example();
  do_vector_example();
  do_singly_linked_list_example();
  
}

// define the methods we declared earlier
void do_array_example() {
  cout << endl << "Example 1: Array" << endl;
  int key = 4; // item searched for
  int numbers[] = {0, 1, 2, 3, 4};
  int numbers_size = sizeof(numbers) / sizeof(numbers[0]) ; // explain
  // array is size (sizeof(int) * number of items), so divide out sizeof(int)
  // each item is 64 bits (4 bytes)
  cout << "NUMBERS: [";
  for (int i=0; i< numbers_size; i++) {
    cout << numbers[i] << ",";
  }
  cout << "]" << endl;
  cout << "Finding value :" << key << endl;
  for (int i=0; i< numbers_size; i++) {
    if (numbers[i] == key) {
      cout << "Found " << key << " @ numbers[" << i << "]" << endl;
    }
  }
  cout << endl;
}
void do_vector_example() {
  // benefits over "raw" array:
  // can dynamically resize with push_back
  // size() just works, don't have to calculate based on word size
  cout << "Example 2: Vector (from #include <vector>)" << endl;
  vector<int> numbers;
  int temp;
  int sum=0; // for average
  cout << "Enter integers, enter 'done' to finish." << endl;
  while (cin>> temp) {
    numbers.push_back(temp);
  }
  cout << "Vector: [" ;
  for (int i=0; i<numbers.size(); i++) {
    cout << numbers[i] << ",";
    sum += numbers[i];
  }
  cout << "]" << endl;
  cout << "size: " << numbers.size();
  cout << " average: " << sum/numbers.size() << endl;
  
}
void do_singly_linked_list_example() {
  
}