### What is Fibonacci Numbers or Fibonacci sequence? 

A series of whole numbers in which each number is the sum of the two preceding numbers. 
Beginning with 0 and 1, the sequence of Fibonacci numbers would be 0,1,1, 2, 3, 5, 8, 13, 21, 34, etc.

question id: 7c89347e-554e-464b-9222-ba7b041f5fe0


### Write a function that takes n and returns nth Fibonacci Number (in Python)

In linear time

answer
```python
def get_nth_fib_number(n: int) -> int:
    if n <= 2:
        return 1

    previous, fib_number = 0, 1
    for _ in range(n - 1):
        # Compute the next Fibonacci number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number

    return fib_number
```

question id: fc327a05-5dea-43e6-aab3-18a9cbbcebe8



### Write a function that takes n and returns nth Fibonacci Number (in Golang)

In linear time

```go
package main

import "fmt"

// your code here

func main() {
	fmt.Println(get_nth_fib_number(8)) // 21
}
```

answer
```go
package main

import "fmt"

func get_nth_fib_number(n int) int {
	if n <= 2 {
		return 1
	}

	var previous, fib_number = 0, 1

	for i := 0; i < n-1; i++ {
		previous, fib_number = fib_number, previous+fib_number

	}
	return fib_number
}

func main() {
	fmt.Println(get_nth_fib_number(8)) // 21
}
```

question id: 5443975b-2e09-4f56-a33f-960015a06918


### Write a function that takes n and returns nth Fibonacci Number (in Rust)

In linear time

template to start from:
```rust
// your code here

fn main() {
   println!("{}", get_nth_fib_number(7))
}
```

answer
```rust
fn get_nth_fib_number(n: i32) -> i32 {
    if n <= 2 {
        return 2
    }

    let (mut previous_number, mut fib_number) = (0, 1);

    for _ in 0..n-1 {
        let temp = previous_number + fib_number;
        previous_number = fib_number;
        fib_number = temp
    }

    return fib_number

}

fn main() {
   println!("{}", get_nth_fib_number(7))
}
```

question id: 7a207534-7e51-48b5-91bd-a3a83f600534



### What is time and space complexity of this function? 

```python
def foo(n):
    if n <= 1:
        return
    foo(n - 1)
```
	
answer

Linear - O(n) - both for time and space

https://youtu.be/oBt53YbR9Kk?t=742

question id: 890baac1-ada7-46b5-91f8-940e9e4a436a




### What is time and space complexity of this function? 

```python
def bar(n):
    if n <= 1:
        return
    bar(n - 2)
```

answer

Linear - O(n) - both for time and space

You could have thought that it would be O(n/2), but it isn't. Why?
big-O says how the performance changes with the change in input size. 
If you double your array, you double your time - whether you read every element, or every other.


O(n):
10 items = 10 steps to execute
100 items = 100 steps to execute
10x growth of items = 10x growth of steps to execute


O(n/2):
10 items = 5 steps to execute
100 items = 50 steps to execute
10x growth of items = 10x growth of steps to execute

So we could eliminate /2 because it doesn't matter in big O notation
as ratio between growth of items and growth of step is the same no matter
whether you have to process every item or every other item

https://youtu.be/oBt53YbR9Kk?t=810

question id: 38e913cf-089a-404b-8c9a-880f736af62b


### What is time complexity of this function and why?

```python
def dib(n):
	if (n <= 1):
		return
	dib(n - 1)
	dib(n - 1)
```

answer
O(2^n) time - because for every additional item in list the size or required operations doubles.

[<img src="/home/aleksandr/yad/Studies/Cheatsheets/dynamic_programming/2_to_the_power_of_n_complexity.png">](2^n complexity)

https://youtu.be/oBt53YbR9Kk?t=910

question id: b02158fc-c568-413e-96e5-2f0526d52b54


### What is space complexity of this function and why?

```python
def dib(n):
    if (n <= 1):
        return
    dib(n - 1)
    dib(n - 1)
```

answer
Linear - O(n). 
Why? Because execution flow goes only in one branch at a time. Then, when it reaches the end, the last function returns
and execution goes to the other (look at the picture). In other words, on each level we only in one stack at a time,
so the number of stacks is equal to number of levels. 

[<img src="/home/aleksandr/yad/Studies/Cheatsheets/dynamic_programming/linear_space_complexity.png">](2^n complexity)

https://youtu.be/oBt53YbR9Kk?t=1101

question id: 752c7826-5129-4531-8f28-5154692201d2


### What is time and space complexity of this function and why?

```python
def dib(n):
    if (n <= 1):
        return
    dib(n - 2)
    dib(n - 2)
```

O(2^n) time
O(n) space

To know why - look through four several questions

question id: dd413367-e067-408d-8416-27e91ab42f3a


### What is time complexity of this function and why?

Note: this is classical function to find Nth Fibonacci number using recursion

```python
def fib2(n):
    if n <= 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)
```

answer

Time complexity of this function is exponential - O(2^n), because for every n+1 you need two times as more operations
than for n. You call finb2, it calls itself two times, two fib2 each call other itsels two times, so no we had 4 fib2
and so on

[<img src="/home/aleksandr/yad/Studies/Cheatsheets/dynamic_programming/2_to_the_power_of_n_complexity.png">](2^n complexity)

question id: 6930250e-a6c8-41ce-9a29-31f1604aea5b



### What is space complexity of this function and why?

Note: this is classical function to find Nth Fibonacci number using recursion

```python
def fib2(n):
    if n <= 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)
```

answer
Linear - O(n).

Why? Visualize the flow of calls. It will grow like a tree. For each call you will have exactly two more calls.
However, because execution flow goes only in one branch at a time and, when it reaches the end, the last function returns
and execution goes to the other  branch(look at the picture), we only have as many stack as the our argument n.  
In other words, on each level we only in one stack at a time, so the number of stacks is equal to number of levels. 

[<img src="/home/aleksandr/yad/Studies/Cheatsheets/dynamic_programming/linear_space_complexity.png">](2^n complexity)

https://youtu.be/oBt53YbR9Kk?t=1101

question id: 19de28c1-28c3-4275-ad48-51163a7d7a71
