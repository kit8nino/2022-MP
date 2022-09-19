import numpy as np

def download():
    yy_max = 0
    maze = []
    with open('maze-for-u.txt') as l:
        for line in l:
            maze.append(line.strip('\n'))
        xx_maax=len(maze[0])
        yy_max=len(maze)
    return xx_maax,yy_max,maze
maax_x,maax_y,maaze = download()
m_l=list(maaze)

P_W = ('N', 'S', 'W', 'E')
c_t = [0, 0]

def step_NN(coord):
    return [coord[0], coord[1]-1]

def step_EE(coord):
    return [coord[0]+1, coord[1]]

def step_SS(coord):
    return [coord[0], coord[1]+1]

def step_WW(coord):
    return [coord[0]-1, coord[1]]


def stepp(coord, direction): 
    if direction == 'N':
         return step_NN(coord)
    elif direction == 'S':
         return step_SS(coord)
    elif direction == 'E':
         return step_EE(coord)
    elif direction == 'W':
         return step_WW(coord)
     

def coord_in_mazee(maze, coord):
    if coord[0]<0 or coord[0]>len(maze[0])-1:
        return False
    if coord[1]<0 or coord[1]>len(maze)-1:
        return False
    return True

def is_coord_exitt(coord):
    if coord[1]>len(maaze)-2:
        return True
    return False

def is_path_cleann(maze, coord):
    if maze[coord[1]][coord[0]] == '#':
        return False
    return True

def empty_symboll(maze, i):
    return [maze[i].find(" "), i]  
    
def cut_way_backk(direction):
    
    if direction == 'N':
        return ('N', 'E', 'W')
    if direction == 'S':
        return ('S', 'E', 'W')
    if direction == 'E':
        return ('N', 'E', 'S')
    if direction == 'W':
        return ('N', 'S', 'W')
    
def shift_the_symboll(m_l, coord, symbol): 
    series = list(m_l[coord[1]])
    series[coord[0]] = symbol
    m_l[coord[1]] = ''.join(series)
    

def jewell(coord):
    global treasure_is_here
    if coord[1]==treasure_is_here[1] and\
        coord[0]==treasure_is_here[0]:
        return True
    return False

def start_pathh(m_l, coord, path_to_exit):      
    for a in path_to_exit:
        shift_the_symboll(m_l,coord,'.') 
        coord=stepp(coord,a)
        
def find_a_wayy(maze, coord, possible_ways):
    global path_to_exit, current_path    
    if not coord_in_mazee(maze, coord):
        return    
    if is_coord_exitt(coord):
        return  
    if jewell(coord):
        path_to_exit = current_path.copy()
        return
    if len(current_path) > len(path_to_exit):  
        return
    for direction in possible_ways: 
        if is_path_cleann(maze, stepp(coord, direction)):
            current_path.append(direction)
            find_a_wayy(maze, stepp(coord, direction), cut_way_backk(direction))
            current_path.pop()
    return

def coordinatess():           
    c = False
    while c == False:
        c_t[0] = int(input(f'Номер столбца (x в пределах от 1 до {maax_x}) ')) - 1 
        c_t[1] = int(input(f'Номер строчки (y в пределах от 1 до {maax_y}) ')) - 1
        if maaze[c_t[1]][c_t[0]] == '#':
            print('Выберите другую точку, здесь находится стена') 
        else:
            treasure_is_here = (abs(c_t[0]) if abs(c_t[0]) < maax_x-1 else maax_x-1, abs(c_t[1]) if abs(c_t[1]) < maax_y-1 else maax_y-1)
            c = True
            return treasure_is_here    
bef = [[-1 for j in range(maax_x)] for i in range(maax_y)] 

def exit_pathh(treasure_is_here,scan):        
    it=list()
    it.append(treasure_is_here)
    bef[treasure_is_here[1]][treasure_is_here[0]] = 0
    while it:
        one=it.pop(0)
        for a in [[-1, 0],[1, 0],[0, -1],[0, 1]]:
            x = one[0] + a[0]
            y = one[1] + a[1]
            if (x < 0 or x >= maax_x or y < 0 or y >= maax_y):
                continue
            if (maaze[y][x] == " " and bef[y][x] == -1):
                bef[y][x] = [one[0],one[1]]
                it.append([x, y]) 
    x = scan[0]
    y = scan[1]  
    while bef[y][x] != 0:
        shift_the_symboll(m_l, [x, y], ',')
        x_n=bef[y][x][0]
        y_n=bef[y][x][1]
        x,y=x_n,y_n
        
path_to_exit = []
for i in range(len( maaze)*len(maaze[0])):
        path_to_exit.append(' ')
        
current_path = []

start_point = empty_symboll(maaze, 0)
exit_point = empty_symboll(maaze, maax_y - 1)

treasure_is_here =[]
treasure_is_here=coordinatess()

shift_the_symboll(m_l, treasure_is_here, '*')

find_a_wayy(maaze, start_point, P_W)

start_pathh(m_l, start_point, path_to_exit)

exit_pathh(treasure_is_here, exit_point)

end= open('maze-for-me-done.txt','w')

for i in range(len(maaze)):
    end.write(m_l[i])
    end.write("\n")
end.close()

print('Путь до сокровища  \n',path_to_exit)