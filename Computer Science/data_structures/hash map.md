### What is a hash table?

It's a very useful data structure that maps keys to 
values in such way that the time of looking up a value
by key is constant (mostly).
Hash table basically is just a hash function and an array. 

question id: 2045bd32-f1d1-4bb2-bf0e-f1965c8dfc5a


### Why is hash table is so useful and ubiquitous?

Because it has (mostly) costant time of look up you value by a given key - O(n)

question id: 8194e8a4-97f6-4b9b-a8de-6a7c2d2f1b8b


### What is perfomance of hash table in average and worst case?
```
            average     bad
insert      O(1)        O(n)
get         O(1)        O(n)
delete      O(1)        O(n)
```

question id: 12edb160-3bf1-4a21-8dc0-3f8fc16da187



### What complexity does dictionary have in the worst case and why?

In the worst case it's linear, O(n). In case there are several 
values stored in one slot (because of collisions) and you have to go 
through them one by one.

question id: 8e9dabca-a390-48bc-9825-8f25ffc9aa0c


### What makes a good hash map?

- low load factor (the less there is free space in your array, the more collision you will have, the worse your perfomace is)
- good hash function (the more evenly it can distribute your values within your array, the better the perfomance is)

question id: ed15a167-bd48-44ca-86cc-0cefff28d217


### What is load factor regarding hash maps?

Ratio between occupied slots in array and the array length. 
For example, hash map with this array - []["some_value"][][] - has a load factor of 1/4.
When load factor of a hash is 1 or more, there is no way you can avoid collisions and have good perfomance for every element.
Once your load factor is greater than .07, it’s time to resize your hash table.

question id: 1d197438-ba07-4e5e-a150-53b11cab7b89



### What are common use cases for hash maps?

- map key to values (for example if you want to create a phone book - name: phone)
- as a cache (for example, store server response for similar request like - request_dat: response_data)

question id: 54948125-da27-48ad-9bcf-6103b7ba8cc4


### How does hash table work under the hood?

1. Your values are stored in an array. 

2. When you assigning key value pair, a hash function takes your key 
and based on it evaluates an integer which should be an index within your array.
For example, you have an array with length of 10 slots. Your key should
evaluate to an integer between 0 and 9. You value would be stored under
this index.

3. When you want to get your value from the hash table (map, dictionary, whatever),
hash map turns your key to the same index as before. And by index you can get your
value in O(1) complexity.

question id: d84e259d-d1ce-4e37-931e-b525cc0f0445


### Give an example of a how hash function turns your key to an index within boudaries of underlying array?

There are different implementations of a hash function, but lets take a simple one.

For example, our keys is 'march 6'. And our array is 10 slots long.
- For every character, including space, we take a corresponding number from ASCII table and add them up.
For 'march 6' the sum is 609.
- Than we want to find a remainder of dividing 609 by 10. 
In Python it is 609 % 10 = 9 (modulo operator, which helps us find a remainder)
- So our result is 9 and we will store value for key 'march 6' under index 9 in our array

```python
sum(ord(letter) for letter in "your_key") % 10  # 7
```

https://youtu.be/ea8BRGxGmlA?t=283

question id: c5301e12-48cf-4a3e-b74d-02af6022581b



### What could go wrong with a hash map?

Different keys could end up to the same index within our array, especially if array is small.
It is called a collision.

question id: 77fb3be1-9eed-4670-b796-7a1302c6eb53


### What are common ways to handle collisions in hash maps? Name a couple

- chaining
- linear probing

question id:31344168-2d84-4902-b307-ec6bbdf83744


### How does chaining method of handling with collisions work?

When you want to store a key value pair and your hash function 
returns you index of array that is already been occupied, 
in chaining method you add a linked list to the occupied slot
and save your key value pair as a tuple in the first slot of
linked list. If there is another collision, the new key value pair
will also get to the linked list, but would be the second there

So this is your array, where the last slot is already occupied.
0 ["I don't know"]
1 []
2 ["whatever"]
3 []
4 []
5 ["initial_value"]

If you add a couple of new key value pairs, that would collide with
the 5 slot, you hash map would turn into this

0 ["I don't know"]
1 []
2 ["whatever"]
3 []
4 []
5 [] -> [("initial_key", "initial_value"), ("another_key", "another_value"), ("new_key", "new_value")]

In case of colllision we have to store collided keys with their values 
to be able to go through the list to find that spefic key that we were looking for.

In that keys lookup complexity becomes O(n) - linear.

question id: b865feac-6105-4085-ab3d-4be536c297d1


### How does linear probing method of handling with collisions work?

If you have a collision at your hand, a value is getting stored in the next free slot
of the array. It is stored with its key, so when you want to get it back, you can find
a proper value among shifted ones.

question id: 545b58de-213a-4133-8929-53d20338f781

