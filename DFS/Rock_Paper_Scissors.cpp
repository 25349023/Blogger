#include <iostream>

using namespace std;

string gesture[3] = {"剪刀", "石頭", "布"};
bool visited[3] = {false};
string arrangement[3];

void dfs(int layer){
    if (layer == 3){
        for (int i = 0; i < 3; i++){
            cout << arrangement[i] << "\t";
        }
        cout << endl;
        return;
    }
    for (int i = 0; i < 3; i++){
        if (visited[i]){
            continue;
        }
        visited[i] = true;
        arrangement[layer] = gesture[i];
        dfs(layer + 1);
        visited[i] = false;
    }
}

int main(){
    dfs(0);

    return 0;
}
