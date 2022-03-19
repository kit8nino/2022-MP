import java.io.FileReader;
import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


import static java.lang.Math.abs;

public class Lab_1
{
    private static final String path_to_file = "maze-for-u.txt";
    private static boolean threasure_is_found = false;
    private static boolean exit_is_found = false;


    public static void main(String[] args) throws IOException {

        List<String> maze = OpenFile(path_to_file);
        List<String> path = OpenFile(path_to_file);

        int max_x = maze.get(0).length();
        int max_y = maze.size();

        String[] POSSIBLE_WAYS = {"N", "E", "W", "S"};

        List<String> path_to_exit = new ArrayList<>();

        for (int i = 0; i < (max_x * max_y); i++) {
            path_to_exit.add(" ");
        }

        List<String> current_path = new ArrayList<>();

        int[] start_point = {0, maze.get(0).indexOf(" ")};

        int[] treasure_is_here = treasure_is_here(max_x, max_y, maze);

        if (!threasure_is_found) {
            find_a_way_to_treasure(maze, start_point, POSSIBLE_WAYS, path_to_exit, current_path, path, treasure_is_here);
        }
        if (threasure_is_found)
        {
            find_a_way(maze, treasure_is_here, POSSIBLE_WAYS, path_to_exit, current_path, path);
        }

        FileWriter writer = new FileWriter("maze-for-me-done.txt.txt");
        for(String str : maze) {
            writer.write(str + " " + System.getProperty("line.separator"));
        }
        writer.close();




    }

    public static int[] treasure_is_here(int max_x, int max_y, List<String> maze)
    {
        boolean good_coord_treasure = false;

        int[] treasure = new int[2];

        while(!good_coord_treasure) {

            System.out.println("Where is threasure? (x is between 1 and " + (max_x - 1) + ")"); // Заменил с 1, а не с 0, чтобы сакровище не спавнилось в стене
            int x = new Scanner(System.in).nextInt();
            System.out.println("Where is threasure? (y is between 1 and " + (max_y - 1) + ")");
            int y = new Scanner(System.in).nextInt();

            if (Character.compare((maze.get(y).charAt(x)), '#') == 0) {
                System.out.println("bad coordinates for the location of treasures");
                continue;
            } else
            {
                if (abs(x) < max_x - 1)
                {
                    treasure[1] = abs(x);
                }
                else treasure[1] = max_x - 1;

                if (abs(y) < max_y - 1)
                {
                    treasure[0] = abs(y);
                }
                else treasure[0] = max_y - 1;
                good_coord_treasure = true;
            }
        }
        return treasure;
    }

    public static List<String> OpenFile(String path) throws IOException {

        FileReader maze = new FileReader(path);

        Scanner scan = new Scanner(maze);

        List<String> maze2 = new ArrayList<>();

        while(scan.hasNextLine())
        {
            maze2.add(scan.nextLine());
        }
        return  maze2;
    }
    private static void find_a_way_to_treasure(List<String> maze, int[] coord, String[] possible_ways, List<String> path_to_treasure, List<String> current_path, List<String> path, int[] treasure_is_here)
    {

        int len_x = maze.size();
        int len_y = maze.get(1).length();
        if (threasure_is_found)
        {
            return;
        }

        if (is_cord_exit(coord, len_x, treasure_is_here))
        {
            threasure_is_found = true;
            System.out.println("new way is found");

            path_to_treasure = current_path;

            System.out.println(path_to_treasure);

            System.out.println("Size path_to_treasure = " + path_to_treasure.size());

            paint_path(maze, path_to_treasure, treasure_is_here);

            return;
        }
        if (!is_coord_in_maze(maze, coord))
        {
            System.out.println("not in bounds!");
            coord[0] = coord[0] - 1;

            return;
        }
        if (current_path.size() > path_to_treasure.size())
        {
            System.out.println("too large path");
            System.out.println(current_path.size() + ">" + path_to_treasure.size());

            return;
        }
       try {
            for (String direction : possible_ways) {
                if (is_path_clean(maze, step(coord, direction), coord)) {

                    current_path.add(direction);

                    find_a_way_to_treasure(maze, step(coord, direction), cut_way_back(direction), path_to_treasure, current_path, path, treasure_is_here);
                }
            }
        }
        catch (Exception ex)
        {
            return;
        }
       if (current_path.size() > 0) {
           current_path.remove(current_path.size() - 1);
       }
    }
    private static boolean is_coord_in_maze(List<String> maze, int[] coord)
    {
        if (coord[0] < 0 || coord[0] > maze.size() - 1)
        {
            return false;
        }
        if (coord[1] < 0 || coord[1] > maze.get(0).length() - 1)
        {
            return false;
        }
        return  true;

    }

