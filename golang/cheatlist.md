### How to check what version of Golang you have on your system?

```shell
go version
```

question id: c5ea6b4e-4c10-47e1-aed2-337dd60a6a11


### How to figure out your GOPATH?

```shell
go env | grep GOPATH
```

question id: 6b0fd54f-890e-4122-a49d-cb26a411baf2


### Write and run hello world in Golang

touch main.go

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello world!")
}
```

go run main.go

question id: 24817ae1-d06a-4b3e-9bb0-820e7d45e4cf


### How to print out type of a variable?


```go
package main

import "fmt"

func main() {
	var whatever = "whatever"
	fmt.Printf("%T\n", whatever)
}
```

>> string

question id: 1b5d4c83-9c61-4646-a258-e00a2541fc9c

### How to round a number up? How to round down? How to get a square root? Write the whole module

```go
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(math.Ceil(2.7))
	fmt.Println(math.Floor(2.7))
	fmt.Println(math.Sqrt(16))
}
```

question id: 3f9561b6-3ffb-4d90-a8ac-6cf7450a5c6


### Write a function that takes a name and returns "Hello <name>" 


```go
package main

import "fmt"

func greeting(name string) string {
	return "Hello " + name
}

func main() {
	fmt.Println(greeting("Whatever"))
}
```

question id: f1e52b75-e90e-4c86-a4cf-04d9fd157cdc


### Write a function that sums up two given integers

```go
package main

import "fmt"

func getSum(num1, num2 int) int {
	return num1 + num2
}

func main() {
	fmt.Println(getSum(1, 2))
}
```

question id: 3de403f0-c543-45bb-bc53-dbbf8798db80


### Create an array, then add "Apple" and "Orange" to this array, then print out the whole array and the first item

```go
package main

import "fmt"

func main() {
	var fruitArr [2]string
	
	fruitArr[0] = "Apple"
	fruitArr[1] = "Orange"
	
	fmt.Println(fruitArr)
	fmt.Println(fruitArr[1])
}
```

question id: 6f5028dc-3dbe-479e-ae92-ef0a3ac21f4f


### Create an array with values "Apple" and "Orange", then print out the whole array and the first item

```go
package main

import "fmt"

func main() {
	fruitArr := [2]string{"Apple", "Orange"}

	fmt.Println(fruitArr)
	fmt.Println(fruitArr[1])
}
```

question id: ff99b24f-adf8-4d9e-bc25-8ae455cdd6e5


### Create a slice with values "Apple", "Orange" and "Grape" and print it out it length

```go
package main

import "fmt"

func main() {
	fruitSlice := []string{"Apple", "Orange", "Slice"}
	fmt.Println(len(fruitSlice))
}
```

question id: cff79a06-f13d-44f8-b5c9-d3411e809831


### Print out from the second to the last values of a slice

For example, you have the following slice

```go
fruitSlice := []string{"Apple", "Orange", "Slice", "Cherry"}
```

answer

```go
package main

import "fmt"

func main() {
	fruitSlice := []string{"Apple", "Orange", "Slice", "Cherry"}
	fmt.Println(fruitSlice[1:4])) // [the end border is exclusive]
}
```

question id: 085fc18d-c47f-4aa1-8922-90307fec1bc8


### What is a general syntax of if else statements in Go?

```go
if x > y {
	// do something
} else if x < y {
	// do something else
} else {
	// do whatever you want
}
```

question id: 0625d907-782f-46dc-b7bc-5596a1ccfa72


### What are operator for OR and AND logic in Go?

'&&' for AND 
'||' for OR

question id: 92edb695-2920-41e3-a8fb-26b49807344a


### How does switch statemt in Go look like?

```go
switch color {
case "red":
	// do something
case "blue":
	// do something else
default:
	// do something defaulty
}
```

question id: ce98623b-20e4-47c1-9e88-8375b05f5543


### How does for loop in Go look like?

```go
for i := 1; i < 10; i++ {
	fmt.Println(i)
}
```

question id: 6a2d3da6-a3c5-41ce-94b1-20d9f8a9b89f


### How is the counterpart of Python dictionary called in Golang?

It's called a map.

question id: deef1bdb-0b4d-4bd2-a27d-bef24949cdbe


### How to define a map where keys and values are of a string type?

```go
emails := make(map[string]string)
```

question id: b94c3545-2812-4edc-906a-d45e2bd3c79d


### How to define a map and fill it with some values at the same time?

values: 
"john" - "john@mail.com" 
"alice" - "alice@email.com"

answer
```go
package main

import "fmt"

func main() {
	emails := map[string]string{"john": "john@mail.com", "alice": "alice@email.com"}
	fmt.Println(emails)
}
```

question id: 41a8654e-1eca-418a-bfab-72e04bfb324f



### How add a key value pair in a map?

```go
emails := make(map[string]string)

