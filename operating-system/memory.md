# Memory Management
The main purpose for memory management is to bring the process to the main memory. 

## Simple Memory Management Techniques
### Fixed-size Partitioning
* Memory is divided into fixed-size section, the process with the size <>= the size of the section will be loaded into the memory

* Inefficent because of the internal fragmentation (the space in the partition is wasted as the size of process must be equal or less than the size of partition)

* Programmer need to write the program to overlay some of the portion of the partition in order to fit the size of the partition

### Dynamic Partitioning
* Each process can be loaded into the partition of exactly the same size of the process  

* Inefficent because of the external fragmentation (some of the space outside of partition can not be used such that decrease the memory utilization when time goes on)

* One of the solution of solving the external fragmentation is compaction that shift the process time to time so that there is larger contiguous space which allows new process to swap in. 

## Paging

## Segmentation

