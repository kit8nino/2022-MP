import numpy as np
def Reader():
    y_max=0
    maze=[]
    with open('maze-for-u.txt') as a:
        for line in a:
            maze.append(line.strip('\n'))
        x_max=len(maze[0])
        y_max=len(maze)
    return x_max,y_max,maze
max_x,max_y,maze=Reader()
m=list(maze)
POSSIBLE_WAYS=('N', 'S', 'W', 'E')
coord_treasure = [0, 0]
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
def is_path_clean(maze, coord): 
    if maze[coord[1]][coord[0]] == '#':
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
    return [coord[0], coord[1]-1]
def step_E(coord):
    return [coord[0]+1, coord[1]]
def step_S(coord):
    return [coord[0], coord[1]+1]
def step_W(coord):
    return [coord[0]-1, coord[1]]
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
def shift_the_symbol(m, coord, symbol): 
    w= list(m[coord[1]])
    w[coord[0]] = symbol
    m[coord[1]] = ''.join(w)
def empty_symbol(maze, i):
    return [maze[i].find(" "), i]
def is_treasure(coord): 
    global treasure_is_here
    if coord[1]==treasure_is_here[1] and\
        coord[0]==treasure_is_here[0]:
        return True
    return False
def start_path(m, coord, path_to_exit):
    for a in path_to_exit:
        shift_the_symbol(m,coord,'-') 
        coord=step(coord,a)
def find_a_way(maze, coord, possible_ways):
    global path_to_exit, current_path    
    if not is_coord_in_maze(maze, coord):
        return    
    if is_coord_exit(coord):
        return  
    if is_treasure(coord):
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
def coordinates(): 
    p=False
    while p==False:
        coord_treasure[0] = int(input(f'Where is threasure? (x is between 1 and {max_x}) ')) - 1 
        coord_treasure[1] = int(input(f'Where is threasure? (y is between 1 and {max_y}) ')) - 1
        if maze[coord_treasure[1]][coord_treasure[0]] == '#':
            print('Error! There can be no treasure here! There\'s a wall here!')
        else:
            treasure_is_here = (abs(coord_treasure[0]) if abs(coord_treasure[0]) < max_x-1 else max_x-1, abs(coord_treasure[1]) if abs(coord_treasure[1]) < max_y-1 else max_y-1)
            p=True
            return treasure_is_here    
last=[[-1 for j in range(max_x)] for i in range(max_y)]
def exit(treasure_is_here,fin):
    it=list()
    it.append(treasure_is_here)
    last[treasure_is_here[1]][treasure_is_here[0]] = 0
    while it:
        one=it.pop(0)
        for a in [[-1, 0],[1, 0],[0, -1],[0, 1]]:
            x=one[0]+a[0]
            y=one[1]+a[1]
            if (x<0 or x>=max_x or y<0 or y>=max_y):
                continue
            if (maze[y][x] == " " and last[y][x] == -1):
                last[y][x] = [one[0],one[1]]
                it.append([x, y]) 
    x=fin[0]
    y=fin[1]  
    while last[y][x] != 0:
        shift_the_symbol(m, [x, y], '+')
        x_n=last[y][x][0]
        y_n=last[y][x][1]
        x,y=x_n,y_n
path_to_exit = []
for i in range(len(maze)*len(maze[0])):
    path_to_exit.append(' ')
current_path = []
start_point = empty_symbol(maze, 0)
exit_point = empty_symbol(maze, max_y - 1)
treasure_is_here = []
treasure_is_here=coordinates()
shift_the_symbol(m, treasure_is_here, '*')
find_a_way(maze, start_point, POSSIBLE_WAYS)
start_path(m, start_point, path_to_exit)
exit(treasure_is_here, exit_point)
end= open('result.txt','w')
for i in range(len(maze)):
    end.write(m[i])
    end.write("\n")
end.close()
print('The way to the treasure',path_to_exit)
print("Open the file to see clearly!")
