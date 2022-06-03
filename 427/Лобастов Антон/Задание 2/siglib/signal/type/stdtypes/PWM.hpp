#include "type/type.hpp"

namespace signal {

    class PWM: public type {
        int duty_cycle;
        public:
        PWM(int dc) : duty_cycle{dc} {
            std::cout << "ШИМ со скважностью: " << duty_cycle << std::endl;
        }
    };

}