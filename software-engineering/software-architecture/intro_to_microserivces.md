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
    * Minimizes the coordination effort as the team can act independently regarding domain logic and tech
  
    * indepentent service allows independent deployment

* Disadavntages
  * Difficult to manage the module
    
    * Massive independent services are running at the same time which lead to the difficulty in managment

  * No strong consistency
    
    * They guarantee eventually consistency instead of real time consistency because of the latency of inter-communication between services 
  
  * Higher latency (communication between services through network) 

## Continuous delivery
It is an approach where software is continuously brought into production with the help of a continuous delivery pipeline.

<p align="center"> 
<img src="img/cd-piepline.png" />
</p>

1. Commit phase
   
   * software compilation
   * unit tests
   * static code analysis

2. Acceptance test

   * Automated tests assure the correctness of the software

3. Capacity tests
   
   * Check the performance at the expected load

4. Explorative tests
   
   * Perform not-yet-considered tests
   * Analyze the aspects that are not yet covered by automated tests.

5. Production

* With microservice architecture, the piepline is faster as the deployment unit is smaller
* The deployment has to be automated in order to make use of the advantages of faster CI.