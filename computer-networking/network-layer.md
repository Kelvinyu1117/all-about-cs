# Network Layer
## Routing Algorithms
### Type of Algorithms
* Link State
  * Requires the knowledge of the whole network topology. i.e. the link cost known to all nodes
  * The router sends the information of its neighbour though flooding (boardcasting)
* Distance Vector
  *  The update of routing table only depends on the current node and its neighbours 
### Dijkstra Algorithm
* Link State algorithm
* Compute the shortest path (i.e. least cost) from each node to all other nodes
* Worst case time complexity: $O(|V|^2)$. It can be improved to $O(|E| + log(|V|)$ by using prioriy queue,where $|V|$ is number of node and $|E|$ is the number of edges in the graph
* Pseudocode
```
    For each node i in graph G:
        if(S != i)
            D(S, i) = INF
        else
            D(S, i) = 0

    Add S to the set N

    Loop:
        Node c = Extract_Min(N)
        For each neighbours j of C:
            if(!visited[j]) 
                D(c, j) = Min(D(j), D(c) + D(c, j))
                add j to set N

        visited[c] = true
    While N is not empty
        
```
### Bellman Ford Algorithm
* Distance vector algorithm
* use the bellman ford equation to calculate the shortest distance from the current node to each node i:
  
  $D_c(i) = min(D_c(v) + D_v(i))$, where v is a intermediate node
* Pseudocode
```
When node c received the distance vectors from its neighbours

use the bellman ford equation to update the distance vector of itself, and send it to its neighbours
```
*