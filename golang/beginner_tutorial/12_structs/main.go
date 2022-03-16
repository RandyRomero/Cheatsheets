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

func (p *Person) hasBirthday() {
	p.age++
}

func (p *Person) getMarried(lastName string) {
	if p.gender == "m" {
		return
	} else {
		p.lastName = lastName
	}
}

func main() {
	person1 := Person{firstName: "Samantha", lastName: "Smith", city: "Boston", gender: "f", age: 25}
	fmt.Println(person1)
	person1.getMarried("Nicolson")
	fmt.Println(person1)
}
