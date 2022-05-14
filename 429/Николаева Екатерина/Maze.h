#pragma once
#include <string>
#include <vector>
#include "Graph.h"

struct Coord {
    int x, y;

    bool operator<(const Coord& c2) const {
        if(y < c2.y) return true;
        else if(y == c2.y) {
            if(x < c2.x) return true;
            else return false;
        }
        else return false;
    }
    bool operator==(const Coord& c2) const {
        if(c2.x == x && c2.y == y) return true;
        else return false;
    }
};

class Maze {
private:
    std::vector<std::string> mazeArr;
    Graph<Coord> graph;         //разворачиваем шаблон графа для Coord
    Coord startPoint, endPoint, treasurePoint;

    void readFile(const std::string&);
    void findStartPoint();
    void findEndPoint();
public:
    Maze(const std::string&);
    void setTreasurePoint(const Coord&, const char symbol = '*');
    void buildGraph();                                   
    void findRoute_stot(std::vector<Coord>&);           
    void findRoute_ttoe(std::vector<Coord>&);           
    void printRoute(std::vector<Coord>&, const char);
    void printToFile(const std::string&) const;
};

