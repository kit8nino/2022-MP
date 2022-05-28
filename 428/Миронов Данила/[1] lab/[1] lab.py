mazeforme = open('maze-for-u.txt', 'r')
maze = mazeforme.readlines()
maze = [maze_line.rstrip() for maze_line in maze]
maze_list = list(maze)

max_x, max_y = len(maze[0]), len(maze) 

POSSIBLE_WAYS = ['N', 'S', 'E', 'W'] 

def step(coord, direction):
    if direction == 'N':
         return step_NORTH(coord)
    elif direction == 'S':
         return step_SOUTH(coord)
    elif direction == 'E':
         return step_EAST(coord)
    elif direction == 'W':
         return step_WEST(coord)

def cut_way_back(direction):
    if direction == 'N':
        return ('N', 'E', 'W')
    if direction == 'S':
        return ('S', 'E', 'W')
    if direction == 'E':
        return ('N', 'S', 'E')
    if direction == 'W':
        return ('N', 'S', 'W')


def step_NORTH(coord): 
    return [coord[0], coord[1]-1]
def step_EAST(coord):
    return [coord[0]+1, coord[1]]
def step_SOUTH(coord):
    return [coord[0], coord[1]+1]
def step_WEST(coord):
    return [coord[0]-1, coord[1]]


def is_coord_in_maze(maze, coord): 
    if coord[0]<0 or coord[0]>len(maze[0])-1:
        return False
    if coord[1]<0 or coord[1]>len(maze)-1:
        return False
    return True

def is_coord_exit(coord):
    if coord[1]>len(maze_list)-2:
        return True
    return False

def is_path_clean(maze, coord): 
    if maze[coord[1]][coord[0]] == '#':
        return False
    return True

coord_treasure = [0, 0] 
def input_coord_of_treasure(): 
    check = False
    while check == False:
        coord_treasure[0] = int(input(f'Где клад? (x is between 1 and {max_x}) ')) - 1 
        coord_treasure[1] = int(input(f'Где клад? (y is between 1 and {max_y}) ')) - 1
        if maze[coord_treasure[1]][coord_treasure[0]] == '#':
            print('Ошибка! Тут стена!')
        else:
            treasure_is_here = (abs(coord_treasure[0]) if abs(coord_treasure[0]) < max_x-1 else max_x-1, abs(coord_treasure[1]) if abs(coord_treasure[1]) < max_y-1 else max_y-1)
            check = True
            return treasure_is_here

def is_coord_treasure(coord): 
    global treasure_is_here
    if(coord[1] == treasure_is_here[1] and coord[0] == treasure_is_here[0]):
        return True
    return False

def replace_symbol(maze_list, coord, symbol): 
    maze_row = list(maze_list[coord[1]])
    maze_row[coord[0]] = symbol
    maze_list[coord[1]] = ''.join(maze_row)

def find_empty_symbol(maze, i): 
    return [maze[i].find(" "), i]



def find_a_way(maze, coord, possible_ways):
    global path_to_exit, current_path

    if not is_coord_in_maze(maze, coord):
        return

    if is_coord_exit(coord):
        return

    if is_coord_treasure(coord):
        path_to_exit = current_path.copy()
        return

    if len(current_path) > len(path_to_exit):
        return

    for direction in possible_ways:
        if is_path_clean(maze, step(coord, direction)):
            current_path.append(direction)
            find_a_way(maze, step(coord, direction), cut_way_back(direction))
            current_path.pop()
    return

def tag_path(maze_list, coord, path_to_exit): 
    for i in path_to_exit:
        replace_symbol(maze_list, coord, '.') 
        coord = step(coord, i) 

prev_coord = [[-1 for j in range(max_x)] for i in range(max_y)]
def find_the_exit(treasure_is_here, exit_point):
    stepby = []
    stepby.append(treasure_is_here)
    prev_coord[treasure_is_here[1]][treasure_is_here[0]] = 0
    while stepby:
        first_element = stepby.pop(0)
        for i in [[-1, 0],[1, 0],[0, -1],[0, 1]]:
            x = first_element[0] + i[0]
            y = first_element[1] + i[1]
            if (x < 0 or x >= max_x or y < 0 or y >= max_y):
                continue
            if (maze[y][x] == " " and prev_coord[y][x] == -1):
                prev_coord[y][x] = [first_element[0],first_element[1]]
                stepby.append([x, y]) 
    x = exit_point[0]
    y = exit_point[1]  
    while prev_coord[y][x] != 0:
        replace_symbol(maze_list, [x, y], ',')
        temp_x = prev_coord[y][x][0]
        temp_y = prev_coord[y][x][1]
        x, y = temp_x, temp_y


path_to_exit = []
for i in range(len(maze)*len(maze[0])):
    path_to_exit.append(' ')

current_path = []

start_point = find_empty_symbol(maze, 0)

treasure_is_here = []
treasure_is_here = input_coord_of_treasure()

replace_symbol(maze_list, treasure_is_here, '*')

find_a_way(maze, start_point, POSSIBLE_WAYS)
tag_path(maze_list, start_point, path_to_exit)

exit_point = find_empty_symbol(maze, max_y - 1)
find_the_exit(treasure_is_here, exit_point)

mazefforme_done = open('maze-for-me-done.txt', 'w')
for i in range(len(maze)):
    mazefforme_done.write(maze_list[i])
    mazefforme_done.write("\n")
mazefforme_done.close()

