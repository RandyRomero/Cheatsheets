Useful links:
https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/

### What is salt?

A salt is a random value that is added to some data to hash them together to
create a unique output.

Usual hash function creates the same output for the same input, so by adding
random salt to the input your create random output.

question id: 1300b9df-3947-4af5-91c0-a4c5001bb81c


### Why and where do we need to use salt?

For example, if different users use the same password, in the database
hashes of their password will look the same. It makes cracking their
passwords easier for hackers. With the added salt we will get different
outputs for the same input (quick remainder: a property of a hash function
is that for the same data it will create the same output).

It is very important that each input is salted with unique random data.

question id: bbaa5dfb-b4a0-4a40-8e63-d1bd19ef33ca


### How do we use salt for storing and looking up passwords?

In practice, we store the salt in cleartext along with the hash in our database.
So that when the user logs in, we can lookup the username, append the salt to 
the provided password, hash it, and then verify if the stored hash matches the computed hash.

"Hashing salts are speed bumps in an attacker's road to breaching your data. 
It does not matter if they are visible and unencrypted, what matters is that they are in place."

question id: a820a0c1-ef51-463e-9f64-6739cccced1e


### What is good salt and what is bad salt?

Bad:
- system-wide salt (one salt for everyone - every password of every user). It just makes the hash longer, but doesn't mitigate hacker attacks
- one salt per user
- salt that is created by your own code (becase creating a good function for creating salts is too complicated)

Good:
- new random salt every time a new password is created (even for the same user, even if his new password is the same as one of his old passwords)

question id: bc8584ec-c6ec-40f9-afa3-7a4efe5d434f