#ifndef PLANE_H
#define PLANE_H

using namespace std;

class Plane
{
    public:
        /** Default constructor */
        Plane() {
            m_callsign = "No Callsign"; // shouldn't happen
        }
        /** parameter constructor */
        Plane(string callsign) {
            m_callsign = callsign;
            m_landingTime = 0;
        }
        /** Default destructor */
        ~Plane() {}

        /** Access m_landingTime
         * \return The current value of m_landingTime
         */
        double GetlandingTime() { return m_landingTime; }
        /** Set m_landingTime
         * \param val New value to set
         */
        void SetlandingTime(double val) {

            m_landingTime = val; }
        /** Access m_callsign
         * \return The current value of m_callsign
         */
        string Getcallsign() { return m_callsign; }
        /** Set m_callsign
         * \param val New value to set
         */
        void Setcallsign(string val) { m_callsign = val; }

    protected:

    private:
        double m_landingTime; //!< Member variable "m_landingTime"
        string m_callsign; //!< Member variable "m_callsign"
};

#endif // PLANE_H
