#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int height = 0, width = 0;
int x, y, xt = 0, yt = 0, x11, y11;
char** mazem;
int** mazemint;
int len;
const int WALL = -1;         // непроходимая ячейка
const int BLANK = -9;         // свободная непомеченная ячейка

ofstream fin1("maze-for-u-done.txt");

int input() //open file and reading maze
{
    ifstream fin("maze-for-u.txt");
    char maze;
    int i = 0, j = 0;
    if (!fin)
    {
        cout << "open file error";
        return 0;
    };
    while (fin.get(maze))
    {
        if (maze == '\n') { height++; }
        if (maze != '\n') { width++; }
    }
    width = (width + height) / height;
    cout << "height: " << height << endl << "width: " << width << endl;
    return(width, height);
    fin.close();
}
char** mazematr() // make dynamic matrix
{
    mazem = new char* [height];
    for (int k = 0; k < height; k++) { mazem[k] = new char[width]; }
    return mazem;
}
int** intmazematr() // make dynamic matrix
{
    mazemint = new int* [height];
    for (int k = 0; k < height; k++) { mazemint[k] = new int[width]; }
    return mazemint;
}
void init(char** mazem) // rewriting maze in dynmic matrix
{
    ifstream fin("maze-for-u.txt");

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            fin.get(mazem[i][j]);
        }
    }
    fin.close();
}
int start()//finding start point
{
    for (int i = 0; i < width; i++)
    {
        if (mazem[0][i] == ' ') { x = i; break; }
    }
    cout << x + 1 << "," << y + 1 << " - Start point" << endl;
    return (x, y);
}
void change()
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (mazem[i][j] == '#') { mazemint[i][j] = -1; }
            if (mazem[i][j] == ' ') { mazemint[i][j] = -9; }
            if (mazem[i][j] == 'S') { mazemint[i][j] = -2; }
            if (mazem[i][j] == 'F') { mazemint[i][j] = -3; }
            if (mazem[i][j] == '.') { mazemint[i][j] = -4; }
            if (mazem[i][j] == ',') { mazemint[i][j] = -5; }
        }

    }
}
void changeback()
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (mazemint[i][j] == -1) { mazem[i][j] = '#'; }
            if (mazemint[i][j] == -9) { mazem[i][j] = ' '; }
            if (mazemint[i][j] == -2) { mazem[i][j] = 'S'; }
            if (mazemint[i][j] == len) { mazem[i][j] = 'F'; }
            if (mazemint[i][j] == -4) { mazem[i][j] = '.'; }
            if (mazemint[i][j] > 0) { mazem[i][j] = ','; }
        }
    }
}
bool dfs(int x, int y)// deep-first scan
{
    mazem[yt - 1][xt - 1] = 'S';
    char* point = &mazem[y][x];
    if (*point == 'S') { return true; }

    if (*point == ' ')
    {
        *point = '.';
        if (dfs(x, y + 1)) { *point = '.'; return true; }
        if (dfs(x + 1, y)) { *point = '.'; return true; }
        if (dfs(x, y - 1)) { *point = '.'; return true; }
        if (dfs(x - 1, y)) { *point = '.'; return true; }
        //return true;
    }

    return false;
}
bool bfs(int ax, int ay, int bx, int by, int W, int H, int* px, int* py)   // поиск пути из ячейки (ax, ay) в ячейку (bx, by)
{
    int dx[4] = { 1, 0, -1, 0 };   // смещения, соответствующие соседям ячейки
    int dy[4] = { 0, 1, 0, -1 };   // справа, снизу, слева и сверху
    int d, x, y, k;
    bool stop;

    if (mazemint[ay][ax] == WALL || mazemint[by][bx] == WALL)

    {
        return false;
    }

    d = 0;
    mazemint[ay][ax] = 0;            // стартовая ячейка помечена 0
    do {
        stop = true;               // предполагаем, что все свободные клетки уже помечены
        for (y = 0; y < H; y++)
            for (x = 0; x < W; x++)
                if (mazemint[y][x] == d)                         // ячейка (x, y) помечена числом d
                {
                    for (k = 0; k < 4; ++k)                    // проходим по всем непомеченным соседям
                    {
                        int iy = y + dy[k], ix = x + dx[k];
                        if (iy >= 0 && iy < H && ix >= 0 && ix < W &&
                            (mazemint[iy][ix] == BLANK || mazemint[iy][ix] == -3))
                        {
                            stop = false;              // найдены непомеченные клетки
                            mazemint[iy][ix] = d + 1;      // распространяем волну
                        }
                    }
                }
        d++;
    } while (!stop && mazemint[by][bx] == -3);

    if (mazemint[by][bx] == -3) return false;  // путь не найден
                                               // восстановление пути
    len = mazemint[by][bx];                    // длина кратчайшего пути из (ax, ay) в (bx, by)
    x = bx;
    y = by;
    d = len;
    while (d > 0)
    {
        px[d] = x;
        py[d] = y;                             // записываем ячейку (x, y) в путь
        d--;
        for (k = 0; k < 4; ++k)
        {
            int iy = y + dy[k], ix = x + dx[k];
            if (iy >= 0 && iy < H && ix >= 0 && ix < W &&
                mazemint[iy][ix] == d && mazemint[iy][ix] != 0)
            {
                mazem[iy][ix] = ',';
                x = x + dx[k];
                y = y + dy[k];                 // переходим в ячейку, которая на 1 ближе к старту
                break;
            }
        }
    }
    px[0] = ax;
    py[0] = ay;                                // теперь px[0..len] и py[0..len] - координаты ячеек пути
    return true;
}

int finish(int z)//finding start point
{
    for (int i = 0; i < width; i++)
    {
        if (mazem[z][i] == ' ') { x11 = i; y11 = z; break; }
    }
    cout << x11 + 1 << "," << y11 + 1 << " - finish point" << endl;
    return (x11, y11);
}

void print()//output changed maze
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            cout << mazem[i][j];
            fin1 << mazem[i][j];
        }

    }
}
int xy()
{
    while (true) {
        cin >> xt;
        cin >> yt;
        if (mazem[yt - 1][xt - 1] == '#') { cout << "try another point" << endl; }
        else
        {
            break;
        }
    }
    return xt, yt;
}
int main()
{
    int z;
    cout << "Where the treasure? " << endl;
    input();
    z = height - 1;
    mazematr();
    init(mazem);
    intmazematr();
    int W = width;         // ширина рабочего поля
    int H = height;
    int* px = new int[W * H];
    int* py = new int[W * H]; // координаты ячеек, входящих  путь
    xy();
    start();
    finish(z);
    char* str = &mazem[yt - 1][xt - 1];
    *str = 'S';
    mazem[y11][x11] = 'F';
    change();

    if (!dfs(x, y)){cout << "No path" << endl;}

    bfs(xt - 1, yt - 1, x11, y11, W, H, px, py);
    print();


    for (int i = 0; i < width; i++)//
    {                              //
        delete[] mazem[i];         //clear memory for the matrix
    }                              //
    delete[] mazem;                //
}
