#include "units.hpp"

namespace signal {

    namespace duration {

        class samples: public units {
        public:
            samples(int c) : units{c} {}
        };

    }

}