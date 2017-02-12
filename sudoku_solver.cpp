#include <bits/stdc++.h>
using namespace std;
#define vi vector <int>
#define pii pair < int,int >
#define pvii pair < vi , pii >
#define pb push_back
#define mp make_pair
#define fr first
#define se second
#define vvi vector < vi >

int flag=0;

void print(vvi ans)
{
    for (int i=0;i<9;i++){
        for (int j=0;j<9;j++){
            cout<<ans[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;
}

bool check( vvi cur )
{
    for (int i=0;i<9;i++){
        for (int j=0;j<9;j++){
            if (cur[i][j] == 0)
                return false;
        }
    }
    return true;
}

inline vi fillone(vi canbe)
{
    for (int i=0;i<10;i++)
        canbe[i]=1;
    return canbe;
}

inline vi rowcheck( vvi cur , vi canbe , int r , int c )
{
    for (int i=0;i<9;i++){
        if (cur[r][i] != 0)
            canbe[cur[r][i]]=0;
    }
    return canbe;
}

inline vi colcheck( vvi cur , vi canbe , int r , int c )
{
    for (int i=0;i<9;i++){
        if (cur[i][c] != 0)
            canbe[cur[i][c]]=0;
    }
    return canbe;
}

inline vi blockcheck( vvi cur, vi canbe , int r, int c )
{
    int rr=r-r%3;
    int cc=c-c%3;
    for (int i=rr;i<rr+3;i++){
        for(int j=cc;j<cc+3;j++){
            if (cur[i][j] != 0)
                canbe[cur[i][j]]=0;
        }
    }
    return canbe;
}

int degree_heuristic( vvi cur , int r , int c )
{
    int counter = 0;
    for (int i=0;i<9;i++){
        counter += (cur[r][i] == 0) ? 1 : 0;
        counter += (cur[i][c] == 0) ? 1 : 0;
    }
    int rr=r-r%3;
    int cc=c-c%3;
    for (int i=rr;i<rr+3;i++){
        for(int j=cc;j<cc+3;j++){
            if (i== r || j==c) continue;
            counter += (cur[i][j] == 0) ? 1 : 0;
        }
    }
    return counter;
}


pvii mrv_heuristic ( vvi cur )
{
    int mrvmin = INT_MAX;
    int degmin = INT_MIN;
    pvii val;
    for (int i=0;i<9;i++){
        for (int j=0;j<9;j++){
            if (cur[i][j] == 0){
                vi canbe(10);
                canbe = fillone(canbe);
                canbe = rowcheck(cur,canbe,i,j);
                canbe = colcheck(cur,canbe,i,j);
                canbe = blockcheck(cur,canbe,i,j);
                int counter = 0;
                for (int k=1;k<=9;k++){
                    if (canbe[k] == 1)
                        counter++;
                }
                int degval = degree_heuristic(cur,i,j);
                if (counter < mrvmin){
                    mrvmin = counter;
                    degmin = degval;
                    val = mp(canbe,mp(i,j));
                }
                else if (counter == mrvmin && degval > degmin){
                    degmin = degval;
                    val = mp(canbe,mp(i,j));
                }
            }
        }
    }
    return val;
}

void solve( vvi cur )
{
    if (check(cur)){
        flag=1;
        print(cur);
        return;
    }
    pvii mrvval = mrv_heuristic(cur);
    vi canbe = mrvval.fr;
    int i = mrvval.se.fr;
    int j = mrvval.se.se;
    for (int k=1;k<=9;k++){
        if (canbe[k] == 1){
            cur[i][j] = k;
            solve(cur);
            cur[i][j] = 0;
        }
        if (flag == 1)
            return;
    }
}

int main ()
{
    freopen("sudoku_input.txt","r",stdin);
//    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    vvi start;
    for (int i=0;i<9;i++){
        vi temp;
        for (int j=0;j<9;j++){
            int foo;
            cin>>foo;
            temp.pb(foo);
        }
        start.pb(temp);
    }
    solve(start);
}
