# Disk Management
## Record Blocking
How to organize record as a sequence of blocks for I/O
<p align="center"> 
<img src="img/record-blocking.png" />
</p>
### Fixed length blocking
Fixed-length records are used, integral number of records are stored in a block

* Disadvantage
  
  * internal fragmentation due to unused space at the end of a block   

### Variable-length spanned blocking
Variable-length records are used and packed into blocks with no unused space, some record may span multiple blocks which require a pointer to the next block

* Advantages
  
  * Efficient for storage
  
  * Size of the records is not limited 

* Disadvantages
  * Difficult to implement
  
  * multiple I/O operations may be required due to the records may span mulitple blocks

### Variable-length unspanned blocking
Variable-length records are used but no spanning to other block

* Disadvantages
  
  * The space is waste because the remainder of a block may not be able to accomedate the next record if the size of the next record > remaining unused space
  
  * Size of the record is limited to the size of 

## Disk Scheduling
How to schedule individual block I/O requests for optimizing performance

### General Disk Performance Parameter
<p align="center"> 
<img src="img/disk-timing.png" />
</p>

* Seek time
  * The time required to move the disk arm to the required track

* Rotational Delay
    * The time required for the addressed area of the disk to rotate into a position where it is accessible by the read/write head.

* Access Time
    * seek time + rotational delay

* Transfer time
    * The time required for the data transfer 

#### Timeing comparision

<p align="center"> 
<img src="img/total-access-time.png" />
</p>

* sequential access (adjcent track): t = time for reading 1st track + time for reading successive tracks
* time for reading 1st track = seek time + rotational delay + time for reading all the sector in a track
* time for reading sccessive track = N tracks * (rotational delay + time for reading all the sector in a track)

5* random access: t = N * (seek time + rotational delay + time for reading 1 sector)  
#### Operation of Disk
* To read/write, the read write head must be positioned at the desired track and at the begining of the desired sector on that track

* Once the track is selected, the disk controller waits until the appropriate sector rotates to line up with the head

* Once the head is in position, read or write operation is performed as the sector moves under the head, finally, transfer the data back


### Disk scheduling algorithm
<p align="center"> 
<img src="img/disk-scheduling-algo.png" />
</p> 
## File Allocation
How to allocate files to free blocks on secondary storage
