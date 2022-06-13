#Плахов Антон 426


def write_maze_done():
    f = open('maze-for-me-done.txt', 'w')
    for m in range(len(maze)):
        for n in range(len(maze[0])):
            if (maze[m][n] == ','):
                f.write(',')
            elif (maze[m][n] == '#'):
                f.write('#')
            elif (maze[m][n] == '.'):
                f.write('.')
            elif (maze[m][n] == '*'):
                f.write('*')
            elif (maze[m][n] == ' '):
                f.write(' ')
        f.write('\n')

    #без этого пишет только половину лабиринта
    f = open('maze-for-me-done.txt', 'r')
    f.close


def get_starting_finishing_points():
    _start = [i for i in range(len(maze[0])) if maze[len(maze)-1][i] == ' ']
    _end = [i for i in range(len(maze[0])) if maze[0][i] == ' ']
    return [0, _end[0]], [len(maze) - 1, _start[0]]


def treasure_locator():
    current_cell = path[len(path) - 1]

    if current_cell == treasure:
        return

    if maze2[current_cell[0] + 1][current_cell[1]] == ' ':
        maze2[current_cell[0] + 1][current_cell[1]] = ','
        path.append([current_cell[0] + 1, current_cell[1]])
        treasure_locator()

    if maze2[current_cell[0]][current_cell[1] + 1] == ' ':
        maze2[current_cell[0]][current_cell[1] + 1] = ','
        path.append([current_cell[0], current_cell[1] + 1])
        treasure_locator()

    if maze2[current_cell[0] - 1][current_cell[1]] == ' ':
        maze2[current_cell[0] - 1][current_cell[1]] = ','
        path.append([current_cell[0] - 1, current_cell[1]])
        treasure_locator()

    if maze2[current_cell[0]][current_cell[1] - 1] == ' ':
        maze2[current_cell[0]][current_cell[1] - 1] = ','
        path.append([current_cell[0], current_cell[1] - 1])
        treasure_locator()

    current_cell = path[len(path) - 1]
    if current_cell != treasure:
        cell_to_remove = path[len(path) - 1]
        path.remove(cell_to_remove)
        maze2[cell_to_remove[0]][cell_to_remove[1]] = ' '


def escape():
    current_cell = path[len(path) - 1]

    if current_cell == finish:
        return

    if maze[current_cell[0] + 1][current_cell[1]] == ' ':
        maze[current_cell[0] + 1][current_cell[1]] = '.'
        path.append([current_cell[0] + 1, current_cell[1]])
        escape()

    if maze[current_cell[0]][current_cell[1] + 1] == ' ':
        maze[current_cell[0]][current_cell[1] + 1] = '.'
        path.append([current_cell[0], current_cell[1] + 1])
        escape()

    if maze[current_cell[0] - 1][current_cell[1]] == ' ':
        maze[current_cell[0] - 1][current_cell[1]] = '.'
        path.append([current_cell[0] - 1, current_cell[1]])
        escape()

    if maze[current_cell[0]][current_cell[1] - 1] == ' ':
        maze[current_cell[0]][current_cell[1] - 1] = '.'
        path.append([current_cell[0], current_cell[1] - 1])
        escape()

    current_cell = path[len(path) - 1]
    if current_cell != finish:
        cell_to_remove = path[len(path) - 1]
        path.remove(cell_to_remove)
        maze[cell_to_remove[0]][cell_to_remove[1]] = ' '


#Открываем файл (сделано плохо, зато думать не надо)
maze = open('maze-for-u.txt', 'r').read().splitlines()
maze = list(map(list,maze))
maze2 = open('maze-for-u.txt', 'r').read().splitlines()
maze2 = list(map(list,maze2))

#Координаты выхода входа и сокровища
start, finish = get_starting_finishing_points()
maze[start[0]][start[1]] = '.'
print('Treasure location X: Enter number between 1 and', len(maze[0]))
x = int(input()) - 1
print('Treasure location Y: Enter number between 1 and', len(maze))
y = int(input()) - 1
treasure = [y,x]
X = x

#main
if maze[y][x] == '#':
    print('Error: treasure is located in the wall')
else:
    path = [start]
    escape()
    path = [start]
    treasure_locator()
    x = len(maze[0]) - 1
    while (maze2[0][x] != ' '):
        x = x - 1
    maze2[0][x] = ','
    for m in range(len(maze)):
        for n in range(len(maze[0])):
            if (maze2[m][n] == ','):
                maze[m][n] = ','
    maze[y][X] = '*'
    write_maze_done()




        
