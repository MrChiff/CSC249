#include <iostream>
#include "Plane.h"
#include "RunwayReserver.h"


using namespace std;

int main()
{
    cout << "Welcome to the Runway Reservation System" << endl;

    RunwayReserver rrs = RunwayReserver();

    // should list empty landing queue
    rrs.listPlanes();

    // create a plane and add it
    Plane myPlane = Plane("N12345");
    double t = 10.0; // landing time
    cout << "adding " << myPlane.getCallsign() << " at time=" << t << endl;
    bool result = rrs.add(myPlane, t);
    cout << "add result = " << result << endl;

    cout << endl;
    cout << "Lookup of t=" << t << ":";
    Plane p = rrs.lookup(t);
    //cout << p->getCallsign() << endl;
    if (p.getTime() != 0) {
        cout << "Found: " << p.getCallsign() << " at time=" << p.getTime() << endl;
    } else {
        cout << "Not found" << endl;
    }

    // add another plane
    Plane plane2 = Plane("N23456");
    Plane plane3 = Plane("AA445");
    rrs.add(plane2, 15);
    rrs.add(plane3, 7);

    // list all planes
    rrs.listPlanes();

    // remove a plane
    result = rrs.remove(15); // should succeed
    result = rrs.remove(16); // should fail

    rrs.listPlanes();

    return 0;
}
