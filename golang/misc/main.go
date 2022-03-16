package main

import "fmt"

func countTotal(slices ...[]int) int {
	totalLen := 0
	for _, slice := range slices {
		totalLen += len(slice)
	}

	return totalLen
}

func main() {

	lst1 := []int{1, 3, 7, 12, 15}
	lst2 := []int{2, 4, 6, 8, 10}
	lst3 := []int{5, 9, 11, 13, 17}

	fmt.Println(countTotal(lst1, lst2, lst3)) // 15
}
