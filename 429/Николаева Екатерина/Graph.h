#pragma once

#include <map>
#include <vector>
#include <algorithm>
#include <queue>


class vertex_nonexist_exception : public std::exception {
private:
    const char* msg;
public:
    vertex_nonexist_exception() : msg{"invalid vertex"} {
    }
    const char* what() const noexcept override {
        return msg;
    }
};

template<typename T>
class Graph {
public:
    //map это контейнер типа ключ-значение
    using GraphMap = std::map<T,std::vector<T>>; //ключ - вершина, соседи - значение этой вершины
private:
    GraphMap graph;
    void recDFS(const T&, const T&, std::vector<T>&, std::map<T,bool>&) const;
public:
    void addEdge(const T&, const T&);
    void DFS(const T&, const T&, std::vector<T>&) const;
    void BFS(const T&, const T&, std::vector<T>&) const;
};

template<typename T>
void Graph<T>::addEdge(const T& v1, const T& v2) {
    graph[v1].push_back(v2);
    graph[v2];              
}

template<typename T>
void Graph<T>::DFS(const T& root, const T& target, std::vector<T>& route) const {
    if(graph.find(root) == graph.cend() ) throw vertex_nonexist_exception{};  
    if(graph.find(target) == graph.cend()) throw vertex_nonexist_exception{}; 

    std::map<T,bool> excluded{};  //карта исключенных вершин
    recDFS(root, target, route, excluded);
    std::reverse(route.begin(), route.end());   
}

template<typename T>
void Graph<T>::recDFS(const T& root, const T& target, std::vector<T>& route, std::map<T,bool>& excluded) const{
    excluded[root] = true;
    if(root == target) route.push_back(root);
    else {
        typename std::vector<T>::const_iterator cit;
        for(cit = graph.at(root).cbegin(); cit != graph.at(root).cend(); cit++) {
            if(excluded[*cit]) continue;
            this->recDFS(*cit, target, route, excluded);
            if(!route.empty()) {
                route.push_back(root);
                break;
            }
        }
    }
}

template<typename T>
void Graph<T>::BFS(const T& root, const T& target, std::vector<T>& route) const {
    if(graph.find(root) == graph.cend()) throw vertex_nonexist_exception{};
    if(graph.find(target) == graph.cend()) throw vertex_nonexist_exception{};

    // graph traversal
    std::queue<T> searchQueue{}; 
    searchQueue.push(root); 
    std::map<T, bool> excluded{};
    std::map<T, T> ancestors{};  //карта предков
    bool targetFound{false};
    while (!searchQueue.empty()) {
        const T current{searchQueue.front()}; 
        searchQueue.pop();
        if (current == target) {
            targetFound = true;
            break;
        }
        else
        {
            typename std::vector<T>::const_iterator cit;
            for(cit = graph.at(current).cbegin(); cit != graph.at(current).cend(); cit++)
            {
                if (!excluded[*cit]) {
                    excluded[*cit] = true;
                    searchQueue.push(*cit);
                    ancestors[*cit] = current;
                }
            }
        }
    }

    // route restore
    if(targetFound) {
        T current {target};
        while(!(current == root)) {
            route.push_back(current);
            current = ancestors[current];
        }
        route.push_back(root);
        std::reverse(route.begin(), route.end());
    }
}