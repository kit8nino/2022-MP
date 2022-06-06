cmake_minimum_required(VERSION 3.20)
project(MazeAlgo)

set(CMAKE_CXX_STANDARD 20)

add_executable(MazeAlgo main.cpp Graph.h Maze.cpp Maze.h)
