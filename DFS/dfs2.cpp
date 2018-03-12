#include <iostream>
#define inf 99999999

using namespace std;

int e[7][7];
bool visited[7] = {false};

void dfs(int now){
    cout << now << "  visited." << endl;
    for (int i = 1; i <= 6; i++){
        if (!visited[i] && e[now][i] == 1){
            visited[i] = true;
            dfs(i);
        }
    }
}

int main(){
    for (int i = 1; i <= 6; i++){
        for (int j = 1; j <= 6; j++){
            e[i][j] = inf;  // e[i][j] 為 i 到 j 的距離, inf 代表走不到
        } e[i][i] = 0;  // 0 代表就是自己
    }
    for (int i = 0; i < 8; i++){
        int a, b;
        cin >> a >> b;
        e[a][b] = 1;  // 1 代表可以走到
        e[b][a] = 1;
    }

    visited[1] = true;
    dfs(1);

    return 0;
}
