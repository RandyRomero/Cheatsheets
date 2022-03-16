package main

import "fmt"

func main() {

	a := 5
	b := &a

	*b = 10
	fmt.Println(a)
}
