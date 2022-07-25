### What is the AWS Global infrastructure?

It is globally distributed hardware and datacenters
that are physically networked together to act as
one large resource for the end customer.

question id: 97b2fff1-f168-4cec-b841-c153034a002c


### What resources AWS Global infrastructure made up of?

- Regions
- Availability Zones
- Direct Connections Locations
- Points of Presence
- Local Zone
- Wavelength Zone

question id: fc553fd2-1528-47a5-813f-e2069874be95


## Regions


### What are **regions** in AWS Global infrasrtucture?

Regions are geographically distinct locations consisting of one or more
Availability Zones (datacenters).


question id: dab2da58-aba1-40ee-b04b-5ee1b84b605d


### Are Amazon Regions isolated from each other? 

answer:

Yes. Every region is isolated and independent of every other regions in terms
of location, power and water supply.

question id:



### Are all services available in all regions?

answer:

Not all services are available in all regions.

question id: 8387a804-0336-416c-bd23-617389fb2f65


### Is the cost of AWS the same in all regions?

answer:

No. The cost of AWS varies per region.

question id: 71fcf9cf-e463-4b9f-9b07-a4250528705a


### What are 4 factors you need to consider when you are choosing a region?

answer:

0. What Regulatory Compliance does this region meet?
1. What is the cost of AWS in this region?
2. What AWS services are available in this region?
3. What is the distance or latency to my end-users?

question id: cdec7a31-3044-4eda-a461-1f5bdd3352d6


### In what region can you see all your billing information?

answer:

In US-East-1

question id: f86dd270-7c9c-46eb-8d92-48f7572e386e


### Are all AWS connected to a specific region?

No, there are services that are global. For example, IAM, S3, CloudFront etc.

question id: 32b7ad91-61d8-4ef1-8498-41614d49ee01



## Availability Zones (AZs)


### What is an Availability Zone?

answer:

An Availability Zone is a physical location made up of one or more datacenters.

question id: 0a65f209-9e3f-4675-a1d9-79e6d3253f02


### How many Availability Zones does a Region generally contain?

answer:

3 Availability zones

question id: 83c791a3-7226-4265-ad67-9c8b736ef351


### Is it okay to run your workload on one Availability Zone?

answer:

Yes, but it is a common practice to run your workload at least on three Availability Zones
to ensure services remain available in case one or two AZ fails.


question id: d97156a4-ba49-4670-9e7f-e611b4d8be7c



### Why the letter at the end is different?

- us-east-1a
- us-east-1b
- us-east-1c

answer

These codes mean the same Region, but three different Availability Zones

question id: 88ddb2cf-1c9e-42ca-82f9-3bb7281a8d76


### Can you choose an Availability Zone when you launch resources?

No, you can only choose a Subnet (sometimes), that is related to a particular AZ.

question id: 2ad87bd8-729e-43a6-85a4-16aff686b005


### What is a physical location that is made up of one or more data centers?

An Availability Zone

question id: ec6103ac-3389-4376-822d-a5fc5aea49ee



### What is a fault domain?

answer:

A fault domain is a section of a network that is vulnerable to damage if a critical device or system fails. 
The purpose of a fault domain is that if a failure occurs it will not cascade outside that domain, limiting the damage possible.

question id: f3570052-f5db-4aa3-9ab0-c2b006eb2fba


### How section of a network that is vulnerable to damage if a critical device or system fails is called?

answer:

A fault domain (or Failure Zone in terms of AWS)

question id: 759307cf-e8db-4b13-9960-0067fc6f3987


### Name four examples of a fault domain

answer:

- specific servers in a rack
- an entire rack in a datacenter
- an entire room in a datacenter
- the entire data center building

question id: 322b8e8f-4428-48ef-93c1-f0d503abcdd1


### What is a Fault Level?

answer:

It's a collection of Fault Domains.

question id: cd5d0eb2-88e2-4156-9f46-bb7ab5011eb7


### How a collection of Fault Domains is called?

answer:

A Fault Level

question id: e565ec38-24db-42ae-a3ae-fb1bef3f72b3


### What would be be a Fault Domain in AWS? A Fault Level?

answer:

- An AWS Region would be a Fault Level
- An Awailability zone would be a Fault Domain (Failure Zone)

question id: 513ea4ef-3ddf-4b54-af55-d8e4e31fc325


### Are Availability Zones isolated from each other?

answer:

Yes, but they are connected through low-latency links

question id: ae2b92c5-3f59-41f4-904c-d0cdbdac87c9


### How does Amazon call a Fault Domain?

answer:

A Failure Zone

question id: ff92b17a-3f0c-4ada-9c47-6961f354b007


### What are Points of Presence (PoP)?

Points of Presence (PoP) are intermediate locations (datacenters of a collection of hardware) between an AWS Region and the end-user.

question id: 0f3ae88e-d7e3-428f-b998-21a3a973c463


### What are Edge Locations in AWS?

Edge Locations - are datacenters that hold cached (copy) on the most popular files (eg. web pages, images and videos) 
so that the delivery of distance to the end users are reduce

question id: 0ef61e3b-5b0a-4f65-ba2b-1c0e8eb74e17


### What is Regional Edge Cache in AWS?

Regional Edge Cache - are datacenters that hold much larger caches (than Edge Locations) of less-popular 
files to reduce a full round trip and also to reduce the cost of transfer fees.​

question id: ea119206-9aa2-44b0-8129-ed54c8371f97


### What AWS services use Point of Presence?

- AWS CloudFront
- AWS S3 Transfer Acceleration
- AWS Global Accelerator

question id: 337e0348-e9e1-4948-b4c1-6efc656321d9


### What is AWS Cloudfront?

It is a Content Delivery Network (CDN) service

question id: 4d63d194-d117-4ed5-800e-4a4a16bf52d2


### What AWS Cloudfront does?

It caches data requestred from your resources on Edge Locations and routes requests to the nearest
(to the user?) Edge Location cache​

question id: 0e121eca-a8ac-490b-abf3-8d9098bef69f


### What is AWS S3 Transfer Acceleration?

It as a special AWS feature, that you can turn on and off separately, that increases the speed of transfering between your bucket
and an end-user by leveraging Edge Locations.


### How does AWS S3 Transfer Acceleration work? 

For example, you have your S3 bucket in Ireland, but you have users all over the world. If they try to upload something on
your bucket, it could take some time because of the distance. However, if you provide to your users a special URL, generated by
AWS S3 Transfer Acceleration, the data of your users will be at first uploaded to the nearest to them Edge Location, and from
there, by direct connection, to your S3 bucket. It makes transferring much faster, but there are additional fees for that.

question id: 


### What is AWS Global Accelerator?




### What are Edge Locations in AWS?

AWS Parters' datacenters that serve several purposes:
- they have direct connection to AWS inner network, so if you client is far from AWS Availabity zones, he still can get fast access to AWS resources
- on such Edge Locations Amazon Cloudfront (Amazon's CDN) caches data to give it to the clients faster
- there is also Amazon Route 53 service running on Edge Locations

question id: 



### What is Cloudfront?

It's Amazon's CDN (Content Delivery Network)

Amazon Cloudfront is a web service that better distributes your content through a worldwide network of of different datacenter partners