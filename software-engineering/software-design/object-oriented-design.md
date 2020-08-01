# Object Oriented Design

## Four Design Principles

### Abstraction

The idea of simplifying the concept in the problem domain to its essentials within some context, which breaking down the concept into simplified description and ignore un-important details. The abstraction should not surprise anyone that capture irrelevant characteristics (Rule of Least Astonishment)


In OOD, abstraction usually refers to the notion of the `Class`, which is the template of a instances of concepts 

### Encapsulation

The idea of encapsulation forms a self-contained object by bundling the related data and functions, expose an interface wherby other object can access and restrict access to certain inside details. It can enhance data integrity and security as the other object can only access the data by the exposed interface, which is full controlled by the design. 


Encapsulation also reduces the complexity for the user of the `class`, thas the internal workings are not relevant to the outside world. It also enhance the reusability of class as the other user can use the `class` by just knowing the interface. 



In practice, all the attributes should be prevented from outside access directly.


### Decomposition

Decomposition is taking a whole thing and dividing it up into different part or reverse. It allows further break down the problems into smaller pieces that are easier to understand and solve

### Generalization 

Generalization generalizes behaviours and reduces the amount of redundancy that eliminate the identical code in the `class`. It can acheived by inheritance (the `subclass` inherits the properites and behaviours of the `super class`)

## General Guidlines for software evaluation

### Coupling and Cohersion
- Coupling refers to the complexity between a module and other modules, high(tight) coupling means the module is highly reliant on the others

- Cohersion refers to the complexity within the module, represent the clarity and responsibility of the module, high cohersion means the module should perform one task and have clear purpose

- well design system should be low coupling, high cohersion

- To evalute the coupling of a module, the following metric is usually used:
  
  -  degree: number of connections between the module and the others
  
  -  ease: how obvious are the connections between the module and the others
  
  -  flexibility: how interchangeable the other modules are for the module, the other modules should be easily replaced by something better 
### Information hiding
It allows modules of the system to give others the minimum amount of information needed to use them correctly and "hide" everything else. It is acheived by the accssor modifier.

### Conceptual Integrity
It is about writing software in consistent manner. The software should refect one set of design ideas than to have one that contains mny good but independent and uncoordinated ideas.

## S.O.I.L.D Principle

### Single responsibilty principle
Every module or class should have responsibility over a single part of the functionaility provided by the software. The module should have one and only one reason to be changed


### Open/closed principle
The software entities should be open for extension, but closed for modification. For using inheritance to extend the functionailities of the class instead of changing it



### Liskov substitution principle
The instances should be replaceable with the instances of its subtypes without affecting the original functionailies or correctness of the program


### Interface segregation principle
It states no client should be forced to depend on methods it does not use. Large interface should be splited into small, specfic interface that the client only have to know the methods that they are interested in.


### Dependency inversion
The principle states:

- High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g. interfaces, abstract class).

- Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions.



  