# Components of Software System
## Database
A software to persist the data
* Data Format
  * structured
  
    * The data conforms to certain structure
 
    * Stored in database in a normalized fashion
    
    * Direct interaction can be done without pre-processing
    
    * SQL is usually used for data management

    * Example
      
      * Personal details of customers

  * Unstructured
    
    * No definite structure
    
    * Data processing need to be performed before interaction 
    
    * Example

      * text
      
      * images
      
      * video 

  * semi-structured
    * A mix of structured and unstructured data
    
    * Often stored in data transport format
      
      * XML

      * JSON 

  * user state
  
    * The information of activity which the user performs on the website
    
    * It is used for enhancing user experience 
### Concpet of Data Consistency
* Strong Consistency
    
    * The data has to be strongly consistent at all times
    
    * Support ACID transcation support
  
* Eventual Consistency
  
  * Enables the data store to be highly available.

  * In the real world use case, as the system is distributed around the globe, the data in every server may not be consistent and synchronized because of the latency. However, eventually the data will be consistent across the server nodes

### CAP Theorem
CAP stands for consistency, availability, partition tolerance. It states that we have to make a choice between availability and consistency, in case of a network failure.

### Type of Database
#### Relational Database
A database saves data containing relationships, and strong data consistency is usually ensured.

* It is suitable for the application requires strong data consistency, and the their business data has well-defined relationship

* Common type of relationships
  * one-one
  
  * one-many
  
  * many-many
  
  * many-one

* ACID Transactions
  * Atomicity
    * Every transactions will be executed with perfection or roll backed to original state if it is failure to execute
  
  * Consistency
  
    * The state of the system before and after the transcation executed is consistence
  
  * Isolation
    
    * All the transaction occurs in isolation fashion, the transcation cannot not modify the data if current transcation is not completed
  
  * Durability
    
    * Once the data has been modified, the state in the DB will not lost (store permanently)
#### NoSQL Database
NoSQL database don't use SQL to manage the data, it is built for high frequency read and write

* It is suitable for the application which has

  * handling a large number of read/write operations
  
  * flexiable data model
  
  * Not require strong consistency at any given time
  
  * Easy for data analytics 
* Advantages over relational database
  * Learning curve is gentle

  * Scalability: easy to scale out without too many human intervention
  
  * Easy to perform clustering
  
  * Schemaless: the data doesn't need to follows certain structure or constraints
  
* Disadvantages
  
  * Data may not be consistent at the same time, as the database system doesn't not guarantee
  
  * Not support for ACID transcation
#### Multi-model Database
A database software support multiple data model (relational, graph, time series...)at the same time, via single API
* Example
  * Arango DB
  
  * Cosmos DB
  
  * Orient DB
  
  * Couchbase
#### Document Oriented Database
It store data in a document-oriented model in independent documents
* It can be used for:
  
  * Real-time feeds
  
  * Live sports apps
  
  * Writing product catalogues
  
  * Inventory management
  
  * Storing user comments
  
  * Web-based multiplayer games

#### Graph Database
It store store data in nodes/vertices and edges in the form of relationships

* It can be used for:
  * Building social network
  * Knowledge
  * Network graphs
  * Writing AI-based apps
  * Recommendation engines
  * Fraud analysis app
  * Storing genetic data
  
#### Key Value Database
These databases use a simple key-value method to store and quickly fetch the data with minimum latency (average O(1))

* It can be used for:
  * caching
  * Persisting user state
  * Persisting user sessions
  * Managing real-time data
  * Implementing queues
  * Creating leaderboards in online games & web apps
  * Implementing a pub-sub system

#### Time Series Database
Time-Series databases are optimized for tracking & persisting time series data.
* It manage data in real-time & continually over a long period of time

## Caching
Caching allows the application with less-er response time

### Caching Strategies
* cache aside
  * The cache works along with the database trying to reduce the hit to db as much as possible
  
  * The system first looks for the data in cache for every request
  
  * best for read-heavy workload
  
  * In this approach, the data is written directly to the database which lead to the problem of data inconsistent. TTL can be used for solving this problem that the data will be invalid from the cache, and refetch is needed

* read-through
  *  The data always consistent as the backend for controlling the cache will update the cache while response to the user 
  
* write through
  
  * Every data written to the DB will also go through the cache
  
  * The high consistency between the cache and database can be achieved

* write back
  * The data is directly written to the cache instead of the database, and after some delay, the data will be written back from cache to the database
  
  * If the cache fails before the DB is updated, the data might get lost

## Message Queue
a queue which routes messages from the source to the destination

* message queue is asynchronous, which means that it allows the modules to communicate with each other in the background without interrupting their current task

* Messaging Model
  
  * publisher-subscriber model
  
  * point to point model

### Publisher-Subscriber Model
multiple consumers receive the same message sent from a single or multiple producers

* publisher = sender = prodcuer

* subscriber = receiver = consumer 

### Point to Point Model
one to one relationship: one producer vs one consumer