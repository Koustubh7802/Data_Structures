//Graph Implementation (Undirected)

#include <iostream>
using namespace std;

int main(){

    //No. of vertices (x) and edges (y)
    int x,y;

    cout<<"Number of vertices = ";
    cin>>x;
    cout<<"Number of edges = ";
    cin>>y;

    //Adjacency matrix of size (x*x):
    int adj[x][x];
    int u,v;

    //**Graph is 0 based indexed but user is showed 0th vertex as 1**
    for(int i=0; i<y; i++){
        cout<<"EDGE "<<i+1<<endl;
        cout<<"Vertex (from) --> ";
        cin>>u;
        cout<<"Vertex (to) --> ";
        cin>>v;

        adj[u-1][v-1] = 1;
        adj[v-1][u-1] = 1;

        cout<<endl;
    }


    //Display of the graph created
    cout<<"\nGRAPH:\n";
    for(int i=0; i<x; i++){
        for(int j=0; j<x; j++){
            if(adj[i][j]!=1){
                adj[i][j] = 0;
            }
            cout<<adj[i][j]<<" ";
        }
        cout<<endl;
    }

    return 0;
}