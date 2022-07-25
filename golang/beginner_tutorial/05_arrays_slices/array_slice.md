### How to append to a slice?

```go
package main

import "fmt"

func main() {
    numbers = []int{};
    numbers = append(numbers, 1);
    fmt.Println(numbers) // [1]
    numbers = append(numbers, 2, 3, 4);
    fmt.Println(numbers) // [1, 2, 3, 4]
}
```

https://tour.golang.org/moretypes/15


question id: 7e20f7ca-f666-42fd-b57e-1c86d581fb91


### How to create an empty slice of integers?

```go
package main

import "fmt"

func main() {
    var collectino = []int{};
}
```

question id: af1c7f90-a412-4f61-8d76-27399cc9e07a


### How to create an empty list of integers with predifined length?

```go
package main

import "fmt"

func main() {
    var collection = make([]int, 12);
}
```

question id: a15c3c61-c5ef-4867-aa75-8891f8323eb3



### How to create a slice of numbers from 10 to 20?

answer
```go
package main

import "fmt"

func get_numbers(start, end int) []int {

	numbers_length := end - start

	numbers := make([]int, numbers_length)

	for i := 0; i < numbers_length; i++ {
		numbers[i] = i + start
	}
	return numbers
}

func main() {
	numbers := get_numbers(10, 21)
	fmt.Println(numbers)
}
```

question id: 9d52a4c7-d485-4aa9-a2a8-d54bbf0b46bd
