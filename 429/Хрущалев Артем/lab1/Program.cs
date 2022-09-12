using System;

namespace lab1
{
    public class Node // Класс узла(вершины)
    { 
        public (int x, int y) Coordinates { get; private set; }
        public (int x, int y) ParentCoordinates { get; private set; }
        public List<Node> childs { get; private set; }
        public Node((int x, int y) x_and_y){ // Конструктор для root
            this.Coordinates = x_and_y;
            childs = new List<Node>();
        } 
        public Node((int x, int y) x_and_y, (int xParent,int yParent) x_and_y_parent ){ // Конструктор для всех child
            this.Coordinates = x_and_y;
            this.ParentCoordinates = x_and_y_parent;
            childs = new List<Node>();
        }
    } 

    public class Graph
    {
        public Node RootNode { get; set; } // Корень графа
        public (int xRoot,int yRoot) Root { get; set; } // Корень графа (координаты)
        public char[][] Matrix { get; set; } // Лабиринт через матрицу
        public Graph(char[][] matrix, (int,int) root){
            this.Matrix = matrix;
            this.Root = root;
            this.RootNode = new Node((root));
            BuildGraph(RootNode);

        } // Конструктор
        public bool CheckNord((int x,int y) currentCoordinates){
            if (currentCoordinates.x > 0){
                if (Matrix[currentCoordinates.x - 1][currentCoordinates.y] == ' ')
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
            else{
                return false;
            }
        }
        public bool CheckEast((int x,int y) currentCoordinates){
            if (currentCoordinates.y < 127){
                if (Matrix[currentCoordinates.x][currentCoordinates.y + 1] == ' ')
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
            else{
                return false;
            }
        }
        
        public bool CheckSouth((int x,int y) currentCoordinates){
            if (currentCoordinates.x < 279){
                if (Matrix[currentCoordinates.x + 1][currentCoordinates.y] == ' ')
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
            else{
                return false;
            }
        }
        
        public bool CheckWest((int x,int y) currentCoordinates){
            if (currentCoordinates.y > 0){
                if (Matrix[currentCoordinates.x][currentCoordinates.y - 1] == ' ')
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
            else{
                return false;
            }
        }

        public void BuildGraph(Node node){ // Сборка графа с выбором корневой вершины
            
            
            if (CheckNord((node.Coordinates.x , node.Coordinates.y)) &&
            (((node.Coordinates.x-1,node.Coordinates.y) != node.ParentCoordinates) 
            || node.ParentCoordinates == (null,null))) // Проверяем проход наверх
            {
                node.childs.Add(new Node((node.Coordinates.x-1,node.Coordinates.y), (node.Coordinates.x,node.Coordinates.y)) );
            } 

            if (CheckSouth((node.Coordinates.x , node.Coordinates.y)) &&
            (((node.Coordinates.x+1,node.Coordinates.y) != node.ParentCoordinates) 
            || node.ParentCoordinates == (null,null))) // Проверяем проход вниз
            {
                node.childs.Add(new Node((node.Coordinates.x+1,node.Coordinates.y), (node.Coordinates.x,node.Coordinates.y)) );
            } 

            if (CheckWest((node.Coordinates.x , node.Coordinates.y)) &&
            (((node.Coordinates.x,node.Coordinates.y-1) != node.ParentCoordinates) 
            || node.ParentCoordinates == (null,null))) // Проверяем проход влево
            {
                node.childs.Add(new Node((node.Coordinates.x,node.Coordinates.y-1), (node.Coordinates.x,node.Coordinates.y)) );
            }

            if (CheckEast((node.Coordinates.x , node.Coordinates.y)) &&
            (((node.Coordinates.x,node.Coordinates.y+1) != node.ParentCoordinates) 
            || node.ParentCoordinates == (null,null))) // Проверяем проход вправо
            {
                node.childs.Add(new Node((node.Coordinates.x,node.Coordinates.y+1), (node.Coordinates.x,node.Coordinates.y)) );
            }

            if (node.childs.Count == 0)
            {
                return ;
            }

            foreach (var child in node.childs)
            {
                BuildGraph(child);
            }
        }

        public void PrintAll(Node node){ // Метод для проверки правильности сборки графа
            Matrix[node.Coordinates.x][node.Coordinates.y] = 'X';
            foreach (var child in node.childs)
            {
                PrintAll(child);
            }
        }

        public Stack<Node> SearchInDepth((int x, int y) Destination){
            Stack<Node> path = new Stack<Node>();
            List<Node> list = new List<Node>();
            bool flagContainAll;
            bool flagContainAny;
            Node currentNode = RootNode;
            var nodes = new Stack<Node>();
            path.Push(currentNode);
            while (true)
            {
                if (currentNode.Coordinates.x == Destination.x && currentNode.Coordinates.y == Destination.y){
                    return path;
                }
                flagContainAll = true;
                flagContainAny = false;
                foreach (var item in currentNode.childs)
                {
                    if(! list.Contains(item)){
                        flagContainAll = false;
                    }
                    if( list.Contains(item)){
                        flagContainAny = true;
                    }
                }
                if (flagContainAll)
                {
                    foreach (var item in currentNode.childs)
                    {
                        list.Remove(item);
                    }
                    list.Add(currentNode);
                    path.Pop();
                    currentNode = path.Peek();
                    continue;
                }
                if (flagContainAny)
                {
                    currentNode = nodes.Pop();
                    path.Push(currentNode);
                    continue;
                }
                if(currentNode.childs.Count != 0){
                    foreach (var node in currentNode.childs)
                    {
                    nodes.Push(node);
                    }
                    currentNode = nodes.Pop();
                    path.Push(currentNode);
                    continue;
                }
                if (currentNode.childs.Count == 0)
                {
                    
                    list.Add(path.Pop());
                    currentNode = path.Peek();
                }
                
            }

        }
        public Stack<Node> SearchInBreadth((int x, int y) Destination){
            Stack<Node> path = new Stack<Node>();
            List<Node> list = new List<Node>();
            Node currentNode = RootNode;
            var nodes = new Queue<Node>();
            path.Push(currentNode);
            
            while (true)
            {
                if (currentNode.Coordinates.x == Destination.x && currentNode.Coordinates.y == Destination.y){
                    path.Push(currentNode);
                    while (currentNode != RootNode)
                    {
                        foreach (var item in list)
                        {
                            if(item.Coordinates == currentNode.ParentCoordinates){
                                path.Push(item);
                                currentNode = item;
                            }
                        }
                    }
                    return path;
                }

                list.Add(currentNode);
                foreach (var child in currentNode.childs)
                {
                    nodes.Enqueue(child);
                }
                currentNode = nodes.Dequeue();
            }
            
        }
}
    internal class Program
    {
        static void Main(string[] args)
        {
            string path = @$"{Environment.CurrentDirectory}\maze-for-u.txt";
            string[] lines = System.IO.File.ReadAllLines(path); // чтение файла
            char[][] matrix = new char[lines.Length][];
            for (int i = 0; i < lines.Length; i++)
            {
                matrix[i] = lines[i].ToCharArray();
            }

            (int x, int y) treasury;
            Console.WriteLine("Ввод координаты Сокровища");
            Console.WriteLine("x - номер строки: "); 
            treasury.x =  Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("y - номер символа в строке: ");
            treasury.y =  Convert.ToInt32(Console.ReadLine());

            Graph graphToTreasury = new Graph(matrix, (0, 2));
            Graph graphToExit = new Graph(matrix, treasury);
            Node temp = new Node((0,0));
            

            Stack<Node> pathToTreasury = graphToTreasury.SearchInDepth(treasury);
            Stack<Node> pathToExit = graphToExit.SearchInBreadth((279, 126));
            
            while (pathToTreasury.Count > 0)
            {
                temp = pathToTreasury.Pop();
                matrix[temp.Coordinates.x][temp.Coordinates.y] = '.';
            }
            
            while (pathToExit.Count > 0)
            {
                temp = pathToExit.Pop();
                matrix[temp.Coordinates.x][temp.Coordinates.y] = ',';
            }
            matrix[treasury.x][treasury.y] = '*';


            string outputPath = @$"{Environment.CurrentDirectory}\maze-for-me-done.txt";
            if(! File.Exists(outputPath)){
                File.Create($"maze-for-me-done.txt").Close();
            }
            for (int i = 0; i < lines.Length; i++)
            {
                lines[i] = new string(matrix[i]);
            }
            
            File.WriteAllLines(outputPath, lines);
            
        }   
    }
}