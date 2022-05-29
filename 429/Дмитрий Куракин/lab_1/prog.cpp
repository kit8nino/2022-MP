#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <stack>
#include <queue>
#include "windows.h"

#define FOREGROUND_WHITE (FOREGROUND_RED | FOREGROUND_BLUE | FOREGROUND_GREEN)
#define FOREGROUND_YELLOW (FOREGROUND_BLUE | FOREGROUND_GREEN)

using namespace std;

struct Edge {
    int begin;
    int end;
};

int main()
{
    vector<vector<int>> vectorMaze;
    int col = 0, row = 0;

    int mazeWidth = 0, mazeHeight = 0;
    string tempStr;

    // ---[Window resizing]---
    system("mode con cols=130"); // system("mode con cols=130 lines=75");

    // ---[Getting size of maze]---
    ifstream inputMazeTxt("C:\\Users\\dmitr\\Documents\\FILES\\Study\\maze-for-u.txt");
    if (inputMazeTxt.is_open())
    {
        getline(inputMazeTxt, tempStr);
        mazeWidth = tempStr.length();
        inputMazeTxt.seekg(0); // Back to 0 string of file

        while (!inputMazeTxt.eof())
        {
            getline(inputMazeTxt, tempStr);
            mazeHeight++;
        }
    }
    inputMazeTxt.seekg(0);

    // ---[vectorMaze resizing]---
    vectorMaze.resize(mazeHeight);
    for (int i = 0; i < mazeHeight; ++i)
        vectorMaze[i].resize(mazeWidth);

    // ---[Vector filling]---
    int numOfNodes = 0;
    while (!inputMazeTxt.eof())
    {
        getline(inputMazeTxt, tempStr);
        for (col = 0; col < mazeWidth; col++)
        {
            if (tempStr[col] == ' ')
            {
                vectorMaze[row][col] = numOfNodes;
                numOfNodes++;
            }
            else
            {
                vectorMaze[row][col] = -1;
            }
        }

        row++;
    }
    inputMazeTxt.close();


    // ---[Treasure position]---
    int letsGoFlag = 0;
    int treasureX = -1, treasureY = -1;
    while (letsGoFlag != 3)
    {
        treasureX = -1;
        treasureY = -1;
        std::cout << "Enter the position of treasure (range X: (0; " << (mazeWidth - 1) << "); range Y: (0; " << (mazeHeight - 1) << ") : " << endl;

        while ((treasureX < 0) || (treasureX >= mazeWidth))
        {
            std::cout << "X: ";
            std::cin >> treasureX;
        }
        while ((treasureY < 0) || (treasureY >= mazeHeight))
        {
            std::cout << "Y: ";
            std::cin >> treasureY;
        }

        if (vectorMaze[treasureY][treasureX] == -1)
        {
            std::cout << "This cell is already occupied. Choose another one!" << endl << endl;
        }
        else
        {
            letsGoFlag = 3;
        }
    }

    int treasureNode = vectorMaze[treasureY][treasureX];


    // ---[Сonstruction of the adjacency matrix]---
    vector<vector<int>> vectorAdjMatr;

    int researcherX = 0, researcherY = 0;

    // vectorAdjMatr resizing
    vectorAdjMatr.resize(numOfNodes);
    for (int i = 0; i < numOfNodes; ++i)
        vectorAdjMatr[i].resize(numOfNodes);

    // Filling vectorAdjMatr's diagonal with zeros
    for (int i = 0; i < numOfNodes; i++)
    {
        vectorAdjMatr[i][i] = 0;
    }

    // Filling vectorAdjMatr
    for (int k = 0; k < numOfNodes; k++)
    {
        for (int i = 0; i < mazeHeight; i++)
        {
            for (int j = 0; j < mazeWidth; j++)
            {
                if (vectorMaze[i][j] == k)
                {
                    if (((i - 1) >= 0) && (vectorMaze[i - 1][j] != -1)) // Bottom
                    {
                        vectorAdjMatr[k][vectorMaze[i - 1][j]] = 1;
                        vectorAdjMatr[vectorMaze[i - 1][j]][k] = 1;
                    }

                    if (((i + 1) <= (mazeHeight - 1)) && vectorMaze[i + 1][j] != -1) // Top
                    {
                        vectorAdjMatr[k][vectorMaze[i + 1][j]] = 1;
                        vectorAdjMatr[vectorMaze[i + 1][j]][k] = 1;
                    }

                    if (((j - 1) >= 0) && (vectorMaze[i][j - 1] != -1)) // Left
                    {
                        vectorAdjMatr[k][vectorMaze[i][j - 1]] = 1;
                        vectorAdjMatr[vectorMaze[i][j - 1]][k] = 1;
                    }

                    if (((j + 1) <= (mazeWidth - 1)) && (vectorMaze[i][j + 1] != -1)) // Right
                    {
                        vectorAdjMatr[k][vectorMaze[i][j + 1]] = 1;
                        vectorAdjMatr[vectorMaze[i][j + 1]][k] = 1;
                    }
                }
            }
        }
    }

    // ---[Depth-first search]---
    stack<int> Stack;
    stack<Edge> Edges;
    int req;
    Edge e;
    vector<int> nodes(numOfNodes);
    vector<int> wayToTreasure;

    for (int i = 0; i < numOfNodes; i++) // Initially, all nodes are equal to zero
    {
        nodes[i] = 0;
    }

    req = treasureNode;

    Stack.push(0); // Put the first node in the queue
    while (!Stack.empty())
    {
        int node = Stack.top();
        Stack.pop();
        if (nodes[node] == 2) continue;
        nodes[node] = 2;

        for (int j = (numOfNodes - 1); j >= 0; j--)
        {
            if (vectorAdjMatr[node][j] == 1 && nodes[j] != 2)
            {
                Stack.push(j);
                nodes[j] = 1;
                e.begin = node; e.end = j;
                Edges.push(e);
                if (node == req) break;
            }
        }
    }
    //std::cout << "Way to TREASURE node:" << req << endl;
    //std::cout << req;
    while (!Edges.empty())
    {
        e = Edges.top();
        Edges.pop();
        if (e.end == req)
        {
            req = e.begin;
            //std::cout << " <- " << req;

            for (int i = 0; i < mazeHeight; i++)
            {
                for (int j = 0; j < mazeWidth; j++)
                {
                    if (vectorMaze[i][j] == req)
                    {
                        wayToTreasure.push_back(vectorMaze[i][j]);
                    }
                }
            }
        }
    }

    // ---[Breadth first search]---
    queue<int> Queue;
    vector<int> wayFromTreasure;

    for (int i = 0; i < numOfNodes; i++) // Initially, all nodes are equal to zero
    {
        nodes[i] = 0;
    }

    req = numOfNodes - 1;

    Queue.push(treasureNode);
    while (!Queue.empty())
    {
        int node = Queue.front();
        Queue.pop();
        nodes[node] = 2;
        for (int j = 0; j < numOfNodes; j++)
        {
            if (vectorAdjMatr[node][j] == 1 && nodes[j] == 0)
            {
                Queue.push(j);
                nodes[j] = 1;
                e.begin = node; e.end = j;
                Edges.push(e);
                if (node == req) break;
            }
        }
    }

    //std::cout << "Way to EXIT node:" << req << endl;
    //std::cout << req;
    while (!Edges.empty())
    {
        e = Edges.top();
        Edges.pop();
        if (e.end == req) {
            req = e.begin;
            //std::cout << " <- " << req;

            for (int i = 0; i < mazeHeight; i++)
            {
                for (int j = 0; j < mazeWidth; j++)
                {
                    if ((vectorMaze[i][j] == req) && (vectorMaze[i][j] != treasureNode))
                    {
                        wayFromTreasure.push_back(vectorMaze[i][j]);
                    }
                }
            }
        }
    }

    // ---[Output]---

    // Console output
    std::cout << endl;
    HANDLE hwnd = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hwnd, FOREGROUND_WHITE);
    int outputRoadFlag;
    for (int i = 0; i < mazeHeight; i++)
    {
        for (int j = 0; j < mazeWidth; j++)
        {
            outputRoadFlag = 1;

            // Way to/from treasure coloring
            for (int k = 0; k < wayToTreasure.size(); k++)
            {
                for (int f = 0; f < wayFromTreasure.size(); f++)
                {
                    if ((vectorMaze[i][j] == wayToTreasure[k]) && (vectorMaze[i][j] == wayFromTreasure[f]))
                    {
                        SetConsoleTextAttribute(hwnd, FOREGROUND_YELLOW | FOREGROUND_INTENSITY);
                        std::cout << ';';
                        SetConsoleTextAttribute(hwnd, FOREGROUND_WHITE);
                        outputRoadFlag = 2;
                        break;
                    }
                }
            }

            // Way to treasure coloring
            for (int k = 0; k < wayToTreasure.size(); k++)
            {
                if ((vectorMaze[i][j] == wayToTreasure[k]) && (outputRoadFlag != 2))
                {
                    SetConsoleTextAttribute(hwnd, FOREGROUND_GREEN | FOREGROUND_INTENSITY);
                    std::cout << '.';
                    SetConsoleTextAttribute(hwnd, FOREGROUND_WHITE);
                    outputRoadFlag = 0;
                    break;
                }
            }

            // Way from treasure coloring
            for (int f = 0; f < wayFromTreasure.size(); f++)
            {
                if ((vectorMaze[i][j] == wayFromTreasure[f]) && (outputRoadFlag != 2))
                {
                    SetConsoleTextAttribute(hwnd, FOREGROUND_BLUE | FOREGROUND_INTENSITY);
                    std::cout << ',';
                    SetConsoleTextAttribute(hwnd, FOREGROUND_WHITE);
                    outputRoadFlag = 0;
                    break;
                }
            }

            // Wall
            if (vectorMaze[i][j] == -1)
            {
                std::cout << '#';
                continue;
            }

            // Treasure
            if (vectorMaze[i][j] == treasureNode)
            {
                SetConsoleTextAttribute(hwnd, FOREGROUND_RED | FOREGROUND_INTENSITY); // Treasure coloring
                std::cout << '*';
                SetConsoleTextAttribute(hwnd, FOREGROUND_WHITE);
                continue;
            }

            // Exit
            if (vectorMaze[i][j] == (numOfNodes - 1))
            {
                SetConsoleTextAttribute(hwnd, FOREGROUND_BLUE | FOREGROUND_INTENSITY); // Exit coloring
                std::cout << ',';
                SetConsoleTextAttribute(hwnd, FOREGROUND_WHITE);
                continue;
            }

            // Road
            if (outputRoadFlag == 1)
            {
                std::cout << ' ';
            }
        }

        std::cout << endl;
    }

    std::cout << endl;
    std::cout << "Number of nodes: " << numOfNodes << endl;
    std::cout << "Treasure node: " << treasureNode << endl;
    std::cout << "The length of the exit path: " << (wayFromTreasure.size() + 1) << endl;

    // vectorAdjMatr output
    /*for (int i = 0; i < numOfNodes; i++)
    {
        for (int j = 0; j < numOfNodes; j++)
        {
            std::cout << vectorAdjMatr[i][j] << " ";
        }
        std::cout << endl;
    }*/


    // TXT output
    tempStr = "";
    std::ofstream outputMazeTxt;
    outputMazeTxt.open("C:\\Users\\dmitr\\Documents\\FILES\\Study\\maze-for-me-done.txt");
    if (outputMazeTxt.is_open())
    {
        int outputRoadFlag;
        for (int i = 0; i < mazeHeight; i++)
        {
            for (int j = 0; j < mazeWidth; j++)
            {
                outputRoadFlag = 1;

                // Way to/from treasure coloring
                for (int k = 0; k < wayToTreasure.size(); k++)
                {
                    for (int f = 0; f < wayFromTreasure.size(); f++)
                    {
                        if ((vectorMaze[i][j] == wayToTreasure[k]) && (vectorMaze[i][j] == wayFromTreasure[f]))
                        {
                            tempStr = tempStr + ';';
                            outputRoadFlag = 2;
                            break;
                        }
                    }
                }

                // Way to treasure coloring
                for (int k = 0; k < wayToTreasure.size(); k++)
                {
                    if ((vectorMaze[i][j] == wayToTreasure[k]) && (outputRoadFlag != 2))
                    {
                        tempStr = tempStr + '.';
                        outputRoadFlag = 0;
                        break;
                    }
                }

                // Way from treasure coloring
                for (int f = 0; f < wayFromTreasure.size(); f++)
                {
                    if ((vectorMaze[i][j] == wayFromTreasure[f]) && (outputRoadFlag != 2))
                    {
                        tempStr = tempStr + ',';
                        outputRoadFlag = 0;
                        break;
                    }
                }

                // Wall
                if (vectorMaze[i][j] == -1)
                {
                    tempStr = tempStr + '#';
                    continue;
                }

                // Treasure
                if (vectorMaze[i][j] == treasureNode)
                {
                    tempStr = tempStr + '*';
                    continue;
                }

                // Exit
                if (vectorMaze[i][j] == (numOfNodes - 1))
                {
                    tempStr = tempStr + ',';
                    continue;
                }

                // Road
                if (outputRoadFlag == 1)
                {
                    tempStr = tempStr + ' ';
                }
            }

            outputMazeTxt << tempStr << endl;
            tempStr = "";
        }
    }
    outputMazeTxt.close();

    return 0;
}