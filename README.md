# Reverse a Linked List In Place in Python

[ ![Reverse a Linked List In Place in Python](./image.png)](https://youtu.be/d60duiYx0YM)

This repository contains the code and solution to the problem of reversing a singly-linked list in-place. The code is written in Python.

I have a video walkthrough of this challenge available on my [YouTube channel](https://youtu.be/d60duiYx0YM) and [my blog](https://kalbartal.net/reverse-a-linked-list-in-place-in-python/).


## Problem Statement
Given a singly-linked list, reverse the order of the list in-place. You cannot use any additional data structure such as arrays, linked lists, etc. and you cannot create any new nodes.

## Solution
The problem can be solved using an iterative approach. We can use a loop to iterate through the nodes and make the necessary changes. The first step is to create a variable called “current” which points to the first node of the list. Then, we can iterate through the list and make the necessary changes. On each iteration, we first save the pointer of the current node in a variable called “next”, point the pointer of the current node to the previous node and finally, set the variable “current” to point to the next node in the list. When the loop is finished, we should have the same list, but with the elements in reversed order.

## Usage
You can run the code using any Python IDE or terminal. To run it in the terminal, navigate to the directory where the code is located, and run the following command:

`main.py`

## Time and Space Complexity
The time complexity of this code is O(n), because it iterates through the list once and does not use any additional data structure, so the number of operations is proportional to the number of nodes in the list. Additionally, it does not perform any extra comparisons or other operations on each iteration, so the time complexity remains linear. The space complexity of this code is also O(1), or constant time, as the space required to perform the operations in the reverseLinkedList() function is independent of the size of the input and we only need to initialize a few variables that take up the same amount of space to perform the reversal. Therefore, this algorithm is very efficient in both time and space complexity.
## Video Tutorial
I've also recorded a video tutorial on this problem, which can be found on my YouTube channel. I discuss the problem, explain the solution, and code it step-by-step in detail. I hope you find it helpful. 

## Contact
If you have any questions or suggestions, please feel free to contact me. My contact details can be found in my blog. Thank you!
