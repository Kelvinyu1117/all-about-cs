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