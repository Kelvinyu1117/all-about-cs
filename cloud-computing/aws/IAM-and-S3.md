# Indentity Access Management & S3

## Indentity Access Management (IAM)

### Features

- Centralised control AWS account

- Share Access to AWS account 

- Ganular Permission (grant permission)

- Identity Federation (allow the authenticate the user to by using external services, like FB, Linkedin)

- Multifactor authentication (MFA, need to special code to login)

- Provide temporary access for user/devices and services where neccessary (e.g. mobile app access temporary)

- allow to setup out own password policy

- integrates with many different services

- Support PCI DSS Compliance (taking credit details need to fulfill the Compliance)     

### Key components

- User

  - End User 

- Groups

  - A collection of users, each user in the group will inherit the perimission of the group

- Polices

  - made up of documents (policy documents) which in JSON format and they give permission as to what a user/group/role is able to do

- Roles
  
  - assign AWS resources to different role of user 



## Simple Storage Service (S3)

### Features

- Object based - allow user to upload files

- Files can be from 0 Bytes to 5 TB

- unlimited storage

- File are stored in Buckets (folder)  

- Tiered Storae Available

- Life cycle Managment ()

-  Versioning

- Encryption

- MFA delete (delete need authen)

- Secure data by access control list and bucket policy   

### Basic

- S3 is a universal namespace, names must be unique globally

- HTTP 200 code if upload is success

- S3 objects properties:
  
  - Key (name of the object)
  
  - Value (the data made up of a sequence of bytes) 
  
  - Version ID 
  
  - Meta data (data about the data)
  
  - Subresources
   
    - Access Control list
    
    - Torrent

### Data consistency of S3

- Read after write consistency for PUTS of new Object (the user is able to read the file immediately after the uploading)

- Eventual Consistency for overwrite PUTS and DELETES (e.g. upload version 2 of the file to overwrite the first version -> the user may got either version 1 or 2 but eventually got version 2 after some time to propogate the version)

### Guarantees from Amazon

- Amazon guarantee 99.9% availability for S3

-  Amazon guarantee (99.999... (11x9) %) durability for S3 (the file is vtery unlikely to be lost)

### Storage class

- **S3 standard** 

  - 99.9% avaliability
  
  - 99.999... (11x9) % durability
  
  - stored redundantly across multiple devices in multiple facilities
  
  - sustain the loss of 2 facilities concurrently

- **S3 IA (infrequently Access)** 

  - for data is accessed less frequently, but requires rapid access when needed
  
  - lowfee than S3, but retrieval fee are charged
  
- **S3 One Zone - IA** 

  - lower cost option for infrequently accessed data, no multiple AZ data resilience 

- **S3 - Intelligent Tiering** 
  
  - Designed to optimized cost by automatically moving data to the most cost-effective access tier, without performance impact or operational overhead 

- **S3 Glacier**
  - Secure, durable, low cost storage class for data archiving.
  
  - User can store any amount of data at cost competitive or cheaper than on-permises
  
  - Retrieval times configurable from minutes to hours

- **S3 Glacier Deep Archive**
  - lowest-cost storage
  - Retrieval times 12 hours

### Storage Charging

- Storage
  
- Requests

- Storage Managment pricing

- Data transfer prcing

- Transfer acceleration
    - Enable fast, easy, and seure transfer ove long distance
  
    - Taking advantage of Amazon CloudFront globally distributed edge location, data arrives at edge location and routed to S3 over an optimized network path
  
- Cross region replication pricing (replicate the bucket to another region)
  