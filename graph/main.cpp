#include <iostream>
#include <vector> 
#include <unordered_map> 
#include <queue> 

using namespace std;

void BFS(vector<vector<int>> graph);

void DFS(vector<vector<int>> graph, unordered_map<int, int> * seen, int cur);

#include <map>

int main() {
    vector<vector<int>> adjList = {
            {1, 3},
            {0},
            {3, 8},
            {0, 4, 5, 2},
            {3, 6},
            {3},
            {4, 7},
            {6},
            {2},
        };
    std::unordered_map<int, int> * seen = new unordered_map<int, int>();

    BFS(adjList);
    DFS(adjList, seen, 0);

    delete seen;
    
    return 0; 
}

void BFS(vector<vector<int>> graph) {
    std::queue<int> queue;
    queue.push(0);
    vector<int> values;
    std::unordered_map<int, int> seen;

    while (!queue.empty()) {
        int index = queue.front();
        vector<int> vertices = graph.at(index);
        queue.pop();
        seen.insert({index, index});
        
        for (int i = 0; i < vertices.size(); i++) {
            // cout << "vertice: " << vertices[i] << endl;
            if (seen.find(vertices.at(i)) == seen.end()) {
                seen.insert({vertices.at(i), vertices.at(i)});
                queue.push(vertices.at(i));
            }
        }

        cout << index << endl;
    }
}

void DFS(vector<vector<int>> graph, unordered_map<int, int> * seen, int cur) {
    if (seen->find(cur) != seen->end()) {
        return;
    } 

    cout << cur << endl;

    seen->insert({cur, cur});

    for (int i = 0; i < graph.at(cur).size(); i++) {
        DFS(graph, seen, graph.at(cur).at(i));
    }
}  