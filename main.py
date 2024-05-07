#  importing os module   
import os  
    
# Directory  
directory = ["Patterns",
"Basic Maths",
"Hashing",
"Sorting",
"Arrays",
"Binary Search [ID, 2D Arrays, Search Space]",
"Strings [Basic and Medium]",
"Learn LinkedList [Single LL Double LL. Medium, Hard Problems]",
"Recursion  ",
"Bit Manipulation",
"Stack and Queues [Learning, Pre-in-Post-fix, Monotonic Stack, Implementation]",
"Sliding Window & Two Pointer Combined Problems",
"Heaps [Learning, Medium, Hard Problems]",
"Greedy Algorithms [Easy, Medium, Hard]",
"Binary Trees [Traversals, Medium and Hard Problems]",
"Binary Search Trees [Concept and Problems]",
"Graphs [Concepts & Problems]",
"Dynamic Programming [Patterns and Problems]",
"Trie",
"General - Hard",
"General - Medium",
"General - Easy"
]
    
# Parent Directory path  
parent_dir = "C:/Users/User/Desktop/DSA" # this folder must already exist
    

for i in directory:
  
    path = os.path.join(parent_dir, i)  
    os.mkdir(path)  
    print("Directory '% s' created" % i)  
