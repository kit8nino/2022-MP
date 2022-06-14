#include "simple.hpp"

namespace signal {

    namespace generate {

        class amplitude_modular: simple { 
            sequence envelope;
            int env_frequency;

        public:
            
            amplitude_modular(type *t, int per, int sam, int amp, duration::units s, sequence env) : simple{t, per, sam, amp, s}, envelope{env} {
                std::cout << "Создан генератор амплитудно-модулированного сигнала" << std::endl;
            }

            void set_frequency(int v) {
                std::cout << "Задана частота огибающей" << std::endl;
            }
        };

    }
    
}