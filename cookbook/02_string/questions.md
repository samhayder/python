# Strings and Text

<details>
<summary>
1. Splitting Strings on Any of Multiple Delimiters
</summary>
Problem: You need to split a string into fields, but the delimiters (and spacing around them) aren’t
consistent throughout the string.

```python
str = 'samsuddin hayder'
str_split = str.split(' ')
print(str_split) #['samsuddin', 'hayder']

note = "helo, i am the boss; oh no sorry! you'r the boss."
import re
note_split = re.split(r'[,;\s]\s*',note)
print(note_split) #['helo', 'i', 'am', 'the', 'boss', 'oh', 'no', 'sorry!', "you'r", 'the', 'boss.']
```

</details>

<details>
<summary>
2. Matching Text at the Start or End of a String
</summary>
Problem: You need to check the start or end of a string for specific text patterns, such as filename
extensions, URL schemes, and so on.

```python
url = "https://www.youtube.com"

if url.startswith('https://'):
    print('Start pattern is match')
else:
    print('please type of start right pattern')

if url.endswith('.com'):
    print('End pattern is match')
else:
    print('please type of end right pattern')
```

</details>

<details>
<summary>
3. Matching Strings Using Shell Wildcard Patterns
</summary>
Problem:You want to match text using the same wildcard patterns as are commonly used when
working in Unix shells (e.g., *.py, Dat[0-9]*.csv, etc.).

```python

```

</details>

<details>
<summary>
4. Matching and Searching for Text Patterns
</summary>
Problem:You want to match or search text for a specific pattern.

```python

```

</details>

<details>
<summary>
5. Searching and Replacing Text
</summary>
Problem:You want to search for and replace a text pattern in a string.

```python

```

</details>

<details>
<summary>
6. Searching and Replacing Case-Insensitive Text
</summary>
Problem:You need to search for and possibly replace text in a case-insensitive manner

```python

```

</details>

<details>
<summary>
7. Specifying a Regular Expression for the Shortest Match
</summary>
Problem:You’re trying to match a text pattern using regular expressions, but it is identifying the
longest possible matches of a pattern. Instead, you would like to change it to find the
shortest possible match.

```python

```

</details>

<details>
<summary>
8. Writing a Regular Expression for Multiline Patterns
</summary>
Problem:You’re trying to match a block of text using a regular expression, but you need the match
to span multiple lines.

```python

```

</details>

<details>
<summary>
9. Normalizing Unicode Text to a Standard Representation
</summary>
Problem:You’re working with Unicode strings, but need to make sure that all of the strings have
the same underlying representation.

```python

```

</details>

<details>
<summary>
10. Working with Unicode Characters in Regular Expressions
</summary>
Problem:You are using regular expressions to process text, but are concerned about the handling
of Unicode characters.

```python

```

</details>

<details>
<summary>
11. Stripping Unwanted Characters from Strings
</summary>
Problem:You want to strip unwanted characters, such as whitespace, from the beginning, end, or
middle of a text string.

```python

```

</details>

<details>
<summary>
12. Sanitizing and Cleaning Up Text
</summary>
Problem:Some bored script kiddie has entered the text “pýtĥöñ” into a form on your web page
and you’d like to clean it up somehow.

```python

```

</details>

<details>
<summary>
13. Aligning Text Strings
</summary>
Problem:You need to format text with some sort of alignment applied.

```python

```

</details>

<details>
<summary>
14. Combining and Concatenating Strings
</summary>
Problem:You want to combine many small strings together into a larger string.

```python

```

</details>

<details>
<summary>
15. Interpolating Variables in Strings
</summary>
Problem:You want to create a string in which embedded variable names are substituted with a
string representation of a variable’s value.

```python

```

</details>

<details>
<summary>
16. Reformatting Text to a Fixed Number of Columns
</summary>
Problem:You have long strings that you want to reformat so that they fill a user-specified number
of columns.

```python

```

</details>

<details>
<summary>
17. Handling HTML and XML Entities in Text
</summary>
Problem:You want to replace HTML or XML entities such as &entity; or &#code; with their
corresponding text. Alternatively, you need to produce text, but escape certain charac‐
ters (e.g., <, >, or &).

```python

```

</details>

<details>
<summary>
18. Tokenizing Text
</summary>
Problem:You have a string that you want to parse left to right into a stream of tokens.

```python

```

</details>

<details>
<summary>
19. Writing a Simple Recursive Descent Parser
</summary>
Problem:You need to parse text according to a set of grammar rules and perform actions or build
an abstract syntax tree representing the input. The grammar is small, so you’d prefer to
just write the parser yourself as opposed to using some kind of framework.

```python

```

</details>

<details>
<summary>
20. Performing Text Operations on Byte Strings
</summary>
Problem:You want to perform common text operations (e.g., stripping, searching, and replacement) on byte strings.

```python

```

</details>