emails["Bob"] = "bob@mail.com"
```

question id: a143a849-506c-4eb0-bf3b-202dc7ed44ed


### How to get a value by a key from a map?

```go
emails := make(map[string]string)

emails["Bob"] = "bob@mail.com"

emails["Bob"] // "bob@mail.com"
```

question id: 3433596a-e488-41d8-b388-1f5d4d8540ce


### How to remove a key value pair from a map by its key?

```go
emails := make(map[string]string)

emails["Bob"] = "bob@mail.com"

delete(emails, "Bob")
```

question id: db646d5b-dbee-4b7f-a99d-f47f04b45de3


### How to declare a map and add key value pairs at one fell swoop?

```go
emails := map[string]string{"Bob": "bob@mail.com", "Sheron": "sheron@mail.com"}
```

question id: 4e26cd2b-d8be-4744-8d6b-ba6089dc2545


### How to iterate over a slice?

You've given a slice 

```go
ids := []int{1, 2, 3, 4, 5}
```
How to print out every item in a loop?

answer
```go
package main

import "fmt"

func main() {
	ids := []int{1, 2, 3, 4, 5}

	// Not using index
	for _, id := range ids {
		fmt.Println(id)
	}
}
```

question id: 763857f8-e7ba-4b5e-bf70-05b247cef3e1


### How to range over a map to print out key value pairs?

You've given a map
```go
emails := map[string]string{"Bob": "bob@mail.com", "Sheron": "sheron@mail.com"}
```

answer
```go
package main

import "fmt"

func main() {
	emails := map[string]string{"Bob": "bob@mail.com", "Sheron": "sheron@mail.com"}
	for key, value := range emails {
		fmt.Printf("%s: %s\n", key, value)
	}
}
```

question id: 504f807e-834c-43b2-b64c-5e25b93a7717


### How to iterate over keys of a map?

You've given a map
```go
emails := map[string]string{"Bob": "bob@mail.com", "Sheron": "sheron@mail.com"}
```

answer

```go
package main

import "fmt"

func main() {

	emails := map[string]string{"Bob": "bob@mail.com", "Sheron": "sheron@mail.com"}
	for key := range emails {
		fmt.Printf("Name: %s\n", key)
	}
}
```

question id: dde5bc4e-3919-45f2-bf3d-522ec02c8301


### What would be the output?

```go
package main

import "fmt"

func main() {

	a := 5
	b := &a
	fmt.Println(a, b)
}
```

answer

something like `5 0xc0000b6010`
because b holds memory adress of a (pointer to a)

question id: e7c76d7e-ea77-4bba-9696-6be72d0a164d


### What would be the output?


```go
package main

import "fmt"

func main() {

	a := 5
	b := &a

	fmt.Println(b, *b)
}
```

answer

something like `0xc0000b6010 5`

because b is a pointer here

question id: b442ef84-b86c-40a5-a2e1-cff98724e1bd

### What does *some_var mean?

* is used to read a value from a memory address, where some_var is a memory adress

question id: ab72e308-a1ac-437f-8845-58ac8d8b3739


### How to print out a type of a variable?


```go
package main

import "fmt"

func main() {

	a := 5
	b := &a

	fmt.Printf("%T\n", b)
	fmt.Printf("%T\n", *b)
}
```

question id: 3e5ce56d-b138-4d4f-9737-fbfac0018e4c


### What would be the output?

```go
package main

import "fmt"

func main() {

	a := 5
	b := &a

	*b = 10
	fmt.Println(a)
}
```

answer
10

question id: 236c0ade-56ea-418c-82a9-6d9d57539b09


### Write a function that takes an integer and returns the sum of all of the taken integers


Example of usage:
```go
func main() {
	sum := adder()
	fmt.Println(sum(1)) // 1
	fmt.Println(sum(5)) // 6
	fmt.Println(sum(10)) // 16
}
```

Hint: use closure

answer

```go
package main

import "fmt"

func adder() func(int) int {
	sum := 0
	return func(num int) int {
		sum += num
		return sum
	}
}

func main() {
	sum := adder()
	fmt.Println(sum(1))
	fmt.Println(sum(5))
	fmt.Println(sum(10))
}
```

question id: d1a13183-b991-43df-bc51-0e8e198b47db


### Create a struct with some fields, then instantiate this struct, populate fields and print it out

```go
package main

import "fmt"

type Person struct {
	firstName string
	lastName  string
	city      string
	gender    string
	age       int
}

func main() {
	person1 := Person{firstName: "Samantha", lastName: "Smith", city: "Boston", gender: "f", age: 25}
	fmt.Println(person1)
	fmt.Println(person1.firstName)
}
```

question id: 93df1a23-4ad2-4568-b6b8-b5a5f988dfbb


### How to get access to an attribute of an instantiate struct?

Via dot. For example

```go
package main

