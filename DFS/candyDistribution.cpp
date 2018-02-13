#include <iostream>

using namespace std;

int current_count[3] = {2, 1, 1};  // 用來儲存各還有幾顆糖果
int arrangement[4];
string candy[3] = {"紅", "藍", "黃"};

void dfs(int layer){
    if (layer == 3){
        for (int j = 0; j < 4; j++){
            cout << candy[arrangement[j]] << "  ";
        } cout << endl;
    }

    for (int i = 0; i < 3; i++){
        if (current_count[i] == 0){  // 如果沒有剩下了
            continue;
        }
        current_count[i]--;  // 用掉一顆
        arrangement[layer] = i;
        dfs(layer + 1);  // 下一層 DFS
        current_count[i]++;
    }
}

int main(){
    dfs(0);

    return 0;
}
