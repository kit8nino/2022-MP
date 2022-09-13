f = open('maze-for-u.txt', 'r')
maze = f.readlines()
f.close()
maze = [m_line.rstrip() for m_line in maze]
maze_list = list(maze)
max_x, max_y = len(maze[0]), len(maze)  
POSSIBLE_WAYS = ('down', 'up', 'left', 'right')
x0y0 = [0, 0]

def step(xy, dirr):
    if dirr == 'left':
         return [xy[0], xy[1]-1]
    elif dirr == 'up':
         return [xy[0]+1, xy[1]]
    elif dirr == 'right':
         return [xy[0], xy[1]+1]
    elif dirr == 'down':
         return [xy[0]-1, xy[1]]
def noway(dirr):
     if dirr == 'down':
        return ('down', 'right', 'left')
     if dirr == 'up':
        return ('up', 'right', 'left')
     if dirr == 'right':
        return ('down', 'right', 'up')
     if dirr == 'left':
        return ('down', 'up', 'left')
def change(maze_list, xy, up):
    maze_row = list(maze_list[xy[1]])
    maze_row[xy[0]] = up
    maze_list[xy[1]] = ''.join(maze_row)
def get_s(maze, i):
    return [maze[i].find(" "), i]
def is_coord_in_maze(maze, xy):
    if xy[0]<0 or xy[0]>len(maze[0])-1:
        return False
    if xy[1]<0 or xy[1]>len(maze)-1:
        return False
    return True
def is_coord_exit(xy):
    if xy[1]>len(maze)-2:
        return True
    return False
def is_coord_treasure(xy):
    global treasure_is_here
    if xy[1] == treasure_is_here[1] and\
        xy[0] == treasure_is_here[0]:
        return True
    return False
def is_path_clean(maze, xy): #
    if maze[xy[1]][xy[0]] == '#':
        return False
    return True
def entercoords():
    q = 0
    while q == 0:
        x0y0[0] = int(input(f'Введите х координату сокровеща (от 1 до {max_x}) ')) - 1 
        x0y0[1] = int(input(f'Введите у координату сокровища (от 1 до {max_y}) ')) - 1
        if maze[x0y0[1]][x0y0[0]] == '#':
            print('Ошбка! Выпопали в стену')
        else:
            treasure_is_here = (abs(x0y0[0]) if abs(x0y0[0]) < max_x-1 else max_x-1, abs(x0y0[1]) if abs(x0y0[1]) < max_y-1 else max_y-1)
            q = 1
            return treasure_is_here
def mark_the_path(maze_list, xy, path_to_exit):
    for i in path_to_exit:
        change(maze_list, xy, 'v')
        xy = step(xy, i)
def find_a_way(maze,xy,ways):
    global path_to_exit,current_path
    if not is_coord_in_maze(maze, xy):
        return
    if is_coord_exit(xy):
        return
    if is_coord_treasure(xy):
        path_to_exit = current_path.copy()
        return
    if len(current_path) > len(path_to_exit):
        return
    for direction in ways:
        if is_path_clean(maze, step(xy, direction)):
            current_path.append(direction)
            find_a_way(maze, step(xy, direction), noway(direction))
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
        change(maze_list, [x, y], 'z')
        temp_x = prev_coord[y][x][0]
        temp_y = prev_coord[y][x][1]
        x, y = temp_x, temp_y
path_to_exit = []
for i in range(len(maze)*len(maze[0])):
    path_to_exit.append(' ')
current_path = []
start_point = get_s(maze, 0)
exit_point = get_s(maze, max_y - 1)
treasure_is_here = []
treasure_is_here = entercoords()
change(maze_list, treasure_is_here, '*')
find_a_way(maze, start_point, POSSIBLE_WAYS)
mark_the_path(maze_list, start_point, path_to_exit)
find_the_exit(treasure_is_here, exit_point)
done = open('maze.txt', 'w')
for i in range(len(maze)):
    done.write(maze_list[i])
    done.write("\n")
done.close()
print('Путь к кладу ',path_to_exit,)
print('Карта в файле maze')
