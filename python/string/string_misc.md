### How to remove something from a string?

You are given this string "What are wonder@#$ful day!".

How to to be left with "What are wonderful day!" ?

answer
Use string.replace()

```python
"What are wonder@#$ful day!".replace("@#$", "")  # 'What are wonderful day!'
```

question id: e6c7ed95-d820-47d4-b9d6-f4e5d1879ea6


### How to remove only the first occurence of some string/char from a string with replace()?

Given string:
"Is there so?methig wrong?"

answer
Use optional 'max' argument like this

```python
"Is there so?methig wrong?".replace("?", "", 1)  # "Is there so?methig wrong?"
```

question id: 1e2417f2-f035-4038-8041-d231d23e8026


### How to get a number of occurences of a substring in a given string?

For example, what number of "e" in this exact sentence?

answer
```python
"For example, what number of 'e' in this exact sentece?".count("e")  # 8
```

question id: 58bd3721-51e6-4b83-80b2-8a6307e07091