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


### How a section of a network that is vulnerable to damage if a critical device or system fails is called?

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


### What would be a Fault Domain in AWS? A Fault Level?

answer:

- An AWS Region would be a Fault Level
- An Availability zone would be a Fault Domain (Failure Zone)

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

Points of Presence (PoP) are intermediate locations (datacenters or a collection of hardware) between an AWS Region and the end-user.

question id: 0f3ae88e-d7e3-428f-b998-21a3a973c463


### What are intermediate locations between an AWS Region and the end-user, and this location could be a data center or a collection of hardware?

Points of presence

question id: 19c240f8-5b61-4e62-83be-08e6847aaebb


### What are Edge Locations in AWS?

Edge Locations - are datacenters that hold cached (copy) of the most popular files (eg. web pages, images and videos) 
so that the distance of delivery to the end users is reduced

question id: 0ef61e3b-5b0a-4f65-ba2b-1c0e8eb74e17


### What is Regional Edge Cache in AWS?

Regional Edge Cache - are datacenters that hold much larger caches (than Edge Locations) of less-popular 
files to reduce a full round trip and also to reduce the cost of transfer fees.​

question id: ea119206-9aa2-44b0-8129-ed54c8371f97


### What are datacenters that hold much larger caches (than Edge Locations) of less popular files?

These are Regional Edge Cache - datacenters that hold much larger caches (than Edge Locations) of less-popular 
files to reduce a full round trip and also to reduce the cost of transfer fees.​

question id: c78580ee-1ded-47a8-8b97-a46ad6e46270


### What AWS services use Point of Presence?

- AWS CloudFront
- AWS S3 Transfer Acceleration
- AWS Global Accelerator

question id: 337e0348-e9e1-4948-b4c1-6efc656321d9


### What is AWS Cloudfront?

It is a Content Delivery Network (CDN) service

question id: 4d63d194-d117-4ed5-800e-4a4a16bf52d2


### What does AWS Cloudfront do?

It caches data requestred from your resources on Edge Locations and routes requests to the nearest
(to the user?) Edge Location cache​

question id: 0e121eca-a8ac-490b-abf3-8d9098bef69f


### What allows you to generate a special URL that can be used by end users to upload files to a nearby Edge Location. Once a file is uploaded to an Edge Location, it can move much faster within the AWS Network to reach S3?

AWS S3 Transfer Acceleration

question id: 29af8247-714e-47a6-b1f9-163e2c849f00


### What can find the optimal path from the end-user to your web servers?

AWS Global Accelerator

question id: 0da2f28d-fb63-4f33-9cc1-dbd0342c8cb6



### What is AWS S3 Transfer Acceleration?

It as a special AWS feature, that you can turn on and off separately, that increases the speed of files transfering between your bucket
and an end-user by leveraging Edge Locations.

question id: fbc76167-07b8-4269-8a97-997f5927c2c3


### How does AWS S3 Transfer Acceleration work? 

For example, you have your S3 bucket in Ireland, but you have users all over the world. If they try to upload something on
your bucket, it could take some time because of the distance. However, if you provide to your users a special URL, generated by
AWS S3 Transfer Acceleration, the data of your users will be at first uploaded to the nearest to them Edge Location, and from
there, by direct connection, to your S3 bucket. It makes transferring much faster, but there are additional fees for that.

question id: 287cf4e3-bd42-4825-bc45-d3114139ca8d


### What is the purpose of AWS Global Accelerator?

AWS Global Accelerator can find the optimal path from the end use to your web-servers. Global Accelerators are deployed within Edge Locations, so
you send user traffic to an Edge Location instead of directly to your web-application.

question id: 3a80f15e-004d-4d32-9198-fe934e64c918


### What is AWS Direct Connect?

AWS Direct Connect is a private/dedicated connection between your datacenter or office and AWS.

question id: f0d86c1a-dbbd-43b1-a556-973d4568f1e9


### How is a private/dedicated connection between your datacenter or office and AWS called?

 AWS Direct Connect

 question id: 57653c26-07f9-4ddb-81f1-e283c44ccdc3


 ### Why does one need to use AWS Direct Connect?

 - it reduces network costs
 - increases network throughput

question id: c65349af-d64c-4a41-af4b-ca0a574c63bc


### What are the two very-fast network connection options that Direct Connect have? 

- 50-500MBps
- 1GBps or 10GBps

question id: cbe455aa-5332-4a17-ba38-b4e8cc50334b



### What are Direct Connect Locations? 

answer

Direct Connect Locations are trusted partnedred datacenters that you need to establish a connection to
if you want to use AWS Direct Connect (if you want to have high-speed low cost connection to AWS from
your office or datacenter)

question id: fc9f815d-30a6-40bf-8a50-7ca06dc9cc22


### What are trusted partnedred datacenters that you can establish a dedicated
high-speed, low-latency connection from your on-premise to AWS?

answer

Direct Connect Location

question id: 84c750ec-54c7-4d3a-8297-a9b81246ab9b


### What are Local Zones?

Local Zones are datacenters located very close to a densely populated area to provide single-digit millisecond low latency performance (eg. 7ms) for that area.
Only some AWS services are available on such Local Zones.

question id: fac9472f-240d-4cd2-9e4b-890fd81316d6


### What are data centers located very close to a densely populated area to provide single-digit millisecond low latency performance (eg. 7ms) for that area?

Local zones

question id: 223329bd-ee4a-4a31-b51d-c30877c6bf21


### What is the purpose of Local Zone?

