# RunwayReservationSystem
# Python implementation
# v2 - by ChatGPT 4/4/23 (ChatGPT v. March 23)
# prompt: "reimplement using a binary search tree
# for the internal data structure""

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = [value] if value else []
        self.left = None
        self.right = None

    def add_plane(self, key, value):
        if key == self.key:
            self.value.append(value)
        elif key < self.key:
            if self.left is None:
                self.left = Node(key, value)
            else:
                self.left.add_plane(key, value)
        else:
            if self.right is None:
                self.right = Node(key, value)
            else:
                self.right.add_plane(key, value)

    def remove_plane(self, key, value):
        if key == self.key:
            if value in self.value:
                self.value.remove(value)
                if not self.value:
                    return self.remove()
        elif key < self.key and self.left is not None:
            self.left = self.left.remove_plane(key, value)
        elif key > self.key and self.right is not None:
            self.right = self.right.remove_plane(key, value)
        return self

    def lookup_plane(self, key, time):
        if key == self.key:
            if time in self.value:
                return f"{key} is scheduled at {time}"
            else:
                return f"{key} is not scheduled at {time}"
        elif key < self.key and self.left is not None:
            return self.left.lookup_plane(key, time)
        elif key > self.key and self.right is not None:
            return self.right.lookup_plane(key, time)
        return f"{key} is not scheduled at {time}"

    def remove(self):
        if self.left is None and self.right is None:
            return None
        elif self.left is None:
            return self.right
        elif self.right is None:
            return self.left
        else:
            successor = self.right
            while successor.left:
                successor = successor.left
            self.key = successor.key
            self.value = successor.value
            self.right = self.right.remove_plane(successor.key, successor.value[0])
        return self


class RunwayReserver:
    def __init__(self):
        self.root = None

    def add_plane(self, callsign, time):
        if self.root is None:
            self.root = Node(callsign, time)
        else:
            self.root.add_plane(callsign, time)

    def remove_plane(self, callsign, time):
        if self.root is not None:
            self.root = self.root.remove_plane(callsign, time)

    def lookup_plane(self, callsign, time):
        if self.root is not None:
            return self.root.lookup_plane(callsign, time)
        return f"{callsign} is not scheduled at {time}"

# sample usage
def main():
  # create a new RunwayReserver object
  r = RunwayReserver()
  
  # add a plane with callsign "AA123" at time 10
  r.add_plane("AA123", 10)
  
  # lookup plane "AA123" at time 10
  print(r.lookup_plane("AA123", 10))  # "AA123 is scheduled at 10"
  
  # remove plane "AA123" at time 10
  r.remove_plane("AA123", 10)
  
  # lookup plane "AA123" at time 10 after removing it
  print(r.lookup_plane("AA123", 10))  # "AA123 is not scheduled at 10"



if __name__ == "__main__":
  main()