#include <list>
#include "direction.hpp"

typedef std::list<direction> list_dirs;

const char wall = '#', pass = ' ', jewel = '*', to_jewel = '.', to_exit = ',';

template <typename T>
direction depth(T maze, coordinates &loc, direction back) {
    loc += !back;

    auto jewel_dir = check(maze, loc, jewel);
    if (jewel_dir != direction::not_found) return direction::founded;

    bool(* const checks[ways_count])(T, coordinates&, direction) = {ch_down, ch_left, ch_right, ch_up};
    list_dirs blocked{back};
    
    for (int i = 0; i < ways_count; ++i) {
        if (i != (int)back && checks[i]) {
            auto res = depth(maze, loc, !((direction)i));
            if (res == (direction)i) {
                if (blocked.size() == ways_count) return !back;
                else blocked.push_back(res);
            } else if (res == direction::founded) {
                maze[loc[x]][loc[y]] = to_jewel;
                loc += back;
                return res;
            }
        } 
    }
    
}