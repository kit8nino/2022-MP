#include <iostream>
#include "Maze.h"

// Для теста
//#include "Graph.h"
//void simpleGraphTest();

void enterTreasurePoint(Coord&);

int main() {
    Maze maze{"Maze.txt"};
    maze.buildGraph();

    Coord treasurePoint {-1, -1};
    enterTreasurePoint(treasurePoint);
    maze.setTreasurePoint(treasurePoint);

    std::vector<Coord> stot{};
    std::vector<Coord> ttoe{};
    maze.findRoute_stot(stot);
    maze.printRoute(stot, '.');
    maze.findRoute_ttoe(ttoe);
    maze.printRoute(ttoe, ',');
    maze.printToFile("MazeEdited.txt");

    // Для теста
    //simpleGraphTest();

    return 0;
}

void enterTreasurePoint(Coord& treasurePoint) {
    std::cout << "~Input the position of the treasure:\n";
    std::cout << "~Input posX: ";
    std::cin >> treasurePoint.x;
    std::cin.clear();
    std::cin.ignore();
    std::cout << "~Input posY: ";
    std::cin >> treasurePoint.y;
    std::cin.clear();
    std::cin.ignore();
}

/* Для теста
void simpleGraphTest() {
    Graph<int> graph;
    graph.addEdge(1, 2);
    graph.addEdge(1,3);
    graph.addEdge(2,4);
    graph.addEdge(2,5);
    graph.addEdge(3,6);
    graph.addEdge(3,7);
    graph.addEdge(4,8);
    graph.addEdge(5,2);
    graph.addEdge(5,6);
    graph.addEdge(5,9);
    graph.addEdge(5,10);

    std::vector<int> route{};

    graph.DFS(1, 6, route);
    std::cout << "DFS: ";
    for(int v : route) std::cout << v << ' ';
    std::cout << std::endl;

    route.clear();
    graph.BFS(1, 6, route);
    std::cout << "BFS: ";
    for(int v : route) std::cout << v << ' ';
    std::cout << std::endl;
}
*/