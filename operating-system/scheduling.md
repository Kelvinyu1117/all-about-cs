# Scheduling
The main idea of scheduling is to assign processes to be executed by the processor over time such that meets system performance requirements

## Type of scheduling
<p align="center"> 
<img src="img/scheduling-state.png" />
</p>

* Long-term
  
  * Determines whether to add a new process to the set of processes that are currently active

  * Controls the degree of multiprogramming (i.e. number of process)
* Mid-term
  
  * Part of the swapping function 

  * Determines whether to add a process to those that are at least partially in main memory and therefore available for execution

* Short-term
  
  * Determines which ready process to execute next
  
  * Another name of the short-term scheduler is called dispatcher
  
  * It is usually invoked by:
    
    * clock interrupts

    * I/O interrupts
    
    * OS system calls/traps/signals 

* I/O 
  
  * Determines which process’s pending I/O request shall be handled by an available I/O device.

## Some Common System performance Metric
* Turnaround time
  
  * Interval of time between the submission of the process and its completion, including **actual execution time** + **waiting time for resources**

* Response time
  
  * Interval of time between the submission of a request between the first response to that request (Arrival time to first execution time)

*  Throughput
   * Number of process completed in unit time

* Processor utilization
  
  * Percentage of time of the processor is busy

* Fairness
  
  * no process should suffer starvation

## Scheduling Algorithms
* Preemptive
  
  * Currently running process may be interrupted based on certain critieria

* Non-preemptive
  
  * Once a process is in the running state, it will continue until it terminates or blocks itself by the I/O or system calls
  
<p align="center"> 
<img src="img/scheduling-algo.png" />
</p>