    private static boolean is_cord_exit(int[] coord, int max_x, int[] treasure_is_here)
    {
        if ((coord[0] == treasure_is_here[0]) && (coord[1] == treasure_is_here[1]))
        {
                return true;
        }
        return false;
    }

    private static boolean is_path_clean(List<String> maze, int[] coord, int[] lastcoord)
    {
        try {
            if (Character.compare((maze.get(coord[0]).charAt(coord[1])), '#') == 0) {return false;}

            if (lastcoord[0] == coord[0] && lastcoord[1] == coord[1]) {return false;}

            return true;
        }
        catch (Exception ex)
        {
            return true;
        }
    }

    private static int[] step(int[] coord, String directions)
    {
        if (directions.equals("N") && (coord[0] != 0)){return step_N(coord);}
        else if (directions.equals("S")) {return step_S(coord);}
        else if (directions.equals("W") && coord[1] != 0) {return step_W(coord);}
        else if (directions.equals("E")) {return step_E(coord);}

        return coord;
    }

    private static int[] step_N(int[] coord)
    {
        int[] step_n = {(coord[0]) - 1, coord[1]};

        return step_n;
    }
    private static int[] step_E(int[] coord)
    {
        int[] step_e = {coord[0], (coord[1]) + 1};

        return step_e;
    }
    private static int[] step_S(int[] coord)
    {
        int[] step_s = {coord[0] + 1, coord[1]};

        return step_s;
    }
    private static int[] step_W(int[] coord)
    {
        int[] step_w = {coord[0], coord[1] - 1};

        return step_w;
    }

    private static String[] cut_way_back(String direction)
    {
        if (direction.equals("N"))
        {
            String[] retrn = {"N", "E", "W"};

            return retrn;
        }
        if (direction.equals("S"))
        {
            String[] retrn = {"E", "W", "S"};

            return retrn;
        }
        if (direction.equals("E"))
        {
            String[] retrn = {"E", "N", "S"};

            return retrn;
        }
        if (direction.equals("W"))
        {
            String[] retrn = {"W", "N", "S"};

            return retrn;
        }
        String[] retrn = {direction, direction, direction};

        return retrn;
    }

    private static void find_a_way(List<String> maze, int[] coord, String[] possible_ways, List<String> path_to_exit, List<String> current_path, List<String> path)
    {
        int last_step = 0;

        List<int[]> the_path_of_number = new ArrayList<>();
        the_path_of_number.add(new int[]{coord[0], coord[1], 0});

        int[] exit = {maze.size() - 1, maze.get(maze.size() - 1).indexOf(" ")};

        int count_path = 1;

        List<int[]> list_of_pathes = new ArrayList<>();
        list_of_pathes.add(coord);

        char[] save_path;
        save_path = path.get(coord[0]).toCharArray();
        save_path[coord[1]] = '0';

        path.set(coord[0], String.valueOf((save_path)));

        while(!exit_is_found)
        {
            List<int[]> list_of_pathes_save = new ArrayList<>(list_of_pathes);
            for (int[] cord : list_of_pathes) {
                for (String direction : possible_ways) {
                    if (is_path_clean(maze, step(cord, direction), cord)) {

                        int[] cord_next = step(cord, direction);

                        if((the_path_of_number.get(the_path_of_number.size() - 1)[0] == exit[0]) && (the_path_of_number.get(the_path_of_number.size() - 1)[1] == exit[1]))
                        {
                            exit_is_found = true;
                            break;
                        }

                        save_path = path.get(cord_next[0]).toCharArray();

                        if (Character.compare((path.get(cord_next[0]).charAt(cord_next[1])), ' ') == 0)
                        {
                            save_path[cord_next[1]] = '.';
                            path.set(cord_next[0], String.valueOf(save_path));
                            current_path.add(direction);

                            the_path_of_number.add(new int[]{cord_next[0], cord_next[1], count_path});

                            list_of_pathes_save.add(step(cord, direction));
                        }
                    }
                }
                list_of_pathes_save.remove(0);
            }

            list_of_pathes = list_of_pathes_save;
            count_path ++;

                if(exit_is_found){
                    System.out.println("the path to the exit = " + the_path_of_number.get(the_path_of_number.size() - 1)[2]);
                    break;
                }
        }

        last_step = the_path_of_number.size() - 1;
        int[] end_point  = {maze.size() - 1, maze.get(maze.size() - 1).indexOf(" ")};

        for(int i = the_path_of_number.get(the_path_of_number.size() - 1)[2]; i > 0; i-- )
        {
            for (int k = the_path_of_number.size() - 1 ; k > 0; k -- )
            {
                if (cheack_step_back(i, k, the_path_of_number, last_step))
                {
                    track(the_path_of_number.get(k),maze, ',');
                    last_step = k;
                    k = the_path_of_number.size() - 1;
                    break;
                }
            }
        }

        track(end_point, maze, ',');

    }


