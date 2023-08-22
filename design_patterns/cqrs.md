### What does CQRS stand for?

Command-Query Responsibility Segregation

question id: 7583e3ef-2336-42cb-a708-4b192b2cb99f


### What is CQRS about?

In CQRS (Command-Query Responsibility Segregation) we follow one simple rule: functions should either modify state or answer questions, but never both. 

For example, POST handle (like /batch) should not return created object. Instead, it should redirect to resource 
endpoint (like /batch/123) or return Location header containing the URI or our new resource

https://www.cosmicpython.com/book/chapter_12_cqrs.html

question id: 9df0bdfc-e2f4-443c-9d3f-84a64076510b