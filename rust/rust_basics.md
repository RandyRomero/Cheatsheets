

### What's cargo?

Cargo is the Rust package manager. Cargo downloads your Rust package's dependencies, compiles your packages, makes distributable packages, and uploads them to crates.io, the Rust community’s package registry.

question id: 2b9f16de-c6da-4083-9788-c1987dc4e198


### How to create a new project?

cargo new project_name

question id: 4e893c15-e5e3-431d-9a7d-82ba98dc2c46



### How to run a rust project?

cd path/inside/your/project
cargo run

question id: 5f17e6ba-a4f5-41e8-9887-133734afdd04


### How to iterater through a range of number from 0 to 10 and print every number out? 

```rust
fn main() {
    for i in 0..11 {
    	println!("{}", i)
    }
}
```

question id: c94b37b1-a818-4fbd-8273-267cb27b5215


### What is an array in Rust?

An array is a collection of objects of the same type T, stored in contiguous memory.

The length of array is immutable - you cannot add or remove elements. 
Though you can change elements inside array. 

Arrays are created using brackets [], and their length, 
which is known at compile time, is part of their type signature [T; length].

question id: 02a22918-945f-4921-bbde-f8d8eb716407


### How to create an array with the given values and print it out?

Given values: "Cats", "Dogs", "Fish"


```rust
fn main() {
    let animals = ["Cats", "Dogs", "Fish"];
    println!("{:?}", animals)
}
```

question id: 5341d884-beb9-4d6c-a631-34972d004133


### How to create an array with 5 zeros in it?

answer
```rust
fn main() {
    let zeroes = [0; 5];
    println!("{:?}", zeroes)
}
```

question id: 6d7ca1da-3b96-403e-b88f-4a101656936



### How to create an array with the given values and print it out?

Given values: 1, 2, 3

```rust
fn main() {
    let numbers = [1, 2, 3];
    println!("{:?}", numbers)
}
```

question id: 0835ccfa-398a-4794-ad56-1f6f076bbe85



### How to print a value from a array one by one? 

You have to define an array that has three items inside:
"Cats", "Dogs", "Fish"
And iterate over it

answer
```rust
fn main() {
    let collection = ["Cats", "Dogs", "Fish"];
    
    for item in collection {
        println!("{}", item)
    }
}
```

question id: 31a4e07d-eafb-484f-b1fd-019d78ccaa6b


### How to change an element in an array?

Given array:
```rust
["John", "Jane", "Jack", "Jill"]
```
How to change John for Jack?

answer
```rust
fn main() {
    let mut users = ["John", "Jane", "Jack", "Jill"];
    users[0] = "Jack";
    println!("{:?}", users)
}
```

question id: 9a289b04-4e7f-4e96-91d7-fde4dc85569a


### How to create a duration of 1 second and print it out?

```rust
use std::time::Duration;

fn main() {
    let time_limit = Duration::new(1,0);

    println!("{:?}", time_limit);
}
```

question id: bef7c7df-f19e-432d-8c4f-eda586f00558


### Write an example of if else

answer

```rust
fn main() {
    let colour = "red";
    
    if colour == "green" {
        println!("green");
    } else if colour == "yellow" {
        println!("yellow");
    } else {
        println!("no match");
    }
}
```

question id: 6f2d01c6-4e98-4684-89e5-86ece8ac804b


# How to iterate over lines of a multiline string?

given string
```
Every face, every shop, bedroom window, public-house, and
dark square is a picture feverishly turned--in search of what?
It is the same with books. What do we seek through millions of pages?
```

answer
```rust
fn main() {
    let text = "\
Every face, every shop, bedroom window, public-house, and
dark square is a picture feverishly turned--in search of what?
It is the same with books. What do we seek through millions of pages?";

    for line in text.lines() {
        println!("{}", line);
    }
}
```

question id: 65e01ef1-eeb1-4ce5-85ef-3b854b286947


### What is a slice in Rust?

A slice in rust is a dynamically-sized view into a contiguous sequence.
Slices are a view into a block of memory represented as a pointer and a length. 

question id: 7abb6a4e-7cbd-48e9-b63e-3a961c5bd52f


### Can slice in Rust expand/contract?

answer:

No. Once you assign it, you can't make it bigger or smaller.

question id: 5b13f8fc-d7f1-4e04-80ad-59ffc60b5cd9


### What does mean in Rust that a slice in rust is a dynamically-sized?

answer:


It means that the size of slice isn't known at compile time. 
Yet, like arrays, these don’t expand or contract.

question id: 82d8d405-fcd8-4fba-90d8-1304b1635405


### How to print out length of a string?

```rust
fn main() {
    let colour = "red";
    println!("{}", colour.len())
}
```

question id: 30ae097e-1b7b-4a5e-beba-c6c5f809e07f


### How to print out length of an Array or Vector?

```rust
fn main() {
    let my_vec = vec![1, 2, 3, 4, 5];
    println!("{}", my_vec.len())
}
```

