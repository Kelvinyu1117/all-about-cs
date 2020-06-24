# Introduction to Microservices

## Monolithic vs Microservices

### Monolithic Application
An application contains the entire application code in a single codebase

* It is suitable for the application that the requirement is pretty simple, and the app is expected to handle a limited amount of traffic.

* Advantages 　  
  
  * Simple to build, test, deploy, monitor and manage as everything reside in one repository
  
* Disadvantages
  
  * Difficult for continuous deployment

    * minor code change in the application needs to re-deploy the entire application
  
  * Difficult for regression testing
    
    *  go through the test of entire application, even though only small changes in the code base
 
  * Signle Point of failure: error in one layer may take down the whole application
  
  * Low flexibility and scalability as it is needed to test all the layer for the change in one layer, it is difficult to manage as the code size increases
  
  * Cannot leverage heterogeneous technologies as the entire application is in a single code base, it is difficult to adapt two different technologies together
  
### Microservice Application
An application that different features are splited into separated, independent, modules, which work in conjunction with each other to forming the application as a whole

* It is suitable for the app which has complex use cases and expect traffic to increase exponentially in future
* Advantages
  * No single point of failure
  
    * Loosely coupled architecture such that the application as a whole is still up even if sme services go down
  
  * Leverage the heterogeneous technologies
    
    * Different technologies can be applied into different modules as they are independent to each other
  
  * Independent and continuous deployments
  
    * indepentent service allows independent deployment

* Disadavntages
  * Difficult to manage the module
    
    * Massive independent services are running at the same time which lead to the difficulty in managment

  * No strong consistency
    
    * They guarantee eventually consistency instead of real time consistency because of the latency of inter-communication between services 