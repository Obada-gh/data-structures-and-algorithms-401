# Challenge Summary
Write a function that LEFT JOINs two hashmaps into a single data structure.

Write a function called left join
Arguments: two hash maps
The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic
NOTES:

Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row.
If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.

## Whiteboard Process

![word](./hashmap-left-join.png)

## Code Link:
[hashmap-left-join](https://github.com/Obada-gh/data-structures-and-algorithms-401/tree/main/Data-Structures/python/hashmap-left-join/hashmap_left_join/hashmap_left_join.py)

## Approach & Efficiency
big o(n)
space O(n^2)


## Solution
```
hash1={'fond': 'enamored','wrath': 'anger','diligent': 'employed','outfit':'grab','guide':'usher' }
hash2={'fond': 'averse','wrath': 'diligent','diligent': 'idle','guide':'follow','flow':'jam' }

def left_join(hash1,hash2):
    newArr=[]
    for i, v in enumerate(hash1):
    
        newArr+=[[v]]
        newArr[i].append(hash1[v])
        if v in hash2:
            newArr[i].append(hash2[v])
        else:
            newArr[i].append(None)
                       
    return newArr


print(left_join(hash1,hash2))
    
```