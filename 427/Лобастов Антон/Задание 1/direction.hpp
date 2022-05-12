#include <cstdint>
#include <array>

#pragma once

const char wall = '#', pass = ' ', to_jewel = '.', to_exit = ',', to_jewel_and_to_exit = ';';

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
bool ch_down(T maze, coordinates &loc, const char pass) { return maze[loc[y]+1][loc[x]] == pass; }

template <typename T>
bool ch_left(T maze, coordinates &loc, const char pass) { return maze[loc[y]][loc[x]-1] == pass; }

template <typename T>
bool ch_right(T maze, coordinates &loc, const char pass) { return maze[loc[y]][loc[x]+1] == pass; }

template <typename T>
bool ch_up(T maze, coordinates &loc, const char pass) { return maze[loc[y]-1][loc[x]] == pass; }

const char jewel = '*';
template <typename T>
bool check_jewel(T maze, coordinates &loc) {
    return ch_down(maze, loc, jewel) || ch_left(maze, loc, jewel) || ch_right(maze, loc, jewel) || ch_up(maze, loc, jewel);
}

const int step[ways_count][2] = {{0, 1}, {-1, 0}, {1, 0}, {0, -1}};

void operator += (coordinates &coord, direction dir) {
    coord[x] += step[(int)dir][x];
    coord[y] += step[(int)dir][y];
}

coordinates operator + (const coordinates &coord, direction dir) {
    return coordinates{coord[x] + step[(int)dir][x], coord[y] + step[(int)dir][y]};
}

std::ostream& operator << (std::ostream &out, const coordinates &coord) {
    out << "x: " << coord[x] << ", y: " << coord[y];

    return out;
}