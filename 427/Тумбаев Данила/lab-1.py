
import numpy as np

'''
file = "maze-for-u.txt"

maze = tuple(open(file).read().split('\n'))
maze = maze[:-1]
maze_list= list(maze)

max_x, max_y = len(maze[0]), len(maze)
print("Max y: ", max_y)
print("Max x: ", max_x)
'''
def Maze_Reader():
    y_max=0
    maze=[]
   
    with open('maze-for-u.txt') as maze2:
        for line in maze2:
           maze.append(line.strip('\n'))
        x_max, y_max = len(maze[0]), len(maze)
    return x_max,y_max, maze

#print(Maze_Reader())

max_x,max_y,maze=Maze_Reader()
maze_list= list(maze)
POSSIBLE_WAYS = ('N', 'S', 'W', 'E')



#Ставит символ sign в лабиринте по координате coord
def set_point(coord, sign):
    global maze_list

    #Преобразовываем строку в список для модификации
    maze_row = list(maze_list[coord[1]])
    maze_row[coord[0]] = sign
    maze_list[coord[1]] = ''.join(maze_row)


#Находит координаты первой пустой точки в ряду
def get_point(maze, row):
    return [maze[row].find(" "), row]


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


#Восстанавливает путь до сокровища от точки coord
def restore_path(coord):
    global maze_list, path_to_exit
    
    for node in path_to_exit:
        set_point(coord, '.')
        #Определяет следующую координату
        coord = step(coord, node)

count_2l_ways = 0 
def find_a_way(maze, coord, possible_ways):
    global path_to_exit, current_path, count_2l_ways
    
    #Проверка границ лабиринта
    #if not is_coord_in_maze(maze, coord):
     #   print('not in bounds!')
      #  return

    #Проверка выхода из лабиринта 
    if is_coord_exit(coord):
        print('exit')
        return

    #Проверка на наход сокровища
    if is_coord_treasure(coord):
        print('finding a new way')
        path_to_exit = current_path.copy()
        return

    #Отбрасываем пути, которые не являются кратчайшими
    if len(current_path) > len(path_to_exit):
        #print('too large path')
        #print(f'{len(current_path)} > {len(path_to_exit)}')
        count_2l_ways+=1
        
        return

    #Рекурсивный поиск по доступным направлениям
    for direction in possible_ways:
        if is_path_clean(maze, step(coord, direction)):
               current_path.append(direction)
               find_a_way(maze, step(coord, direction), cut_way_back(direction))
               current_path.pop()
        
    return 
    

#past_way хранит координаты точки, из которой пришли
past_way = [[-1 for j in range(max_x)] for i in range(max_y)] # инициализация



def find_the_exit(treasure, end):
    #treasure[0] - column, treasure[1] - row
    #y - row, x - column

    #Инициализируем очередь и заносим туда координаты сокровища
    queue = []
    queue.append(treasure)

    past_way[treasure[1]][treasure[0]] = 0 #Обозначм 0 местонахождение сокровища
    
    #Пока очередь не пуста
    while queue:
        #Забираем первый элемент из очереди
        node = queue.pop(0)
        
        for i in [[-1, 0],[1, 0],[0, -1],[0, 1]]:
            x = node[0] + i[0]
            y = node[1] + i[1]
            #Проверка на принадлежность лабиринту
            if (x < 0 or x >= max_x or y < 0 or y >= max_y):
                continue
            #Если точку еще не посетили - добавить в очередь
            if (maze[y][x] == " " and past_way[y][x] == -1):
                past_way[y][x] = [node[0],node[1]]
                queue.append([x, y]) 
    
    x = end[0]
    y = end[1]  
    
    #В список past_way передаём координаты выхода(поиск в ширину), а затем мы забираем координаты x,y в отдельные
    #переменные и перезаписывам их
    while past_way[y][x] != 0:
        set_point([x,y], ',')
        temp_x = past_way[y][x][0]
        temp_y = past_way[y][x][1]
        x, y = temp_x, temp_y
        #print(past_way[y][x])

path_to_exit = []
for i in range(len(maze)*len(maze[0])):
    path_to_exit.append(' ')
current_path = []

#Получение стартовой и конечной точек
start_point = get_point(maze, 0)
end_point = get_point(maze, max_y-1)
print("start:", start_point)
print("end:",end_point)

treasure_is_here = ()

#Чтобы сокровище не спавнилось в стене
while(not (treasure_is_here and is_path_clean(maze, treasure_is_here))):
    x = np.random.randint(40,85) #int(input(f'Where is threasure? (x is between 0 and {max_x-1}) '))
    y = np.random.randint(90,190) #int(input(f'Where is threasure? (y is between 0 and {max_y-1}) '))
    treasure_is_here = (abs(x) if abs(x) < max_x-1 else max_x-1, abs(y) if abs(y) < max_y-1 else max_y-1)

#Отмечаем сокровище на карте
set_point(treasure_is_here, '*')
print("treasure is here:",treasure_is_here)

#Ищем путь до сокровища
find_a_way(maze, start_point, POSSIBLE_WAYS)

#Восстанавливаем путь до сокровища
restore_path(start_point)

#Ищем выход 
find_the_exit(treasure_is_here, end_point)

#Записываем в файл
f = open('maze-for-me-done.txt', 'w')
for i in range(len(maze_list)):
    f.write(maze_list[i])
    f.write("\n")
f.close()
print('The quontity of too long paths that we cut off: ', count_2l_ways) 
print("Done!")