The purpose of Local Zone is to support highly-demanding applications sensitive to latency:
- Media & Entertainment​
- Electronic Design Automation​
- Ad-Tech​
- Machine Learning

question id: 6313b114-d7e1-4590-a4fa-fc6ca88504bf


### What are Wavelength Zones for?

answer:

AWS Wavelength Zones allow for edge-computing on 5G Networks to provide ultra-low latency be being as close as possible to the users

question id: ee7bbcdc-817b-44a5-acf5-9fe5253de9ba


### What allows for edge-computing on 5G Networks?

answer:

AWS Wavelength Zones

question id: 80deee81-fabc-412c-ace5-eab1413b4f73


### What is Data Residency?

answer: 

Data residency is the requirement that all customer content processed and stored in an IT system must remain within a specific country’s borders

question id: aa3d35b1-e611-4c75-a6ae-ce03ccbf7d49


### How is it called: a requirement that all customer content processed and stored in an IT system must remain within a specific country’s borders?

answer:

Data Residency

question id: 353fc13f-3067-4de8-8c93-1935831e1c6f


### What is Compliance Boundaries?

answer:

A legal requirement by a government or organization that describes where data and cloud resources are allowed to reside


question id: bd22226b-3515-45cd-ad28-61203e46afe3


### What is a regulatory compliance (legal requirement) by a government or organization that describes where data and cloud resources are allowed to reside?

answer:

Compliance Boundaries

question id: 7d4d95a4-2276-412c-9f24-0c4f903b1a50


### What is is the jurisdictional control or legal authority that can be asserted over data because its physical location is within jurisdictional boundaries?

answer:

Data Sovereignty

question id: b67ec440-fd3f-47b2-a40e-0f441661fac8


### What is AWS Outposts?

answer:

AWS Outposts is a physical rack of servers that you can put in your data center. 
Your data will reside whenever the Outpost Physically resides

question id: baa69d3f-a52c-4820-b250-b9e2732c4c72


### What is a physical rack of servers that you can put in your data center?

answer:

AWS Outposts

question id: 09c5b81a-0f91-462c-bf17-ab551dbb5530


### AWS has special regions for US regulation called ....

answer:

GovCloud

question id: e67ad8e6-8f6c-4547-aafe-e83a9c18049d


### Are GovCloud Regions globally accessible?

answer:

They are only accessible from the US soil.

question id: cb908115-5c5a-4670-9aec-e49e01e7e788


### What are regions that allow customers to host sensitive Controlled Unclassified Information and other types of regulated workloads?

answer:

GovRegions

question id: 0ff4ca64-bc86-4b54-9c01-afbc50e86f57


### What are the two Regions in Mainland China?

answer:

- Beijing Cn
- Ningxia CN

question id: 0a03c089-5389-4b82-af1f-b1b564a75184


### What is AWS in China?

answer:

AWS in China is the AWS cloud offerings in Mainland China, completely isolated from AWS Global to meet regulatory compliance for Mainland China.

question id: e8635173-44ef-426c-96f3-78549f5a62a6


### What parts AWS Cloud’s Sustainability are composed of?

answer:

- Renewable Energy

- Cloud Efficiency

- Water Stewardship

question id: d7ee8b2b-ea6d-4879-9f38-cb8208d9803f


### Which part of AWS Cloud's Sustainability goals states AWS is working towards having their AWS Global Infrastructure powered by 100% renewable energy by 2025?

answer:

Renewable Energy

question id: d12cbbcf-87d6-48c0-8fc7-3cd8655a0ecf


### What is "Cloud Efficiency" as part of AWS Cloud's Sustainability goals?

answer:

AWS’s infrastructure is 3.6 times more energy-efficient than the median of U.S. enterprise data centers surveyed.

question id: 28c6dd9f-08ba-4e6d-a3e6-5c71677be972


### What is "Water Stewardship" as part of AWS Cloud's Sustainability goals?

answer:

Basically, it's an effecient usage of water. Data centers use huge amount of water, so they had better be efficient in it.

question id: e6cf6f8a-d663-4185-8467-7fb98e3f2884


### What is AWS Ground Station?

AWS Ground Station is a service that lets you control satellite communications, e.g. select a satellite and download data from it
without building your own Ground Station (a huge dish and a facility to mangage this dish that can communicate with satellites).

question id: a37293a6-2913-427e-8cf4-208778a81bde


### What are use cases for AWS Ground Station?

answer:


Use cases for Ground Station:

- weather forecasting
- surface imaging
- communications
- video broadcasts

question id: 7a21b9ad-0835-4271-ad26-d80f72020b94


### What is a fully managed service that lets you control satellite communications, process data, and scale your operations without having to worry about building or managing your own ground station infrastructure?

answer:

AWS Ground Station

question id: 7d5d2a40-3978-4ab8-a2c6-a7a72fa21a4b


### What is AWS Outposts?

answer:

AWS Outposts is a rack of servers running AWS Infrastructure on your physical location

question id: 8736a495-5ef8-462f-b46c-58e976bbdfbd


### What is a frame design to hold and organize IT equipment?

answer:

Server rack

question id: 6d8d8800-0f87-48de-ac64-6cb5cd6711e8


### What is a fully managed service that offers the same AWS infrastructure, AWS services, APIs, and tools to virtually any data center, co-location space, or on-premises facility for a truly consistent hybrid experience?

answer:

AWS Outposts

question id: 0ede7c64-0cfe-4ce2-896c-59a919e534a6