#include <iostream>

using namespace std;

class Node{
public:
    string data;
    Node* next[3] = {nullptr, nullptr, nullptr};

    Node(string s): data(s){
    }
};

Node* buildTree(){
    Node* root = new Node("red-1");
    root->next[0] = new Node("orange-2");
    root->next[1] = new Node("lime-3");
    root->next[2] = new Node("green-4");
    root->next[0]->next[0] = new Node("yellow-5");
    root->next[2]->next[0] = new Node("blue-6");
    root->next[2]->next[1] = new Node("violet-7");
    
    return root;
}

void dfs(Node* start){
    if (start == nullptr){
        return;
    }
    cout << start->data << "  visited." << endl;
    for (int i = 0; i < 3; i++){
        dfs(start->next[i]);
    }
}

int main(){
    Node *tree = buildTree();
    dfs(tree);
    return 0;
}
