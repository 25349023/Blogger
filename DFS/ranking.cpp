#include <iostream>

using namespace std;

bool visited[5] = {false};
int arrangement[3];
string people[5] = {"甲", "乙", "丙", "丁", "戊"};

void dfs(int layer){
    if (layer == 3){
        for (int j = 0; j < 3; j++){
            cout << people[arrangement[j]] << "  ";
        } cout << endl;
        return;
    }

    for (int i = 0; i < 5; i++){
        if (visited[i]){
            continue;
        }
        visited[i] = true;
        arrangement[layer] = i;
        dfs(layer + 1);
        visited[i] = false;
    }
}

int main(){
    dfs(0);

    return 0;
}
