file_maze = open('maze-for-u.txt', 'r')
maze = file_maze.readlines()
file_maze.close()
maze = [maze_line.rstrip() for maze_line in maze]
maze_list = list(maze)

max_x = len(maze[0]) 
max_y = len(maze) 
    
POSSIBLE_WAYS = ['U', 'D', 'R', 'L'] 
coord_treasure = [0, 0] 



def step(coord, direction): 
    if direction == 'U':
         return step_up(coord)
    elif direction == 'D':
         return step_down(coord)
    elif direction == 'R':
         return step_right(coord)
    elif direction == 'L':
         return step_left(coord)
def step_up(coord): 
    return [coord[0], coord[1]-1]
def step_right(coord): 
    return [coord[0]+1, coord[1]]
def step_down(coord): 
    return [coord[0], coord[1]+1]
def step_left(coord): 
    return [coord[0]-1, coord[1]]

def cut_way_back(direction): 
    if direction == 'U':
        return ('U', 'R', 'L')
    if direction == 'D':
        return ('D', 'R', 'L')
    if direction == 'R':
        return ('U', 'D', 'R')
    if direction == 'L':
        return ('U', 'D', 'L')


def change_the_symbol(maze_list, coord, symbol): 
    maze_row = list(maze_list[coord[1]])
    maze_row[coord[0]] = symbol
    maze_list[coord[1]] = ''.join(maze_row)
    
def get_the_symbol(maze, i): 
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

def is_path_clean(maze, coord): 
    if maze[coord[1]][coord[0]] == '#':
        return False
    return True

def enter_coord_of_treasure():
    q = 0
    while q == 0:
        coord_treasure[0] = int(input(f'Where is threasure? (x is between 1 and {max_x}) ')) - 1 
        coord_treasure[1] = int(input(f'Where is threasure? (y is between 1 and {max_y}) ')) - 1
        if maze[coord_treasure[1]][coord_treasure[0]] == '#':
            print('Error! There can be no treasure here! There\'s a wall here!')
        else:
            treasure_is_here = (abs(coord_treasure[0]) if abs(coord_treasure[0]) < max_x-1 else max_x-1, abs(coord_treasure[1]) if abs(coord_treasure[1]) < max_y-1 else max_y-1)
            q = 1
            return treasure_is_here




def mark_the_path(maze_list, coord, path_to_exit):
    for i in path_to_exit:
        change_the_symbol(maze_list, coord, '.') 
        coord = step(coord, i) 

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




path_to_exit = []
for i in range(len(maze)*len(maze[0])):
    path_to_exit.append(' ')
current_path = []

start_point = get_the_symbol(maze, 0)
exit_point = get_the_symbol(maze, max_y - 1)

treasure_is_here = []
treasure_is_here = enter_coord_of_treasure()

change_the_symbol(maze_list, treasure_is_here, '*')

find_a_way(maze, start_point, POSSIBLE_WAYS)

mark_the_path(maze_list, start_point, path_to_exit)

find_the_exit(treasure_is_here, exit_point)

file_maze_done = open('maze-for-me-done.txt', 'w')
for i in range(len(maze)):
    file_maze_done.write(maze_list[i])
    file_maze_done.write("\n")
file_maze_done.close()

print("Done!")
