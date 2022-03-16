## What is JWT?

JSON Web Token, or JWT, is an open standard (RFC 7519) for safely passing claims that defines a 
compact and self-contained way for securely transmitting information between parties as 
a JSON object. This information can be verified and trusted because it is digitally signed. 
JWTs can be signed using a secret (with the HMAC algorithm) or a public/private key pair using 
RSA or ECDSA.

In Other words, A JSON Web Token (or JWT) is simply a JSON payload containing a particular claim.

### A JWT is made of 3 parts:
- The Header
- The Payload
- Signature

Example of a JWT:

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFiaGlzaGVrIEtpc2hvciIsImlhdCI6MTUxNjIzOTAyMn0.zBsxPZ5jCc68g6ukcEfSs0rUDIPAqf8iJOimZuBfR3Y

It does have 3 parts separated by dots.

The first part before the first dot is the JWT Header:

JWT Header:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
The second part, between the first dot and the second, is the Payload:

JWT Payload:
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFiaGlzaGVrIEtpc2hvciIsImlhdCI6MTUxNjIzOTAyMn0
Last part, after the second dot is the Signature:

JWT Signature:
zBsxPZ5jCc68g6ukcEfSs0rUDIPAqf8iJOimZuBfR3Y

The Payload, the Header, and the Signature are still in there in readable form.

#### JWT Header

- technical metadata information about the token itself, like a type of used signature
```json
{
  "alg": "RS256",
  "typ": "JWT"
}
```

encoded in base64url

#### JWT Payload
The payload of a JWT is just a plain Javascript object like this
```json
{
  "name": "John Doe",
  "email": "john@johndoe.com",
  "admin": true
}
```
Long story short:
- plain JSON object
- usually contains identification information and a role
- not encrypted
- encoded in base64url

In this case, the payload contains identification information about a given user, but in general, 
the payload could be anything else such as for example information about a bank transfer.

There are no restrictions on the content of the payload, but it's important to know that a JWT is 
not encrypted. So any information that we put in the token is still readable to anyone who 
intercepts the token.

Therefore it's important not to put in the Payload any user information that an attacker could leverage directly.


#### JWT signature
a.k.a. Message Authentication Code (or MAC)

The signature of a JWT can only be produced by someone in possession of both the 
payload (plus the header) and a given secret key.

## How does HS256 signature work?

Server get's a JWT token from a client. Server puts together JWT Header, JWT Payload and a special secret, then
hash the resulting string. If the result is equal to signature from the received JWT, then the token is valid. Because 
only the party who possesses same exact secret could come out with this particular token.

HMACSHA256(JWT Header + JWT Payload + Your Secret) should be equal to the signature from the received JWT

## How does RS256 signature works?

Long story short:
Instead of hashing JWT header and payload together with a secret as in HS256, 
in RS256 header and payload are hashed without secret, than signed/encrypted with a private key (RSA). 

That's encrypt_with_private_key(hash(base64url(JWT Header).base64url(JWT Payload))) is a signature

To validate it you should decrypt signature with your public key and check against JWT header and payload

It uses two keys, private and public. The private one can be used only to sign signatures, and the public one can 
be used only to validate signatures. 

The public key does not need to be kept private and it often is not, because if the attacker gets it there is no way 
to use it to forge signatures.

RS256 signatures use a particular type of keys, called RSA Keys. RSA is the name of an encryption/decryption algorithm 
that takes one key to encrypt and a second key to decrypt.

Note that RSA is not a Hashing function, because by definition the output of encryption can be reversed and we can get 
back the initial result.

To encrypt payload takes time, so instead of it to create or validate a signature we hash JWT header and payload and
encrypt the hash - it is much faster.

With the RS256 the flow looks pretty identical. Server puts together JWT Header and JWT Payload, _hashes_ them, then
encrypts this hash using its private key thereby makes a signature. To validate such a token you do basically the same, 
but with your public key.

The main benefit of RS256 is that you can easily give away public keys to your clients.

https://habr.com/en/post/456968/

https://medium.com/@abhishekaadi/jwt-in-a-nutshell-part-1-84bf7c7018d#:~:text=JSON%20Web%20Token%2C%20or%20JWT,parties%20as%20a%20JSON%20object.

https://blog.angular-university.io/angular-jwt/

https://blog.miguelgrinberg.com/post/json-web-tokens-with-public-key-signatures


### What advantage does RS256 algorithm have over HS256?

In RS256 you use separate keys for making a signature and validating a token. For validation you use a public key, 
which can't be used for forging signatures. It's much easier to distribute public keys of RS256 than a secret in HS256.

Why do you even need to distribute any keys if signing validating tokens takes place on the same server? That's
exactly the answer - to be able to use one service for signing tokens and to validate tokens on any number of other
services. Like when you use microservices - one microservice sign a token and give it to a client, and any other
microservices can validate this token. It's also possible with HS256, since there is the same key for signing and 
validating tokens, there is a chance that the key will be stolen during transferring this key from one service to 
another.

question id: 2d1d029c-f8ee-4be5-8a48-6e6a7b7a5101


### How to be able to invalidate user access or/and refresh token(s)?

If your system doesn't have any tool for it yet, you can change JWT secret.
However, it will make all tokens invalid - for all users at the same time.

What if we want to be able to invalidate a token for specified user?
You can add to jwt payload of the token fields like **modified_at** and
**refresh_modified_at** or something of this kind. On generating token,
you can add there timestamp as an integer when the token was generated.

Then, when you want to invalidate any of users tokens, you can set in 
Redis new timestamp, of just now. And, while checking token, make sure
that if there is a version for that user in Redis, the version in token
must be equal or bigger than in Redis. Otherwise, you raise an error
that the token is not valid:
- user cannot get access to your service anymore
- front-end takes this error as a sign to redirect the user to the login
page

P.S. You don't need to store current version in database. You don't have
to store it anywhere rather then in token itself.

question id: b47f0541-ebce-412d-856f-66a741da1a13