# MorseCodeDecoder
* [Part 2 Link]()
* [Worksheet 3 Link]()

*Feb 2023*

Within this worksheet we were challenged to make a binary tree to encode and decode morse code, where a '.' refers to a left movement and '-' a right movement.

### Index
* [Development](#development-1)
    * [Creating a Tree](#creating-a-tree)
    * [Encoding](#encoding)
    * [Decoding](#decoding)
    * [Printing Tree](#printing-tree)
* [How to run](#how-to-run)
* [Tests](#tests)


# Development [^1]
### Creating a tree
To start off with this project I wanted to create a tree, I had a few options of how to do this, to save time and in an attempt to make the code look better I decided to not manually list each node of the tree when inserting:
```python
tree.insert.left.left.right.left("F")
```
Instead of doing this I created a function to create the tree for me, all I had to do was provide the morse code for each character via a python Dictionary. This let me better visulise what was being done and let me add characters with ease.

> The dictionary is not used anywhere else apart from the setup to allow for true encode and decoding

To then implement this actually into the tree a ```for``` loop was used to move the 'cursor' according to what the morsecode value was of each given then the value could be assigned.

This is the code used to create the tree:
```python
for x in morseCode:
    cur = self.root
    for char in morseCode[x]:
        if char == '.':
            if cur.left == None:
                cur.left = Node()
            cur = cur.left
            
        elif char == '-':
            if cur.right == None:
                cur.right = Node()
            cur = cur.right

    if cur.value == "":
        cur.value = x
    else:
        print("Error, same values")
        exit()
```
### Encoding
The `encode` function acts as a middle man from the input to the `getMorse` function which uses recursion to search the binary tree previously created for a given character. By searching with a pre-order traversal search I can ensure it is searching each node and is fairly efficient within this program. The function returns true when found and appends the morse code it has found.

### Decoding
The `decode` function is fairly simple as it takes the input of an encoded message eg.`..-.` and traverses the binary tree accordingly.

### Printing tree
To print out the tree we have a `printTree` function which, via recursion, prints out a visual representation of the tree, allowing the user to see the tree with ease.

Output:

![Ouput of tree]()

### How to run
This git comes with two files, a test file and the main `morse.py` where the morse code takes place. This codes only requirements is a valid version of python, preferably python 3.

> This code was written on python 3.8.10

Test file:
To run the test file, `main.py`, ensure the `morse.py` is in the same directory or adjust the file accordingly.

Morse file:
The morse file has no requirements to run and can be ran immediately with a valid version of pyhton

### Tests
To test out my morse code I created 10 different tests, I wanted to test the limitations of my code and how well it can handle certain curveballs thrown at it, here are the tests I ran with the ideal ouput and actual output:
Input | Tested ouput | Actual Output | Functional | Testing
------------- | ------------- | ------------- | ------------- | -------------
`us` | `..- ...` | `..- ...` | ✅ | Simple Encode
`..- ...`  | `us` | `US` | ❌ | Simple Decode - Output is always capitalised
`..- ...`  | `US` | `US` | ✅ | Simple Decode - Output is always capitalised
`SOS` | `... --- ...` | `... --- ...` | ✅ | Simple Encode
`... --- ...` | `SOS` | `SOS`  | ✅ | Simple Decode
`HELLO WORLD!` | `.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--` | `.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--` | ✅ | To test spaces
`.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--` | `HELLO WORLD!` | `HELLO WORLD!` | ✅ | To test spaces
`H,ELL .O?:(WO'+ R)$-D` | `.... --..-- . .-.. .-.. / .-.-.- --- ..--.. ---... -.--. .-- --- .----. .-.-. / .-. -.--.- ...-..- -....- -..` | `.... --..-- . .-.. .-.. / .-.-.- --- ..--.. ---... -.--. .-- --- .----. .-.-. / .-. -.--.- ...-..- -....- -..` | ✅ | To test additional characters
`.... --..-- . .-.. .-.. / .-.-.- --- ..--.. ---... -.--. .-- --- .----. .-.-. / .-. -.--.- ...-..- -....- -..` | `H,ELL .O?:(WO'+ R)$-D` | `H,ELL .O?:(WO'+ R)$-D` | ✅ | To test additional characters
`This shouldn't be working due to the incorrect morse code` | `- .... .. ... / ... .... --- ..- .-.. -.. -. .----. - / -... . / .-- --- .-. -.- .. -. --. / -.. ..- . / - --- / - .... . / .. -. -.-. --- .-. .-. . -.-. - / -- --- .-. ... . -.-. --- -.. .` | `- .... .. ... / ... .... --- ..- .-.. -.. -. .----. - / -... . / .-- --- .-. -.- .. -. --. / -.. ..- . / - --- / - .... . / .. -. -.-. --- .-. .-. . -.-. - / -- --- .-. ... . / -.-. --- -.. .` | ❌ | Missing last space on purpose
> The `main.py` file, when run, should return 2 out of 10 errors

---
[^1]: Within some of the snippets the comments and code have been altered for ease of reading, but will still function
