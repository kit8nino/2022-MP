#include "base/base_t.hpp"

namespace signal {

    class analyzer {
        sequence signal;
    public:
        analyzer(sequence sig) : signal{sig} {
            std::cout << "Создан анализатор сигнала" << std::endl;
        }

        void plot() {
            std::cout << "График сигнала" << std::endl;
        }
        void fourier_plot() {
            std::cout << "График спектра" << std::endl;
        }
        void reverse_fourier_plot() {
            std::cout << "Примерный график по обратному преобразованию Фурье" << std::endl;
        }

        void disperse() {
            std::cout << "Дисперсия" << std::endl;
        }
        void mean() {
            std::cout << "Среднее" << std::endl;
        }
        void median() {
            std::cout << "Медиана" << std::endl;
        }
        void min() {
            std::cout << "Минимум" << std::endl;
        }
        void max() {
            std::cout << "Максимум" << std::endl;
        }
        void span() {
            std::cout << "Размах" << std::endl;
        }
    };

}
