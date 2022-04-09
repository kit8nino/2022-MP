#include <fstream>
#include <iostream>
#include <array>

enum class direction: uint8_t {
    down, left,right, up, founded
};

direction operator ! (direction dir) {
    switch (dir) {
        case direction::down: return direction::up;
        case direction::left: return direction::right;
        case direction::right: return direction::left;
        case direction::up: return direction::down;
        default: throw("ERROR");
    }
}

using blocked_dirs = std::array<direction, 3>;

const int width = 128, height = 280, x = 0, y = 1, ways_count = 4;
char maze[height][width+1] = {};
    
const char file_name[] = "maze-for-u.txt", 
           wall = '#', pass = ' ', jewel = '*', to_jewel = '.', to_exit = ',';

using coordinates = int[2];
coordinates entry = {1,0}, escape = {width-1, height}, current_point = {entry[x], entry[y]};

bool down() { return maze[current_point[x]+1][current_point[y]] == pass; }
bool left() { return maze[current_point[x]][current_point[y]+1] == pass; }
bool right() { return maze[current_point[x]][current_point[y]-1] == pass; }
bool up() { return maze[current_point[x]-1][current_point[y]] == pass; }

bool jewel_chek() {
    return maze[current_point[x]+1][current_point[y]] == jewel ||
           maze[current_point[x]][current_point[y]+1] == jewel ||
           maze[current_point[x]][current_point[y]-1] == jewel ||
           maze[current_point[x]-1][current_point[y]] == jewel;
}

bool(* const direction_funcs[ways_count])() = {down, left, right, up};
const int directions[ways_count][2] = {{1, 0}, {0, 1}, {0, -1}, {-1, 0}};

direction check(blocked_dirs block) {
    for (int i = 0; i < ways_count; ++i) {
        for (auto blocked : block) { 
            if (i != int(blocked) && direction_funcs[i]()) return (direction)i;
        }
    }
    return !block.front();
}

direction depth(direction back) {
    blocked_dirs block = {!back};
    if (jewel_chek()) return direction::founded;

    for (int i = 1; i < 3; ++i) {
        direction dir = check(block);
        if (dir == back) return back;
        current_point[x] += directions[(int)dir][x];
        current_point[y] += directions[(int)dir][y];
        direction buf = depth(dir);
        if (buf == direction::founded) return direction::founded;
        else if (buf == back && i == 2) return back;
        else block[i] = buf;
    }/////////////////////////////////////////////////////////////////


}

int main() {
    std::ifstream maze_file(file_name);
    
    if (maze_file.is_open()) {
        for (auto line : maze) maze_file.getline(line, width+1);
    } else {
        std::cout << "File  " << file_name << "  not found" << std::endl;
        return 0;
    }
    
    maze_file.close();

    unsigned int a, b;
    do {
        std::cout << "Input jewel coordinates (x: 1 - 127, y: 1 - 279):\nx: ";
        std::cin >> a;
        std::cout << "y: "; std::cin >> b;
    } while ((maze[a-1][b] == wall && maze[a+1][b] == wall && maze[a][b-1] == wall && maze[a][b+1] == wall) ||
            a > width-1 || b > height-1);
    
    maze[a][b] = jewel;

    return 0;
}