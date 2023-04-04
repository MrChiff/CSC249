# RunwayReservationSystem
# Python implementation
# v1 - by ChatGPT 4/4/23 (ChatGPT v. March 23)
class RunwayReserver:
    def __init__(self):
        self.reservations = {}

    def add_plane(self, callsign, time):
        if time not in self.reservations:
            self.reservations[time] = []
        self.reservations[time].append(callsign)

    def remove_plane(self, callsign, time):
        if time in self.reservations and callsign in self.reservations[time]:
            self.reservations[time].remove(callsign)

    def lookup_plane(self, callsign, time):
        if time in self.reservations and callsign in self.reservations[time]:
            return f"{callsign} is scheduled at {time}"
        return f"{callsign} is not scheduled at {time}"

# sample usage by ChatGPT
def main():
  # create a new RunwayReserver object
  r = RunwayReserver()
  
  # add a plane with callsign "AA123" at time 10
  r.add_plane("AA123", 10.0)
  
  # lookup plane "AA123" at time 10
  print(r.lookup_plane("AA123", 10.0))  # "AA123 is scheduled at 10"
  
  # remove plane "AA123" at time 10
  r.remove_plane("AA123", 10.0)
  
  # lookup plane "AA123" at time 10 after removing it
  print(r.lookup_plane("AA123", 10.0))  # "AA123 is not scheduled at 10"

if __name__ == "__main__":
  main()