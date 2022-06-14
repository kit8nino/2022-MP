#include "type/type.hpp"

namespace signal {

    class harmonic: public type {
    public:
        harmonic() {
            std::cout << "Гармонический сигнал" << std::endl;
        }
    };

}