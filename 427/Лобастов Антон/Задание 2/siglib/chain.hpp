#include "iout.hpp"

class chain: public iout {
    signal::sequence input, output;

public:
    chain(signal::sequence in) {
        std::cout << "Создана цепь" << std::endl;
    }

    void bypass() {
        std::cout << "Проход сигнала юез изменений" << std::endl;
    }
    void Butterworth() {
        std::cout << "Фильтр Беттерворта" << std::endl;
    }

    void push(signal::sample s) {
        std::cout << "Добавлено новое значение сигнала" << std::endl;
    }

    void push(signal::sequence s) {
        std::cout << "Добавлена новая выборка сигнала" << std::endl;
    }
};