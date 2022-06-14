#include "units.hpp"

namespace signal {

    namespace duration {

        class seconds: public units {
            int descrete;
        public:
            seconds(int c, int d) : units{c}, descrete{d} {}

            signal::sample count() const override { return value * descrete; }
        };

    }

}