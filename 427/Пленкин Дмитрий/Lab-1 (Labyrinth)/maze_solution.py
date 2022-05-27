import numpy as np

def maze_reader():
    y_max = 0
    maze = []
    with open('maze-for-u.txt') as maze_length:
        for line in maze_length:
           maze.append(line.strip('\n'))
        x_max, y_max = len(maze[0]), len(maze)
    return x_max, y_max, maze

#Инициализация переменных
max_x, max_y, maze = maze_reader()
maze_list = list(maze)
POSSIBLE_WAYS = ('UP', 'DOWN', 'LEFT', 'RIGHT')
large_toexit_ways = 0
prev_coord = [[-1 for j in range(max_x)] for i in range(max_y)] #Предыдущая координата
treasure_coordinates = ()
path_to_exit = []
for i in range(len(maze) * len(maze[0])):
    path_to_exit.append(' ')
current_path = []
border = 2

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

#Проверка точки на клетке в лабиринте
def is_coordinates_in_maze(maze, coord):
    if coord[0] < 0 or coord[0] > len(maze[0]) - 1:
        return False
    if coord[1] < 0 or coord[1] > len(maze) - 1:
        return False
    return True

#Проверка точки на клетке с выходом
def is_coordinates_exit(coord):
    if coord[1] > len(maze) - 2:
        return True
    else:
        return False

#Проверка точки на клетке с сокровищем 
def is_coordinates_treasure(coord):
    global treasure_coordinates
    if coord[1] == treasure_coordinates[1] and coord[0] == treasure_coordinates[0]:
        return True
    else:
        return False

#Проверка точки на 
def is_path_clean(maze, coord):
    if maze[coord[1]][coord[0]] == '#':
        return False
    else:
        return True

def step(coord, direction):
    if direction == 'UP':
         return step_up(coord)
    elif direction == 'DOWN':
         return step_down(coord)
    elif direction == 'RIGHT':
         return step_right(coord)
    else:
         return step_left(coord)

def step_up(coord):
    return [coord[0], coord[1] - 1]
def step_down(coord):
    return [coord[0], coord[1] + 1]
def step_left(coord):
    return [coord[0]  -1, coord[1]]
def step_right(coord):
    return [coord[0] + 1, coord[1]]

def cut_way_back(direction):
    if direction == 'UP':
        return ('UP', 'RIGHT', 'LEFT')
    if direction == 'DOWN':
        return ('DOWN', 'RIGHT', 'LEFT')
    if direction == 'RIGHT':
        return ('UP', 'RIGHT', 'DOWN')
    if direction == 'LEFT':
        return ('UP', 'DOWN', 'LEFT')

#Восстанавливает путь до сокровища от точки coord
def restore_path(coord):
    global maze_list, path_to_exit
    
    for node in path_to_exit:
        set_point(coord, '.')
        coord = step(coord, node)

def find_a_way(maze, coord, possible_ways):
    global path_to_exit, current_path, large_toexit_ways
    
    #Проверка на наличие выхода из лабиринта 
    if is_coordinates_exit(coord):
        print('exit')
        return 0
    
    #Проверка на нахождение сокровища
    if is_coordinates_treasure(coord):
        print('finding a new way')
        path_to_exit = current_path.copy()
        return 0
    
    #Отбрасываем некрайтчашие пути
    if len(current_path) > len(path_to_exit):
        large_toexit_ways += 1
        return 0

    #Рекурсивный поиск по доступным направлениям
    for direction in possible_ways:
        if is_path_clean(maze, step(coord, direction)):
               current_path.append(direction)
               find_a_way(maze, step(coord, direction), cut_way_back(direction))
               current_path.pop()
    return 1

def find_the_exit(treasure, end):
    queue = []
    queue.append(treasure)
    prev_coord[treasure[1]][treasure[0]] = 0 #Обозначим 0 местонахождение сокровища
    
    #Пока очередь не пуста
    while queue:
        #Забираем первый элемент из очереди
        node = queue.pop(0)  
        for i in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x = node[0] + i[0]
            y = node[1] + i[1]
            if (x < 0 or x >= max_x or y < 0 or y >= max_y):
                continue
            #Добавление в очередь, если точку еще не посетили
            if (maze[y][x] == " " and prev_coord[y][x] == -1):
                prev_coord[y][x] = [node[0], node[1]]
                queue.append([x, y]) 
    x = end[0]
    y = end[1]  
    while prev_coord[y][x] != 0:
        set_point([x, y], ',')
        temp_x = prev_coord[y][x][0]
        temp_y = prev_coord[y][x][1]
        x, y = temp_x, temp_y

#Получение стартовых и конечных координат
start_point = get_point(maze, 0)
end_point = get_point(maze, max_y - 1)
print("start:", start_point)
print("end:", end_point)

#Создаем случайные координаты сокровища в лабиринте, пока точка случайно выбирается в стене
while(not (treasure_coordinates and is_path_clean(maze, treasure_coordinates))):
    x = np.random.randint(border, len(maze[0]) - border)
    y = np.random.randint(border, len(maze) - border)
    treasure_coordinates = (abs(x) if abs(x) < max_x - 1 else max_x - 1, abs(y) if abs(y) < max_y - 1 else max_y - 1)

set_point(treasure_coordinates, '$') 
print("treasure is here:",treasure_coordinates) #Отмечаем сокровище на карте
find_a_way(maze, start_point, POSSIBLE_WAYS)    #Ищем путь до сокровища
restore_path(start_point)                       #Восстанавливаем путь до сокровища
find_the_exit(treasure_coordinates, end_point)  #найтивыход 
f = open('maze-for-me-done.txt', 'w')           #Запись в файл
for i in range(len(maze_list)):
    f.write(maze_list[i])
    f.write("\n")
f.close()
print('The number of too long paths: ', large_toexit_ways) 
print("Created'n'written down")