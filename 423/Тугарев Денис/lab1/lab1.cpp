#include <iostream>
#include <vector>
#include <fstream>
#include <string.h>

using namespace std;

void read_maze(vector<char>& maze, int& numb_of_lines, int& numb_of_element_in_line)
{
	fstream maze_read_file;
	maze_read_file.open("maze-for-u.txt", fstream::in);
	char s;
	int elements = 0, lines = 0;
	bool stop_count_el = true;
	while(1)
	{
		maze_read_file.get(s); // чтение одно символа из файла
		if(stop_count_el) elements++; // подсчет количества элемнтов в строке
		if(s == '\n') // подсчет количества строк
		{
			stop_count_el = false;
			lines++;
		}
		maze.push_back(s); // запись считанного из файла элемента в вектор
		if(maze_read_file.eof()) break; // условие окончание чтения (eof - end of file)
	}
	maze_read_file.close();
	numb_of_lines = lines - 1;
	numb_of_element_in_line =elements;
}

void write_to_file(vector<char>& maze)
{
	fstream out;
    out.open("maze-for-me-done.txt", fstream::out);
    if(!out.is_open()) cout << "File cannot be open for output" << endl;
    else
    {
        cout << "Save the data in file" << endl;

        for(int i = 0; i < maze.size(); i++)
            out << maze.at(i);
    }
    out.close();
}

void put_target_on_maze(vector<char>& maze, int& x_target, int& y_target, int& numb_of_lines, int& numb_of_element_in_line)
{
	int coord[2] = {0, 0};
	do
	{
		cout << "Write x : ";
		cin >> coord[0];
		cout << "Write y : ";
		cin >> coord[1];
		if(coord[0] > 0 && coord[1] > 0)
		{
			if (coord[0] <= numb_of_element_in_line-2 && coord[1] <= numb_of_lines) // проверка на выход за границы лабиринта
			{	
				if(maze.at(coord[0] - 1 + (numb_of_element_in_line) * (coord[1]-1)) == ' ') break; 
			}

		}
	}while(true);
	maze.at(coord[0] - 1 + (numb_of_element_in_line) * (coord[1]-1)) = '*';
	x_target = coord[0];
	y_target = coord[1];
}


void road_to_target(vector<char>& maze, int& x_target, int& y_target, int& numb_of_lines, int& numb_of_element_in_line)
{
	int current_x = 0; // текущее значение х в лабиринте при обходе
	int current_y = 0; // текущее значение у в лабиринте при обходе
	bool left=true, right=true, up=true, down=true; // возможные направление движения
	char mat[numb_of_lines][numb_of_element_in_line] = {0}; // матрица, хранящая путь до клада (1 - пройденный путь, 2 - тупик, 0 - не участвует в обходе)
	memset(mat,0,numb_of_lines*numb_of_element_in_line*sizeof(char));


	while(maze.at(current_x) == '#') current_x++; // поиск входа
	mat[0][current_x] = 1;

	while(true)
	{

		// Если путь был пройдет или мы знаем, что там тупик (mat[][] = 2 или = 1) или там стена, то путь закрыт (false)
		// Определение возможного направления движения
		if(mat[current_y][current_x+1] || maze.at(current_x+1 + (numb_of_element_in_line) * (current_y)) == '#') right = false;
		if(mat[current_y][current_x-1] || maze.at(current_x-1 + (numb_of_element_in_line) * (current_y)) == '#') left = false;
		if(current_y != 0 && (mat[current_y-1][current_x] || maze.at(current_x + (numb_of_element_in_line) * (current_y-1)) == '#')) up = false;
		if(mat[current_y+1][current_x] || maze.at(current_x + (numb_of_element_in_line) * (current_y+1)) == '#') down = false;

		// Если мы близки к кладу
		if(maze.at(current_x+1 + (numb_of_element_in_line) * (current_y)) == '*') {left=false; right=true; up=false; down=false;}
		if(maze.at(current_x-1 + (numb_of_element_in_line) * (current_y)) == '*') {left=true; right=false; up=false; down=false;}
		if(current_y != 0 && maze.at(current_x + (numb_of_element_in_line) * (current_y-1)) == '*') {left=false; right=false; up=true; down=false;}
		if(maze.at(current_x + (numb_of_element_in_line) * (current_y+1)) == '*') {left=false; right=false; up=false; down=true;}


		if(!right && !left && !up && !down)
		{
			// Если мы попали в тупик, то движемся в обратном направлении
			mat[current_y][current_x] = 2;
			if(mat[current_y-1][current_x] == 1) current_y--;
			else if(mat[current_y][current_x-1] == 1) current_x--;
			else if(mat[current_y][current_x+1] == 1) current_x++;
			else if(mat[current_y+1][current_x] == 1) current_y++;
		}
		else{
			// Задание приоритета движения
			if(down && current_y > y_target && (right || left || up)) down = false;
			if(up && current_y < y_target && (right || left || down)) up = false;
			if(left && current_x < x_target && (right || down || up)) left = false;
			if(right && current_x > x_target && (down || left || up)) right = false;

			// Движение по лабиринту
			if(down)
			{
				current_y++;
				mat[current_y][current_x] = 1;
			}
			else if(right)
			{
				current_x++;
				mat[current_y][current_x] = 1;
			}else if(left)
			{
				current_x--;
				mat[current_y][current_x] = 1;
			}else if(up)
			{
				current_y--;
				mat[current_y][current_x] = 1;
			}
		}

		

		left=true; right=true; up=true; down=true;
		if(current_y == y_target-1 ) break;
	}

	mat[y_target-1][x_target-1] = 0;

	// Обновление лабиринта (строим путь до клада)
	for(int i = 0; i < numb_of_lines; i++)
	{
		for(int j = 0; j < numb_of_element_in_line; j++)
		{
			if(mat[i][j] == 1)
			{
				maze.at(j + (numb_of_element_in_line) * (i)) = '.';
			}
		}
	}
}



