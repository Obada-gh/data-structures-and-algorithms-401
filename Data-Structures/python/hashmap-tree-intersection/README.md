# Challenge Summary
Find all values found to be in 2 binary trees

Write a function called tree intersection
Arguments: two binary trees
Return: array

## Whiteboard Process

![word](./treeHash.png)

## Code Link:
[hashmap-tree-intersection](https://github.com/Obada-gh/data-structures-and-algorithms-401/tree/main/Data-Structures/python/hashmap-tree-intersection/hashmap_tree_intersection/treeHash.py)

## Approach & Efficiency
big o(n)
space O(n)
there is some builtin methods.

## Solution
```
def repeated_word(string):
    hash = set()
    Mystring=string.replace(',', '')
    for word in Mystring.split():
        if word.lower() in hash:
            return word
        else:
            hash.add(word.lower())
    
    return 'None'
```