import numpy as np

def protivopolozhnoye(way):
    if way=="up":
        return "down"
    if way=="left":
        return "right"
    if way=="down":
        return "up"
    if way=="right":
        return "left"                

def are_borders_ok(coordx, coordy):
    global len_lab_x, len_lab_y
    if coordx>len_lab_x-1 or coordx<0 or coordy>len_lab_y-1 or coordy<0:
        return False
    return True

def go(coordx, coordy, way):
    if way=="up":
        return (coordx, coordy-1)
    if way=="left":
        return (coordx-1, coordy)
    if way=="down":
        return (coordx, coordy+1)
    if way=="right":
        return (coordx+1, coordy)

def no_way_back(way):
    global all_ways
    new_list=all_ways.copy()
    new_list.remove(protivopolozhnoye(way))
    return new_list

def drawdraw(coordx, coordy, s):
    global stroki
    stroki[coordy]=str(stroki[coordy][:coordx]+s+stroki[coordy][coordx+1:])

def find_the_treasure(coordx, coordy, waylist):
    global treasure_path, we_find_treasure_path, stroki, coord_treasure_x, coord_treasure_y
    if coordx==coord_treasure_x and coordy==coord_treasure_y:
        we_find_treasure_path=True
        return
    for way in waylist:
        coordx1, coordy1 = go(coordx, coordy, way)
        if are_borders_ok(coordx1, coordy1):
            if stroki[coordy][coordx]==' ':
                treasure_path.append(way)
                find_the_treasure(coordx1, coordy1, no_way_back(way))
                if we_find_treasure_path:
                    return
                del treasure_path[len(treasure_path)-1]
    return


def find_exit_path(coordx, coordy):
    global exit_path, we_find_exit_path, finding_matrix, coord_treasure_x, coord_treasure_y, stroki, len_lab_y
    if coordx==coord_treasure_x and coordy==coord_treasure_y:
        we_find_exit_path=True
        return
    for way in all_ways:
        coordx1, coordy1 = go(coordx, coordy, way)
        if are_borders_ok(coordx1, coordy1):
            if finding_matrix[coordy1][coordx1]==finding_matrix[coordy][coordx]-1 or (coordx==stroki[len_lab_y-1].find(' ') and coordy==len_lab_y-1):
                exit_path.append(way)
                find_exit_path(coordx1, coordy1)
                if we_find_exit_path:
                    return

all_ways=["up", "left", "down", "right"]

with open('maze-for-u.txt') as file:
    stroki=file.readlines()

file.close()

len_lab_x=len(stroki[0])-1 # Переход на новую строку не считаем
len_lab_y=len(stroki)

space_is_correct=False

while not space_is_correct:
    coord_treasure_x=int(input(f"Enter treasure coord x from 0 to {len_lab_x-1}: "))
    coord_treasure_y=int(input(f"Enter treasure coord y from 0 to {len_lab_y-1}: "))
    if are_borders_ok(coord_treasure_x, coord_treasure_y):
        if stroki[coord_treasure_y][coord_treasure_x]=='#':
            print("Here is not a space")
        else:
            space_is_correct=True
    else:
        print() # Для красоты
        print("Error")

print() # Для красоты

treasure_path=[]
exit_path=[]

we_find_treasure_path=False
we_find_exit_path=False

drawdraw(coord_treasure_x, coord_treasure_y, '*')

if stroki[0].find('*')==-1: # если сокровище в самом начале
    find_the_treasure(stroki[0].find(' '), 0, all_ways)

for_visiting = []
for_visiting.append([coord_treasure_x, coord_treasure_y, 2]) # 2, чтобы избежать возможных ошибок

finding_matrix = np.zeros((len_lab_y, len_lab_x))

for i in range(len_lab_y):
    for j in range(len_lab_x):
        if stroki[i][j]=='#':
            finding_matrix[i][j]=-2 # -2, чтобы избежать возможных ошибок

while len(for_visiting)>0:  # Поиск в ширину
    x, y, i = for_visiting.pop(0)
    for way in all_ways:
        x1, y1 = go(x, y, way)
        if are_borders_ok(x1, y1) and finding_matrix[y1][x1]==0:
            finding_matrix[y][x]=i
            for_visiting.append([x1, y1, i+1])

find_exit_path(stroki[len_lab_y-1].find(' '), len_lab_y-1)

final_exit_path=[]

for i in range(len(exit_path)):
    w=exit_path.pop()
    final_exit_path.append(protivopolozhnoye(w))

print(final_exit_path)

ax=stroki[0].find(' ')
ay=0

if stroki[0].find('*')==-1:
    for n in treasure_path:
        drawdraw(ax, ay, '.')
        ax, ay = go(ax, ay, n) # Саму точку сокровища не зарисовываем

ax=coord_treasure_x
ay=coord_treasure_y

for n in final_exit_path:
    ax, ay = go(ax, ay, n) # Саму точку сокровища не зарисовываем
    drawdraw(ax, ay, ',')

"""
ff=open('proverka.txt', 'w') # Матрица в файле для проверки
for i in range(len_lab_y):
    for j in range(len_lab_x):
        m=str(int(finding_matrix[i][j]))
        ff.write(m)
        for k in range(5-len(m)):
            ff.write(" ")
    ff.write("\n")

ff.close()
"""
f=open('maze-for-me-done.txt', 'w')
for i in range(len(stroki)):
    f.write(stroki[i]) # Здесь с переходом на новую строку
f.close()

print() # Для красоты
print("Complited")