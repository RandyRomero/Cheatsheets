### How to return first word from the random string?

Write a function that takes a string and returns the first word it finds in that string. 
If the function doesn’t find a space in the string, the whole string must be one word, 
so the entire string should be returned.

answer
```rust
fn get_first_word(s: &str) -> &str {  // &str is a string slice type
    let bytes = s.as_bytes();  // to be able to go throug String item by item

    for (i, &item) in bytes.iter().enumerate() {  // enumerate means the same as in Python
        if item == b' ' {  // if we found a space
            return &s[0..i];  // return string slice between first character and space
        }
    }

    &s[..]  // return the whole string if a space was not found
}

fn main() {
    let my_sentence = "Whatever you like.";
    println!("{}", get_first_word(my_sentence))
}
```

https://doc.rust-lang.org/book/ch04-03-slices.html


question id: 46c2129d-ceb4-4d79-ba64-f3d37b52a76d