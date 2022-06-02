#include "generator.hpp"
#include "type/type.hpp"

namespace signal {

    namespace generate {

        class simple {
        public:
            generator generate;
            
            simple(type *t, int per, int sam, int amp, duration::units s) {
                std::cout << "Создан генератор простых сигналов" << std::endl;
            }

        };

    }
    
}