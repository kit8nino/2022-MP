#include <queue>
#include <list>
#include <tuple>
#include <set>
#include "direction.hpp"

typedef std::pair<coordinates, coordinates> parent_child;
typedef std::list<parent_child> nodes;

template <typename T, typename V>
void set_char(T maze, V coord) {
    if (maze[coord[y]][coord[x]] == to_jewel)
        maze[coord[y]][coord[x]] = to_jewel_and_to_exit;
    else maze[coord[y]][coord[x]] = to_exit;
}

template <typename T>
int breadth(T maze, const coordinates &start, const coordinates &exit) {
    bool(* const check_way[ways_count])(T, coordinates&, const char) = {ch_down, ch_left, ch_right, ch_up};
    nodes queue{{start, start}};
    // queue.push({start, start});
    std::set<coordinates> checked{};

    auto i = queue.begin();
    while (true) {
        if (i == queue.end()) return -1;

        checked.insert(i->second);
        if (i->second == exit) break;
        
        for (int j = 0; j < ways_count; ++j) {
            auto new_node = i->second + (direction)j;
            if ((check_way[j](maze, i->second, pass) || check_way[j](maze, i->second, to_jewel)) && !checked.contains(new_node)) {
                
                queue.push_back({i->second, new_node});
            }
            
        }
        ++i;
    }
    
    set_char(maze, i->first);
    set_char(maze, i->second);
    int length = 2;
    auto buf = i->first;
    for (; i != queue.begin(); --i) {
        if (i->second == buf) {
            set_char(maze, i->first);
            buf = i->first;
            ++length;
        }
    }

    return length;
}