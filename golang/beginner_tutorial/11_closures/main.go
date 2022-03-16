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
