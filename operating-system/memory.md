# Memory Management
The main purpose for memory management is to bring the process to the main memory. 
There are two types of memory: Main memory and virtual memory
* Main memory
  
  * Usually is RAM, the address is called physical address

* Virtual memory
  
  * Usually is a small portion of secondary storage, the address is called virtual address/logical address, relative address is the address relative to the origin of the program

## Requirements of Managment
### 
## Memory Management Techniques
### Fixed-size Partitioning
* Memory is divided into fixed-size section, the process with the size <>= the size of the section will be loaded into the memory

* Inefficent because of the internal fragmentation (the space in the partition is wasted as the size of process must be equal or less than the size of partition)

* Programmer need to write the program to overlay some of the portion of the partition in order to fit the size of the partition

### Dynamic Partitioning
* Each process can be loaded into the partition of exactly the same size of the process  

* Inefficent because of the external fragmentation (some of the space outside of partition can not be used such that decrease the memory utilization when time goes on)

* One of the solution of solving the external fragmentation is compaction that shift the process time to time so that there is larger contiguous space which allows new process to swap in. 

### Paging
* The main idea is to partition the memory into equal fixed-size chunks (frames), and also divide the process using the same way (pages).
  
* No external fragmentation and only consists of small portion of internal fragmentation in the last page (last part of the memoey of the process)

* The process maintain its page table that consist of the page of the process, each entry is pointing to the frame of that page

* Each logical address is calculated by the page number and offset, which is very easy for hardware to implement.

#### Address Translation
For the address n + m bits, where n bits for page number and m bits for offset
1. Extract the leftmost n bits that is the page number

2. Use the page number to find the corresponding frame number k in the process page table

3. The physical address = k * 2^m (left shift by m bits) + offset, however, the physical address need not to be calculated, as the structure must be in the ((frame number, offset)). Append the offset to the frame number will be the physical address.

#### Calculation
* Page size = frame size = 2^m
  
* Number of page = 2^n and for each page with size 2^m

#### Multi-level page table
* The main idea is to further split the portion of page number into smaller portion that to index the multiple page table instead of using the whole part of page number to index a large page table

* leftmost is the outer address
  
* increase the translation latency but reduce the page table size (the process only need to hold the outer table, which is smaller)  


### Segmentation
* The main idea is to partition the process into small variable-size of chunks called segments, that is not required in the same size, but there is a maximum length of the segement.

* No internal fragmentation and only consists of small portion of external fragmentation (as some of the space outside the partition may not be used, but the size of the segment can be small such that there is only a small portion of external fragmentation)

* Each process maintain its segement table， each entry provide the starting address in the memory of corresponding segment and the length of the segment to validate the address.

* Each logical address is calculated by the segment number and offset.
#### Address Translation
For the address n + m bits, where n bits for segment number and m bits for offset

1. Extract the leftmost n bits that is the segment number

2. Use the segment number to find the starting address of the segment in the memory

3. Compare the offset to the length of the segment, invalid if offset >= length

4. Physical address = starting address + offset  