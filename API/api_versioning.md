### Why and when do you need API versioning?

answer:

If you are going to change the API and these changes are going to force users
of the API change their clients, it's called breaking changes. 

If you introduce breaking changes and you are not in control of clients that use 
your API, it's a good idea not just change your API all of a sudden, 
but release a new version and keep the old one for a while.
There are different ways you can separate new and old version of your API or its parts,
all of them have their pros and cons. 

question id: fc702f0d-0566-493a-99ca-c893a1e1f932


### Do you always need to keep different verions of your API? When you don't need to do it?

answer:

No. In ideal case it's better not to have different verisons at all,
because maitaining them can be a problem.

If you can release new version of API in sync with new consumers,
don't use API versioning.

If you can introduce changes slightly, without breaking anything,
it's better to do is so, than maintain two or more different versions
of your API.

question id: cf605283-e1f2-42ce-876c-4ceae0479b3b


### Give examples of breaking changes in API

answer:

- different request/reponse format (json instead of xml)
- changing a property name in request/response
- adding a new required field
- removing a property from the response

question id: fdfeab6f-5efa-4f9f-ad07-2063b5ed032a


### Describe steps of effective API change

answer:

- keep supporting existing properties
- add new properties instead of changing the existing ones
- thoughtfully sunset obsolete properties/endpoints

question id: f4575e03-0bfb-42d8-ae50-6bfd0d95f2a9


### Name four places where you can denote a version of an API/endpoint

answer

- URI Path
```
http://www.example.com/api/v1/products
http://api.example.com/v1/products
```

- query params
```
http://www.example.com/api/products?version=1
```

- header
`Accept: version=1.0`

- mixed

```
# URI path and query params combo
http://api.example.com/v1/products?version=1
http://api.example.com/v1/products?version=2
```

```
# Extended headers, for http://api.example.com/products
Accept: api-version=1; resource-version=1
Accept: api-version=1; resource-version=2
```

question id: 19808a41-44be-46b4-abd8-a217045b85b3


### What is the most common way to implement API versioning?

answer:

URI Path

```
http://www.example.com/api/v1/products
http://api.example.com/v1/products
```

question id: c22ecccf-5a07-4702-af8c-cbaa5ae91704


### What are pros and cons of implmenting API versioning using URI path?

URI Path

```
http://www.example.com/api/v1/products
http://api.example.com/v1/products
```

answer:

+ most common
+ very obvious
- not very clear whether it means the version of the whole API or a particular endpoint

question id: b084912e-e0ad-4821-95b8-2800af199290


### What are pros and cons of implmenting API versioning using Query Params?

```
http://www.example.com/api/products?version=1
```

answer:
+ very convenient if you only want to denote a version of a specific rest endpoint
- you really don't want a mess of different endpoints each having a different version - that could be very confusing

question id: 40b5c7bb-504f-4ce2-884d-149d4182a3e4


### What are pros and cons of implmenting API versioning using headers?

`Accept: version=1.0`

answer:
+ very convenient to specify granularity of any given resource
- not that obvious (whereas api version is hard not to see in an url or query params)
- still hard to tell whether 1.0 refers to the version of the endpoint or the API itself

question id: 1a8d35bd-15b4-4aad-b891-0a76127129e6


### What are pros and cons of implmenting API versioning using mixed ways?

For example:

```
# URI path and query params combo
http://api.example.com/v1/products?version=1
http://api.example.com/v1/products?version=2
```

```
# Extended headers, for http://api.example.com/products
Accept: api-version=1; resource-version=1
Accept: api-version=1; resource-version=2
```

answer:

+ very flexible
- confusing

question id: 97656cba-f5d8-47ab-8665-37ebe7d8b0cf