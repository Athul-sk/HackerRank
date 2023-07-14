"""
1) insert i e: Insert integer e at i position .
2) print: Print the list.
3) remove e: Delete the first occurrence of integer e.
4) append e: Insert integer e at the end of the list.
5) sort: Sort the list.
6) pop: Pop the last element from the list.
7) reverse: Reverse the list.
Initialize your list and read in the value of N followed by N lines of commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.
"""

N = int(input())
l = []
for i in range(N):
    choice = list(input().split())
    if choice[0] == "insert":
        l.insert(int(choice[1]), int(choice[2]))
    if choice[0] == "print":
        print(l)
    if choice[0] == "remove":
        l.remove(int(choice[1]))
    if choice[0] == "append":
        l.append(int(choice[1]))
    if choice[0] == "sort":
        l.sort()
    if choice[0] == "pop":
        l.pop()
    if choice[0] == "reverse":
        l.reverse()