question id: 09773502-f270-418d-a945-f3984c205e07


### Take a slice

Having an array [1, 2, 3, 4, 5] take a slice ([2, 3]) of array's elements, 
print it out and say what type it has

answer
```rust
fn main() {
    let collection = [1, 2, 3, 4, 5];
    let slice = &collection[1..3];  // type of slice is &[i32]
    println!("{:?}", slice)
}
```

question id: b83eeb33-d98f-4c22-9a6b-b9816aad3112


### What is Vector? 

answer
Vectors (Vec<T>) are growable lists of item of the same type.

https://doc.rust-lang.org/book/ch08-01-vectors.html

question id: e3e49a3c-e7c4-46e7-99ae-4621485671cc


### How to define a new Vector without any values and print it out?

answer
```rust
let collection: Vec<i32> = Vec::new();

// or just

let mut collection = Vec::new();
```

question id: ae19f142-0e80-4d15-9d42-fb335dd77cdf



### How to define a new vector with 1, 2, 3 in it as initial values?

answer

```rust
fn main() {
    let collection = vec![1, 2, 3];
    println!("{:?}", collection)
}
```

question id: 70598e3b-4399-4d2a-a6f9-8cb4bfccad57


### How to create a new **emtpy** Vector and then add some values to it?

answer
```rust
fn main() {
    let mut collection = Vec::new();

    collection.push(5);
    collection.push(6);
    collection.push(7);
    collection.push(8);

    println!("{:?}", collection)
}
```

question id: 130c593f-1003-42e3-a2e9-f13e7697c8a1


### How to remove a value from Vector?

Given vector
[1, 2, 3, 4, 5]

answer
```rust
fn main() {
    let mut collection = vec![1, 2, 3, 4, 5];

    collection.remove(0); // removing the first element
    collection.remove(3); // removing the last element
    
    println!("{:?}", collection)
}
```

question id: 45435939-c0cf-4ce2-a6ce-5688d4eb86fc


### How to figure out if some words a part of a given sentece?

Given sentence: "There are some words that pretend to be a sentence"
Find out if there word "some" inside

answer

```rust
fn main() {
    let my_sentence = "There are some words that pretend to be a sentence";
    println!("{:?}", my_sentence.contains("words"))
}
```

question id: 3f6b438b-ead7-4e57-bf88-02ecfd0eae4f


### How to create a Vector with predefined capacity?

For example, I know that my Vector whould store exaclty 100 elements, but not right away, somewhere later.
How do I make a new empty vector which and allocate 100 slots for items in it?

answer
```rust
fn main() {
    let mut my_vec: Vec<i32> = Vec::with_capacity(100);
}
```

question id: 90d1c937-c0f1-491c-a3b3-d29fca4984e8


### Why do we need Vec::with_capacity()?

answer
with_capacity() creates a vector with the given capacity but with zero length. 
It means that until this capacity is reached, push() calls won't reallocate the vector, making push() essentially free

question id: b70273aa-5b33-467c-a62b-3c5c0132c742


### How to check if Vector has no value? 

answer
.is_empty()

question id: c5cce4b2-762a-40ab-8407-cb38905f85ec


### What is saturating_sub() in Rust?

answer

It is subtraction, like in 10 - 5 = 0, but for types that does not support negative values.
For example, usize doesn't support negative values. If you subtact from it a number that is 
bigger than your usize number, you'll get a panick. However, instead of subraction you can use
saturating_sub, which will return 0 instead of panicking.

```rust
fn main() {
  let mut tag: usize = 5;
  tag = tag.saturating_sub(10);
  println!("{}", tag)
}
```

question id: efe038de-8a36-4f7c-8174-651805db8e33


### What's tuple in Rust?