import "fmt"

type Person struct {
	firstName string
	lastName  string
	city      string
	gender    string
	age       int
}

func main() {
	person1 := Person{firstName: "Samantha", lastName: "Smith", city: "Boston", gender: "f", age: 25}
	fmt.Println(person1)
	fmt.Println(person1.firstName)
	person1.age++
	fmt.Println(age)
}
```

question id: 35519aca-e4a0-44aa-968c-8ed41c8f12a7


### What are two types of methods of a struct and what is the difference?

- value receivers
- pointer receivers

Use value receiver when you don't change any data of an instance of your struct
Use pointer receivers otherwise

question id: e47350e8-c475-470a-bf7d-9779683dd734


### Write an example of value receiver method

You have the following struct 

```go
package main

import "fmt"

type Person struct {
	firstName string
	lastName  string
	city      string
	gender    string
	age       int
}

func main() {
	person1 := Person{firstName: "Samantha", lastName: "Smith", city: "Boston", gender: "f", age: 25}
	fmt.Println(person1)
}
```

Write a method `greet` that uses first and last name of a person and his or her age

Output should be like 'Hi, I am Ivan Ivanov and I am 34 year old`

answer

```go
package main

import (
	"fmt"
	"strconv"
)

type Person struct {
	firstName string
	lastName  string
	city      string
	gender    string
	age       int
}

func (p Person) greet() string {
	return "Hi, I am " + p.firstName + " " + p.lastName + " and I am " + strconv.Itoa(p.age) + " years old."
}

func main() {
	person1 := Person{firstName: "Samantha", lastName: "Smith", city: "Boston", gender: "f", age: 25}
	fmt.Println(person1)
	fmt.Println(person1.greet()) // "Hi, I am Samantha Smith and I am 25 years old."
}
```

question id: 062a5c7b-9db6-48fc-8810-83584c5a29c


### Write an example of pointer receiver

You've given the following struct

```go
package main

import "fmt"

type Person struct {
	firstName string
	lastName  string
	city      string
	gender    string
	age       int
}

func main() {
	person1 := Person{firstName: "Samantha", lastName: "Smith", city: "Boston", gender: "f", age: 25}
	fmt.Println(person1)
}
```

Write a method `hasBirthday` that increments the age of a person by one

answer

```go
package main

import "fmt"

type Person struct {
	firstName string
	lastName  string
	city      string
	gender    string
	age       int
}

func (p *Person) hasBirthday() {
	p.age++
}

func main() {
	person1 := Person{firstName: "Samantha", lastName: "Smith", city: "Boston", gender: "f", age: 25}
	fmt.Println(person1) // {Samantha Smith Boston f 25}
	person1.hasBirthday()
	fmt.Println(person1)  // {Samantha Smith Boston f 26}
}
```

question id: 27e27685-39ce-4ff7-89b4-3a042687ac27


### Write an example of pointer receiver

You've given the following struct

```go
package main

import "fmt"

type Person struct {
	firstName string
	lastName  string
	city      string
	gender    string
	age       int
}

func main() {
	person1 := Person{firstName: "Samantha", lastName: "Smith", city: "Boston", gender: "f", age: 25}
	fmt.Println(person1)
}
```

Write a method `getMarried` which takes `lastName` and assigns this last name to the person if the person is female

answer

```go
package main

import (
	"fmt"
	"strconv"
)

type Person struct {
	firstName string
	lastName  string
	city      string
	gender    string
	age       int
}


func (p *Person) getMarried(lastName string) {
	if p.gender == "m" {
		return
	p.lastName = lastName
}

func main() {
	person1 := Person{firstName: "Samantha", lastName: "Smith", city: "Boston", gender: "f", age: 25}
	fmt.Println(person1) // {Samantha Smith Boston f 25}
	person1.getMarried("Nicolson")
	fmt.Println(person1) // {Samantha Nicolson Boston f 25}
}
```

question id: bb802143-a0fa-48f0-96ad-cc5a5c5184eb


### How to convert an int to a string?

strconv.Itoa(54) // "54"

question id: 99c37691-4038-4f67-b318-9fc99ea27098


### How to skip a line with linting error?

// nolint

question id: d49ba03c-31af-4f07-af9c-773b8f3b0e0dcl


### How to remove packages installed with go get?

answer:

`go mod tidy` will remove all unnecessary packages from your go.mod and go.sum, though folders
you have to remove from disk manually

question id: 162a7206-c2aa-4b23-b563-6b184b1a6bee


### How to set and get an environmental variable?

```golang
package main

import (
	"fmt"
	"os"
)

func main() {
	os.Setenv("DB", "Whatever")
	fmt.Println(os.Getenv("DB"))
}
```

question id: 3bd3d492-18e2-4304-a41c-3741673afba4