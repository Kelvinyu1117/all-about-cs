# Network Layer
## Routing Algorithms
### Type of Algorithms
* Link State
  * Requires the knowledge of the whole network topology. i.e. the link cost known to all nodes
  * The router sends the information of its neighbour though flooding (boardcasting)
* Distance Vector
  *  The update of routing table only depends on the current node and its neighbours 
* Hybrid
  * Contains some charactistics of the link state and distance vector protocol
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
                Add j to set N

        visited[c] = true
    While N is not empty
```
### Bellman Ford Algorithm
* Distance vector algorithm
* use the Bellman Ford equation to calculate the shortest distance from the current node to each node i:
  
  $D_c(i) = min(D_c(v) + D_v(i))$, where v is a intermediate node
* Pseudocode
```
When node c received the distance vectors from its neighbours

use the bellman ford equation to update the distance vector of itself, and send it to its neighbours
```
#### Problem of count-to-infinity
When the link cost is changed or the link is down, routing loop may occur that the algorithm need too long time to converge or even does not converge.  

#### Solution: Split horizon with poison reverse
The main idea of split horizon is to prevent to advertise the route to the interface which learnt from. With poison reverse machanism, the router will report INF to that interface instead.

### Comparsion between Link state and distance vector algorithm
|                      	| Link State                                                                                	| Distance Vector                                                                             	|   	|   	|
|----------------------	|-------------------------------------------------------------------------------------------	|---------------------------------------------------------------------------------------------	|---	|---	|
| Message complexity   	| Always requires O(VE) messages, flood the link info to all the nodes if it is changed 	| propagate the new link info to the neighbours only if the new cost result in shortest path  	|   	|   	|
| Robustness           	| It will advertise incorrect link cost, but error only stays in its routing table          	| It will advertise incorrect path cost, and propagate the error to the network               	|   	|   	|
| Speed of Convergence 	| Guarantee O(V^2) time in the worst case                                                   	| It may not be converge, because of count-to-infinity problem                                	|   	|   	|

### Hierarchical Routing 
The main idea is that as the routers know the best path to other router in the same domain, and also the destination router in the different domain. So the router in the same domain can be groupped into a cluster, the controlled unit from the individual router itself to the cluster/grouop, such that the size of routing table can be reduced.
* The next hop router in the routing table contains the gateway router in the same domain
#### Disadvantages
* The path may not be optimal, as we don't have the full picture of the network topology.

## Routing in the Internet
The usual practice in Internet routing is to consider the same set of router as a  autonomous system (AS), and apply the different routing algorithm within the AS (Intra-AS routing) and between the AS (Inter-AS routing) based on the need. It makes the networks in the Interet become much more managable.
The main reasons for using this approach instead of just adpoting the traditional routing algorithm are:
* Scale of the network
  * It is difficult to directly applying the algorithm into numerous of routers in the internet as the routing information may require excessive of memory for storage
* Adminstrative policy 
  * Some set of routers belongs to certain organizations. They may have special policies in term of network adminstration.
### Type of routing algorithms
* Intra-AS algorithm
* Inter-AS algorithm
#### Routing Information Protocol (RIP)
* Intra-AS routing protocol
* Distance vector algorithm
* Cost metric (# of hops, Max: 15)
* Exchange information every 30 seconds
* If no information exchange after 180 seconds, the link is declared to be down
* Poison reverse is used to prevent loops by setting the link cost to 16 (INF)
* Advertisment sent in UDP packet
#### Open Shortest Path First (OSPF)
* Intra-AS routing protocol
* Link State algorithm (Dijkstra)
* The advertisments are flooded to all other routers in entire AS
* All message are authenticated (security)
* multiple cost metrics is allowed
* multicast and hierarchical version is supported
####  Enhanced Interior Gateway Routing Protocol (EIGRP)
* Intra-AS routing protocol
* Hybrid routing algorithm
* Cost metric: bandwidth, delay, reliabiity, load
#### Border Gateway Protocol (BGP) 
* Inter-AS routing protocol
* Type of BGPs
  * eBGP
    * obtain subnet reachability from the neighoring AS (inter-AS)
  * iBGP
    * propgate the reachability information among all the router within the AS (intra-AS) 
* Best path is defined by the policy
* The route attribute consists of prefix and next hop, it will append the AS prefix at the front.
* Routing selection
   1. Local preference value attribute: policy decision
   2. Minimum number of intra-AS hop
   3. Closest next hop router - hot potato routing 
##### Hot Potato Routing
1. Learn the routing information from the source router to the gateway router within the AS
2. Choose the gateway router with the least cost to exit the AS.
## Software Defined Network (SDN)
A remote controller interact with the local control agent in the router to compute the routing/forward table
### SDN Controller
* API for network control apps
* Network OS for state management
* Low level protocol for communicating to the controlled devices.
### Advantages
* Avoid router misconfiguration
* "Program" the router is allowed 
## Other protocols in the network layer
### ICMP
* Mainly use for error reporting (reachability test), correction, reply/request (ping)