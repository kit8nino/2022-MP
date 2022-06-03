#include <functional>
#include "units.hpp"

    class iout {
    protected:
        int counter, duration;
        std::function<int(int)> rule;
        signal::sequence *out;
    public:

        signal::sequence operator () (signal::duration::units n) {
            std::cout << "Возвращена выборка" << std::endl;
            return {};
        }

        signal::sample next() {
            std::cout << "Возвращено следующее значение сигнала" << std::endl;
            return {};
        }
    };