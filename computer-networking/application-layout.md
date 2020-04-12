# Application Layer

## Application architectures
### Client-Server Model
* Server
  
  * Permanent IP address
  
  * Data centers for scaling

* Client
  
  * May have dynamic IP address
  
  * Do not communicate directly with each other
### Peer-to-peer Model
* No always relie on dedicated server

* Self-scalability -> when new peer come in, we will get the resources of that peer, but also add the load to the system

* cost effective -> not require server infrastructure 
## Process communication
* Client process is the process initiate the process, server process is the process waits to be contacted. They communicate to each other by socket

* The process use IP address and port number to address each other

## Transport Services avilable to application
The services provided by transport-layer protocol to the application layer

* Reliable data transfer
* 