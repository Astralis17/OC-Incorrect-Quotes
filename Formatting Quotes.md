There are a number of things when formatting quotes for use, such as character case of names, names themselves and line breaks

For example
Here is a formatted and unformatted quote

#### Unformatted
Person 1: What's going on? 

Person 2 chuckling nervously: I don't know what you're talking about. Everything is completely 
normal and Person 3 is exactly where they're supposed to be

Person 1: What do you mean? WHERE IS PERSON 3

#### Formatted
P1, ": What's going on?", "&", P2, " chuckling nervously: I don't know what you're talking about. Everything is completely normal and ", P3, " is exactly where they're supposed to be", "&", P1, ": What do you mean? WHERE IS ", P3CAP


First thing you'll notice is the persons name is replaced by "P" with a following number

The "&", represents a line break

In order to make a name entirely uppercase simply add "CAP" to the end "P3" -> "P3CAP"

Make sure to add spaces in your strings to keep names and text separate (Although don't do so for your colons in order to keep them )


Now for a step by step on how to do it

Lets say we want format this quote


Person 1: I couldn't help you even if I wanted to. 

Person 2: But you don't want to. 

Person 1: No, no I don't.

##### Firstly take the text (including the colons but not the names) for each line and put it in a string and put a comma after each one except the last one

Person 1": I couldn't help you even if I wanted to.",

Person 2": But you don't want to.",

Person 1": No, no I don't.",

##### Secondly add "&" to the end of each line except the last one (including quotation marks) and put a comma after them

Person 1": I couldn't help you even if I wanted to.", "&"

Person 2": But you don't want to.", "&"

Person 1": No, no I don't."

##### Thirdly replace Person 1, Person 2... with P1, P2... (don't put it quotation marks)

P1, ": I couldn't help you even if I wanted to.", "&",

P2, ": But you don't want to.", "&",

P1, ": No, no I don't."

##### Fourthly put all of it on one line

P1, ": I couldn't help you even if I wanted to.", "&", P2, ": But you don't want to.", "&", P1, ": No, no I don't."

##### Finally put square brackets [] around all of it and put a comma after it

[P1, ": I couldn't help you even if I wanted to.", "&", P2, ": But you don't want to.", "&", P1, ": No, no I don't."]