#include <functional>

#pragma once

namespace signal {

    class type {
    protected:
        std::function<int(int)> rule;
    public:
        auto get_rule() const {
            return rule;
        }
    };

}