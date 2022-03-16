https://golangbot.com/interfaces-part-1/


### What is an interface? 

It is a set of method signatures, that (set) are implemented by different types.
If some type has methods that are implemented in some interfaces it is said that
this type implements this interface. 

If you have inteface *shape* with method *area() float64* and you also have type 
type *circle* with method *area() float64* that means your type *circle* implements your
*shape* interface.
  
There is an example:

```go
package main

import (
	"fmt"
	"math"
)

// some particular shape
type circle struct {
	radius float64
}

// method of this shape to calculate its area
func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

// another example of shape with other attributes
type rect struct {
	width  float64
	height float64
}

// specific for rectangular shape method of cacluclating its square
func (r rect) area() float64 {
	return r.width * r.height
}

// intefrace that unions methods of shape how to calculate their square
type shape_interface interface {
	area() float64
}

func main() {
	circle1 := circle{radius: 10}
	rect1 := rect{width: 10, height: 5}
	fmt.Println(circle1)
	fmt.Println(rect1)

	// without shape interface you would not be able to put a circle and a rectanlge in one slice
	all_shapes := []shape_interface{circle1, rect1}
	var total_square float64 = 0.0
	for _, shape := range all_shapes {
		total_square += shape.area()
	}
	fmt.Printf("Total square of %d elements is %f", len(all_shapes), total_square)
}
```

https://www.youtube.com/watch?v=lh_Uv2imp14

question id: 771b4b44-7e6e-432c-9531-152047825f23


### What is the purpose of interfaces? What problem do they solve?

Inteface makes possible to perform operations in bulk on a different types as long
as these types implement the same interface.

To perform something on types Cat, Dog, Parrot in Python you can just put them in list
and iterate over them. In Go you cannot put different types in one slice. However, 
if all of them implement set of method signatures of some interface, you can use
this interface as a type while create a slice of different types

There is an example:

```go
package main

import (
	"fmt"
	"math"
)

// some particular shape
type circle struct {
	radius float64
}

// method of this shape to calculate its area
func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

// another example of shape with other attributes
type rect struct {
	width  float64
	height float64
}

// specific for rectangular shape method of cacluclating its square
func (r rect) area() float64 {
	return r.width * r.height
}

// intefrace that unions methods of shape how to calculate their square
type shape_interface interface {
	area() float64
}

func main() {
	circle1 := circle{radius: 10}
	rect1 := rect{width: 10, height: 5}
	fmt.Println(circle1)
	fmt.Println(rect1)

	// without shape interface you would not be able to put a circle and a rectanlge in one slice
	all_shapes := []shape_interface{circle1, rect1}
	var total_square float64 = 0.0
	for _, shape := range all_shapes {
		total_square += shape.area()
	}
	fmt.Printf("Total square of %d elements is %f", len(all_shapes), total_square)
}
```

question id: 8cb75f1e-2c7b-429d-b136-5321afc5f967



### Which interface do all the types in Go always implement?

An empty interface - interface{}

question id: b66bcc91-3c71-4bfa-91ae-c9425beafca5


### How does Any type look in Golang? 

It's an empty interface

question id: 63444fe6-1863-4be8-8f42-36f1a43307d1


### Why can empty interface in Go be used as typing.Any in Python?

Because any type is considered to be implementing particular interface if this type has all methods of this interface.
Therefore, all types implement empty interface by default.

question id: 0a5a5049-87f8-45ee-9b4c-c6ef9fff703c


### Show on example how to use an interface

You have the following structures that represent two types of employees

```go
package main

import (
	"fmt"
)

type Contract struct {
	empId    int
	basicpay int
}

//salary of contract employee is the basic pay alone
func (c Contract) CalculateSalary() int {
	return c.basicpay
}

type Freelancer struct {
	empId       int
	ratePerHour int
	totalHours  int
}


//salary of freelancer
func (f Freelancer) CalculateSalary() int {
	return f.ratePerHour * f.totalHours
}

func main() {
	cemp1 := Contract{
		empId:    3,
		basicpay: 3000,
	}
	freelancer1 := Freelancer{
		empId:       4,
		ratePerHour: 70,
		totalHours:  120,
	}
	freelancer2 := Freelancer{
		empId:       5,
		ratePerHour: 100,
		totalHours:  100,
	}
}

func main() {
	// your code here
}
```

You need to write a code that calculates total amount of salaries of the given employees

answer

```go
package main

import (
	"fmt"
)

type SalaryCalculator interface {
	CalculateSalary() int
}

type Contract struct {
	empId    int
	basicpay int
}

type Freelancer struct {
	empId       int
	ratePerHour int
	totalHours  int
}

//salary of contract employee is the basic pay alone
func (c Contract) CalculateSalary() int {
	return c.basicpay
}

//salary of freelancer
func (f Freelancer) CalculateSalary() int {
	return f.ratePerHour * f.totalHours
}


func main() {
	cemp1 := Contract{
		empId:    3,
		basicpay: 3000,
	}
	freelancer1 := Freelancer{
		empId:       4,
		ratePerHour: 70,
		totalHours:  120,
	}
	freelancer2 := Freelancer{
		empId:       5,
		ratePerHour: 100,
		totalHours:  100,
	}
	employees := []SalaryCalculator{cemp1, freelancer1, freelancer2}

	expense := 0
	for _, employee := range employees {
		fmt.Printf("Type = %T, value = %v\n", v, v)
		expense = expense + v.CalculateSalary()
	}
	fmt.Printf("Total Expense Per Month $%d\n", expense)
}
```

question id: cd5db917-5705-4d7f-ade4-60f3d19c3747




For example, you have circle type and rectangle type, that can have different properties, but
they both implement area() method. Implementation could be different, but as long as they
both have exactly the same method signature, you can write shape inte

### What is an interface?

- In Go, an interface is a set of method signatures.
- Interface specifies what methods a type must have and the type decides how to implement these methods.
- When a type provides definition for all the methods in the interface, it is said to implement the interface. 

- For example, Shape can be an interface with method square(), that returns you square of any shape.
And you have two types, circle and rectangle. They both have square() method with identical signature, but
details are different. In this case, we can say both circle and rectangular implements type Shape.

How is that useful? For example, you want to calculate the total square of all different shapes you have.
So you need to go through a slice of all you shapes. Hovewer, they are all of different types, how would you 
put them into one slice? The decision is to declare a slice of interface Shape. If all of your circles, rectangles and
other shapes has the same square() method as in Shape interface, you can put them into this []Shape{}
 slice and iterare over them. The only caveat is that you can only call the method square from the elements of this []Shape{} slice.



- For example WashingMachine can be an interface with method signatures Cleaning() and Drying(). 
- Any type which provides definition for Cleaning() and Drying() methods is said to implement the WashingMachine interface.
- Go interfaces are implemented implicitly if a type contains all the methods declared in the interface.
