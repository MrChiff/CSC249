#include <iostream>
#include <string>
using namespace std;

/*
CSC 249
M3Lab2 - Merge Sort
hardwicj
2023/02/16

*/
static int COMPARES = 0;
static int SWAPS = 0; // any time we switched fingers and swapped
static int COMPS = 0; // any if statement comparing L' and R'
static int COPIES = 0; // # of copy operations into a temp array
const bool DEBUG = true;
string ArrayToString(int* array, int arraySize);

void Merge(int* numbers, int leftFirst, int leftLast, int rightLast) {
   int mergedSize = rightLast - leftFirst + 1;       // Size of merged partition
   int* mergedNumbers = new int[mergedSize]; // Dynamically allocates temporary
                                             // array for merged numbers
   int mergePos = 0;                         // Position to insert merged number
   int leftPos = leftFirst;                  // Initialize left partition position
   int rightPos = leftLast + 1;              // Initialize right partition position

   if (DEBUG){
    cout << "\tCalling Merge(" << leftFirst << ", " << leftLast << ") with (";
    cout << leftLast+1 << ", " << rightLast << ")" << endl;
   }
   // Add smallest element from left or right partition to merged numbers
   // while there are unsorted items left...
   while (leftPos <= leftLast && rightPos <= rightLast) {
        COMPS++; // picking left or right counts as a comparison
      //either pick left item (if it's the smallest)
      if (numbers[leftPos] <= numbers[rightPos]) {
         mergedNumbers[mergePos] = numbers[leftPos];
         leftPos++;
         SWAPS++;
      }
      //or pick right item (if it's the smallest)
      else {
         mergedNumbers[mergePos] = numbers[rightPos];
         rightPos++;
         SWAPS++;
      }
      mergePos++;
   }
   // The two cases below occur if we've exhausted one side (L' or R'), no more compares needed
   // If left partition is not empty, add remaining elements to merged numbers
   while (leftPos <= leftLast) {
      mergedNumbers[mergePos] = numbers[leftPos];
      leftPos++;
      mergePos++;
   }

   // If right partition is not empty, add remaining elements to merged numbers
   while (rightPos <= rightLast) {
      mergedNumbers[mergePos] = numbers[rightPos];
      rightPos++;
      mergePos++;
   }

   // Copy merged numbers back to numbers
   // if we tracked COPY OPERATIONS, this would be COPY_OPERATIONS += mergedSIZE
   COPIES += mergedSize;
   for (mergePos = 0; mergePos < mergedSize; mergePos++) {
      numbers[leftFirst + mergePos] = mergedNumbers[mergePos];
   }
   // DEBUG: print the temp array before disposal
   cout << "\tA': " << ArrayToString(mergedNumbers, mergedSize) << endl;
   // Free temporary array
   delete[] mergedNumbers;
}

void MergeSort(int* numbers, int startIndex, int endIndex) {
   if (startIndex < endIndex) {

    if (DEBUG){
        cout << "calling MergeSort(" << startIndex << ", " << endIndex << ")" << endl;
    }
      // Find the midpoint in the partition
      int mid = (startIndex + endIndex) / 2;

      // Recursively sort left and right partitions
      MergeSort(numbers, startIndex, mid);
      MergeSort(numbers, mid + 1, endIndex);

      // Merge left and right partition in sorted order
      Merge(numbers, startIndex, mid, endIndex);
      if (DEBUG){
        cout << "Ops so far:" << "comps = " << COMPS << " swaps=" << SWAPS << " copies=" << COPIES << endl;
      }
   }
}

string ArrayToString(int* array, int arraySize) {
   // Special case for empty array
   if (0 == arraySize) {
      return string("[]");
   }

   // Start the string with the opening '[' and element 0
   string result = "[" + to_string(array[0]);

   // For each remaining element, append comma, space, and element
   for (int i = 1; i < arraySize; i++) {
      result += ", ";
      result += to_string(array[i]);
   }

   // Add closing ']' and return result
   result += "]";
   return result;
}

int main() {
   // Create an array of numbers to sort
   int numbers[] = { 61, 76, 19, 4, 94, 32, 27, 83, 58 };
   int numbersSize = sizeof(numbers) / sizeof(numbers[0]);

   // Display the contents of the array
   cout << "UNSORTED: " << ArrayToString(numbers, numbersSize) << endl;

   // Call the MergeSort function
   MergeSort(numbers, 0, numbersSize - 1);

   // Display the sorted contents of the array
   cout << "SORTED:   " << ArrayToString(numbers, numbersSize) << endl;
}
