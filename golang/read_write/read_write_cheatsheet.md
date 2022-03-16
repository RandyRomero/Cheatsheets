### How to read body of a request?

For example, you are making a request like this:

```golang
package main

import (
	"fmt"
	"io"
	"net/http"
)


func main() {
	// make GET request
	response, err := http.Get("https://reqres.in/api/products")
	if err != nil {
		fmt.Println(err)
	}
	// how to ready body of this request?
}
```

answer:

```golang
package main

import (
	"fmt"
	"io"
	"net/http"
)

func main() {
	// make GET request
	response, err := http.Get("https://reqres.in/api/products")
	if err != nil {
		fmt.Println(err)
	}

	// read response body
	body, err := io.ReadAll(response.Body) // ioutil.Readall() for golang <= 1.15
	if err != nil {
		fmt.Println(err)
	}
	// close response body
	response.Body.Close()

	// print response body
	fmt.Println(string(body))
}
```

https://www.educative.io/edpresso/how-to-read-the-response-body-in-golang
https://stackoverflow.com/a/9650373

question id: 0e3b9265-7752-44e6-8ffc-d587fc0fb657