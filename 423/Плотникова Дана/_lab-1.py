maze = ('######## #',
        '#  #   # #',
        '## # ### #',
        '##   #   #',
        '#  ##  ###',
        '##     # #',
        '# ## ### #',
        '# ## # # #',
        '####     #',
        '####### ##', 
        '####### ##')

max_x, max_y = len(maze[0]), len(maze)

POSSIBLE_WAYS = ('N', 'S', 'W', 'E')

def is_coord_in_maze(maze, coord):
    if coord[0]<0 or coord[0]>len(maze[0])-1:
        return False
    if coord[1]<0 or coord[1]>len(maze)-1:
        return False
    return True

def is_coord_exit(coord):
    if coord[0]>9:
        return True
    return False

def is_path_clean(maze, coord):
    if maze[coord[0]][coord[1]] == '#':
        return False
    return True

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
    return [coord[0]-1, coord[1]]

def step_E(coord):
    return [coord[0], coord[1]+1]

def step_S(coord):
    return [coord[0]+1, coord[1]]

def step_W(coord):
    return [coord[0], coord[1]-1]

def cut_way_back(direction):
    """
    Cut the opposite direction in possible ways to prevent stepping back
    """
    if direction == 'N':
        return ('N', 'E', 'W')

    if direction == 'S':
        return ('S', 'E', 'W')

    if direction == 'E':
        return ('N', 'E', 'S')

    if direction == 'W':
        return ('N', 'S', 'W')


def find_a_way(maze, coord, possible_ways):

    len_y, len_x = len(maze), len(maze[0])
    global path_to_exit, current_path
    #print('x: ', len_x, ' y:', len_y)
    #print('Start from: ', coord)

    if not is_coord_in_maze(maze, coord):
        print('not in bounds!')
        return

    if is_coord_exit(coord):
        print('new way is found')
        path_to_exit = current_path.copy()
        return

    if len(current_path) > len(path_to_exit):
        print('too large path')
        print(f'{len(current_path)} > {len(path_to_exit)}')

        return

    for direction in possible_ways:
        if is_path_clean(maze, step(coord, direction)):
               print(direction)
               current_path.append(direction)
               find_a_way(maze, step(coord, direction), cut_way_back(direction))
               current_path.pop()

    return 

path_to_exit = []
for i in range(len(maze)*len(maze[0])):
    path_to_exit.append(' ')
current_path = []

start_point = [0, 8]
print(len(path_to_exit))
x = int(input(f'Where is threasure? (x is between 0 and {max_x-1}) '))
y = int(input(f'Where is threasure? (y is between 0 and {max_y-1}) '))
treasure_is_here = (abs(x) if abs(x) < max_x-1 else max_x-1, abs(y) if abs(y) < max_y-1 else max_y-1)

print(type(treasure_is_here))
print(treasure_is_here)
find_a_way(maze, start_point, POSSIBLE_WAYS)
print(path_to_exit)
