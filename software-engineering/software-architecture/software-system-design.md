# Software System Design
## Different Tiers in Software Architecture
### Single Tier Application
An application where the user interface, backend, business logic and database all reside in the same machine

* Advantages
  
  * No network latency as all the component is located on the same machine
  
  * Use experience is faster as no data request to backend server
  
  * No transmssion -> much easier to secure the data safety

* Disadvantages
  
  * The company has no control over the application as the software is shipped to the client -> No changes or updates can be made 
  
  * Vulnerable to being tweaked or reverse engineered
  
  * Performance depends on the configuration of the user machine

### Two Tier Application and Three Tier Application

* Two Tier Application
An application involves a client and server. Client machine contains the user interface and business logic, Server machine contains the backend and database 

* Three Tier Application
= Two Tier application move the business logic to the Server (physically separate)


### N Tier Application
An application has more than three components (UI, Backend, database), for example, cache, message queue, load balancer 

#### Reasons for using this architecture
* Single Responsiblity Principle*

  * Only **one** responsibility to a component

  * Allows a lot of flexibility and makes management easier 

* Separation Of Concerns

  * Seperate the system into different component, and only focus on one component without worrying about the rest of the stuff
  
  * Makes component resuable
  
  * Easy to scale the system in the future

## System Properties
### Scalability

The ability of application to handle and withstnd increased workload without affecting the latency

#### Important Metric: Latency

The amount of time a system takes to respond to a user request
* Latency in web application
  * Network Latency
    
    * The amount of time the network takes for sending data from A to B
  
  * Application Latency
  
    * The amount of time the application takes to process a user request 

#### Types of scalability

* Vertical Scaling (scale up)
  * Add more power (RAM/DISK/Prcossor...) to a single machine
  
  * Less effort to scale up as the code doesn't need to change too much
  
  * Availability risk as the entire application going offline if the server goes down 
  
  * Suitable for the application that the traffic load would not increase significiantly

* Horizontal Scaling (scale out)
  
  * Add more machine with similiar performance

  * Difficult to program and maintain data consistency 
  
  * Suitable for the application that the traffic spike exponenetially 

* Cloud Elasticity
  * The ability to scale up or scale out dynamically, the user only pay for the resources that they required 

#### Bottleneck of Scalability

* Database
  * Picking Wrong database
  
  * Database doesn't scale which cannot handle a amount of request
  
* Application architecture
  
  * Asynchronous over sequential (it may block the system)

* Caching
  
  * Using the cache to speed up the response time and reduce the overall load
* Load Balancer
  
  * As it is the gateway of the application, it affect the latency if using too many of them. In contrast, too few of them may also affect the ability of handling the large workload  

* Programming style
  
  * unneccessary loops
  
  * Not paying attention to Big-O complexity

#### Methods for tuning the performance (scalability)

* Profiling
    
    * To determine which process of the system takes too long time or eating too much resource

* Caching
    
    * Cache everywhere, hit the data when it is really needed

* CDN
    
    * Reduce the latency of the application as the CDN will route the content to the user from the data center based on the proximity of the user

* Data Compression
    
    * Reduce data size -> consumes less bandwidth -> faster download speed

* Avoid Unneccessary requests
    
    * Try to pack multiple request into one packet of request
##### Testing criterion
Apply load and stress test (simulate the traffic) to check the following items

*  CPU usage

*  Network bandwidth consumption

*  Throughput

*  The number of requests processed within a stipulated time, latency, memory usage of the program

*  End-user experience when the system is under heavy load

### Availability
The ability of the system to stay online even though having failures at the infrastructural level in real-time

#### Reasons For System Failures
* Software Crashes
  
  * Normal error by programming

* Hardware Failures
  
  * Overloaded hardware (CPU/RAM/HDD), netowrk outages

* Human Errors
  
  * Mis-configuration

* Planned Downtime
  
  * Planned downtime for routine maintenance or upgrade

#### Ultimate Goal: Make system become fault tolerance

The ability of the system to stay up even though error occurs, the system will not go down even though some services go offline

* One of the solution is to break a massive service into small managetable services - microservices 

##### Some ideas to achieve high availiability
* Redundancy (Active-Passive Node)

  * A backup mechanism that duplicate the components and let them standby to take over in case the service goes down

  * Advantages
    * Getting rid of single point failure as many redunant component is standing by to take over

    * It allows self-recovery of the system because of monitoring automation

* Replication (Active-Aassive Node)
  *  A backup mechanism that allows similiar serivce running together, if one of them goes down, the load can be separated to other similiar services

  * All the component in the system is active at any point of time

##### Case study: High Availability Clustering
* Contains set of node (computing devices) running in conjunction with each other to ensure high avilability

* Those nodes are connected by a private network called Heartbeat network which monitors the heath and status of each node in the clusuter continuously

* The state across all the nodes is acheived with the help of shared distributed memory and co-ordination mechansim

* Serveral techniques (RAID, redundant network connection, redundant electrical power) also applied to ensure the avilability

* Multiple cluster run together in one geographical zone to ensuring minimum downtime and continual service
### Load Balancing

