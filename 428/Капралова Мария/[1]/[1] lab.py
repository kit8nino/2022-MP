import os

file = open('maze-for-u.txt', 'r')
maze = file.readlines()
file.close()
maze = [m_line.rstrip() for m_line in maze]
maze_list = list(maze)
max_x = len(maze[0])
max_y = len(maze)    
movement = ['Up', 'Down', 'Right', 'Left']
coord_tr = [0, 0]


def Up(coord): #шаг вверх
    return [coord[0], coord[1]-1]
def Right(coord): #шаг вправо
    return [coord[0]+1, coord[1]]
def Down(coord): #шаг вниз
    return [coord[0], coord[1]+1]
def Left(coord): #шаг влево
    return [coord[0]-1, coord[1]]

def step(coord, direction): #проверка направления -> вызов шага
    if direction == 'Up':
         return Up(coord)
    elif direction == 'Down':
         return Down(coord)
    elif direction == 'Right':
         return Right(coord)
    elif direction == 'Left':
         return Left(coord)
        
def new_ways(direction): #новые варианты направлений, чтобы не ходить куда ходили
    if direction == 'Up':
        return ('Up', 'Right', 'Left')
    if direction == 'Down':
        return ('Down', 'Right', 'Left')
    if direction == 'Right':
        return ('Up', 'Down', 'Right')
    if direction == 'Left':
        return ('Up', 'Down', 'Left')
    
def change(maze_list, coord, s):              #изменение массива лабиринта - добавление меток
    maze_row = list(maze_list[coord[1]])      # s - точка, запятая или звездочка
    maze_row[coord[0]] = s
    maze_list[coord[1]] = ''.join(maze_row)
    
def get_passage(maze, i): #нахождение хода (для координат входа и выхода)
    return [maze[i].find(" "), i]

def is_coord_in_maze(maze, coord): #попадает ли координата в размер лабиринта?
    if coord[0]<0 or coord[0]>len(maze[0])-1:
        return False
    if coord[1]<0 or coord[1]>len(maze)-1:
        return False
    return True

def is_coord_exit(coord): #это - координата выхода?
    if coord[1]>len(maze)-2:
        return True
    return False

def is_coord_treasure(coord): #нашли сокровище?
    global treasure_is_here
    if (coord[1] == treasure_is_here[1] and coord[0] == treasure_is_here[0]):
        return True
    return False

def is_path_clean(maze, coord): #путь или стена?
    if maze[coord[1]][coord[0]] == '#':
        return False
    return True

def treasure_new_coords(): #задание координат сокровища пользователем
    q = 0
    while q == 0:
        coord_tr[0] = int(input(f'Where is threasure? (x is between 1 and {max_x}) ')) - 1 
        coord_tr[1] = int(input(f'Where is threasure? (y is between 1 and {max_y}) ')) - 1
        print('')
        if maze[coord_tr[1]][coord_tr[0]] == '#':
            print('No luck! You hit the wall!')
        else:
            treasure_is_here = (abs(coord_tr[0]) if abs(coord_tr[0]) < max_x-1 else max_x-1, abs(coord_tr[1]) if abs(coord_tr[1]) < max_y-1 else max_y-1)
            q = 1
            return treasure_is_here


def mark_the_path(maze_list, coord, path_to_treasure): #путь до сокровища -> добавление метки - точка
    for i in path_to_treasure:
        change(maze_list, coord, '.')
        coord = step(coord, i)
        
def find_a_way(maze,coord,ways): #поиск пути
    global path_to_treasure,current_path
    if not is_coord_in_maze(maze, coord):
        return
    if is_coord_exit(coord):
        return
    if is_coord_treasure(coord):
        path_to_treasure = current_path.copy()
        return
    if len(current_path) > len(path_to_treasure):
        return
    for direction in ways:
        if is_path_clean(maze, step(coord, direction)):
            current_path.append(direction)
            find_a_way(maze, step(coord, direction), new_ways(direction))
            current_path.pop()
    return
    
prev_coord = [[-1 for j in range(max_x)] for i in range(max_y)]

def find_the_exit(treasure_is_here, exit_point): #поиск пути до выхода от точки сокровища, метка - запятые
    iteration = []                               #если накладывается путь до сокровища и путь до выхода
    iteration.append(treasure_is_here)           #то победят запятые и они перекрою точки
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
        change(maze_list, [x, y], ',')
        temp_x = prev_coord[y][x][0]
        temp_y = prev_coord[y][x][1]
        x, y = temp_x, temp_y


path_to_treasure = []

for i in range(len(maze)*len(maze[0])):
    path_to_treasure.append(' ')
    
current_path = []
start_point = get_passage(maze, 0)
exit_point = get_passage(maze, max_y - 1)
treasure_is_here = []
treasure_is_here = treasure_new_coords()

change(maze_list, treasure_is_here, '*') #добавление метки сокровища

find_a_way(maze, start_point, movement)
mark_the_path(maze_list, start_point, path_to_treasure)
find_the_exit(treasure_is_here, exit_point)

done = open('maze-for-me-done.txt', 'w')
for i in range(len(maze)):
    done.write(maze_list[i])
    done.write("\n")
print('The way to the treasure: ',path_to_treasure,'\n')

count=0 #шаги сокровище->выход
for i in range(0, len(maze_list)):
    for j in range(0, len(maze_list[0])):
        if maze_list[i][j]==',':
            count=count+1
print('The shortest path from the treasure to the exit contains ', count, ' steps.\n')

done.close()

#чтобы сразу открылся файл и не пришлось искать
#os.startfile(r'maze-for-me-done.txt')
