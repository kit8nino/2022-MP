#include <fstream>
#include <iostream>
#include <array>
#include "depth.hpp"

using blocked_dirs = std::array<direction, 3>;

const int width = 128, height = 280;
char maze[height][width+1] = {};
    
const char file_name[] = "maze-for-u.txt";

coordinates entry = {1,0}, escape = {width-1, height}, location = {entry[x], entry[y]};



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