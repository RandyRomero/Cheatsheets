### What's CRUD?

CRUD stands for Create, Read, Update, Delete. It describes a type of backend-app, that provides an API that supports 
these functions. 

question id: 32468286-2628-4532-baeb-3187add0a248


### What are common methods that are used in REST?

GET, POST, PUT, PATCH, DELETE

These correspond to create, read, update, and delete (or CRUD) operations, respectively.

question id: ced22b5c-1dfb-4714-b66b-1abaaf757129


### What's POST method for? What are common response of the server?

In REST the POST method is used to **create** new child resources on the server. So POST to /items creates a resources 
that lives under the /items resource, for example /items/1. Sending the same post packet twice will create two 
resources with different URIs.


201 (Created), 404 (Not Found), 409 (Conflict) if resource already exists.

question id: f8ee0b97-2436-4dad-8c6e-d13c81419c21


### What's GET method for? What are common response of the server?

The GET method is used for getting information from the server. 

200 (OK), 404 (Not Found)

question id: 9eeaadf0-0597-4151-8700-b9172b10c73a


### What's PUT method for? What are common response of the server?

PUT to a URL creates/replaces the resource in its entirety at the client defined URL.
PUT replaces the resource at the known url if it already exists, so sending the same request twice has no effect. 
In other words, calls to PUT are idempotent.

200 (OK) or 204 (No Content). 404 (Not Found), 405 (Method Not Allowed), unless you want to update/replace every 
resource in the entire collection.

question id: 5c58222a-8eef-4043-b82d-e7bafa356ad3

### What's PATCH method for? What are common response of the server?

In REST the PATCH method is used for partial update of the resource. The PATCH request only needs to contain the 
changes to the resource, not the complete resource.

200 (OK) or 204 (No Content). 404 (Not Found), unless you want to modify the collection itself.

question id: 3f0994ed-9853-4ff8-8ea4-1192cec44433


### What's DELETE method for? What are common response of the server?

It is used to **delete** a resource identified by a URI.

On successful deletion, return HTTP status 200 (OK) along with a response body, perhaps the representation of the 
deleted item (often demands too much bandwidth), or a wrapped response (see Return Values below). Either that or 
return HTTP status 204 (NO CONTENT) with no response body.

200 (OK). 404 (Not Found), 405 (Method Not Allowed) unless you want to delete the whole collection—not often desirable.

HTTP-spec-wise, DELETE operations are idempotent. If you DELETE a resource, it's removed. Repeatedly calling DELETE on 
that resource ends up the same: the resource is gone. If calling DELETE say, decrements a counter (within the resource),
the DELETE call is no longer idempotent. As mentioned previously, usage statistics and measurements may be updated 
while still considering the service idempotent as long as no resource data is changed. Using POST for non-idempotent 
resource requests is recommended.

There is a caveat about DELETE idempotence, however. Calling DELETE on a resource a second time will often return a 
404 (NOT FOUND) since it was already removed and therefore is no longer findable. This, by some opinions, makes 
DELETE operations no longer idempotent, however, the end-state of the resource is the same. Returning a 404 is 
acceptable and communicates accurately the status of the call.

question id: 24f95d86-8c0e-4f68-9ad2-35e89c0bd497

### What's idempotence?

An idempotent operation is an operation, action, or request that can be applied multiple times without changing the 
result.

x=5 is idempotent because the state of x will always be 5 no matter how many times you assign 5 to it 

vs x++ is not idempotent because every time the state of x will be different

question id: 7aa6af9a-7c31-4ece-91f7-868a0ef65868
