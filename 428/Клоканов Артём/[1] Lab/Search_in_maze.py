#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


file_maze = open('maze-for-u.txt', 'r')
maze = file_maze.readlines()
file_maze.close()
maze = [maze_line.rstrip() for maze_line in maze]
maze_list = list(maze)

max_x, max_y = len(maze[0]), len(maze) # размеры
start_point=[maze[0].find(' '),0] # вход
exit_point=[maze[len(maze)-1].find(' '),len(maze)-1] # выход
    
POSSIBLE_WAYS = ['U', 'D', 'R', 'L']

# функции движения в лабиринте

def step(coord, direction):
    if direction == 'N':
         return step_N(coord)
    elif direction == 'S':
         return step_S(coord)
    elif direction == 'E':
         return step_E(coord)
    elif direction == 'W':
         return step_W(coord)

def step_N(coord):
    return [coord[0]-1, coord[1]] #вверх

def step_E(coord):
    return [coord[0], coord[1]+1] #вправо

def step_S(coord):
    return [coord[0]+1, coord[1]] #вниз

def step_W(coord):
    return [coord[0], coord[1]-1] #влево

def cut_way_back(direction): # убирает возможность вернуться назад
    
    if direction == 'N':
        return ('N', 'E', 'W')

    if direction == 'S':
        return ('S', 'E', 'W')

    if direction == 'E':
        return ('N', 'E', 'S')

    if direction == 'W':
        return ('N', 'S', 'W')

# функции проверки координат и изменения символов

def change_the_symbol(maze_list, coord, symbol): # изменение символа в строке
    maze_row = list(maze_list[coord[1]])
    maze_row[coord[0]] = symbol
    maze_list[coord[1]] = ''.join(maze_row)
    
def get_the_symbol(maze, i): # поиск пустого символа в строке
    return [maze[i].find(" "), i]

def is_coord_in_maze(maze, coord):
    if coord[0]<0 or coord[0]>len(maze[0])-1:
        return False
    if coord[1]<0 or coord[1]>len(maze)-1:
        return False
    return True

def is_coord_exit(coord):
    if coord[1]>len(maze)-2:
        return True
    return False

def is_coord_treasure(coord): # проверка местонахождения сокровища
    global treasure_is_here
    if coord[1] == treasure_is_here[1] and        coord[0] == treasure_is_here[0]:
        return True
    return False

def is_path_clean(maze, coord): # путь свободен?
    if maze[coord[1]][coord[0]] == '#':
        return False
    return True

# функции поиска и записи пути

def mark_the_path(maze_list, coord, path_to_exit): # нарисовать путь в файле
    for i in path_to_exit:
        change_the_symbol(maze_list, coord, '.') # проставление точек на всем маршруте
        coord = step(coord, i) # поиск следующей координаты

def find_a_way(maze, coord, possible_ways):
    global path_to_exit, current_path
    
    if not is_coord_in_maze(maze, coord):
        return
    
    if is_coord_exit(coord):
        return
    
    if is_coord_treasure(coord):
        path_to_exit = current_path.copy()
        return
    
    if len(current_path) > len(path_to_exit): # проверка на длину
        return
    
    for direction in possible_ways:
        if is_path_clean(maze, step(coord, direction)):
            current_path.append(direction)
            find_a_way(maze, step(coord, direction), cut_way_back(direction))
            current_path.pop()
    return
    
prev_coord = [[-1 for j in range(max_x)] for i in range(max_y)]
def find_the_exit(treasure_is_here, exit_point):
    iteration = []
    iteration.append(treasure_is_here)
    prev_coord[treasure_is_here[1]][treasure_is_here[0]] = 0
    while iteration:
        first_element = iteration.pop(0)
        for i in [[-1, 0],[1, 0],[0, -1],[0, 1]]:
            x = first_element[0] + i[0]
            y = first_element[1] + i[1]
            if (x < 0 or x >= max_x or y < 0 or y >= max_y):
                continue
            if (maze[y][x] == " " and prev_coord[y][x] == -1):
                prev_coord[y][x] = [first_element[0],first_element[1]]
                iteration.append([x, y]) 
    x = exit_point[0]
    y = exit_point[1]  
    while prev_coord[y][x] != 0:
        change_the_symbol(maze_list, [x, y], ',')
        temp_x = prev_coord[y][x][0]
        temp_y = prev_coord[y][x][1]
        x, y = temp_x, temp_y




# Программный код

x=0 
y=0       
while (is_path_clean(maze,[x,y])==False): # проверка координат сокровища
    x = int(input(f'Where is threasure? (x is between 0 and {max_x-1}) '))
    y = int(input(f'Where is threasure? (y is between 0 and {max_y-1}) '))
    print('Treasure is in the wall! Try again.')
treasure_is_here=[x,y]
change_the_symbol(maze_list, treasure_is_here, '*')

path_to_exit = []
for i in range(len(maze)*len(maze[0])):
    path_to_exit.append(' ')
current_path = []

change_the_symbol(maze_list, treasure_is_here, '*') # помечаем сокровище

find_a_way(maze, start_point, POSSIBLE_WAYS)

mark_the_path(maze_list, start_point, path_to_exit)

find_the_exit(treasure_is_here, exit_point)

f2 = open('maze-for-me-done.txt', 'w')
for i in range(len(maze)):
    f2.write(maze_list[i])
    f2.write("\n")
f2.close()
print('Finish!')

