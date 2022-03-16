### Find a word using regex and print out line with this word 

There is your text:

"We were somewhere around Barstow on the edge of the desert when the drugs began to take hold. 
I remember saying something like “I feel a bit lightheaded; maybe you should drive”
And suddenly there was a terrible roar all around us and the sky was full of what looked like huge bats, 
all swooping and screeching and diving around the car, which was going about 100 miles an 
hour with the top down to Las Vegas. And a voice was screaming: “Holy Jesus! What are these goddamn animals?"

Find any word you want via regex and print out the line with this word. A lookup word should be accepted via 
command line arguments

Here is a template:
```rust
use std::env; // to catch command line arguments


fn main() {
    let command_line_args: Vec<String> = env::args().collect();  // collect() to turn iterator returned by args to a collection

    if command_line_args.len() < 2 {
        println!("You should type a search word when you run the scirpt.\nFor example: cargo run Barstow");
        return
    }

    let search_word = &command_line_args[1];

    // your code here
}
```

answer

```rust
use regex::Regex;
use std::env; // to catch command line arguments


fn main() {
    let command_line_args: Vec<String> = env::args().collect();  // collect() to turn iterator returned by args to a collection

    let quote = "We were somewhere around Barstow on the edge of the desert when the drugs began to take hold. 
    I remember saying something like “I feel a bit lightheaded; maybe you should drive”
    And suddenly there was a terrible roar all around us and the sky was full of what looked like huge bats, 
    all swooping and screeching and diving around the car, which was going about 100 miles an 
    hour with the top down to Las Vegas. And a voice was screaming: “Holy Jesus! What are these goddamn animals?";

    if command_line_args.len() < 2 {
        println!("You should type a search word when you run the scirpt.\nFor example: cargo run Barstow");
        return
    }

    let search_word = &command_line_args[1];

    let re = Regex::new(search_word).unwrap();
    for line in quote.lines() {
        let containes_substring = re.find(line);
        match containes_substring {
            Some(_) => println!("{}", line),
            None => (),
        }
    }
}
```

question id: 827d3b33-97ca-4fbd-bf5c-3cd9645485c2


