#ifndef RUNWAYRESERVER_H
#define RUNWAYRESERVER_H
#import <vector>
#import <algorithm>     // for sort()
using namespace std;



/*
RunwayReserver is the main entry point to the Runway Reservation System.
Our aim is to implement the same interface with multiple data structures
to compare and contrast.

v1 will ignore inheritance for now, but we will later want to look at
subclassing a virtual RRS with for example VectorRRS, BSTRRS, etc.

we are treating time as a double -- presumably it is in minutes.
*/
class RunwayReserver
{
    static const bool DEBUG = false; //true;
    public:
        /** Default constructor */
        RunwayReserver() {
            // internal storage is m_planes

            // default landing window k is 3.0 minutes
            m_landingWindow = 3.0;
        }
        /** Default destructor */
        ~RunwayReserver() {
        }

        /** Access m_landingWindow
         * \return The current value of m_landingWindow
         */
        double getTime() { return m_landingWindow; }
        /** Set m_landingWindow
         * \param val New value to set
         */
        void setTime(double val) {
            if (val > 0) {
                    m_landingWindow = val;
            }
        }

        // Defined interface of a RRS -- add plane, delete plane, lookup plane
        bool add(Plane p, double t) {
            // add plane p in order at time t
            // return true if successful, false otherwise
            // add plane to our internal vector
            if (DEBUG) { cout <<"adding "<< p.getCallsign()<<" at t="<<t<<endl;}
            p.setTime(t);
            m_planes.push_back(p); // inserts a copy of p into m_planes
            // if the insert fails, we should reset plane's time to 0
            // (but if it fails, it's not copied)

            // sort the vector
            sort(m_planes.begin(), m_planes.end());

            // in debug mode, check RI each time
            if (DEBUG) {
                bool check = checkRI();
                if (!check) {
                    cout << "Error: Representational Invariant is FALSE" << endl;
                    // NOTE: planes' landing time is possibly invalid!
                    return false;
                }
            }

            return true;
        }

        bool remove(double t) {
            // remove plane at time t
            // return true if successful, false otherwise
            // Last, if remove succeeds, set plane's internal time to 0
            // if p exists, p.SetLandingTime(0)
            // this is not necessary, as the removed plane is disposed of
            for (int i=0; i < m_planes.size(); i++) {
                if (m_planes[i].getTime() == t) {
                    // item i is found at vector.begin() + index
                    m_planes.erase(m_planes.begin() + i);
                    return true; // successful remove
                }
            }
            /*
            for (Plane p: m_planes) {
                if (p.getTime() == t) {
                    if (DEBUG) {cout << "Removing plane at t=" << t << endl;}
                    m_planes.remove(m_planes.begin(), m_planes_end(), p);
                }

            }
            */
            return false; // not found
        }

        Plane lookup(double t) {
            // find plane at time t if it exists, nullptr otherwise
            // TODO: this is not working, the time check fails
            for (auto plane: m_planes) {
                if (DEBUG) {
                    cout << "Checking plane: " << plane.getCallsign() << " at " << plane.getTime() << endl;
                }
                if (plane.getTime() == t) {
                    if (DEBUG) {
                        cout << "plane " << plane.getCallsign() << " found at t=" << t << endl;
                    }
                    return plane; // should this be a reference?
                }
            }
            // didn't find anything
            if (DEBUG) { cout << "lookup failed, nothing at t=" << t << endl;}
            return Plane(); // not found -- this isn't ideal
        }

        // listPlanes() -- print each plane in order
        void listPlanes() {
            cout << "Landing Queue:" << endl;
            if (m_planes.size() == 0) {
                cout << "No planes scheduled to land." << endl;
                return;
            }
            // "Rank" is order the plane has in the landing queue
            // first plane is rank 1, etc.
            int rank = 1;
            for (Plane plane: m_planes) {
                cout << "Rank #" << rank << ": " << plane.getCallsign();
                cout << " landing at t=" << plane.getTime() << endl;
                rank++;
            }
            cout << "End of landing queue." << endl;
            return;
        }


    protected:

    private:
        unsigned int m_landingWindow; //!< Member variable "m_landingWindow"
        vector<Plane> m_planes; // internal storage
        bool checkRI() {
            // Check Representational Invariant
            // (assert that the data structure is still valid)
            // when debugging, we should do this after every update (add/remove)
            // check that each plane in order has an increasing time
            // TODO: This is NOT the k window check!
            double last_time = 0.0;
            for (auto plane : m_planes) {
                double current_time = plane.getTime();
                if (DEBUG) {
                    cout << plane.getCallsign() << " " << current_time << endl;
                }

                if (current_time < last_time) {
                    cout << "RI invalid -- planes not sorted" << endl;
                    return false;
                } else {
                    last_time = current_time;
                }
            }

            return true;
        }
};

#endif // RUNWAYRESERVER_H
