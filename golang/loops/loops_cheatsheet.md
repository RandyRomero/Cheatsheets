### How to write an infinite while loop in Golang?

```golang
package main

import "fmt"

func main() {
	for { // golang does not have separate statement for while loops
		fmt.Println("whatever")
	}
}
```

question id: 0728769a-7d01-44ac-84c0-ea8a4d7d2bfd