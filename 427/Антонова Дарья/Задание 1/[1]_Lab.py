import numpy as np

maze = tuple(open("maze-for-u.txt").read().split('\n'))
maze = maze[:-1]
maze_list = list(maze)

max_x, max_y = len(maze[0]), len(maze)

POSSIBLE_WAYS = ('D', 'U', 'L', 'R')


#Ставим . по координате
def set_point_before_treasure(coord):
    global maze_list

    #Преобразовываем строку в список для модификации
    maze_row = list(maze_list[coord[1]])
    maze_row[coord[0]] = '.'
    maze_list[coord[1]] = ''.join(maze_row)
    
#Ставим , по координате
def set_point_after_treasure(coord):
    global maze_list

    maze_row = list(maze_list[coord[1]])
    maze_row[coord[0]] = ','
    maze_list[coord[1]] = ''.join(maze_row)
    
#Ставим * по координате
def set_point_treasure(coord):
    global maze_list

    maze_row = list(maze_list[coord[1]])
    maze_row[coord[0]] = '*'
    maze_list[coord[1]] = ''.join(maze_row)


#Находим координаты первой пустой точки в ряду
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
    if coord[1] == treasure_is_here[1] and coord[0] == treasure_is_here[0]:
        return True
    return False


def is_path_clean(maze, coord):
    if maze[coord[1]][coord[0]] == '#':
        return False
    return True


def step(coord, direction):
    if direction == 'D':
         return step_D(coord)
    elif direction == 'U':
         return step_U(coord)
    elif direction == 'R':
         return step_R(coord)
    elif direction == 'L':
         return step_L(coord)


def step_D(coord):
    return [coord[0], coord[1]-1]


def step_R(coord):
    return [coord[0]+1, coord[1]]


def step_U(coord):
    return [coord[0], coord[1]+1]


def step_L(coord):
    return [coord[0]-1, coord[1]]


def cut_way_back(direction):
    
    if direction == 'D':
        return ('D', 'R', 'L')

    if direction == 'U':
        return ('U', 'R', 'L')

    if direction == 'R':
        return ('D', 'R', 'U')

    if direction == 'L':
        return ('D', 'U', 'L')


#Восстанавливаем путь до сокровища от точки
def restore_path(coord):
    global maze_list, path_to_exit
    
    for node in path_to_exit:
        set_point_before_treasure(coord)
        #Определяем следующую координату
        coord = step(coord, node)

count = 0
def find_a_way(maze, coord, possible_ways):
    global path_to_exit, current_path, count
    
    #Проверка выхода из лабиринта 
    if is_coord_exit(coord):
        print('exit')
        return

    #Проверка на сокровище
    if is_coord_treasure(coord):
        print('\nway is found')
        path_to_exit = current_path.copy()
        return

    #Отбрасываем пути, которые не являются кратчайшими
    if len(current_path) > len(path_to_exit):
        count += 1
        return

    #Рекурсивный поиск по доступным направлениям
    for direction in possible_ways:
        if is_path_clean(maze, step(coord, direction)):
               current_path.append(direction)
               find_a_way(maze, step(coord, direction), cut_way_back(direction))
               current_path.pop()
        
    return 


#was хранит координаты точки, из которой пришли
was = [[-1 for j in range(max_x)] for i in range(max_y)]


def find_the_exit(treasure, end):
    
    #Инициализируем очередь и заносим туда координаты сокровища
    queue = []
    queue.append(treasure)

    was[treasure[1]][treasure[0]] = 0

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
            #Если точку еще не посетили, то добавить в очередь
            if (maze[y][x] == " " and was[y][x] == -1):
                was[y][x] = [node[0],node[1]]
                queue.append([x, y]) 

    x = end[0]
    y = end[1]  

    while was[y][x] != 0:
        set_point_after_treasure([x,y])
        temp_x = was[y][x][0]
        temp_y = was[y][x][1]
        x, y = temp_x, temp_y


path_to_exit = []
for i in range(len(maze)*len(maze[0])):
    path_to_exit.append(' ')
current_path = []

start_point = get_point(maze, 0)
end_point = get_point(maze, max_y-1)
print("start:", start_point)
print("end:",end_point)

treasure_is_here = ()

#Чтобы сокровища не было в стене
while(not (treasure_is_here and is_path_clean(maze, treasure_is_here))):
    x = np.random.randint(0, max_x)
    y = np.random.randint(0, max_y)
    treasure_is_here = (abs(x) if abs(x) < max_x-1 else max_x-1, abs(y) if abs(y) < max_y-1 else max_y-1)

#Отмечаем сокровище на карте
set_point_treasure(treasure_is_here)
print("treasure is here:",treasure_is_here)

#Ищем путь до сокровища
find_a_way(maze, start_point, POSSIBLE_WAYS)

#Восстанавливаем путь до сокровища
restore_path(start_point)

#Ищем выход 
find_the_exit(treasure_is_here, end_point)

print('\nthe number of too long paths that we cut off: ', count) 
#Записываем в файл
f = open('maze-for-me-done.txt', 'w')
for i in range(len(maze_list)):
    f.write(maze_list[i])
    f.write("\n")
f.close()

print("\ndone")