void find_exit(vector<char>& maze, int& x_target, int& y_target, int& numb_of_lines, int& numb_of_element_in_line)
{
	int current_x = x_target-2;
	int current_y = y_target-1 ;
	bool left=true, right=true, up=true, down=true;
	char mat[numb_of_lines][numb_of_element_in_line] = {0};
	memset(mat,0,numb_of_lines*numb_of_element_in_line*sizeof(char));

	while(true)
	{

		if(mat[current_y][current_x+1] || maze.at(current_x+1 + (numb_of_element_in_line) * (current_y)) == '#') right = false;
		if(mat[current_y][current_x-1] || maze.at(current_x-1 + (numb_of_element_in_line) * (current_y)) == '#') left = false;
		if(current_y != 0 && (mat[current_y-1][current_x] || maze.at(current_x + (numb_of_element_in_line) * (current_y-1)) == '#')) up = false;
		if(mat[current_y+1][current_x] || maze.at(current_x + (numb_of_element_in_line) * (current_y+1)) == '#') down = false;

		if(!right && !left && !up && !down)
		{
			mat[current_y][current_x] = 2;
			if(mat[current_y-1][current_x] == 1) current_y--; 
			else if(mat[current_y][current_x-1] == 1) current_x--;
			else if(mat[current_y][current_x+1] == 1) current_x++;
			else if(mat[current_y+1][current_x] == 1) current_y++;
		}
		else{
			if(down)
			{
				current_y++;
				mat[current_y][current_x] = 1;
			}
			else if(right)
			{
				current_x++;
				mat[current_y][current_x] = 1;
			}else if(left)
			{
				current_x--;
				mat[current_y][current_x] = 1;
			}else if(up)
			{
				current_y--;
				mat[current_y][current_x] = 1;
			}
		}

		

		left=true; right=true; up=true; down=true;
		if(current_y == numb_of_lines-1 && current_x == numb_of_element_in_line-3) break;
	}
	
	for(int i = 0; i < numb_of_lines; i++)
	{
		for(int j = 0; j < numb_of_element_in_line; j++)
		{
			if(mat[i][j] == 1)
			{
				if(maze.at(j + (numb_of_element_in_line) * (i)) == '.')
					maze.at(j + (numb_of_element_in_line) * (i)) = ';';
				else
					maze.at(j + (numb_of_element_in_line) * (i)) = ',';
			}
		}
	}
	maze.at(x_target-1 + (numb_of_element_in_line) * (y_target-1)) = '*';
}

int main()
{
	vector<char> maze; // лабиринт
	int numb_of_element_in_line = 0; // число элементов в строке лабиринта
	int numb_of_lines = 0; // число строк в лабиринте

	// положение клада
	int x_target = 0;
	int y_target = 0;

	read_maze(maze, numb_of_lines, numb_of_element_in_line);
	put_target_on_maze(maze, x_target, y_target, numb_of_lines, numb_of_element_in_line);
	road_to_target(maze, x_target, y_target, numb_of_lines, numb_of_element_in_line);
	find_exit(maze, x_target, y_target, numb_of_lines, numb_of_element_in_line);
	write_to_file(maze);
	return 0;
}