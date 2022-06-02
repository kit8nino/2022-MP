#include "../base_t.hpp"

#pragma once

namespace signal {

    namespace duration {

        class units {
        protected:
            int value;
        public:
            units(int c): value{c} {}

            virtual signal::sample count() const { return value; }
        }; 

    }

}