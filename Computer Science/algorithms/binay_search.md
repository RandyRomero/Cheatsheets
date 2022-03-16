### What is a binary search?

A binary search is a searching algorithm.
It takes only sorted input. In one iteration
it eliminates half of the wrong options.

For example, you need to guess number that I 
have in mind, between 0 to 100. You'll start with 
50 and I say it's to low. That's how you know
number from 0 to 50 are wrong. If you started from 0
and asked about every number consequtively, it would 
take you 50 steps to get there, where with binary 
search you got just in one! 

Then, you ask if 75 is right number. And I say it's too
high. Again, in one step you figure out that 25 number between
75 and 100 are wrong. Then you ask is 63 
(halfway between 50 and 75) is right number... You 
got the idea, right? 

question id: d2a95035-adaf-46c2-8506-8439a4c360af


### What is required from an array of values to implement binary search?

answer
The array of values should be sorted.

question id: 674a196e-1a7f-402b-84b6-c16670bc7be6


### What is time complexity of binary search? 

O(logn) That means, that for search in array of 100 items it will
take you at top 7 steps to find the right number:

2**6 = 64 (not enough, we have 100 elements)
2**7 = 128

question id: 9d46a9e8-a632-40ca-b6f6-b8d08cfade33


### Write a Python function that performs binary search

Use this template:
```python
numbers = list(range(234, 789))

def get_index_of_number():
    # your code here
        
GUESS = 669
print(get_index_of_number(GUESS, numbers))  # returns index of GUESS number in numbers
print(numbers.index(GUESS)) # just to double check
```

answer

```python
numbers = list(range(234, 789))

def get_index_of_number(number, numbers_list):
    low = 0
    high = len(numbers_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        guess = numbers_list[mid]
        if guess == number:
            return mid
        elif guess < number:
            print("too low")
            low = mid + 1
        else:
            print("too high")
            high = mid - 1
    return -1
        
GUESS = 669
print(get_index_of_number(GUESS, numbers))
print(numbers.index(GUESS))
```

question id: 53a192b7-8b3a-41a0-bed9-984dfc3a0cba


### Write a Rust function that performs binary search

Use this template:
```rust
// your code here

fn main() {
    let guess = 383;
    let numbers: Vec<i32> = (234..789).collect();
    let idx_from_position = numbers.iter().position(|&x| x == guess);
    let idx_from_get_index = get_index(guess, numbers);
    println!("get index by my get_index(): {}", idx_from_get_index);
    println!("get index by position(): {:?}", idx_from_position);
}
```

answer

```rust
fn get_index(number: i32, number_list: Vec<i32>) -> i32 {
    let mut low = 0;
    let mut high = number_list.len() - 1;

    while low <= high {
        let mid = (low + high) / 2;
        println!("mid: {}", mid);
        let guess = number_list[mid];

        if guess == number {
            return mid as i32;
        } else if guess < number {
            low = mid + 1;
            println!("too low");
        } else {
            println!("too high");
            high = mid - 1;
        }
    }
    return -1
}

fn main() {
    let guess = 383;
    let numbers: Vec<i32> = (234..789).collect();
    let idx_from_position = numbers.iter().position(|&x| x == guess);
    let idx_from_get_index = get_index(guess, numbers);
    println!("get index by my get_index(): {}", idx_from_get_index);
    println!("get index by position(): {:?}", idx_from_position);
}
```

question id: 50df5475-7206-4641-8df2-63ab523a6c18


### Write a Golang function that performs binary search


Use the template:
```go
package main

import "fmt"

func get_number_position() {
    // your code here
}

func get_numbers(start, end int) []int {

	numbers_length := end - start

	numbers := make([]int, numbers_length)

	for i := 0; i < numbers_length; i++ {
		numbers[i] = i + start
	}
	return numbers
}

func main() {
	numbers := get_numbers(100, 945)
	fmt.Println(get_number_position(333, numbers))
}
```

answer
```go
package main

import "fmt"

func get_number_position(number int, number_list []int) int {
	low := 0
	high := len(number_list) - 1

	for low <= high {
		mid := (low + high) / 2
		guess := number_list[mid]

		if guess == number {
			return mid
		} else if guess > number {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}
	return -1
}

func get_numbers(start, end int) []int {

	numbers_length := end - start

	numbers := make([]int, numbers_length)

	for i := 0; i < numbers_length; i++ {
		numbers[i] = i + start
	}
	return numbers
}

func main() {
	numbers := get_numbers(100, 945)
	fmt.Println(get_number_position(333, numbers))
}
```

question id: 840f06b8-481f-47ae-9d88-657ee54f15b