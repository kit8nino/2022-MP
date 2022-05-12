#include "direction.hpp"

const int width = 128, height = 280;
char maze[height][width+1] = {};

template <typename T>
direction depth(T maze, coordinates &loc, direction back) {
    loc += back;
    maze[loc[y]][loc[x]] = to_jewel;

    if (check_jewel(maze, loc)) return direction::founded;

    bool(* const check_way[ways_count])(T, coordinates&, const char) = {ch_down, ch_left, ch_right, ch_up};
    
    for (int i = 0; i < ways_count; ++i) {
        if (check_way[i](maze, loc, pass)) {
            auto way = (direction)i, res = depth(maze, loc, way);
            if (res == direction::founded) return direction::founded;
        }
    }

    maze[loc[y]][loc[x]] = pass;
    loc += !back;
    return back;
}