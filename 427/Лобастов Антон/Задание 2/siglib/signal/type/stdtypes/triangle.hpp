#include "type/type.hpp"

namespace signal {

    class triangle: public type {
    public:
        triangle() {
            std::cout << "Треугольник" << std::endl;
        }
    };

}