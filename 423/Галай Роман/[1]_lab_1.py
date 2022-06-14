#Делал в паре с Андреем Чебыровым
f = open('maze.txt', 'r')
maze = f.readlines()
f.close()
maze = [m_line.rstrip() for m_line in maze]
maze_list = list(maze)
max_x, max_y = len(maze[0]), len(maze)  
POSSIBLE_WAYS = ('N', 'S', 'W', 'E')
cor0 = [0, 0]

def W(coord):
    return [coord[0], coord[1]-1]
def S(coord):
    return [coord[0]+1, coord[1]]
def E(coord):
    return [coord[0], coord[1]+1]
def N(coord):
    return [coord[0]-1, coord[1]]
def step(coord, dirr):
    if dirr == 'W':
         return W(coord)
    elif dirr == 'S':
         return S(coord)
    elif dirr == 'E':
         return E(coord)
    elif dirr == 'N':
         return N(coord)
def noway(dirr):
     if dirr == 'N':
        return ('N', 'E', 'W')
     if dirr == 'S':
        return ('S', 'E', 'W')
     if dirr == 'E':
        return ('N', 'E', 'S')
     if dirr == 'W':
        return ('N', 'S', 'W')
def change(maze_list, coord, s):
    maze_row = list(maze_list[coord[1]])
    maze_row[coord[0]] = s
    maze_list[coord[1]] = ''.join(maze_row)
def get_s(maze, i):
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
def is_coord_treasure(coord):
    global treasure_is_here
    if coord[1] == treasure_is_here[1] and\
        coord[0] == treasure_is_here[0]:
        return True
    return False
def is_path_clean(maze, coord): #
    if maze[coord[1]][coord[0]] == '#':
        return False
    return True
def entercoords():
    q = 0
    while q == 0:
        cor0[0] = int(input(f'Where is threasure? (x is between 1 and {max_x}) ')) - 1 
        cor0[1] = int(input(f'Where is threasure? (y is between 1 and {max_y}) ')) - 1
        if maze[cor0[1]][cor0[0]] == '#':
            print('Error! You have hit a wall!')
        else:
            treasure_is_here = (abs(cor0[0]) if abs(cor0[0]) < max_x-1 else max_x-1, abs(cor0[1]) if abs(cor0[1]) < max_y-1 else max_y-1)
            q = 1
            return treasure_is_here
def mark_the_path(maze_list, coord, path_to_exit):
    for i in path_to_exit:
        change(maze_list, coord, '.')
        coord = step(coord, i)
def find_a_way(maze,coord,ways):
    global path_to_exit,current_path
    if not is_coord_in_maze(maze, coord):
        return
    if is_coord_exit(coord):
        return
    if is_coord_treasure(coord):
        path_to_exit = current_path.copy()
        return
    if len(current_path) > len(path_to_exit):
        return
    for direction in ways:
        if is_path_clean(maze, step(coord, direction)):
            current_path.append(direction)
            find_a_way(maze, step(coord, direction), noway(direction))
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
        change(maze_list, [x, y], ',')
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
done = open('maze1.txt', 'w')
for i in range(len(maze)):
    done.write(maze_list[i])
    done.write("\n")
done.close()
print('The way to the treasure: ',path_to_exit,'\n Open the file to see the map')