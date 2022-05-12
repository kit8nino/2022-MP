#include <fstream>
#include <iostream>
#include "depth.hpp"
#include "breadth.hpp"
    
const char file_name[] = "maze-for-u.txt", maze_done[] = "maze-for-me-done.txt";

coordinates entry = {1,0}, escape = {width-2, height-1}, location = {entry[x], entry[y]};

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
    
    maze[b][a] = jewel;

    auto first_step = direction::down;
    maze[location[y]][location[x]] = to_jewel;
    auto search_result = depth(maze, location, first_step);
    
    if (search_result == first_step) {
        std::cout << "Jewel not found" << std::endl;
        return 0;
    } else if (search_result == direction::founded) std::cout << "Jewel founded." << std::endl;
    else throw "FINDING ERROR";

    int path_len = breadth(maze, location, escape);
    if (path_len+1) std::cout << "Escape founded.\n\t Length of shortest path to escape: " << path_len << std::endl;
    else {
        std::cout << "Escape not found" << std::endl;
        return 0;
    }

    std::ofstream maze_done_file(maze_done);
    if (!maze_done_file.is_open()) {
        std::cout << "File  " << maze_done << "  not found" << std::endl;
        return 0;
    }

    for (auto line : maze) maze_done_file << line << '\n';

    maze_done_file.close();

    return 0;
}