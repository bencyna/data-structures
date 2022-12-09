#include <iostream>
#include <vector> 
#include <unordered_map> 
#include <queue> 

using namespace std;

void BFS(vector<vector<int>> graph);

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

    BFS(adjList);
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
            if (seen.find(vertices[i]) == seen.end()) {
                seen.insert({vertices[i], vertices[i]});
                queue.push(vertices[i]);
            }
        }

        cout << index << endl;
    }
}