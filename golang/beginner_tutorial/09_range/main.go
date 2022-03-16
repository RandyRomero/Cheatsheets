package main

import "fmt"

func main() {
	// ids := []int{1, 2, 3, 4, 5}

	// // Not using index
	// for _, id := range ids {
	// 	fmt.Println(id)
	// }

	emails := map[string]string{"Bob": "bob@mail.com", "Sheron": "sheron@mail.com"}
	for key := range emails {
		fmt.Printf("Name: %s\n", key)
	}
}
