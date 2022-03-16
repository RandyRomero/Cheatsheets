package main

import (
	"fmt"
	"io/ioutil"
	"math/rand"
	"os"
	"strings"
	"time"
)

func main() {
	// fileBytes, err := ioutil.ReadFile("what_to_learn.txt")
	fileBytes, err := ioutil.ReadFile("programming_next.txt")

	rand.Seed(time.Now().UnixNano())

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	sliceData := strings.Split(string(fileBytes), "\n")

	// fmt.Println(sliceData)
	randIndex := rand.Intn(len(sliceData))
	fmt.Println(randIndex)
	fmt.Println(sliceData[randIndex])

}
