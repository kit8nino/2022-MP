#include "type/type.hpp"

namespace signal {

    class saw: public type {
    public:
        saw() {
            std::cout << "Пила" << std::endl;
        }
    };

}