## Why do we need access and refresh tokens?

Let's imaging we use for authentication only login and password. In this case,
our client would be obliged to store login and password and send them with each
and every request. That increases chances that login and password will be intercepted
by some hacker and he will be able to use it, let's say, for three month. 

Tokens make this more secure. 

User uses his login and password when he goes to the website for the first time.
There he gets access token and refresh token. Since then with every request the 
client sends in headers access token. 

Access token can be used many times, but 
lives very short - usually 15 minutes or so. Hence, if access token is got
intercepted by a hacker, this hacker can only use this access token for as long as
15 minutes.
After access token is expired, client uses refresh token to obtain new access and 
refresh token. Refresh token lives long, e.g. a month, but can be used only once.
This means, even if a hacker intercepts you access token and refresh token, when your
access token gets expired you will get new access and refresh token, and those of the 
hacker will be invalid.

https://habr.com/en/post/456968/