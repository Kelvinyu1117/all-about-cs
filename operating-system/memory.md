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
* The main idea is to partition the memory into equal fixed-size chunks (frames), and also divide the process using the same way (pages).
  
* No external fragmentation and only consists of small portion of internal fragmentaation in the last page (last part of the memoey of the process)

* The OS maintain the page table that consist of the page of the process, each entry pointing to the frame of that page

* Each logical address is calculated by the page number and offset, which is very easy for hardware to implement.

### Address Translation
For the address n + m bits, where n bits for page number and m bits for offset
1. Extract the leftmost n bits that is the page number

2. Use the page number to find the corresponding frame number k in the process page table

3. The physical address = k * 2^m (left shift by m bits) + offset, however, the physical address need not to be calculated, as the structure must be in the ((frame number, offset)). Append the offset to the frame number will be the physical address.

### Calculation
* Page size = frame size = 2^m
  
* Number of page = 2^n and for each page with size 2^m

## Segmentation

