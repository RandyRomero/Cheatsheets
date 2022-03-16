### What are generics and why do we need them in Golang?

Generics are kind of like functions for variable types. For example recently in Go, every function we write must apply 
to only a single type, and of course, this is not scalable and leads to code duplication. Without generics, we would 
need to repeat our code multiple times, each time with a different type. 

For example, it is not possible to write a simple copy function that can operate on any container type, e.g., map. 
What we have to do is write separate functions, with almost the same signature except for the types, for the different 
target types.

The goal of adding generics to the language is clear to be able to write libraries or functions that would work 
or operate on arbitrary types or values.

Let's say you need to make a function that takes one slice and prints it. Then you might write this type of function:
```
func Print(s []string) {
	for _, v := range s {
		fmt.Print(v)
	}
}
```
Simple, right? What if we want to have the slice be an integer? You will need to make a new method for that:

```
func Print(s []int) {
	for _, v := range s {
		fmt.Print(v)
	}
}
```

These solutions might seem redundant, as we're only changing the parameter. But currently, that's how we solve it in Go without resorting to making it into some interface.

question id: 6aaa1177-3de2-44e4-8384-801c0d68625c


