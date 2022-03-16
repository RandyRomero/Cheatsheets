### What is NGINX and gunicorn and why to use it together?

Both are web servers, but NGINX is fast and Gunicorn can run python web apps. 

Also, Gunicorn is optimised for fast clients, low latency and high bandwidth.
So, usually, NGINX is used as a reverse proxy, which means it receives requests from internet and 
serves static files (CSS, JS and images) on its own, but for dynamically generated response
NGINX passes request to Gunicorn.

question id: 09b039b9-7bd9-40f5-8bdf-93d035a89839



### What is reverse proxy? 

A reverse proxy is a type of proxy server where the servers return resources to the client where 
 it would appear to the network that it originated from the reverse proxy server itself.

Example scenario: A client on the internet (cloud on the left) makes a request to a reverse proxy 
server (red oval in the middle). The proxy inspects the request, determines that it is valid and 
that it does not have the requested resource in its own cache. It then forwards the request to some 
internal web server (oval on the right). The internal server delivers the requested resource back 
to the proxy, which in turn delivers it to the client. The client on the internet is unaware of the 
internal network, and cannot tell whether it is communicating with a proxy or directly with a 
web server.

question id: c04af593-b0a5-4ca0-b08e-4dad3b414c36


### What is WSGI?

WSGI (Web Server Gateway Interface) is a protocol, it’s a standard of communication that describes 
how a web server communicates with web applications. For example, how Gunicorn communicates with 
Flask or Django.

https://www.fullstackpython.com/wsgi-servers.html

https://www.agiliq.com/blog/2013/07/basics-wsgi/

https://apirobot.me/posts/what-is-wsgi-and-why-do-you-need-gunicorn-and-nginx-in-django

question id: a69ffc8e-7eac-4d5f-8f8b-886e1ce835dd


### Why is WSGI necessary?

A traditional web server does not understand or have any way to run Python applications. In the 
late 1990s, a developer named Grisha Trubetskoy came up with an Apache module called mod_python to 
execute arbitrary Python code. For several years in the late 1990s and early 2000s, Apache 
configured with mod_python ran most Python web applications.

https://www.fullstackpython.com/wsgi-servers.html

https://www.agiliq.com/blog/2013/07/basics-wsgi/

https://apirobot.me/posts/what-is-wsgi-and-why-do-you-need-gunicorn-and-nginx-in-django

question id: 9f7d9c11-01aa-4ded-ab6a-2411e939d86e


### What is Gunicorn? 

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

question id: dabde38a-2adf-4ca3-9ec4-11b761526740


### What is NGINX?

NGINX high‑performance, highly scalable web server, reverse proxy, load balancer.

question id: bb7d9a13-34a0-4973-86b7-65e4293a08f