### How to unpack a slice to a function as separate arguments?

For example, you have a function that takes a variable type of elements of the same type
```go
package main

import "fmt"

func getMultiples(factor int, args ...int) []int {
	multiples := make([]int, len(args))
	for index, val := range args {
		multiples[index] = val * factor
	}
	return multiples
}

func main() {
	numbers := []int{10, 20, 30}
	mult1 := getMultiples() // how to upack numbers to getMultiples() function?
	fmt.Println(mult1)
}
```

...and you want to call it, passing an array of elements but as individual arguments.
How would you do it?

answer


```go
package main

import "fmt"

func getMultiples(factor int, args ...int) []int {
	multiples := make([]int, len(args))
	for index, val := range args {
		multiples[index] = val * factor
	}
	return multiples
}

func main() {
	s := []int{10, 20, 30}
	mult1 := getMultiples(2, s...) // this is how
	fmt.Println(mult1)
}
```

https://medium.com/rungo/variadic-function-in-go-5d9b23f4c01a

question id: fdc3ab23-30df-4813-81cd-63b28809b812


### Write a function that takes any number of slices of integers

...and returns total length of numbers in slices

```golang
func countTotal() {
	// your code here
}

func main() {

	lst1 := []int{1, 3, 7, 12, 15}
	lst2 := []int{2, 4, 6, 8, 10}
	lst3 := []int{5, 9, 11, 13, 17}

	fmt.Println(countTotal(lst1, lst2, lst3))  // 15
}
```

answer

```golang
func countTotal(slices ...[]int) int {
	totalNumber := 0
	for _, slc := range slices {
		totalNumber += len(slc)
	}
	return totalNumber
}

func main() {

	lst1 := []int{1, 3, 7, 12, 15}
	lst2 := []int{2, 4, 6, 8, 10}
	lst3 := []int{5, 9, 11, 13, 17}

	fmt.Println(countTotal(lst1, lst2, lst3))
}
```

question id: 41752cf2-1119-498a-b016-d179b9b76a04