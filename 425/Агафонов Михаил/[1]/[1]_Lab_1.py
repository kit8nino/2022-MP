import numpy as np

def download():
    y_max = 0
    maze = []
    with open('maze-for-u.txt') as a:
        for line in a:
            maze.append(line.strip('\n'))
        x_max=len(maze[0]) # количество столбцов в лабиринте
        y_max=len(maze) # количество строк 
    return x_max,y_max,maze
max_x,max_y,maze = download()
m_l=list(maze)

POSSIBLE_WAYS = ('N', 'S', 'W', 'E') # движение по лабиринту: вверх/вниз/влево/вправо
coord_treasure = [0, 0]  # точка сокровища (x;y)

def step_N(coord): # шаг смещения по лабиринту
    return [coord[0], coord[1]-1]

def step_E(coord):
    return [coord[0]+1, coord[1]]

def step_S(coord):
    return [coord[0], coord[1]+1]

def step_W(coord):
    return [coord[0]-1, coord[1]]


def step(coord, direction): 
    if direction == 'N':
         return step_N(coord)
    elif direction == 'S':
         return step_S(coord)
    elif direction == 'E':
         return step_E(coord)
    elif direction == 'W':
         return step_W(coord)
     

def coord_in_maze(maze, coord):  # координата в лабиринте
    if coord[0]<0 or coord[0]>len(maze[0])-1:
        return False
    if coord[1]<0 or coord[1]>len(maze)-1:
        return False
    return True

def is_coord_exit(coord): #координата выхода
    if coord[1]>len(maze)-2:
        return True
    return False

def is_path_clean(maze, coord): # обход стен в виде #
    if maze[coord[1]][coord[0]] == '#':
        return False
    return True

def empty_symbol(maze, i):       # Нахождение прохода в лабиринте
    return [maze[i].find(" "), i]  
    
def cut_way_back(direction): # чтобы не возвращатся назад
    
    if direction == 'N':
        return ('N', 'E', 'W')
    if direction == 'S':
        return ('S', 'E', 'W')
    if direction == 'E':
        return ('N', 'E', 'S')
    if direction == 'W':
        return ('N', 'S', 'W')
    
def shift_the_symbol(m_l, coord, symbol): 
    series = list(m_l[coord[1]])
    series[coord[0]] = symbol
    m_l[coord[1]] = ''.join(series)
    

def jewel(coord):     # клад
    global treasure_is_here
    if coord[1]==treasure_is_here[1] and\
        coord[0]==treasure_is_here[0]:
        return True
    return False

def start_path(m_l, coord, path_to_exit):      
    for a in path_to_exit:
        shift_the_symbol(m_l,coord,'.') 
        coord=step(coord,a)
        
def find_a_way(maze, coord, possible_ways):         # нахождение пути
    global path_to_exit, current_path    
    if not coord_in_maze(maze, coord):  # быть в пределах лабиринта
        return    
    if is_coord_exit(coord): # Проверка выхода из лабиринта 
        return  
    if jewel(coord): # Проверка на сокровище
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
    c = False
    while c == False:
        coord_treasure[0] = int(input(f'Номер столбца (x в пределах от 1 до {max_x}) ')) - 1 
        coord_treasure[1] = int(input(f'Номер строчки (y в пределах от 1 до {max_y}) ')) - 1
        if maze[coord_treasure[1]][coord_treasure[0]] == '#':
            print('Выберите другую точку, здесь находится стена (#)') 
        else:
            treasure_is_here = (abs(coord_treasure[0]) if abs(coord_treasure[0]) < max_x-1 else max_x-1, abs(coord_treasure[1]) if abs(coord_treasure[1]) < max_y-1 else max_y-1)
            c = True
            return treasure_is_here    
bef = [[-1 for j in range(max_x)] for i in range(max_y)] 

def exit_path(treasure_is_here,scan):        
    it=list()
    it.append(treasure_is_here)
    bef[treasure_is_here[1]][treasure_is_here[0]] = 0
    while it:
        one=it.pop(0)
        for a in [[-1, 0],[1, 0],[0, -1],[0, 1]]:
            x = one[0] + a[0]
            y = one[1] + a[1]
            if (x < 0 or x >= max_x or y < 0 or y >= max_y):
                continue
            if (maze[y][x] == " " and bef[y][x] == -1):
                bef[y][x] = [one[0],one[1]]
                it.append([x, y]) 
    x = scan[0]
    y = scan[1]  
    while bef[y][x] != 0:
        shift_the_symbol(m_l, [x, y], ',')
        x_n=bef[y][x][0]
        y_n=bef[y][x][1]
        x,y=x_n,y_n
        
path_to_exit = []
for i in range(len( maze)*len(maze[0])): # добавляет в массив букву следования к сокровищу
        path_to_exit.append(' ')
        
current_path = []

start_point = empty_symbol(maze, 0)
exit_point = empty_symbol(maze, max_y - 1)

treasure_is_here =[]
treasure_is_here=coordinates()

shift_the_symbol(m_l, treasure_is_here, '*')

find_a_way(maze, start_point, POSSIBLE_WAYS)

start_path(m_l, start_point, path_to_exit)

exit_path(treasure_is_here, exit_point)

# запись в файл
end= open('maze-for-me-done.txt','w')

for i in range(len(maze)):
    end.write(m_l[i])
    end.write("\n")
end.close()

print('Путь до сокровища: \n',path_to_exit)