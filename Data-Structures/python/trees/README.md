# Trees

Trees are non-linear data structures that represent nodes connected by edges. Each tree consists of a root node as the Parent node, and the left node and right node as Child nodes.

## Challenge

Node
Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
Binary Tree
Create a Binary Tree class
Define a method for each of the depth first traversals:
pre order
in order
post order which returns an array of the values, ordered appropriately.
Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
Binary Search Tree
Create a Binary Search Tree class
This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
Add
Arguments: value
Return: nothing
Adds a new node with that value in the correct location in the binary search tree.
Contains
Argument: value
Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency

The Big O time complexity for inserting a new node is O(n). Searching for a specific node will also be O(n). Because of the lack of organizational structure in a Binary Tree, the worst case for most operations will involve traversing the entire tree. If we assume that a tree has n nodes, then in the worst case we will have to look at n items, hence the O(n) complexity.

The Big O space complexity for a node insertion using breadth first insertion will be O(w), where w is the largest width of the tree. For example, in the above tree, w is 4.

A “perfect” binary tree is one where every non-leaf node has exactly two children. The maximum width for a perfect binary tree, is 2^(h-1), where h is the height of the tree. Height can be calculated as log n, where n is the number of nodes.

## Code Link:
[Code Link](https://github.com/Obada-gh/data-structures-and-algorithms-401/blob/main/Data-Structures/python/trees/trees/trees.py)

## API
I use this methods and functions:

### Add method:
Arguments: value
Return: nothing
Adds a new node with that value in the correct location in the binary search tree.
### Contains method:
Argument: value
Returns: boolean indicating whether or not the value is in the tree at least once.

### build_tree function:
Arguments: array
return : root with builded tree.

### in_order method:
Arguments: nothing
Return: array with in order the root for the tree
### pre_order method:
Argument: nothing
Returns: array with pre order  the root for the tree

### post_order method:
Arguments: nothing
return : array with post order  the root for the tree