# Data Structures and Algorithms

<details>
<summary>
1. Unpacking a Sequence into Separate Variables
</summary>
Problem:You have an N-element tuple or sequence that you would like to unpack into a collection of N variables.

```Python
element = (2,4)
x,y = element
print(element)
print(x)
print(y)

details = ('Samsuddin',35,'Mirpur','Job')
name,age,address,desc = details
print(name)
print(age)
print(address)
print(desc)
```

</details>

<details>
<summary>
2. Unpacking Elements from Iterables of Arbitrary Length
</summary>
Problem: You need to unpack N elements from an iterable, but the iterable may be longer than N elements, causing a “too many values to unpack” exception.

```Python
records = ('Samsuddin',32, '01684711032','01732005860')
name,age,*mobile = records
print(name)
print(age)
print(*mobile)
```

</details>

<details>
<summary>
3. Keeping the Last N Items
</summary>
Problem: You want to keep a limited history of the last few items seen during iteration or during
some other kind of processing.

```Python

```

</details>

<details>
<summary>
4. Finding the Largest or Smallest N Items
</summary>
Problem: You want to make a list of the largest or smallest N items in a collection

```Python
def find_large_small(arr):
    largest_number = arr[0]
    smallest_number = arr[0]

    for i in range(len(arr)):
        if largest_number < arr[i]:
            largest_number = arr[i]
        elif smallest_number > arr[i]:
            smallest_number = arr[i]
    return f"Largest Number- {largest_number}, Smallest Number- {smallest_number}"

print(find_large_small([23,5,17,65,40])) #L=65, S=5
print(find_large_small([-12,-5,-69,-2])) #L=-2, S=-69
```

</details>

<details>
<summary>
5. Implementing a Priority Queue
</summary>
Problem: You want to implement a queue that sorts items by a given priority and always returns
the item with the highest priority on each pop operation.

```Python
def priority_queue(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(0,arr_len-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j] #swap data
    return arr

list_1 = priority_queue([4,3,5,8,1,9,15,2])
print(list_1.pop()) #15
print(list_1.pop()) #9
```

</details>

<details>
<summary>
6. Mapping Keys to Multiple Values in a Dictionary
</summary>
Problem: You want to make a dictionary that maps keys to more than one value (a so-called
“multidict”).

```Python
disc = {
    '1':[1,2,3,4],
    '2':[5,4,3,2]
}
print(disc) #{'1': [1, 2, 3, 4], '2': [5, 4, 3, 2]}
```

</details>

<details>
<summary>
7. Keeping Dictionaries in Order
</summary>
Problem: You want to create a dictionary, and you also want to control the order of items when
iterating or serializing.

```Python
disc = {}
disc['one'] = "1"
disc['two'] = "2"
disc['three'] = "3"
disc['four'] = "4"
disc['five'] = "5"

for key in disc:
    print(key, disc[key])
```

</details>

<details>
<summary>
8. Calculating with Dictionaries
</summary>
Problem: You want to perform various calculations (e.g., minimum value, maximum value, sort‐
ing, etc.) on a dictionary of data.

```Python
phone_prices = {
    'Apple':19500,
    'Samsung':65874,
    'Opp':215,
    'Walton':2548
}

min_prices = min(zip(phone_prices.values(),phone_prices.keys())) #(65874, 'Samsung')
max_prices = max(zip(phone_prices.values(),phone_prices.keys())) #(215, 'Opp')
sort_prices = sorted(zip(phone_prices.values(),phone_prices.keys())) #[(215, 'Opp'), (2548, 'Walton'), (19500, 'Apple'), (65874, 'Samsung')]
```

</details>

<details>
<summary>
9. Finding Commonalities in Two Dictionaries
</summary>
Problem: You have two dictionaries and want to find out what they might have in common (same
keys, same values, etc.).

```Python

```

</details>

<details>
<summary>
10. Removing Duplicates from a Sequence while Maintaining Order
</summary>
Problem: You want to eliminate the duplicate values in a sequence, but preserve the order of the
remaining items.

```Python

```

</details>

<details>
<summary>
11. Naming a Slice
</summary>
Problem: Your program has become an unreadable mess of hardcoded slice indices and you want
to clean it up.

```Python

```

</details>

<details>
<summary>
12. Determining the Most Frequently Occurring Items in a Sequence
</summary>
Problem: You have a sequence of items, and you’d like to determine the most frequently occurring
items in the sequence.

```Python

```

</details>

<details>
<summary>
13. Sorting a List of Dictionaries by a Common Key
</summary>
Problem: You have a list of dictionaries and you would like to sort the entries according to one
or more of the dictionary values.

```Python

```

</details>

<details>
<summary>
14. Sorting Objects Without Native Comparison Support
</summary>
Problem: You want to sort objects of the same class, but they don’t natively support comparison
operations.

```Python

```

</details>

<details>
<summary>
15. Grouping Records Together Based on a Field
</summary>
Problem: You have a sequence of dictionaries or instances and you want to iterate over the data
in groups based on the value of a particular field, such as date.

```Python

```

</details>

<details>
<summary>
16. Filtering Sequence Elements
</summary>
Problem: You have data inside of a sequence, and need to extract values or reduce the sequence
using some criteria.

```Python

```

</details>

<details>
<summary>
17. Extracting a Subset of a Dictionary
</summary>
Problem: You want to make a dictionary that is a subset of another dictionary.

```Python

```

</details>

<details>
<summary>
18. Mapping Names to Sequence Elements
</summary>
Problem: You have code that accesses list or tuple elements by position, but this makes the code
somewhat difficult to read at times. You’d also like to be less dependent on position in
the structure, by accessing the elements by name.

```Python

```

</details>

<details>
<summary>
19. Transforming and Reducing Data at the Same Time
</summary>
Problem: You need to execute a reduction function (e.g., sum(), min(), max()), but first need to
transform or filter the data.

```Python

```

</details>

<details>
<summary>
20. Combining Multiple Mappings into a Single Mapping
</summary>
Problem: You have multiple dictionaries or mappings that you want to logically combine into a
single mapping to perform certain operations, such as looking up values or checking
for the existence of keys.

```Python

```

</details>
