### How to covert a struct to json?

For example, you have a struct like this:
```golang
package main


type Foo struct {
	Name string
}

func main() {
	foo := Foo{Name: "Whatever"}
}
```

How to serializer it to json?

answer

```golang
package main

import (
	"encoding/json"
	"fmt"
)

type Foo struct {
	Name string
}

func main() {
	foo := Foo{Name: "Whatever"}
	fooJson, err := json.Marshal(&foo)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(fooJson) // bunch of bytes which is our JSON representation of foo
}
```

question id: 01266e4a-7aa2-45be-b81c-ce591e1e571c


### Why can't we serialize a struct like this to JSON?

For example, you have a struct like this:
```golang
package main


type Foo struct {
	name string
}

func main() {
	foo := Foo{name: "Whatever"}
}
```

And if we serialize it, we will get an empty byte string. Why?

answer:

keys in your struct should be capitalized if you want them to be in resulting JSON

https://stackoverflow.com/questions/26327391/json-marshalstruct-returns

question id: b5f14880-a488-444d-9ee8-83dfdfa967e0


### How to deserialize JSON bytes to a map?

For example, you have JSON bytes like this
```golang
package main

import (
	"encoding/json"
	"fmt"
)

type Foo struct {
	Name string
}

func main() {
	foo := Foo{Name: "Whatever"}
	fooJson, err := json.Marshal(&foo)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(fooJson) // bunch of bytes

	// How to deserialize `fooJson` to a map?
}
```

How to deserialize `fooJson` to a map?

answer

```golang
package main

import (
	"encoding/json"
	"fmt"
)

type Foo struct {
	Name string
}

func main() {
	foo := Foo{Name: "Whatever"}
	fooJson, err := json.Marshal(&foo)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(fooJson) // bunch of bytes

	// convert fooJson bytes to golang map

	var whatever map[string]interface{}

	err = json.Unmarshal(fooJson, &whatever)
	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(whatever) // map[Name:Whatever]
}
```

question id: 88c248f7-b751-4970-85b1-b5a3f8093836