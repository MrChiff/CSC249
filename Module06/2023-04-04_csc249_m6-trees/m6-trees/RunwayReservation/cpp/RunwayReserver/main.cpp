#include <iostream>
#include "Plane.h"
#include "RunwayReserver.h"


using namespace std;

int main()
{
    cout << "Welcome to the Runway Reservation System" << endl;

    RunwayReserver rrs = RunwayReserver();
    Plane myPlane = Plane("N12345");
    double t = 10.0; // landing time
    cout << "adding " << myPlane.Getcallsign() << " at time=" << t << endl;
    bool result = rrs.add(myPlane, t);
    cout << "add result = " << result << endl;

    cout << endl;
    cout << "Lookup of t=" << t << ":";
    Plane* p = rrs.lookup(t);
    if (p != nullptr) {
        cout << p->Getcallsign() << endl;
    } else {
        cout << "Not found" << endl;
    }

    return 0;
}
