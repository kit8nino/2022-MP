#include <cstdint>
#include <array>

enum class direction: uint8_t {
    down, left, right, up, founded, not_found
};

direction operator ! (direction dir) {
    if ((int)dir < (int)direction::founded) return (direction)((~(uint8_t)dir) & 03);
    else throw "ERROR";
}

enum axis {
    x, y
};

const int ways_count = 4;

typedef std::array<int, 2> coordinates;

template <typename T>
bool ch_down(T maze, coordinates &loc, const char pass) { return maze[loc[x]+1][loc[y]] == pass; }

template <typename T>
bool ch_left(T maze, coordinates &loc, const char pass) { return maze[loc[x]][loc[y]+1] == pass; }

template <typename T>
bool ch_right(T maze, coordinates &loc, const char pass) { return maze[loc[x]][loc[y]-1] == pass; }

template <typename T>
bool ch_up(T maze, coordinates &loc, const char pass) { return maze[loc[x]-1][loc[y]] == pass; }

template <typename T>
direction check(T maze, coordinates &loc, const char pass) {
    if (ch_down(maze, loc, pass)) return direction::down;
    if (ch_right(maze, loc, pass)) return direction::right;
    if (ch_left(maze, loc, pass)) return direction::left;
    if (ch_up(maze, loc, pass)) return direction::up;
    else return direction::not_found;
}

const int step[ways_count][2] = {{1, 0}, {0, 1}, {0, -1}, {-1, 0}};

void operator += (coordinates &coord, direction dir) {
    coord[x] += step[(int)dir][x];
    coord[y] += step[(int)dir][y];
}