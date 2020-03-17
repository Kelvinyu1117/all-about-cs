# Concurrency
## Common Concurrency Problems
### Deadlock 
A set of processes/threads is blocked because each of them is holding a resource and waiting for another resource acquired by some other process

<p align="center"> 
<img src="img/deadlock.png" />
</p>

#### Conditions for casusing deadlock 

##### Mutual exclusion (Necessary)   
No process can access a resource unit that has been allocated to another process
##### Hold and wait (Necessary)   
A process hold allocated resources while awaiting assignment of other resources
##### No preemption (Necessary)
No resource can be forcibly removed from a process holding it.
##### Circular wait (Sufficient)   
A closed chain of processes exists such that at least one resource needed by the next process in the chain 

#### Resource allocation graph

<p align="center"> 
<img src="img/allocation_graph.png" />
</p>

##### How to interpret the graph
* Arrow from the resource to the process: Resource assignment to process
* Arrow from the process to resources: Resource request from process
* The dot in the resource: the number of that resource available

##### How to identify deadlock
* Observation method
  
  1. find cycle, cycle means deadlock **may** happen, but not neccessarily.
  
  2. Evalute each process, re-distribute the resources such that the process can be executed and exit, then delete that process in the graph. 
  3. If no process can be executed, it is in deadlock state. (Irreducible process)
   
* Table method
  
  1. Build the allocation table, request table, and availability table based on the graph
   
  2. Check the availability of each resources whether cause the some process to exit, if yes, reduce the row of allocation table, update the availability table
   
  3. Keep doing step 2 to reduce the process, if no process can be executed, it is in deadlock state.(Irreducible process) 