    private static boolean cheack_step_back(int i, int k, List<int[]> the_path_of_number, int last_step)
    {
        if  (i == the_path_of_number.get(k)[2])
        {
            if (the_path_of_number.get(last_step)[0] == (the_path_of_number.get(k)[0] + 1))
            {
                if (the_path_of_number.get(last_step)[1] == the_path_of_number.get(k)[1])
                {return true;}
            }

            if (the_path_of_number.get(last_step)[0] == (the_path_of_number.get(k)[0] - 1))
            {
                if (the_path_of_number.get(last_step)[1] == the_path_of_number.get(k)[1])
                {return true;}
            }

            if (the_path_of_number.get(last_step)[1] == (the_path_of_number.get(k)[1] + 1))
            {
                if (the_path_of_number.get(last_step)[0] == the_path_of_number.get(k)[0])
                {return true;}
            }

            if (the_path_of_number.get(last_step)[1] == (the_path_of_number.get(k)[1] - 1))
            {
                if (the_path_of_number.get(last_step)[0] == the_path_of_number.get(k)[0])
                {return true;}
            }

        }
        return false;
    }

    private static void paint_path(List<String> maze, List<String> path_to_treasure, int[] treasure_is_here)
    {
        int[] start_point = {0, maze.get(0).indexOf(" ")};

        path_to_treasure.remove(path_to_treasure.size() - 1);
        track(start_point, maze, '.');


            for(String pathToTreasure: path_to_treasure) {
                if (pathToTreasure.equals("S") && (start_point[1] < maze.size() - 1)) {

                    start_point[0] = start_point[0] + 1;

                    track(start_point, maze, '.');

                }
                if (pathToTreasure.equals("N") && (start_point[1] < maze.size() - 1)) {

                    start_point[0] = start_point[0] - 1;

                    track(start_point, maze, '.');

                }
                if (pathToTreasure.equals("E") && (start_point[1] < maze.size() - 1)) {
                    start_point[1] = start_point[1] + 1;

                    track(start_point, maze, '.');

                }
                if (pathToTreasure.equals("W") && (start_point[1] < maze.size() - 1)) {
                    start_point[1] = start_point[1] - 1;

                    track(start_point, maze, '.');
                }
            }

        char[] final_path;
        final_path = maze.get(treasure_is_here[0] ).toCharArray();
        final_path[treasure_is_here[1]] = '*';
        maze.set(treasure_is_here[0], String.valueOf((final_path)));
    }

    private static void track(int[] start_point, List<String> maze, char a)
    {
        char[] final_path;
        final_path = maze.get(start_point[0]).toCharArray();
        final_path[start_point[1]] = a;
        maze.set(start_point[0], String.valueOf((final_path)));
    }
    private static void track2(int[] path_of_number, List<String> maze, char a)
    {
        char[] final_path;
        final_path = maze.get(path_of_number[0]).toCharArray();
        final_path[path_of_number[1]] = a;
        maze.set(path_of_number[0], String.valueOf((final_path)));

    }


}