It's a linear data structure that groups together different types.
Basically, its a struct, but without names for its members.
Length of tuple cannot be changed.
You can change any value withing tuple by assignment (in comparison, in Python you can't).

question id: 06c404d5-adb2-48da-95cd-d5ff18edd4ef


### Create a tuple with these elements and print out just one value from it

3, true, "Whatever"

answer
```rust
fn main() {
  let my_tup = (3, true, "Whatever");
  println!("{:?}", my_tup.1)
}
```

question id: 7168920a-6888-4faf-9d71-86a2c5e9f1c1


### Create a tuple with these elements with types and print out just one value from it

answer
```rust
fn main() {
    let my_tup: (i32, bool, &str) = (3, true, "Whatever");
    println!("{:?}", my_tup.1)
}
```

question id: 0472e26e-56d2-417c-9c9c-ef905aece9c5


### Having these values, make a tuple with them, then assign three separate variables with values from this tuple

3, true, "Whatever"

answer
```rust
fn main() {
  let my_tup = (3, true, "Whatever");
  let (a, b, c) = my_tup;
  println!("{}, {}, {}", a, b, c)
}
```

question id: fd039a52-fa34-419e-94b1-acdf3ec6ccb


### What is this type?

Vec<Vec<(usize, String)>>

answer

It is vector of vectors of tuples where the 1st element of tuple is usize and the 2nd is a String.

answer: aad3f8ab-d572-4b0b-8438-a496f023c41f


### How is package called in Rust?

crate

question id: aa9f2614-dad1-4c5b-a991-f3443b7aeb99


### How to add a crate (package) to dependencies? 

cargo add your_crate_name

question id: 87512924-8ddc-4aba-8f24-95f6c55a7a4


### How to print out the first command line argument?

For example, you run your rust script with a command line argument. 
How to catch it and print it out?

answer

```rust
use std::env; // use std::env::args() to catch command line arguments


fn main() {
    let command_line_args: Vec<String> = env::args().collect();  // collect() to turn iterator returned by args to a collection

    if command_line_args.len() < 2 {
        println!("You forget to pass a command line argument.\nFor example: cargo run Barstow");
        return
    }

    println!("Your command line argument is: {}", &command_line_args[1])
}
```

question id: ffacd556-742e-4662-acca-a1dd7a0e5cd1


### How to assign two mutable variables in one line?

answer

```rust
let (mut previous, mut fib_number) = (0, 1);
```
However, you cannot assign types at the same time

question id: aa520845-efaf-4ee8-87ed-56acac9023b7


### How to create a Vector with range of numbers between 289 and 789?

answer
```rust
fn main() {
    let numbers: Vec<i32> = (234..789).collect();
    println!("{:?}", numbers)
}
```

question id: 55c5cae8-71aa-49f2-91ac-c45e23a15c3b


### How to find an index of a value within Vector?

You have to create a vector with a range of numbers 
and find an index of a number 333 

answer
```rust
fn main() {
    let numbers: Vec<i32> = (234..789).collect();
    let result = numbers.iter().position(|&x| x == 333);
    match result {
        Some(result) => println!("{:?}", result),
        None => println!("Item not in the vector")
    }
}
```

question id: 7fdc2258-9e2f-428a-b0cf-a9b13684000f

### How to read text from a file?

For example, read and print line by line Cargo.toml

answer
```rust
use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;

fn main() {
    let f = File::open("Cargo.toml").unwrap();
    let reader = BufReader::new(f);

    for line_ in reader.lines() {
        let line = line_.unwrap();
        println!("{}", line);
    }
}
```

question id: 638f91c2-c945-4dc6-a3b3-48e54e86acfd


### What's unit type?

It is used to express that a function returns no value.
It looks like this - '()' - and formally it is a empty tuple.
However, we usually don't need to show explicitly that function
returns nothing. Although, if you want to, it would look something
like this:


```rust
fn clear(text: &mut String) -> () {
    *text = String::from("");
}
```

question id: 0b6ae0b9-ee30-4dc1-b43a-e13b5ed40bd2


### How to denote that a function returns nothing?

answer

Use a 'Never' type - !

```rust
fn dead_end() -> ! {
    panic!("you have reached a dead end");
}
```

question id: 8169deab-ac2d-4ba0-bf70-72eced9544ce


### How to denote and print out a struct?

For example, you want to denote User struct
with fields: id, active, name

```rust
#[derive(Debug)]
    struct User{
        id: i32,
        active: bool,
        name: String,
    }


fn main() {
    let jack_the_user = User{
        id: 1,
        active: true,
        name: String::from("Jack"),
    };

    println!("{:?}", jack_the_user);
}
```

question id: ae550556-3061-400e-a143-5a7f65c3bcd3



### Using the Field Init Shorthand when Variables and Fields Have the Same Name 

You have this struct:

```rust
#[derive(Debug)]
struct User {
    active: bool,
    username: String,
    email: String,
}

// your code here

fn main() {
    let user = build_user(String::from("Jack"), String::from("Whatever"));
    println!("{:?}", user)
}
```

Create a function build_user which takes two arguments: username and email, and 
returns a new user

answer
```rust
#[derive(Debug)]
struct User {
    active: bool,
    username: String,
    email: String,
}

fn build_user(username: String, email: String) -> User{
    User {
        username,
        email,
        active: true
    }
}

fn main() {
    let user = build_user(String::from("Jack"), String::from("Whatever"));
    println!("{:?}", user)
}
```

https://doc.rust-lang.org/book/ch05-01-defining-structs.html#using-the-field-init-shorthand-when-variables-and-fields-have-the-same-name


question id: 0fb885ec-31d0-4ab1-8440-d9be4b7b69de


### How can you make your struct printable?

By default, after you define your struct and make a new instance of it, you can't print it out.
Example:

```rust
struct User {
    name: &str
}

fn main() {
    let user = User{name: "Jack"};
    println!("{:?}", user)
}
```
It will give you an error. What should you do to fix this?

answer:

add `#[derive(Debug)]` on top of your struct like this:
```rust
#[derive(Debug)]
struct User {
    name: &str
}

fn main() {
    let user = User{name: "Jack"};
    println!("{:?}", user)
}
```

question id: e6befc99-143e-4706-8887-846166a6b86b
